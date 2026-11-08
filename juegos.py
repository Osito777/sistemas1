"""
juegos.py · Motores de juego reutilizables
==========================================

Aquí está la LÓGICA de los juegos. El CONTENIDO (preguntas, parejas, pasos...)
vive en `contenido.py`, así se puede ampliar sin tocar este archivo.

Tipos de juego disponibles:
    - quiz              Preguntas de opción múltiple, una a una.
    - verdadero_falso   Lista de afirmaciones: ¿verdadero o falso?
    - emparejar         Une cada concepto con su descripción.
    - ordenar           Pon los pasos en el orden correcto.
    - calculadora_fuente  Herramienta interactiva para dimensionar una fuente.

Idea clave de Streamlit: cada vez que pulsas algo, el script se ejecuta de nuevo
de arriba abajo. Lo que queremos "recordar" entre ejecuciones (puntos, pregunta
actual...) se guarda en `st.session_state`.
"""

import random

import streamlit as st

PLACEHOLDER = "— elige —"


# ----------------------------------------------------------------------------
# Utilidades comunes
# ----------------------------------------------------------------------------
def _k(game_id: str, nombre: str) -> str:
    """Crea una clave única para session_state: 'hw_quiz::pos', etc."""
    return f"{game_id}::{nombre}"


def reiniciar(game_id: str) -> None:
    """Borra todo el estado de un juego para poder volver a jugarlo."""
    prefijo = f"{game_id}::"
    for clave in list(st.session_state.keys()):
        if isinstance(clave, str) and clave.startswith(prefijo):
            del st.session_state[clave]


def registrar_puntos(game_id: str, aciertos: int, total: int) -> None:
    """Guarda el resultado del juego para mostrarlo en la barra lateral."""
    st.session_state.setdefault("puntos", {})
    st.session_state["puntos"][game_id] = (aciertos, total)


def _boton_reiniciar(game_id: str, texto: str = "🔄 Volver a jugar") -> None:
    if st.button(texto, key=_k(game_id, "btn_reiniciar")):
        reiniciar(game_id)
        st.rerun()


def _mensaje_nota(aciertos: int, total: int) -> str:
    porcentaje = aciertos / total if total else 0
    if porcentaje == 1:
        return "🏆 ¡Perfecto! Dominas este tema."
    if porcentaje >= 0.8:
        return "🎉 ¡Muy bien! Casi lo tienes todo."
    if porcentaje >= 0.5:
        return "👍 Aprobado. Repasa los fallos y vuelve a intentarlo."
    return "📚 Toca repasar. Lee el «Repaso rápido» y prueba otra vez."


def _resultado_final(game_id: str, aciertos: int, total: int) -> None:
    registrar_puntos(game_id, aciertos, total)
    st.metric("Tu resultado", f"{aciertos} / {total}")
    st.progress(aciertos / total if total else 0)
    st.markdown(_mensaje_nota(aciertos, total))
    if aciertos == total and not st.session_state.get(_k(game_id, "celebrado")):
        st.session_state[_k(game_id, "celebrado")] = True
        st.balloons()


# ----------------------------------------------------------------------------
# 1) QUIZ
# ----------------------------------------------------------------------------
def quiz(game_id: str, preguntas: list, n: int = 10) -> None:
    """
    `preguntas`: lista de dicts con las claves
        pregunta, correcta, incorrectas (lista), explicacion
    En cada partida se eligen `n` preguntas al azar y las opciones se barajan.
    """
    k = lambda nombre: _k(game_id, nombre)  # noqa: E731

    # Primera vez: preparamos la partida
    if k("indices") not in st.session_state:
        cuantas = min(n, len(preguntas))
        st.session_state[k("indices")] = random.sample(range(len(preguntas)), cuantas)
        st.session_state[k("pos")] = 0
        st.session_state[k("aciertos")] = 0
        st.session_state[k("eleccion")] = None  # None = aún sin responder
        st.session_state[k("opciones")] = {}

    indices = st.session_state[k("indices")]
    pos = st.session_state[k("pos")]
    total = len(indices)

    # ¿Fin de la partida?
    if pos >= total:
        _resultado_final(game_id, st.session_state[k("aciertos")], total)
        _boton_reiniciar(game_id)
        return

    p = preguntas[indices[pos]]

    # Las opciones se barajan una sola vez por pregunta
    guardadas = st.session_state[k("opciones")]
    if pos not in guardadas:
        opciones = [p["correcta"]] + list(p["incorrectas"])
        random.shuffle(opciones)
        guardadas[pos] = opciones
    opciones = guardadas[pos]

    st.progress(pos / total, text=f"Pregunta {pos + 1} de {total}")
    st.markdown(f"### {p['pregunta']}")

    eleccion = st.session_state[k("eleccion")]

    if eleccion is None:
        # Fase 1: el alumno elige
        marcada = st.radio(
            "Elige una respuesta:", opciones, index=None, key=k(f"radio_{pos}")
        )
        if st.button(
            "Comprobar", key=k(f"comprobar_{pos}"), disabled=marcada is None, type="primary"
        ):
            st.session_state[k("eleccion")] = marcada
            if marcada == p["correcta"]:
                st.session_state[k("aciertos")] += 1
            st.rerun()
    else:
        # Fase 2: mostramos el resultado y la explicación
        for opcion in opciones:
            if opcion == p["correcta"]:
                st.success(f"✅ {opcion}")
            elif opcion == eleccion:
                st.error(f"❌ {opcion}  ← tu respuesta")
            else:
                st.markdown(f"◻️ {opcion}")
        st.info(f"💡 {p['explicacion']}")

        etiqueta = "Siguiente ➡️" if pos + 1 < total else "Ver resultado 🏁"
        if st.button(etiqueta, key=k(f"siguiente_{pos}"), type="primary"):
            st.session_state[k("pos")] += 1
            st.session_state[k("eleccion")] = None
            st.rerun()

    st.caption(f"Aciertos hasta ahora: {st.session_state[k('aciertos')]}")


# ----------------------------------------------------------------------------
# 2) VERDADERO / FALSO
# ----------------------------------------------------------------------------
def verdadero_falso(game_id: str, afirmaciones: list) -> None:
    """`afirmaciones`: lista de tuplas (texto, es_verdadera, explicacion)."""
    k = lambda nombre: _k(game_id, nombre)  # noqa: E731

    if k("orden") not in st.session_state:
        orden = list(range(len(afirmaciones)))
        random.shuffle(orden)
        st.session_state[k("orden")] = orden
        st.session_state[k("resultado")] = None

    orden = st.session_state[k("orden")]
    resultado = st.session_state[k("resultado")]

    if resultado is None:
        st.write("Marca cada afirmación como verdadera o falsa y pulsa **Comprobar**.")
        for n, i in enumerate(orden, start=1):
            st.radio(
                f"**{n}.** {afirmaciones[i][0]}",
                ["Verdadero", "Falso"],
                index=None,
                horizontal=True,
                key=k(f"r{i}"),
            )
        if st.button("Comprobar", key=k("comprobar"), type="primary"):
            respuestas = {i: st.session_state.get(k(f"r{i}")) for i in orden}
            if any(r is None for r in respuestas.values()):
                st.warning("Responde a todas las afirmaciones antes de comprobar.")
            else:
                st.session_state[k("resultado")] = respuestas
                st.rerun()
        return

    # Mostrar resultados
    aciertos = 0
    for n, i in enumerate(orden, start=1):
        texto, es_verdadera, explicacion = afirmaciones[i]
        dijo_verdadero = resultado[i] == "Verdadero"
        acierto = dijo_verdadero == es_verdadera
        aciertos += acierto
        solucion = "Verdadero" if es_verdadera else "Falso"
        if acierto:
            st.success(f"**{n}.** {texto}  \n✅ {solucion}. {explicacion}")
        else:
            st.error(
                f"**{n}.** {texto}  \n❌ Respondiste «{resultado[i]}»; "
                f"es **{solucion}**. {explicacion}"
            )
    _resultado_final(game_id, aciertos, len(orden))
    _boton_reiniciar(game_id)


# ----------------------------------------------------------------------------
# 3) EMPAREJAR
# ----------------------------------------------------------------------------
def emparejar(game_id: str, pares: list) -> None:
    """
    `pares`: lista de tuplas (concepto, descripcion).
    Las descripciones pueden repetirse (por ejemplo «BIOS» o «UEFI»).
    """
    k = lambda nombre: _k(game_id, nombre)  # noqa: E731

    if k("opciones") not in st.session_state:
        opciones = sorted({respuesta for _, respuesta in pares})
        random.shuffle(opciones)
        st.session_state[k("opciones")] = opciones
        st.session_state[k("resultado")] = None

    opciones = st.session_state[k("opciones")]
    resultado = st.session_state[k("resultado")]

    if resultado is None:
        st.write("Elige en cada desplegable la opción que corresponde y pulsa **Comprobar**.")
        for i, (concepto, _) in enumerate(pares):
            col_izq, col_der = st.columns([1, 1])
            col_izq.markdown(f"**{concepto}**")
            col_der.selectbox(
                concepto,
                [PLACEHOLDER] + opciones,
                key=k(f"s{i}"),
                label_visibility="collapsed",
            )
        if st.button("Comprobar", key=k("comprobar"), type="primary"):
            respuestas = [st.session_state.get(k(f"s{i}"), PLACEHOLDER) for i in range(len(pares))]
            if PLACEHOLDER in respuestas:
                st.warning("Falta alguna pareja por elegir.")
            else:
                st.session_state[k("resultado")] = respuestas
                st.rerun()
        return

    aciertos = 0
    for (concepto, correcta), dada in zip(pares, resultado):
        if dada == correcta:
            aciertos += 1
            st.success(f"**{concepto}** → {correcta}")
        else:
            st.error(f"**{concepto}** → ~~{dada}~~  \n✅ Correcto: **{correcta}**")
    _resultado_final(game_id, aciertos, len(pares))
    _boton_reiniciar(game_id)


# ----------------------------------------------------------------------------
# 4) ORDENAR
# ----------------------------------------------------------------------------
def ordenar(game_id: str, pasos: list) -> None:
    """`pasos`: lista de textos YA en el orden correcto."""
    k = lambda nombre: _k(game_id, nombre)  # noqa: E731

    if k("barajados") not in st.session_state:
        barajados = list(pasos)
        while barajados == list(pasos) and len(pasos) > 1:
            random.shuffle(barajados)
        st.session_state[k("barajados")] = barajados
        st.session_state[k("resultado")] = None

    barajados = st.session_state[k("barajados")]
    resultado = st.session_state[k("resultado")]

    if resultado is None:
        st.write("**Elementos desordenados:**")
        for elemento in barajados:
            st.markdown(f"- {elemento}")
        st.write("**Ponlos en orden:**")
        for n in range(len(pasos)):
            st.selectbox(
                f"Posición {n + 1}", [PLACEHOLDER] + barajados, key=k(f"p{n}")
            )
        if st.button("Comprobar", key=k("comprobar"), type="primary"):
            respuestas = [st.session_state.get(k(f"p{n}"), PLACEHOLDER) for n in range(len(pasos))]
            if PLACEHOLDER in respuestas:
                st.warning("Rellena todas las posiciones.")
            elif len(set(respuestas)) != len(respuestas):
                st.warning("Hay elementos repetidos: cada uno solo puede usarse una vez.")
            else:
                st.session_state[k("resultado")] = respuestas
                st.rerun()
        return

    aciertos = 0
    for n, (dada, correcta) in enumerate(zip(resultado, pasos), start=1):
        if dada == correcta:
            aciertos += 1
            st.success(f"**{n}.** {dada}")
        else:
            st.error(f"**{n}.** ~~{dada}~~  \n✅ Aquí iba: **{correcta}**")
    _resultado_final(game_id, aciertos, len(pasos))
    _boton_reiniciar(game_id)


# ----------------------------------------------------------------------------
# 5) CALCULADORA DE FUENTE DE ALIMENTACIÓN (herramienta, no puntúa)
# ----------------------------------------------------------------------------
def calculadora_fuente(game_id: str) -> None:
    st.write(
        "Regla de la unidad: **procesador + gráfica + 75 W** para el resto de piezas, "
        "y un **30 % de margen**. Mueve los deslizadores y comprueba qué fuente necesitas."
    )
    cpu = st.slider("Consumo del procesador (W)", 35, 300, 125, step=5, key=_k(game_id, "cpu"))
    gpu = st.slider("Consumo de la tarjeta gráfica (W)", 0, 600, 300, step=25, key=_k(game_id, "gpu"))
    resto = 75

    base = cpu + gpu + resto
    con_margen = base * 1.3
    comerciales = [300, 400, 450, 500, 550, 650, 750, 850, 1000, 1200, 1600]
    recomendada = next((w for w in comerciales if w >= con_margen), comerciales[-1])

    col1, col2, col3 = st.columns(3)
    col1.metric("Consumo estimado", f"{base} W")
    col2.metric("Con 30 % de margen", f"{con_margen:.0f} W")
    col3.metric("Fuente recomendada", f"{recomendada} W")

    st.code(f"{cpu} + {gpu} + {resto} = {base} W  →  fuente de {recomendada} W", language="text")
    if gpu > 75:
        st.info(
            "Esta gráfica necesita **alimentación extra** además de los 75 W de la ranura PCIe: "
            "conector PCIe de 6+2 pines (150 W cada uno) o 12V-2x6 (hasta 600 W)."
        )
    if cpu > 125:
        st.warning("Un procesador de mucho consumo pide buena refrigeración (valora la líquida, AIO).")
    if gpu > 0 and recomendada >= 1000:
        st.caption("Con estas cifras conviene una fuente de calidad, por ejemplo con certificación 80 PLUS Gold o superior.")
