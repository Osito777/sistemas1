"""
app.py · Informática en juego
=============================

Aplicación de Streamlit para repasar jugando:
    🔧 Hardware por dentro
    🚀 El arranque del ordenador
    📜 Software y licencias

Para ejecutarla en tu ordenador:
    pip install -r requirements.txt
    streamlit run app.py
"""

import streamlit as st

import juegos
from contenido import SECCIONES

st.set_page_config(
    page_title="Informática en juego",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded",
)

INICIO = "🏠 Inicio"


# ----------------------------------------------------------------------------
# Lanzar un juego según su tipo
# ----------------------------------------------------------------------------
def pintar_juego(juego: dict) -> None:
    tipo, gid, datos = juego["tipo"], juego["id"], juego["datos"]

    if juego.get("descripcion"):
        st.caption(juego["descripcion"])

    if tipo == "quiz":
        juegos.quiz(gid, datos, n=juego.get("n", 10))
    elif tipo == "verdadero_falso":
        juegos.verdadero_falso(gid, datos)
    elif tipo == "emparejar":
        juegos.emparejar(gid, datos)
    elif tipo == "ordenar":
        juegos.ordenar(gid, datos)
    elif tipo == "calculadora_fuente":
        juegos.calculadora_fuente(gid)
    else:
        st.error(f"Tipo de juego desconocido: {tipo}")


# ----------------------------------------------------------------------------
# Barra lateral: navegación y progreso
# ----------------------------------------------------------------------------
def barra_lateral() -> str:
    st.sidebar.title("🖥️ Informática en juego")

    opciones = [INICIO] + [f"{s['icono']} {s['titulo']}" for s in SECCIONES.values()]
    seleccion = st.sidebar.radio("Apartados", opciones, key="seccion")

    puntos = st.session_state.get("puntos", {})

    st.sidebar.divider()
    st.sidebar.subheader("📊 Tu progreso")
    total_a = sum(a for a, _ in puntos.values())
    total_t = sum(t for _, t in puntos.values())
    if total_t:
        st.sidebar.metric("Aciertos totales", f"{total_a} / {total_t}")
    else:
        st.sidebar.caption("Aún no has terminado ningún juego.")

    for s in SECCIONES.values():
        ids = [j["id"] for j in s["juegos"] if j["tipo"] != "calculadora_fuente"]
        hechos = sum(1 for i in ids if i in puntos)
        st.sidebar.progress(hechos / len(ids), text=f"{s['icono']} {s['titulo']}: {hechos}/{len(ids)} juegos")

    if puntos and st.sidebar.button("🗑️ Borrar mi progreso"):
        for clave in list(st.session_state.keys()):
            if clave != "seccion":
                del st.session_state[clave]
        st.rerun()

    return seleccion


# ----------------------------------------------------------------------------
# Páginas
# ----------------------------------------------------------------------------
def pagina_inicio() -> None:
    st.title("🖥️ Informática en juego")
    st.markdown(
        "Repasa **cómo es un ordenador por dentro**, **cómo arranca** y **qué tipos de "
        "software y licencias existen**, jugando. Elige un apartado en el menú de la izquierda."
    )

    columnas = st.columns(len(SECCIONES))
    for columna, s in zip(columnas, SECCIONES.values()):
        with columna:
            with st.container(border=True):
                st.subheader(f"{s['icono']} {s['titulo']}")
                st.write(s["lema"])
                st.caption(f"{len(s['juegos'])} juegos y herramientas")
                for j in s["juegos"]:
                    st.markdown(f"- {j['icono']} {j['nombre']}")

    st.divider()
    st.markdown(
        """
**¿Cómo se juega?**
1. Abre un apartado y lee el **📚 Repaso rápido** (opcional, pero ayuda).
2. Elige un juego: quiz, verdadero o falso, emparejar o ordenar.
3. Pulsa **Comprobar** para ver tus aciertos y la explicación de cada fallo.
4. Repite todas las veces que quieras: los quiz sacan preguntas distintas cada vez.
        """
    )


def pagina_seccion(clave: str) -> None:
    s = SECCIONES[clave]
    st.title(f"{s['icono']} {s['titulo']}")
    st.write(s["lema"])

    with st.expander("📚 Repaso rápido"):
        st.markdown(s["resumen"])

    juegos_seccion = s["juegos"]
    etiquetas = {j["id"]: f"{j['icono']} {j['nombre']}" for j in juegos_seccion}
    elegido = st.radio(
        "🎮 Elige un juego",
        [j["id"] for j in juegos_seccion],
        format_func=lambda i: etiquetas[i],
        horizontal=True,
        key=f"juego_{clave}",
    )

    st.divider()
    juego = next(j for j in juegos_seccion if j["id"] == elegido)
    pintar_juego(juego)


# ----------------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------------
seleccion = barra_lateral()

if seleccion == INICIO:
    pagina_inicio()
else:
    for clave, s in SECCIONES.items():
        if seleccion == f"{s['icono']} {s['titulo']}":
            pagina_seccion(clave)
            break
