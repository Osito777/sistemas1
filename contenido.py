"""
contenido.py · Todo el CONTENIDO didáctico del juego
====================================================

Para ampliar el juego NO hace falta tocar `app.py` ni `juegos.py`:
basta con añadir preguntas, parejas o pasos en este archivo.

Formatos:
    q(pregunta, correcta, [3 incorrectas], explicacion)      -> quiz
    (afirmacion, True/False, explicacion)                    -> verdadero/falso
    (concepto, descripcion)                                  -> emparejar
    ["paso 1", "paso 2", ...]  (ya en orden correcto)        -> ordenar
"""


def q(pregunta, correcta, incorrectas, explicacion):
    """Atajo para crear una pregunta de quiz."""
    return {
        "pregunta": pregunta,
        "correcta": correcta,
        "incorrectas": incorrectas,
        "explicacion": explicacion,
    }


# =============================================================================
# 🔧 SECCIÓN 1 · EL HARDWARE POR DENTRO
# =============================================================================
HW_RESUMEN = """
**Placa base** · Circuito impreso (PCB) con varias capas de pistas de cobre. Todo se conecta a ella y decide qué procesador, memoria y dispositivos puedes usar.

| Formato | Medidas | PCIe | Uso típico |
|---|---|---|---|
| E-ATX | 305 × 330 mm | hasta 7 | Workstation |
| ATX | 305 × 244 mm | hasta 7 | Sobremesa |
| Micro-ATX | 244 × 244 mm | hasta 4 | Oficina |
| Mini-ITX | 170 × 170 mm | 1 | PC compacto |

**Zócalo** · **PGA** (pines en el procesador, ej. AM4), **LGA** (pines en la placa, actual en Intel y AM5) y **BGA** (procesador soldado: portátiles, miniPC, consolas, Raspberry Pi). *Regla de oro: la placa fija el zócalo y el zócalo fija los procesadores; el chipset y la UEFI también deben admitirlo.*

**Chipset** · Antes: puente norte (CPU, RAM, gráfica) y puente sur (USB, SATA, red, audio). Ahora el puente norte está dentro del procesador y en la placa queda un solo chip, el chipset (PCH).

**Memoria RAM** · Volátil (se borra al apagar). DDR4 (2014, 1,2 V) y DDR5 (2021, 1,1 V) no son intercambiables. En Dual Channel, 2 × 8 GB rinde más que 1 × 16 GB. Activa XMP o EXPO en la UEFI.

**Ranuras PCIe** · x1 (red, sonido, Wi-Fi), x4 (NVMe), x8 (redes rápidas), x16 (gráfica). Cada versión duplica la velocidad y son compatibles entre sí.

**Almacenamiento** · HDD (~200 MB/s) → SSD SATA (~550 MB/s) → SSD NVMe PCIe 4.0 (~7.000 MB/s) → PCIe 5.0 (~14.000 MB/s).

**Tarjeta gráfica** · La GPU tiene miles de núcleos sencillos; la CPU, pocos y muy potentes. El monitor va siempre a la tarjeta gráfica.

**Fuente de alimentación** · ATX 24 pines → placa; EPS 8 pines (4+4) → procesador; PCIe 6+2 → gráfica; SATA → discos. Potencia = procesador + gráfica + 75 W + 30 % de margen.

**Refrigeración** · Silicio → IHS → pasta térmica → disipador → ventilador. Si se calienta demasiado: *thermal throttling* y, al final, apagado.
"""

HW_QUIZ = [
    q("¿Qué pieza une todas las demás y tiene unas pistas de cobre que forman los buses?",
      "La placa base",
      ["La fuente de alimentación", "El chipset", "La tarjeta gráfica"],
      "La placa base es un circuito impreso (PCB) con varias capas de pistas de cobre. Todo se conecta a ella, directa o indirectamente."),
    q("¿Qué formato de placa mide 305 × 244 mm, admite hasta 7 ranuras PCIe y es típico de sobremesa?",
      "ATX",
      ["Mini-ITX", "Micro-ATX", "E-ATX"],
      "ATX: 305 × 244 mm. E-ATX (305 × 330 mm) es para workstation, Micro-ATX (244 × 244 mm) para oficina y Mini-ITX (170 × 170 mm) para PC compacto."),
    q("¿Qué formato de placa elegirías para un PC compacto con una sola ranura PCIe?",
      "Mini-ITX",
      ["E-ATX", "ATX", "Micro-ATX"],
      "Mini-ITX mide 170 × 170 mm y tiene una sola ranura PCIe."),
    q("En un zócalo LGA, ¿dónde están los pines?",
      "En la placa base",
      ["En el procesador", "En el disipador", "En los módulos de RAM"],
      "En LGA el procesador tiene contactos planos y los pines están en el zócalo. En PGA, en cambio, los pines están en el procesador."),
    q("¿Qué tipo de zócalo es el AMD AM4?",
      "PGA",
      ["LGA", "BGA", "M.2"],
      "AM4 es PGA (pines en el procesador) y admite Ryzen 1000 a 5000. Si se doblan los pines, se estropea el micro. AM5, en cambio, es LGA."),
    q("¿Qué significa que un procesador sea BGA?",
      "Que está soldado a la placa y no se puede cambiar",
      ["Que tiene los pines en el procesador", "Que se coloca en un zócalo con palanca", "Que solo funciona con refrigeración líquida"],
      "BGA = procesador soldado. Es lo habitual en portátiles, miniPC, consolas y Raspberry Pi."),
    q("¿Qué procesadores admite un zócalo AMD AM5?",
      "Ryzen 7000 y 9000",
      ["Ryzen 1000 a 5000", "Core de 12ª, 13ª y 14ª generación", "Core Ultra 200S"],
      "AM5 (LGA): Ryzen 7000 y 9000. AM4: Ryzen 1000-5000. Intel LGA1700: Core 12ª-14ª. Intel LGA1851: Core Ultra 200S (desde 2024)."),
    q("Según la «regla de oro», ¿qué determina qué procesadores puedes montar?",
      "El zócalo de la placa (y que el chipset y la UEFI lo admitan)",
      ["Solo la cantidad de RAM", "Solo la potencia de la fuente", "El tamaño de la caja"],
      "La placa fija el zócalo, y el zócalo fija qué procesadores puedes montar. El chipset y la UEFI también tienen que admitirlo."),
    q("¿Qué ha pasado con el puente norte en los equipos actuales?",
      "Se ha integrado dentro del procesador",
      ["Se ha integrado en la fuente de alimentación", "Se ha movido a la tarjeta gráfica", "Ha desaparecido sin que nadie haga su función"],
      "El controlador de memoria, el PCIe y la gráfica integrada están ahora en la CPU. En la placa queda un solo chip: el chipset (PCH), unido por DMI/PCIe."),
    q("En las placas antiguas, ¿con qué se comunicaba el puente sur?",
      "USB, SATA, red y audio",
      ["La CPU y la RAM", "La CPU y la tarjeta gráfica", "La fuente de alimentación"],
      "El puente norte trataba con CPU, RAM y gráfica; el puente sur, con las tarjetas de red, el almacenamiento, los periféricos y los puertos."),
    q("¿Qué le pasa a la memoria RAM cuando se apaga el equipo?",
      "Pierde su contenido: es volátil",
      ["Conserva los datos indefinidamente", "Copia los datos a la UEFI", "Solo pierde los datos del sistema operativo"],
      "La RAM es volátil: guarda lo que se está usando y se borra al apagar. El almacenamiento (HDD, SSD, NVMe) conserva los datos sin corriente."),
    q("¿Qué afirmación sobre DDR5 frente a DDR4 es correcta?",
      "DDR5 es de 2021 y trabaja a 1,1 V",
      ["DDR5 es de 2014 y trabaja a 1,2 V", "Un módulo DDR4 entra sin problema en una placa DDR5", "DDR5 es más lenta que DDR4"],
      "DDR4: 2014, 1,2 V, 2133-3200 MT/s. DDR5: 2021, 1,1 V, 4800-8000 MT/s. La muesca es distinta, así que no son intercambiables."),
    q("Tienes que montar 16 GB de RAM con Dual Channel. ¿Qué configuración rinde más?",
      "2 módulos de 8 GB, uno en cada canal (A2 y B2)",
      ["1 módulo de 16 GB", "Da igual: rinden lo mismo", "Un módulo DDR4 y otro DDR5"],
      "Con Dual Channel el procesador accede a dos módulos a la vez: 2 × 8 GB rinde más que 1 × 16 GB."),
    q("¿Qué hay que activar en la UEFI para que la RAM funcione a su velocidad anunciada?",
      "XMP o EXPO",
      ["Secure Boot", "TPM 2.0", "PXE"],
      "Por defecto la RAM puede ir más lenta. El perfil XMP (Intel) o EXPO (AMD) la pone a su velocidad nominal."),
    q("¿Qué ranura PCIe usa normalmente una tarjeta gráfica?",
      "PCIe x16",
      ["PCIe x1", "PCIe x4", "PCIe x8"],
      "x1: red, sonido, Wi-Fi. x4: SSD NVMe. x8: tarjetas de red rápidas. x16: tarjeta gráfica. Cuantos más carriles, más larga la ranura."),
    q("¿Qué ocurre con las versiones de PCIe (3.0, 4.0, 5.0, 6.0)?",
      "Cada una duplica la velocidad y son compatibles: van a la velocidad de la más lenta",
      ["Cada una duplica la velocidad pero obliga a cambiar la placa", "Solo cambia el tamaño de la ranura", "Reducen el consumo, pero no la velocidad"],
      "En x16: PCIe 3.0 ≈ 15,8 GB/s, 4.0 ≈ 31,5 GB/s, 5.0 ≈ 63 GB/s y 6.0 ≈ 121 GB/s."),
    q("¿Qué almacenamiento se atornilla en la placa y usa carriles PCIe?",
      "SSD M.2 NVMe",
      ["Disco duro (HDD)", "SSD SATA con cable", "Memoria USB"],
      "El M.2 NVMe es el estándar para el disco del sistema. Ojo: hay SSD M.2 que son SATA por dentro, así que mira siempre la ficha."),
    q("¿Cuál es la velocidad de lectura aproximada de un HDD y de un SSD NVMe PCIe 4.0?",
      "200 MB/s y 7.000 MB/s",
      ["550 MB/s y 7.000 MB/s", "200 MB/s y 550 MB/s", "7.000 MB/s y 14.000 MB/s"],
      "HDD ≈ 200 MB/s, SSD SATA ≈ 550 MB/s, NVMe PCIe 4.0 ≈ 7.000 MB/s y NVMe PCIe 5.0 ≈ 14.000 MB/s."),
    q("¿En qué se diferencia una GPU de una CPU?",
      "La GPU tiene miles de núcleos sencillos que hacen la misma operación sobre muchos datos a la vez",
      ["La GPU tiene pocos núcleos muy potentes", "La GPU solo se encarga del audio", "La CPU tiene más núcleos que la GPU"],
      "CPU: pocos núcleos muy potentes para tareas variadas, una detrás de otra. GPU: miles de núcleos sencillos en paralelo."),
    q("Has instalado una gráfica dedicada y conectas el monitor al HDMI de la placa. ¿Qué es lo normal?",
      "No ver nada: el monitor va a la tarjeta gráfica",
      ["Ver la imagen perfectamente", "Que se apague el equipo", "Que se estropee la gráfica"],
      "El monitor siempre va a la tarjeta gráfica. Las salidas de la placa usan la gráfica integrada del procesador."),
    q("¿Qué conector de la fuente alimenta al procesador?",
      "EPS de 8 pines (4+4)",
      ["ATX de 24 pines", "PCIe de 6+2 pines", "SATA de corriente"],
      "ATX 24 pines: la placa. EPS 8 pines: el procesador. PCIe 6+2: la gráfica (150 W cada uno). SATA: discos duros y SSD SATA."),
    q("¿Qué certificación 80 PLUS indica la fuente más eficiente?",
      "Titanium (94 %)",
      ["Estándar (80 %)", "Bronze (85 %)", "Gold (90 %)"],
      "Eficiencias: Estándar 80 %, Bronze 85 %, Silver 88 %, Gold 90 %, Platinum 92 %, Titanium 94 %."),
    q("¿Cuánta pasta térmica hay que poner entre el procesador y el disipador?",
      "Una capa fina, del tamaño de un guisante",
      ["Una capa gruesa que cubra todo el zócalo", "Ninguna si el disipador es de cobre", "Solo en las aspas del ventilador"],
      "La pasta térmica rellena los microhuecos. Nunca hay que montar el disipador sin ella."),
    q("¿Qué es el thermal throttling?",
      "El procesador baja su velocidad para protegerse del calor",
      ["Una técnica para subir la frecuencia", "Un tipo de pasta térmica", "Un fallo de la fuente de alimentación"],
      "Si el procesador se calienta demasiado, reduce su velocidad (thermal throttling) y, en último caso, el equipo se apaga."),
    q("¿Qué conector interno tiene forma de L y es serie?",
      "SATA",
      ["IDE", "FDD", "PS/2"],
      "SATA (Serial ATA) tiene forma de L y es serie. El IDE es un conector paralelo y el FDD era para la disquetera (en desuso)."),
    q("Un conector de ventilador de 4 pines incluye PWM. ¿Para qué sirve?",
      "Para controlar la velocidad del ventilador",
      ["Para alimentar la tarjeta gráfica", "Para conectar el altavoz de la caja", "Para actualizar la UEFI"],
      "Los conectores FAN tienen 3 o 4 pines. Con 4 pines incluyen PWM, el control de velocidad. Siempre hay al menos uno para el ventilador de la CPU."),
    q("¿Qué velocidad corresponde a un puerto USB-A de color azul?",
      "5 Gb/s",
      ["10 Gb/s", "Solo USB 2.0", "2,5 Gb/s"],
      "Negro: USB 2.0. Azul: 5 Gb/s. Rojo o turquesa: 10 Gb/s. En USB-C, la forma no dice la velocidad."),
    q("¿Para qué sirve la pila CR2032 de la placa base?",
      "Mantiene la hora y la configuración",
      ["Alimenta el procesador", "Carga el disco duro", "Alimenta la tarjeta gráfica"],
      "Alimenta de forma continua el chip de la UEFI/BIOS. Si el reloj se atrasa, hay que cambiarla."),
]

HW_VF = [
    ("La memoria RAM conserva sus datos cuando se apaga el equipo.", False,
     "La RAM es volátil: se borra al apagar."),
    ("Un módulo DDR4 puede instalarse en una placa DDR5.", False,
     "No son intercambiables: la muesca es distinta."),
    ("Una tarjeta PCIe pequeña funciona en una ranura grande.", True,
     "Una tarjeta x1 funciona en una ranura x16, pero no al revés."),
    ("El EPS de 8 pines (CPU) y el PCIe de 8 pines (gráfica) son iguales.", False,
     "No lo son. Si no entra con suavidad, nunca fuerces un conector."),
    ("Con una gráfica dedicada, el monitor debe ir conectado a la tarjeta gráfica.", True,
     "Si se conecta al HDMI de la placa, lo normal es no ver nada."),
    ("El conector SATA es paralelo y el IDE es serie.", False,
     "Es al revés: SATA es serie (forma de L) e IDE es paralelo."),
    ("Los zócalos actuales de Intel y AMD AM5 son de tipo LGA.", True,
     "En LGA los pines están en la placa y el procesador tiene contactos planos."),
    ("Existen SSD M.2 que, por dentro, son SATA.", True,
     "Por eso hay que mirar siempre la ficha técnica."),
    ("Un disco duro (HDD) es más rápido que un SSD NVMe.", False,
     "Un HDD ronda los 200 MB/s; un NVMe PCIe 4.0, unos 7.000 MB/s."),
    ("En los equipos actuales el puente norte está dentro del procesador.", True,
     "En la placa queda un solo chip: el chipset."),
    ("La pasta térmica se aplica en una capa gruesa para que enfríe mejor.", False,
     "Se aplica una capa fina, del tamaño de un guisante."),
    ("Un procesador BGA se puede sustituir fácilmente por otro.", False,
     "Está soldado a la placa y no se puede cambiar."),
    ("La GPU tiene miles de núcleos sencillos, frente a los pocos y potentes de la CPU.", True,
     "Por eso la GPU es ideal para hacer la misma operación sobre muchos datos."),
    ("Un puerto USB-A negro es USB 2.0.", True,
     "Azul: 5 Gb/s. Rojo o turquesa: 10 Gb/s."),
]

HW_PLACA = [
    ("Zócalo", "Aloja el procesador"),
    ("Ranuras DIMM", "Alojan los módulos de memoria RAM"),
    ("Conector de 24 pines", "Alimentación de la placa base"),
    ("Ranura M.2", "Aloja un SSD NVMe"),
    ("Chipset", "Gestiona la comunicación con USB, SATA, red y audio"),
    ("Ranuras PCIe", "Tarjetas de expansión: gráfica, red, sonido..."),
    ("Pila CR2032", "Mantiene la hora y la configuración"),
    ("Puertos SATA", "Conectan discos duros y SSD SATA"),
    ("Panel trasero", "Conectores externos"),
    ("Conectores internos de la caja", "Botones, USB y audio frontales"),
]

HW_ZOCALOS = [
    ("Intel LGA1700", "Core de 12ª, 13ª y 14ª generación"),
    ("Intel LGA1851", "Core Ultra 200S (desde 2024)"),
    ("AMD AM4", "Ryzen 1000 a 5000"),
    ("AMD AM5", "Ryzen 7000 y 9000"),
    ("PGA", "Pines en el procesador"),
    ("LGA", "Pines en la placa"),
    ("BGA", "Procesador soldado"),
]

HW_FUENTE = [
    ("ATX 24 pines", "La placa base"),
    ("EPS 8 pines (4+4)", "El procesador"),
    ("PCIe 6+2 pines", "La gráfica (150 W cada uno)"),
    ("12V-2x6, 16 pines", "Gráficas actuales (hasta 600 W)"),
    ("SATA de corriente", "Discos duros y SSD SATA"),
]

HW_PCIE = [
    ("PCIe x1", "Red, sonido, Wi-Fi"),
    ("PCIe x4", "SSD NVMe (también en M.2)"),
    ("PCIe x8", "Tarjetas de red rápidas"),
    ("PCIe x16", "Tarjeta gráfica"),
]

HW_CONECTORES = [
    ("USB-A negro", "USB 2.0"),
    ("USB-A azul", "5 Gb/s"),
    ("USB-A rojo o turquesa", "10 Gb/s"),
    ("RJ-45", "Red por cable (Ethernet)"),
    ("PS/2", "Teclado o ratón antiguos"),
    ("Conector óptico S/PDIF", "Audio digital"),
    ("Jacks de 3,5 mm de colores", "Audio analógico"),
    ("Botón Clear CMOS", "Borra la configuración de la UEFI"),
]

HW_CALOR = [
    "Silicio (die): genera el calor",
    "IHS: tapa metálica del procesador",
    "Pasta térmica: rellena los microhuecos",
    "Disipador: aluminio o cobre, con heatpipes",
    "Ventilador: saca el calor al aire",
]

HW_BUSES = [
    "ISA",
    "PCI",
    "AGP",
    "PCI Express",
    "M.2",
]

HW_ALMACENAMIENTO = [
    "Disco duro (HDD)",
    "SSD SATA",
    "SSD NVMe PCIe 4.0",
    "SSD NVMe PCIe 5.0",
]


# =============================================================================
# 🚀 SECCIÓN 2 · EL ARRANQUE DEL ORDENADOR
# =============================================================================
BOOT_RESUMEN = """
**El problema** · Al encender, la RAM está vacía y el sistema operativo está en el disco, pero para leer el disco hace falta un programa. **Solución: el bootstrap**, arrancar por etapas; cada etapa prepara la siguiente.

| Fase | Qué ocurre |
|---|---|
| 1 · Encendido y firmware | Botón → la fuente se estabiliza (*Power Good*) → la CPU pone su contador de programa (PC) en una dirección fija → ejecuta la UEFI |
| 2 · POST | Comprueba CPU y registros, memoria RAM, gráfica y dispositivos. Si falla: pitidos, código en display o LED de diagnóstico |
| 3 · Dispositivo de arranque | Busca el disco según el orden de arranque (SSD → USB → red PXE → DVD) |
| 4 · Gestor de arranque | GRUB o Windows Boot Manager: localiza el kernel, lo carga en la RAM y le cede el control |
| 5 · Carga del kernel | El núcleo pasa a la RAM |
| 6 · Inicio del sistema | Drivers, memoria, primer proceso y servicios |
| 7 · Inicio de sesión | Ya puedes usar el equipo |

**BIOS vs UEFI** · BIOS: 16 bits, interfaz de texto, MBR (máx. 2 TB), sin seguridad, arranque más lento. UEFI: 32/64 bits, interfaz gráfica con ratón, GPT (discos enormes), Secure Boot y TPM, arranque más rápido.

**MBR** · Primer sector del disco (512 bytes): 446 de código de arranque + 64 de particiones + 2 de firma `55 AA`.
**UEFI · GPT** · Partición del sistema EFI (ESP): pequeña, en FAT32, con gestores como archivos `.efi`.

**Linux** · GRUB → kernel `vmlinuz` → `systemd` (proceso 1) → servicios → inicio de sesión.
**Windows** · Windows Boot Manager → `winload.efi` → kernel `ntoskrnl.exe` → `smss.exe` y servicios → inicio de sesión.

**Si no arranca** · Averigua en qué fase se ha parado y empieza por lo más sencillo y barato (cables, enchufe, piezas sueltas) antes de cambiar nada.
"""

BOOT_QUIZ = [
    q("Al encender, la RAM está vacía y el sistema operativo está en el disco. ¿Cómo se resuelve el problema?",
      "Con el bootstrap: se arranca por etapas y cada una carga la siguiente",
      ["Cargando el sistema operativo directamente desde el teclado", "Descargándolo de internet en cada arranque", "Con un programa que escribe el usuario a mano"],
      "Un programa pequeño grabado en la placa carga otro más grande, y ese carga el sistema operativo. Cada etapa prepara la siguiente."),
    q("¿Qué programa se ejecuta primero al encender el ordenador?",
      "El firmware (UEFI o BIOS)",
      ["El gestor de arranque", "El kernel del sistema operativo", "La pantalla de inicio de sesión"],
      "El firmware está grabado en un chip flash de la placa, en la dirección fija a la que apunta el contador de programa al encender."),
    q("Al encender, ¿qué registro de la CPU apunta siempre al firmware?",
      "El contador de programa (PC)",
      ["La unidad de control", "El chipset", "La pila CR2032"],
      "El PC es el registro que dice cuál es la siguiente instrucción. Al encender, apunta siempre al firmware."),
    q("¿Qué hace el POST?",
      "Comprueba el hardware: CPU, RAM, gráfica y periféricos",
      ["Instala el sistema operativo", "Carga el kernel en la RAM", "Pide el usuario y la contraseña"],
      "Es la autocomprobación inicial. Si algo falla, la placa avisa con pitidos, códigos en un display o LED de diagnóstico (CPU, DRAM, VGA, BOOT)."),
    q("Los ventiladores giran, no hay imagen y suenan pitidos. ¿En qué fase falla el arranque?",
      "2 · POST",
      ["1 · Encendido", "4 · Gestor de arranque", "7 · Inicio de sesión"],
      "Revisa la RAM mal encajada, la gráfica y el LED de diagnóstico. El significado de los pitidos depende del fabricante: búscalo en el manual."),
    q("Aparece «No bootable device». ¿Qué revisas?",
      "El orden de arranque y que el disco esté conectado y tenga sistema",
      ["La pila CR2032", "La pasta térmica", "Los ventiladores de la caja"],
      "Es un fallo de la fase 3 (dispositivo de arranque). También puede ser un USB olvidado que se arranca antes que el disco."),
    q("¿Qué hay en los dos últimos bytes del MBR?",
      "La firma 55 AA, en binario 01010101 10101010",
      ["La firma 55 AA, en binario 10101010 01010101", "La tabla de particiones, en binario 00000000 00000000", "El código de arranque, en binario 11111111 00000000"],
      "55 en hexadecimal es 01010101 y AA es 10101010. Esta firma indica que el disco es arrancable."),
    q("¿Cómo se reparten los 512 bytes del MBR?",
      "446 de código de arranque, 64 de particiones y 2 de firma",
      ["64 de código, 446 de particiones y 2 de firma", "256 de código, 254 de particiones y 2 de firma", "512 de código de arranque"],
      "446 + 64 + 2 = 512 bytes: código de arranque, tabla de particiones y firma 55 AA."),
    q("Con UEFI, ¿dónde busca el firmware el gestor de arranque?",
      "En la partición del sistema EFI (ESP), en FAT32, como archivos .efi",
      ["En el primer sector del disco (MBR)", "En la memoria RAM", "En la pila CR2032"],
      "Por ejemplo: `\\EFI\\Microsoft\\Boot\\bootmgfw.efi` o `\\EFI\\ubuntu\\grubx64.efi`."),
    q("¿Qué ventaja tiene GPT frente a MBR?",
      "Admite discos enormes (MBR llega como máximo a 2 TB)",
      ["Es más antiguo y compatible con todo", "Solo admite discos de 512 GB", "Funciona en modo de 16 bits"],
      "BIOS usa MBR (máximo 2 TB); UEFI usa GPT, que admite discos enormes."),
    q("¿Qué hace Secure Boot?",
      "Solo arranca software firmado y bloquea los virus que se cargan antes que el sistema",
      ["Guarda las claves de cifrado del equipo", "Permite arrancar cualquier programa sin comprobar", "Mantiene la hora cuando se desenchufa"],
      "Secure Boot es una característica de UEFI. Guardar claves de cifrado es función del TPM."),
    q("¿Qué es el TPM 2.0?",
      "Un módulo que guarda claves de cifrado y es obligatorio para Windows 11",
      ["El gestor de arranque de Linux", "Un tipo de memoria RAM", "La partición de arranque de UEFI"],
      "Junto con Secure Boot, forma parte de las medidas de seguridad de UEFI que la BIOS clásica no tenía."),
    q("Tienes Windows y Ubuntu en el mismo disco. ¿Quién te deja elegir al arrancar?",
      "El gestor de arranque (GRUB)",
      ["El POST", "El kernel", "La pila CR2032"],
      "Es el arranque dual: GRUB muestra un menú para elegir sistema o versión del kernel."),
    q("¿Qué proceso arranca primero en Linux y es el padre de todos los demás?",
      "systemd (proceso 1)",
      ["vmlinuz", "smss.exe", "winload.efi"],
      "Cadena en Linux: GRUB → kernel vmlinuz → systemd (proceso 1) → servicios → inicio de sesión."),
    q("En Windows, ¿cuál es el archivo del kernel?",
      "ntoskrnl.exe",
      ["winload.efi", "bootmgfw.efi", "smss.exe"],
      "Cadena en Windows: Windows Boot Manager → winload.efi → kernel ntoskrnl.exe → smss.exe y servicios → inicio de sesión."),
    q("Aparece «grub rescue>». ¿Qué ha fallado?",
      "El gestor de arranque: hay que repararlo desde un USB de instalación",
      ["La memoria RAM", "La pila CR2032", "La fuente de alimentación"],
      "Es un fallo de la fase 4 (gestor de arranque)."),
    q("Pantalla azul o «kernel panic» al cargar el sistema. ¿Qué haces?",
      "Arrancar en modo seguro y revisar el controlador o la actualización reciente",
      ["Cambiar la placa base", "Quitar la pila CR2032", "Cambiar la pasta térmica"],
      "Es un fallo de las fases 5-6 (sistema operativo), normalmente por un controlador o una actualización reciente."),
    q("La hora del ordenador se atrasa cada vez que lo desenchufas. ¿Qué cambias?",
      "La pila CR2032",
      ["La fuente de alimentación", "El disco duro", "La memoria RAM"],
      "La pila mantiene la hora y la configuración del firmware."),
    q("¿Qué teclas dan acceso al menú de arranque al encender?",
      "F12, F11 o F8, según la marca",
      ["Solo Supr", "Alt + F4", "Ctrl + Z"],
      "Para entrar en la configuración de la UEFI se usa Supr, F2 o F10 (también depende de la marca)."),
    q("El equipo no arranca. ¿Cuál es el mejor método?",
      "Averiguar en qué fase se ha parado y empezar por lo más sencillo y barato",
      ["Cambiar directamente la placa base", "Reinstalar siempre el sistema operativo", "Cambiar la fuente y la RAM a la vez"],
      "La fase te dice si el problema es del hardware, del disco o del sistema operativo. Primero cables, enchufe y piezas sueltas."),
]

BOOT_VF = [
    ("Al encender el ordenador, la RAM está vacía.", True,
     "Por eso hace falta el bootstrap: arrancar por etapas."),
    ("El firmware está grabado en un chip flash de la placa, por lo que se puede actualizar.", True,
     "Se puede actualizar, pero con cuidado."),
    ("La BIOS clásica trabaja en 16 bits y con interfaz de texto, solo con teclado.", True,
     "UEFI es de 32 o 64 bits y tiene interfaz gráfica con ratón."),
    ("El arranque con BIOS clásica es más rápido que con UEFI.", False,
     "Es al revés: UEFI arranca más rápido."),
    ("MBR permite discos de hasta 2 TB.", True,
     "GPT, en cambio, admite discos enormes."),
    ("Secure Boot permite arrancar cualquier software sin comprobarlo.", False,
     "Solo arranca software firmado."),
    ("LILO es el gestor de arranque estándar de Linux hoy en día.", False,
     "LILO era el gestor clásico y hoy está sustituido por GRUB."),
    ("Con UEFI, los gestores de arranque están en una partición pequeña en FAT32 llamada ESP.", True,
     "Son archivos con extensión .efi."),
    ("«No bootable device» indica un fallo en la fase del dispositivo de arranque.", True,
     "Revisa el orden de arranque, que el disco esté conectado y con sistema."),
    ("Si la hora se desajusta al desenchufar, el problema suele ser la pila CR2032.", True,
     "La pila mantiene la hora y la configuración."),
    ("El POST se ejecuta después de cargar el kernel.", False,
     "El POST es la fase 2, mucho antes de cargar el kernel."),
    ("El TPM 2.0 es obligatorio para Windows 11.", True,
     "Guarda claves de cifrado."),
]

BOOT_SINTOMAS = [
    ("No hace nada: ni luces ni ventiladores", "1 · Encendido"),
    ("Los ventiladores giran, no hay imagen y pita", "2 · POST"),
    ("«No bootable device» o «Reboot and select proper boot device»", "3 · Dispositivo de arranque"),
    ("Aparece «grub rescue>»", "4 · Gestor de arranque"),
    ("Pantalla azul o «kernel panic» al cargar", "5-6 · Sistema operativo"),
    ("La hora se desajusta al desenchufar", "Firmware (pila CR2032)"),
]

BOOT_BIOS_UEFI = [
    ("Trabaja en modo de 16 bits", "BIOS (Legacy)"),
    ("Trabaja en modo de 32 o 64 bits", "UEFI"),
    ("Interfaz de texto, solo con teclado", "BIOS (Legacy)"),
    ("Interfaz gráfica, con ratón", "UEFI"),
    ("Discos MBR, máximo 2 TB", "BIOS (Legacy)"),
    ("Discos GPT, enormes", "UEFI"),
    ("Sin medidas de seguridad", "BIOS (Legacy)"),
    ("Incluye Secure Boot y TPM", "UEFI"),
    ("Arranque más lento", "BIOS (Legacy)"),
    ("Arranque más rápido", "UEFI"),
]

BOOT_GESTORES = [
    ("GRUB", "El estándar de Linux: muestra un menú para elegir sistema o kernel"),
    ("Windows Boot Manager", "El gestor de Windows, integrado con la UEFI"),
    ("LILO", "Gestor clásico de Linux, hoy sustituido por GRUB"),
    ("MBR", "Primer sector del disco (512 bytes) con BIOS"),
    ("ESP", "Partición pequeña en FAT32 con los gestores .efi"),
    ("PXE", "Arranque por red"),
]

BOOT_FASES = [
    "Encendido y firmware",
    "POST",
    "Dispositivo de arranque",
    "Gestor de arranque",
    "Carga del kernel",
    "Inicio del sistema",
    "Inicio de sesión",
]

BOOT_ENCENDIDO = [
    "Pulsas el botón de encendido",
    "La fuente se estabiliza (Power Good)",
    "La CPU pone su contador de programa en una dirección fija",
    "Se ejecuta el firmware (UEFI)",
]

BOOT_LINUX = [
    "GRUB",
    "Kernel: vmlinuz",
    "systemd (proceso 1)",
    "Servicios",
    "Inicio de sesión",
]

BOOT_WINDOWS = [
    "Windows Boot Manager",
    "winload.efi",
    "Kernel: ntoskrnl.exe",
    "smss.exe y servicios",
    "Inicio de sesión",
]

BOOT_ORDEN_DISPOSITIVOS = [
    "SSD o disco interno",
    "Memoria USB",
    "Red (PXE)",
    "DVD",
]


# =============================================================================
# 📜 SECCIÓN 3 · SOFTWARE Y LICENCIAS
# =============================================================================
SW_RESUMEN = """
**Sistema operativo** · El software principal: gestiona el hardware, la memoria, los archivos y los programas, y hace de intermediario con el usuario (Windows 11, Ubuntu, macOS, Android, iOS).
**Software de aplicación** · Todo lo demás: los programas que usamos para tareas concretas (ofimática, navegadores, correo, videojuegos, IA...).
**La pila completa** · Hardware → Firmware → Sistema operativo → Aplicaciones → Personas.

**Software propietario** · El fabricante conserva todos los derechos. No compras el programa: compras permiso para usarlo. Código cerrado. Copiarlo o repartirlo suele estar prohibido.

**Software libre: cuatro libertades**
0. Usarlo para lo que quieras.
1. Estudiar cómo funciona.
2. Copiarlo y repartirlo.
3. Mejorarlo y publicar las mejoras.

> **Libre no significa gratis.** Hay programas gratis que no son libres, y se puede cobrar por software libre.

| Licencia | Qué te deja hacer | Ejemplo |
|---|---|---|
| Propietaria de pago | Usarlo pagando, una vez o por suscripción. Sin copiar ni modificar | Windows 11, Microsoft 365 |
| OEM | Viene con el equipo nuevo y solo vale para ese equipo | Windows de un portátil |
| Por volumen | Una clave para muchos equipos de una empresa o centro | Windows de las aulas |
| Freeware | Usarlo gratis, pero el código es cerrado | Acrobat Reader, Chrome |
| Shareware o de prueba | Probarlo un tiempo o con funciones limitadas; después se paga | WinRAR |
| Libre (GPL) | Usar, estudiar, copiar y mejorar. Las versiones modificadas siguen siendo libres | Linux, VLC |
"""

SW_QUIZ = [
    q("¿Cuál es el software principal que gestiona el hardware, la memoria, los archivos y los programas?",
      "El sistema operativo",
      ["El firmware", "El software de aplicación", "El gestor de arranque"],
      "El sistema operativo también hace de intermediario con el usuario."),
    q("¿Cuál de estos programas NO es un sistema operativo?",
      "LibreOffice",
      ["Ubuntu", "Android", "macOS"],
      "LibreOffice es una aplicación de ofimática. Windows 11, Ubuntu, macOS, Android e iOS son sistemas operativos."),
    q("¿Cuál es el orden correcto de la pila completa?",
      "Hardware → Firmware → Sistema operativo → Aplicaciones → Personas",
      ["Hardware → Sistema operativo → Firmware → Aplicaciones → Personas", "Firmware → Hardware → Aplicaciones → Sistema operativo → Personas", "Personas → Aplicaciones → Hardware → Firmware → Sistema operativo"],
      "Un sistema informático es hardware + software + personas; el firmware une los dos primeros."),
    q("En el software propietario, ¿qué compras realmente?",
      "El permiso para usarlo, no el programa",
      ["El código fuente", "El derecho a copiarlo y repartirlo", "El derecho a modificarlo"],
      "El fabricante conserva todos los derechos y el código es cerrado."),
    q("¿Cuál de estas NO es una de las cuatro libertades del software libre?",
      "Cobrar siempre por cada copia que se use",
      ["Estudiar cómo funciona", "Copiarlo y repartirlo", "Mejorarlo y publicar las mejoras"],
      "Las libertades son: usarlo para lo que quieras (0), estudiarlo (1), copiarlo y repartirlo (2), y mejorarlo y publicar las mejoras (3)."),
    q("¿Qué significa «libre» en software libre?",
      "Que respeta las libertades de usar, estudiar, copiar y mejorar; no tiene por qué ser gratis",
      ["Que siempre es gratis", "Que no tiene ninguna licencia", "Que no se puede cobrar por él"],
      "Libre no significa gratis: hay programas gratis que no son libres y se puede cobrar por software libre."),
    q("¿Qué es una licencia OEM?",
      "La que viene con el equipo nuevo y solo vale para ese equipo",
      ["Una clave para muchos equipos de una empresa", "Una licencia de prueba temporal", "Una licencia libre GPL"],
      "Ejemplo: el Windows 11 que venía en tu portátil."),
    q("¿Qué es una licencia por volumen?",
      "Una clave para muchos equipos de una empresa o centro",
      ["La que viene con un equipo nuevo", "Una licencia gratuita de código cerrado", "Una licencia para probar el programa"],
      "Ejemplo: el Windows de las aulas."),
    q("¿Cómo se llama el software que se usa gratis pero con código cerrado?",
      "Freeware",
      ["Shareware", "Libre (GPL)", "OEM"],
      "Ejemplos: Acrobat Reader y Chrome."),
    q("¿Qué es el shareware?",
      "Software que se puede probar un tiempo o con funciones limitadas y después se paga",
      ["Software gratuito de código abierto", "Software que solo vale para un equipo", "Software que se reparte con el sistema operativo"],
      "Ejemplo: WinRAR."),
    q("¿Qué garantiza la licencia GPL?",
      "Que las versiones modificadas siguen siendo libres",
      ["Que el programa es siempre gratis", "Que el código es cerrado", "Que solo vale para un equipo"],
      "Con GPL puedes usar, estudiar, copiar y mejorar, y las versiones modificadas deben seguir siendo libres. Ejemplos: Linux y VLC."),
    q("¿Qué tipo de licencia tiene el Windows 11 que venía en tu portátil?",
      "OEM",
      ["Por volumen", "Libre (GPL)", "Freeware"],
      "OEM: viene con el equipo nuevo y solo vale para ese equipo."),
    q("¿Cuál de estos programas es software libre?",
      "VLC",
      ["Photoshop", "Microsoft Office", "WinRAR"],
      "Linux, LibreOffice, Firefox y VLC son software libre. Windows, Microsoft Office y Photoshop son propietarios."),
]

SW_VF = [
    ("Software libre es lo mismo que software gratuito.", False,
     "Libre no significa gratis: se puede cobrar por software libre."),
    ("En el software propietario puedes ver y modificar el código.", False,
     "El código es cerrado: no puedes verlo ni cambiarlo."),
    ("Google Chrome es freeware: gratis, pero con código cerrado.", True,
     "Igual que Acrobat Reader."),
    ("Una licencia OEM sirve para instalar el programa en cualquier equipo.", False,
     "Solo vale para el equipo con el que se vendió."),
    ("LibreOffice es software libre.", True,
     "Como Linux, Firefox y VLC."),
    ("Windows, Microsoft Office y Photoshop son software propietario.", True,
     "El fabricante conserva todos los derechos."),
    ("El software de aplicación es todo el software que no es el sistema operativo.", True,
     "Ofimática, navegadores, correo, videojuegos, IA..."),
    ("WinRAR es un ejemplo de shareware.", True,
     "Se puede probar y después se paga."),
    ("Un sistema informático es solo hardware y software; las personas no cuentan.", False,
     "Es hardware + software + personas; el firmware une los dos primeros."),
    ("La licencia por volumen da una clave para muchos equipos de una empresa o centro.", True,
     "Ejemplo: el Windows de las aulas."),
]

SW_LICENCIAS = [
    ("Ubuntu", "Libre"),
    ("Windows 11 que venía en tu portátil", "OEM"),
    ("WinRAR", "Shareware o de prueba"),
    ("VLC", "Libre"),
    ("Google Chrome", "Freeware"),
    ("Microsoft 365", "Propietaria de pago"),
    ("LibreOffice", "Libre"),
    ("Adobe Acrobat Reader", "Freeware"),
]

SW_TIPOS_LICENCIA = [
    ("Propietaria de pago", "Usarlo pagando, una vez o por suscripción; sin copiar ni modificar"),
    ("OEM", "Viene con el equipo nuevo y solo vale para ese equipo"),
    ("Por volumen", "Una clave para muchos equipos de una empresa o centro"),
    ("Freeware", "Usarlo gratis, pero el código es cerrado"),
    ("Shareware o de prueba", "Probarlo un tiempo o con funciones limitadas; después se paga"),
    ("Libre (GPL)", "Usar, estudiar, copiar y mejorar; las versiones modificadas siguen siendo libres"),
]

SW_LIBERTADES = [
    ("Libertad 0", "Usarlo para lo que quieras"),
    ("Libertad 1", "Estudiar cómo funciona"),
    ("Libertad 2", "Copiarlo y repartirlo"),
    ("Libertad 3", "Mejorarlo y publicar las mejoras"),
]

SW_TIPOS_SOFTWARE = [
    ("Windows 11", "Sistema operativo"),
    ("Ubuntu", "Sistema operativo"),
    ("Android", "Sistema operativo"),
    ("iOS", "Sistema operativo"),
    ("Ofimática", "Software de aplicación"),
    ("Navegadores", "Software de aplicación"),
    ("Correo", "Software de aplicación"),
    ("Videojuegos", "Software de aplicación"),
]

SW_PILA = [
    "Hardware",
    "Firmware",
    "Sistema operativo",
    "Aplicaciones",
    "Personas",
]


# =============================================================================
# ESTRUCTURA GENERAL: secciones y juegos
# (el orden de esta lista es el orden en que aparecen en la app)
# =============================================================================
SECCIONES = {
    "hw": {
        "titulo": "Hardware por dentro",
        "icono": "🔧",
        "lema": "Abrimos la caja: placa base, procesador, memoria, almacenamiento, gráfica y alimentación.",
        "resumen": HW_RESUMEN,
        "juegos": [
            {"id": "hw_quiz", "tipo": "quiz", "icono": "❓", "nombre": "Quiz", "datos": HW_QUIZ, "n": 10,
             "descripcion": "10 preguntas al azar de un banco de más de 25."},
            {"id": "hw_vf", "tipo": "verdadero_falso", "icono": "✅", "nombre": "Verdadero o falso", "datos": HW_VF,
             "descripcion": "¿Verdadero o falso? Cuidado con las trampas."},
            {"id": "hw_placa", "tipo": "emparejar", "icono": "🧩", "nombre": "Partes de la placa base", "datos": HW_PLACA,
             "descripcion": "Une cada elemento de la placa base con su función."},
            {"id": "hw_zocalos", "tipo": "emparejar", "icono": "🧩", "nombre": "Zócalos y procesadores", "datos": HW_ZOCALOS,
             "descripcion": "Zócalos de Intel y AMD, y los tipos PGA, LGA y BGA."},
            {"id": "hw_fuente", "tipo": "emparejar", "icono": "🧩", "nombre": "Conectores de la fuente", "datos": HW_FUENTE,
             "descripcion": "¿Qué alimenta cada conector? Nunca fuerces uno."},
            {"id": "hw_pcie", "tipo": "emparejar", "icono": "🧩", "nombre": "Ranuras PCIe", "datos": HW_PCIE,
             "descripcion": "Cuantos más carriles, más larga la ranura."},
            {"id": "hw_conectores", "tipo": "emparejar", "icono": "🧩", "nombre": "Conectores del panel trasero", "datos": HW_CONECTORES,
             "descripcion": "USB por colores, red, audio, PS/2..."},
            {"id": "hw_calor", "tipo": "ordenar", "icono": "🔢", "nombre": "El camino del calor", "datos": HW_CALOR,
             "descripcion": "Ordena desde donde se genera el calor hasta donde sale."},
            {"id": "hw_buses", "tipo": "ordenar", "icono": "🔢", "nombre": "Evolución de las ranuras", "datos": HW_BUSES,
             "descripcion": "De la más antigua a la más moderna."},
            {"id": "hw_almacenamiento", "tipo": "ordenar", "icono": "🔢", "nombre": "Almacenamiento por velocidad", "datos": HW_ALMACENAMIENTO,
             "descripcion": "De más lento a más rápido (velocidad de lectura aproximada)."},
            {"id": "hw_calc", "tipo": "calculadora_fuente", "icono": "🧮", "nombre": "Calculadora de fuente", "datos": None,
             "descripcion": "Herramienta: ¿cuántos vatios necesito?"},
        ],
    },
    "boot": {
        "titulo": "El arranque del ordenador",
        "icono": "🚀",
        "lema": "Qué pasa desde que pulsas el botón hasta que aparece la pantalla de inicio de sesión.",
        "resumen": BOOT_RESUMEN,
        "juegos": [
            {"id": "boot_quiz", "tipo": "quiz", "icono": "❓", "nombre": "Quiz", "datos": BOOT_QUIZ, "n": 10,
             "descripcion": "10 preguntas al azar de un banco de 20."},
            {"id": "boot_vf", "tipo": "verdadero_falso", "icono": "✅", "nombre": "Verdadero o falso", "datos": BOOT_VF,
             "descripcion": "Firmware, BIOS, UEFI, MBR, POST..."},
            {"id": "boot_fases", "tipo": "ordenar", "icono": "🔢", "nombre": "Las 7 fases", "datos": BOOT_FASES,
             "descripcion": "Ordena las fases desde el botón de encendido hasta el inicio de sesión."},
            {"id": "boot_encendido", "tipo": "ordenar", "icono": "🔢", "nombre": "Fase 1: encendido", "datos": BOOT_ENCENDIDO,
             "descripcion": "¿Qué ocurre justo al pulsar el botón?"},
            {"id": "boot_linux", "tipo": "ordenar", "icono": "🐧", "nombre": "Arranque de Linux", "datos": BOOT_LINUX,
             "descripcion": "De GRUB al inicio de sesión."},
            {"id": "boot_windows", "tipo": "ordenar", "icono": "🪟", "nombre": "Arranque de Windows", "datos": BOOT_WINDOWS,
             "descripcion": "Del Windows Boot Manager al inicio de sesión."},
            {"id": "boot_orden", "tipo": "ordenar", "icono": "🔢", "nombre": "Orden de arranque", "datos": BOOT_ORDEN_DISPOSITIVOS,
             "descripcion": "El orden habitual de dispositivos de arranque."},
            {"id": "boot_sintomas", "tipo": "emparejar", "icono": "🩺", "nombre": "Diagnóstico de fallos", "datos": BOOT_SINTOMAS,
             "descripcion": "Une cada síntoma con la fase donde falla el arranque."},
            {"id": "boot_biosuefi", "tipo": "emparejar", "icono": "⚔️", "nombre": "BIOS contra UEFI", "datos": BOOT_BIOS_UEFI,
             "descripcion": "¿Característica de la BIOS clásica o de UEFI?"},
            {"id": "boot_gestores", "tipo": "emparejar", "icono": "🧩", "nombre": "Gestores y particiones", "datos": BOOT_GESTORES,
             "descripcion": "GRUB, Windows Boot Manager, LILO, MBR, ESP y PXE."},
        ],
    },
    "sw": {
        "titulo": "Software y licencias",
        "icono": "📜",
        "lema": "Tipos de software y licencias.",
        "resumen": SW_RESUMEN,
        "juegos": [
            {"id": "sw_quiz", "tipo": "quiz", "icono": "❓", "nombre": "Quiz", "datos": SW_QUIZ, "n": 8,
             "descripcion": "8 preguntas al azar de un banco de 13."},
            {"id": "sw_vf", "tipo": "verdadero_falso", "icono": "✅", "nombre": "Verdadero o falso", "datos": SW_VF,
             "descripcion": "Libre no significa gratis... ¿y qué más?"},
            {"id": "sw_licencias", "tipo": "emparejar", "icono": "🪪", "nombre": "¿Qué licencia tiene?", "datos": SW_LICENCIAS,
             "descripcion": "Une cada programa con su tipo de licencia."},
            {"id": "sw_tipos_licencia", "tipo": "emparejar", "icono": "🧩", "nombre": "Qué te deja hacer", "datos": SW_TIPOS_LICENCIA,
             "descripcion": "Une cada tipo de licencia con lo que permite."},
            {"id": "sw_libertades", "tipo": "emparejar", "icono": "🗽", "nombre": "Las cuatro libertades", "datos": SW_LIBERTADES,
             "descripcion": "Libertades 0, 1, 2 y 3 del software libre."},
            {"id": "sw_tipos", "tipo": "emparejar", "icono": "💻", "nombre": "Sistema operativo o aplicación", "datos": SW_TIPOS_SOFTWARE,
             "descripcion": "Clasifica cada ejemplo."},
            {"id": "sw_pila", "tipo": "ordenar", "icono": "🔢", "nombre": "La pila completa", "datos": SW_PILA,
             "descripcion": "Del hardware a las personas."},
        ],
    },
}
