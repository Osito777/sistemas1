# 🖥️ Informática en juego

Juego didáctico hecho con [Streamlit](https://streamlit.io) para repasar tres temas de informática:

| Apartado | Qué se trabaja |
|---|---|
| 🔧 **Hardware por dentro** | Placa base y formatos, zócalos (PGA, LGA, BGA), chipset, RAM, PCIe, almacenamiento, GPU, fuente de alimentación, refrigeración y conectores |
| 🚀 **El arranque del ordenador** | Las 7 fases, firmware, POST, BIOS frente a UEFI, MBR y GPT, gestores de arranque, arranque de Linux y de Windows, diagnóstico de fallos |
| 📜 **Software y licencias** | Sistema operativo y aplicaciones, software libre y propietario, las cuatro libertades, tipos de licencia |

## Tipos de juego

- ❓ **Quiz**: preguntas al azar con las opciones barajadas y explicación de cada respuesta.
- ✅ **Verdadero o falso**
- 🧩 **Emparejar** conceptos con su descripción
- 🔢 **Ordenar** pasos o procesos
- 🧮 **Calculadora de fuente de alimentación** (herramienta interactiva)

## Estructura del proyecto

```
informatica-en-juego/
├── app.py              # La aplicación: menú, páginas y progreso
├── juegos.py           # Lógica de cada tipo de juego (quiz, emparejar, ordenar...)
├── contenido.py        # TODO el contenido: preguntas, parejas, pasos y repasos
├── requirements.txt    # Dependencias
├── .streamlit/
│   └── config.toml     # Colores de la aplicación
└── README.md
```

## Ejecutarlo en tu ordenador

```bash
pip install -r requirements.txt
streamlit run app.py
```

Se abrirá en `http://localhost:8501`.

## Subirlo a GitHub

1. Crea un repositorio nuevo en GitHub (por ejemplo `informatica-en-juego`).
2. Sube **todos** los archivos manteniendo la estructura (incluida la carpeta `.streamlit`).
   - Desde la web: *Add file → Upload files* y arrastra la carpeta.
   - O desde la terminal:
     ```bash
     git init
     git add .
     git commit -m "Primer commit"
     git branch -M main
     git remote add origin https://github.com/TU_USUARIO/informatica-en-juego.git
     git push -u origin main
     ```

## Abrirlo en Streamlit Community Cloud (gratis)

1. Entra en [share.streamlit.io](https://share.streamlit.io) con tu cuenta de GitHub.
2. Pulsa **Create app** → **Deploy a public app from GitHub**.
3. Elige tu repositorio, la rama `main` y el archivo principal `app.py`.
4. Pulsa **Deploy**. En un par de minutos tendrás un enlace público para compartir con tu clase.

## Cómo ampliar el contenido

Todo se edita en `contenido.py`, sin tocar el resto del código.

**Añadir una pregunta de quiz** (a la lista `HW_QUIZ`, `BOOT_QUIZ` o `SW_QUIZ`):

```python
q("¿Qué pieza genera la imagen que se envía al monitor?",
  "La tarjeta gráfica",                      # respuesta correcta
  ["La fuente", "El chipset", "La RAM"],     # 3 incorrectas
  "La GPU genera la imagen que se envía al monitor."),   # explicación
```

**Añadir una pareja** (a cualquier lista de emparejar): `("Concepto", "Descripción")`.

**Añadir una afirmación de verdadero o falso**: `("Texto", True, "Explicación")`.

**Añadir un juego nuevo**: crea su lista de datos y añade una línea en `SECCIONES`, dentro de la sección que quieras:

```python
{"id": "hw_nuevo", "tipo": "emparejar", "icono": "🧩",
 "nombre": "Mi juego", "datos": MI_LISTA, "descripcion": "Texto de ayuda"},
```

Los tipos válidos son `quiz`, `verdadero_falso`, `emparejar`, `ordenar` y `calculadora_fuente`. El `id` debe ser único.
