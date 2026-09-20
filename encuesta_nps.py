import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Encuesta Dismerca",
    page_icon="🏍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS RESPONSIVE
# ============================================================

st.markdown("""
<style>

/* ============================================================
   OCULTAR ELEMENTOS DE STREAMLIT
   ============================================================ */

#MainMenu,
header,
footer {
    display: none !important;
}

/* ============================================================
   CUERPO
   ============================================================ */

html,
body {
    margin: 0 !important;
    padding: 0 !important;
}

/* ============================================================
   FONDO
   ============================================================ */

.stApp {
    background: linear-gradient(
        180deg,
        #f3f5f7 0%,
        #ffffff 100%
    );
}

/* ============================================================
   CONTENEDOR PRINCIPAL
   ============================================================ */

.block-container {

    max-width: 900px !important;

    width: 100% !important;

    height: 100vh !important;

    min-height: 100vh !important;

    box-sizing: border-box;

    padding-top: 10px !important;

    padding-bottom: 5px !important;

    padding-left: 15px !important;

    padding-right: 15px !important;

    overflow: hidden !important;
}


/* ============================================================
   LOGOS
   ============================================================ */

.logos {

    display: flex;

    justify-content: center;

    align-items: center;

    gap: clamp(
        20px,
        4vw,
        50px
    );

    height: clamp(
        70px,
        14vh,
        140px
    );

    margin-bottom: 4px;
}


/* ============================================================
   TAMAÑO DE LOS LOGOS
   ============================================================ */

.logo {

    height: clamp(
        70px,
        14vh,
        140px
    );

    width: auto;

    max-width: 290px;

    object-fit: contain;
}


/* ============================================================
   TITULO
   ============================================================ */

.titulo {

    text-align: center;

    font-size: clamp(
        23px,
        4vh,
        40px
    );

    font-weight: 900;

    color: #17345f;

    line-height: 1.05;

    margin: 0;
}


/* ============================================================
   SEDE
   ============================================================ */

.subtitulo {

    text-align: center;

    font-size: clamp(
        15px,
        2.4vh,
        22px
    );

    color: #666;

    margin-top: 4px;
}


/* ============================================================
   MENSAJE
   ============================================================ */

.mensaje {

    text-align: center;

    font-size: clamp(
        13px,
        2.1vh,
        20px
    );

    color: #666;

    margin-top: 8px;

    margin-bottom: 10px;

    line-height: 1.2;
}


/* ============================================================
   TARJETA
   ============================================================ */

.tarjeta {

    background: white;

    padding:
        clamp(14px, 2.5vh, 30px)
        clamp(15px, 3vw, 35px);

    border-radius:
        clamp(18px, 3vh, 28px);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.10);

    text-align: center;

    width: 100%;

    box-sizing: border-box;
}


/* ============================================================
   PREGUNTA
   ============================================================ */

.pregunta {

    font-size: clamp(
        19px,
        3vh,
        29px
    );

    font-weight: 700;

    line-height: 1.15;

    margin-bottom: 8px;
}


/* ============================================================
   DESCRIPCIÓN
   ============================================================ */

.descripcion {

    font-size: clamp(
        14px,
        2.2vh,
        20px
    );

    color: #666;

    line-height: 1.3;

    margin-bottom: 10px;
}


/* ============================================================
   AVISO
   ============================================================ */

.aviso {

    background: #fff7d6;

    border: 2px solid #f0c419;

    border-radius: 15px;

    padding:
        clamp(9px, 1.7vh, 18px)
        clamp(10px, 2vw, 18px);

    margin:
        8px 0
        clamp(10px, 1.8vh, 22px);

    font-size: clamp(
        12px,
        2vh,
        19px
    );

    line-height: 1.3;

    color: #333;

    box-sizing: border-box;
}


/* ============================================================
   TITULO AVISO
   ============================================================ */

.aviso-titulo {

    font-size: clamp(
        15px,
        2.5vh,
        23px
    );

    font-weight: 800;

    margin-bottom: 5px;
}


/* ============================================================
   OPCIÓN TALLER
   ============================================================ */

.opcion {

    font-size: clamp(
        14px,
        2.5vh,
        24px
    );

    font-weight: 800;

    color: #1d4ed8;

    line-height: 1.2;

    margin-top: 7px;
}


/* ============================================================
   BOTÓN
   ============================================================ */

.boton {

    display: block;

    width: 100%;

    box-sizing: border-box;

    padding:
        clamp(13px, 2.3vh, 22px)
        10px;

    border-radius: 16px;

    background: #1d4ed8;

    color: white !important;

    text-decoration: none !important;

    font-size: clamp(
        17px,
        2.8vh,
        27px
    );

    font-weight: 800;

    text-align: center;
}

.boton:hover {

    background: #163ea8;
}


/* ============================================================
   PIE
   ============================================================ */

.pie {

    text-align: center;

    margin-top: clamp(
        5px,
        1vh,
        12px
    );

    color: #888;

    font-size: clamp(
        11px,
        1.7vh,
        15px
    );
}


/* ============================================================
   QR
   ============================================================ */

.qr-container {

    display: flex;

    justify-content: center;

    align-items: center;

    width: 100%;

    margin-top: 5px;

    margin-bottom: 0;
}

.qr {

    width: clamp(
        65px,
        11vh,
        115px
    );

    height: auto;

    display: block;
}


/* ============================================================
   TABLET / CELULAR
   ============================================================ */

@media (max-width: 600px) {

    .block-container {

        padding-left: 10px !important;

        padding-right: 10px !important;
    }

    .logos {

        gap: 20px;
    }

    .logo {

        max-width: 230px;
    }
}


/* ============================================================
   PANTALLA BAJA
   ============================================================ */

@media (max-height: 700px) {

    .block-container {

        padding-top: 5px !important;

        padding-bottom: 3px !important;
    }

    .logos {

        height: 100px;

        margin-bottom: 2px;
    }

    .logo {

        height: 104px;

        max-width: 230px;
    }

    .mensaje {

        margin-top: 4px;

        margin-bottom: 6px;
    }

    .tarjeta {

        padding-top: 12px;

        padding-bottom: 12px;
    }

    .aviso {

        margin-top: 5px;

        margin-bottom: 10px;
    }

    .qr-container {

        margin-top: 3px;
    }

    .qr {

        width: 90px;
    }
}


/* ============================================================
   PANTALLA MUY BAJA
   ============================================================ */

@media (max-height: 580px) {

    .logos {

        height: 75px;
    }

    .logo {

        height: 75px;

        max-width: 180px;
    }

    .titulo {

        font-size: 22px;
    }

    .subtitulo {

        font-size: 14px;
    }

    .mensaje {

        font-size: 12px;

        margin: 3px 0;
    }

    .tarjeta {

        padding: 9px 12px;
    }

    .pregunta {

        font-size: 18px;

        margin-bottom: 4px;
    }

    .descripcion {

        font-size: 12px;

        margin-bottom: 5px;
    }

    .aviso {

        padding: 6px 8px;

        margin: 5px 0 7px;

        font-size: 11px;
    }

    .aviso-titulo {

        font-size: 14px;
    }

    .opcion {

        font-size: 13px;

        margin-top: 3px;
    }

    .boton {

        padding: 10px;

        font-size: 17px;
    }

    .pie {

        margin-top: 3px;

        font-size: 10px;
    }

    .qr-container {

        margin-top: 2px;
    }

    .qr {

        width: 65px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNCIÓN PARA CONVERTIR IMAGEN A BASE64
# ============================================================

def imagen_base64(imagen):

    buffer = BytesIO()

    imagen.save(
        buffer,
        format="PNG"
    )

    return base64.b64encode(
        buffer.getvalue()
    ).decode()


# ============================================================
# CARGAR LOGOS
# ============================================================

logo_auteco = Image.open(
    "logo3.png"
).convert("RGBA")

logo_dismerca = Image.open(
    "logo4.png"
).convert("RGBA")


# ============================================================
# CARGAR QR
# ============================================================

qr = Image.open(
    "qr.png"
).convert("RGBA")


# ============================================================
# CONVERTIR IMÁGENES
# ============================================================

auteco_b64 = imagen_base64(
    logo_auteco
)

dismerca_b64 = imagen_base64(
    logo_dismerca
)

qr_b64 = imagen_base64(
    qr
)


# ============================================================
# LOGOS
# ============================================================

st.markdown(
    f'<div class="logos">'
    f'<img class="logo" '
    f'src="data:image/png;base64,{auteco_b64}">'
    f'<img class="logo" '
    f'src="data:image/png;base64,{dismerca_b64}">'
    f'</div>',
    unsafe_allow_html=True
)


# ============================================================
# TITULO
# ============================================================

st.markdown(
    '<div class="titulo">'
    'Tu experiencia nos importa'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SEDE
# ============================================================

st.markdown(
    '<div class="subtitulo">'
    'Sede Lo Amador'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MENSAJE
# ============================================================

st.markdown(
    '<div class="mensaje">'
    'Ayúdanos a seguir mejorando nuestro servicio'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TARJETA PRINCIPAL
# ============================================================

st.markdown(
    '<div class="tarjeta">'

    '<div class="pregunta">'
    '¿Quieres realizar nuestra encuesta?'
    '</div>'

    '<div class="descripcion">'
    'Tu opinión es muy importante para nosotros.<br>'
    'Solo te tomará unos segundos.'
    '</div>'

    '<div class="aviso">'

    '<div class="aviso-titulo">'
    '👉 IMPORTANTE'
    '</div>'

    'Al ingresar a la encuesta, cuando te solicite '
    'seleccionar el servicio que deseas evaluar:'

    '<div class="opcion">'
    '🏍️ Marca: TALLER - POSTVENTA'
    '</div>'

    'Esto permitirá que tu opinión sea registrada '
    'correctamente.'

    '</div>'

    '<a class="boton" '
    'href="https://impulsa-front.web.app/nps?sap=550018941">'
    'INICIAR ENCUESTA'
    '</a>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MENSAJE FINAL
# ============================================================

st.markdown(
    '<div class="pie">'
    'Gracias por confiar en nosotros ❤️'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# QR
# ============================================================

st.markdown(
    f'<div class="qr-container">'
    f'<img class="qr" '
    f'src="data:image/png;base64,{qr_b64}">'
    f'</div>',
    unsafe_allow_html=True
)