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
# ESTILOS - PANTALLA COMPLETA RESPONSIVE
# ============================================================

st.markdown("""
<style>

/* ============================================================
   OCULTAR ELEMENTOS STREAMLIT
   ============================================================ */

#MainMenu,
header,
footer {
    visibility: hidden;
    height: 0;
}

/* ============================================================
   ELIMINAR ESPACIOS INNECESARIOS
   ============================================================ */

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
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

    width: 100% !important;
    max-width: 900px !important;

    height: 100vh !important;
    min-height: 100vh !important;

    box-sizing: border-box;

    padding-top: clamp(8px, 2vh, 25px) !important;
    padding-bottom: clamp(8px, 2vh, 20px) !important;
    padding-left: clamp(10px, 3vw, 25px) !important;
    padding-right: clamp(10px, 3vw, 25px) !important;

    overflow: hidden !important;
}

/* ============================================================
   CONTENEDOR DE LOGOS
   ============================================================ */

.logos {

    display: flex;

    justify-content: center;
    align-items: center;

    gap: clamp(15px, 4vw, 45px);

    width: 100%;

    height: clamp(45px, 10vh, 90px);

    margin-bottom: clamp(3px, 1vh, 10px);
}

.logo {

    width: auto;

    height: clamp(35px, 8vh, 75px);

    max-width: 150px;

    object-fit: contain;
}

/* ============================================================
   TITULO
   ============================================================ */

.titulo {

    text-align: center;

    font-size: clamp(
        22px,
        4.2vh,
        42px
    );

    font-weight: 900;

    color: #17345f;

    line-height: 1.05;

    margin: 0;
}

/* ============================================================
   SUBTITULO
   ============================================================ */

.subtitulo {

    text-align: center;

    font-size: clamp(
        14px,
        2.5vh,
        22px
    );

    font-weight: 500;

    color: #666;

    margin-top: clamp(2px, 0.8vh, 8px);
}

/* ============================================================
   MENSAJE SUPERIOR
   ============================================================ */

.mensaje {

    text-align: center;

    font-size: clamp(
        13px,
        2.3vh,
        20px
    );

    font-weight: 500;

    color: #666;

    line-height: 1.2;

    margin-top: clamp(5px, 1.5vh, 18px);

    margin-bottom: clamp(7px, 1.8vh, 20px);
}

/* ============================================================
   TARJETA
   ============================================================ */

.tarjeta {

    background: white;

    padding:
        clamp(15px, 3vh, 35px)
        clamp(15px, 3vw, 35px);

    border-radius: clamp(15px, 3vh, 28px);

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
        18px,
        3.4vh,
        29px
    );

    font-weight: 700;

    line-height: 1.15;

    margin-bottom: clamp(
        7px,
        1.5vh,
        18px
    );
}

/* ============================================================
   DESCRIPCIÓN
   ============================================================ */

.descripcion {

    font-size: clamp(
        13px,
        2.5vh,
        20px
    );

    color: #666;

    line-height: 1.35;

    margin-bottom: clamp(
        8px,
        1.8vh,
        22px
    );
}

/* ============================================================
   AVISO
   ============================================================ */

.aviso {

    background: #fff7d6;

    border: 2px solid #f0c419;

    border-radius: clamp(
        10px,
        2vh,
        16px
    );

    padding:
        clamp(10px, 2vh, 20px)
        clamp(10px, 2vw, 18px);

    margin:
        clamp(7px, 1.5vh, 18px)
        0
        clamp(10px, 2vh, 25px)
        0;

    font-size: clamp(
        12px,
        2.3vh,
        21px
    );

    line-height: 1.3;

    color: #333;

    box-sizing: border-box;
}

/* ============================================================
   TITULO DEL AVISO
   ============================================================ */

.aviso-titulo {

    font-size: clamp(
        15px,
        2.7vh,
        24px
    );

    font-weight: 800;

    margin-bottom: clamp(
        3px,
        0.8vh,
        8px
    );
}

/* ============================================================
   OPCIÓN TALLER
   ============================================================ */

.opcion {

    font-size: clamp(
        14px,
        2.8vh,
        25px
    );

    font-weight: 800;

    color: #1d4ed8;

    line-height: 1.2;

    margin-top: clamp(
        4px,
        1vh,
        10px
    );
}

/* ============================================================
   BOTÓN
   ============================================================ */

.boton {

    display: block;

    width: 100%;

    box-sizing: border-box;

    padding:
        clamp(12px, 2.5vh, 24px)
        10px;

    border-radius: clamp(
        10px,
        2vh,
        18px
    );

    background: #1d4ed8;

    color: white !important;

    text-decoration: none !important;

    font-size: clamp(
        16px,
        3.2vh,
        27px
    );

    font-weight: 800;

    text-align: center;
}

.boton:hover {

    background: #163ea8;
}

/* ============================================================
   PIE DE PÁGINA
   ============================================================ */

.pie {

    text-align: center;

    margin-top: clamp(
        6px,
        1.5vh,
        18px
    );

    color: #888;

    font-size: clamp(
        11px,
        1.8vh,
        15px
    );
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

        gap: 15px;

    }

    .logo {

        max-width: 115px;

    }

}

/* ============================================================
   PANTALLAS MUY BAJAS
   Ejemplo: celular horizontal
   ============================================================ */

@media (max-height: 650px) {

    .block-container {

        padding-top: 5px !important;
        padding-bottom: 5px !important;

    }

    .logos {

        height: 45px;

        margin-bottom: 2px;

    }

    .logo {

        height: 38px;

    }

    .mensaje {

        margin-top: 4px;

        margin-bottom: 6px;

    }

    .tarjeta {

        padding-top: 12px;

        padding-bottom: 12px;

    }

}

/* ============================================================
   PANTALLAS EXTREMADAMENTE BAJAS
   ============================================================ */

@media (max-height: 550px) {

    .logos {

        height: 35px;

    }

    .logo {

        height: 30px;

    }

    .mensaje {

        display: none;

    }

    .tarjeta {

        padding-top: 10px;

        padding-bottom: 10px;

    }

    .aviso {

        margin-top: 5px;

        margin-bottom: 8px;

        padding-top: 7px;

        padding-bottom: 7px;

    }

    .boton {

        padding-top: 10px;

        padding-bottom: 10px;

    }

    .pie {

        margin-top: 4px;

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
# CONVERTIR LOGOS
# ============================================================

auteco_b64 = imagen_base64(
    logo_auteco
)

dismerca_b64 = imagen_base64(
    logo_dismerca
)


# ============================================================
# LOGOS
# ============================================================

st.markdown(
    f"""
    <div class="logos">

        <img
            class="logo"
            src="data:image/png;base64,{auteco_b64}"
        >

        <img
            class="logo"
            src="data:image/png;base64,{dismerca_b64}"
        >

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITULO
# ============================================================

st.markdown(
    """
    <div class="titulo">
        Tu experiencia nos importa
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SEDE
# ============================================================

st.markdown(
    """
    <div class="subtitulo">
        Sede Lo Amador
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MENSAJE
# ============================================================

st.markdown(
    """
    <div class="mensaje">
        Ayúdanos a seguir mejorando nuestro servicio
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TARJETA PRINCIPAL
# ============================================================

st.markdown(
    """
    <div class="tarjeta">

        <div class="pregunta">
            ¿Quieres realizar nuestra encuesta?
        </div>

        <div class="descripcion">
            Tu opinión es muy importante para nosotros.<br>
            Solo te tomará unos segundos.
        </div>

        <div class="aviso">

            <div class="aviso-titulo">
                👉 IMPORTANTE
            </div>

            Al ingresar a la encuesta, cuando te solicite
            seleccionar el servicio que deseas evaluar:

            <div class="opcion">
                🏍️ Marca: TALLER - POSTVENTA
            </div>

            Esto permitirá que tu opinión sea registrada
            correctamente.

        </div>

        <a
            class="boton"
            href="https://impulsa-front.web.app/nps?sap=550018941"
        >
            INICIAR ENCUESTA
        </a>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PIE
# ============================================================

st.markdown(
    """
    <div class="pie">
        Gracias por confiar en nosotros ❤️
    </div>
    """,
    unsafe_allow_html=True
)