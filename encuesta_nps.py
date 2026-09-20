import streamlit as st

st.set_page_config(
    page_title="Encuesta Dismerca",
    page_icon="🏍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

#MainMenu, header, footer {
    visibility: hidden;
}

.stApp {
    background: linear-gradient(
        180deg,
        #f3f5f7 0%,
        #ffffff 100%
    );
}

.block-container {
    max-width: 750px;
    padding-top: 50px;
}

.icono {
    text-align: center;
    font-size: 75px;
}

.titulo {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
}

.subtitulo {
    text-align: center;
    font-size: 22px;
    color: #666;
    margin-bottom: 40px;
}

.tarjeta {
    background: white;
    padding: 45px 35px;
    border-radius: 28px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.10);
    text-align: center;
}

.pregunta {
    font-size: 29px;
    font-weight: 700;
    margin-bottom: 20px;
}

.descripcion {
    font-size: 20px;
    color: #666;
    line-height: 1.5;
    margin-bottom: 25px;
}

.aviso {
    background: #fff7d6;
    border: 2px solid #f0c419;
    border-radius: 16px;
    padding: 20px 18px;
    margin: 20px 0 30px 0;
    font-size: 21px;
    line-height: 1.5;
    color: #333;
}

.aviso-titulo {
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 8px;
}

.opcion {
    font-size: 25px;
    font-weight: 800;
    color: #1d4ed8;
    margin-top: 10px;
}

.boton {
    display: block;
    width: 100%;
    padding: 24px 10px;
    border-radius: 18px;
    background: #1d4ed8;
    color: white !important;
    text-decoration: none !important;
    font-size: 27px;
    font-weight: 800;
}

.boton:hover {
    background: #163ea8;
}

.pie {
    text-align: center;
    margin-top: 30px;
    color: #888;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CONFIGURACIÓN DE LOGOS Y FRASE
# ============================================================

TAMANO_LOGO_AUTECO = 90
TAMANO_LOGO_DISMERCA = 90

# Espacio entre AUTECO y la frase
ESPACIO_FRASE = 300

# Configuración del texto
TAMANO_TEXTO = 16
NEGRILLA = 700
ALTURA_LINEA = 1.2
COLOR_TEXTO = "#555555"


# ============================================================
# LOGOS + FRASE
# ============================================================

with col1:

    logo_col1, texto_col, logo_col2 = st.columns(
        [1, 1.8, 1],
        vertical_alignment="center"
    )

    # --------------------------------------------------------
    # AUTECO
    # --------------------------------------------------------
    with logo_col1:
        st.image(
            "logo3.png",
            width=TAMANO_LOGO_AUTECO
        )

    # --------------------------------------------------------
    # FRASE
    # --------------------------------------------------------
    with texto_col:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:{TAMANO_TEXTO}px;
                font-weight:{NEGRILLA};
                color:{COLOR_TEXTO};
                line-height:{ALTURA_LINEA};
                margin-left:{ESPACIO_FRASE}px;
                white-space:nowrap;
            ">
                TU EXPERIENCIA NOS IMPORTA
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # DISMERCA
    # --------------------------------------------------------
    with logo_col2:
        st.image(
            "logo4.png",
            width=TAMANO_LOGO_DISMERCA
        )
# -------------------------------------------------------logo.png-----
# TITULO CENTRAL
# ------------------------------------------------------------

with col2:

    st.markdown(
        "<div style='text-align:center; "
        "font-size:42px; "
        "font-weight:900; "
        "color:#17345f; "
        "line-height:1.1;'>"
        "Tu experiencia nos importa"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='text-align:center; "
        "font-size:22px; "
        "font-weight:500; "
        "color:#666; "
        "margin-top:8px;'>"
        "Sede Lo Amador"
        "</div>",
        unsafe_allow_html=True
    )

# ============================================================
# MENSAJE INFERIOR
# ============================================================

st.markdown(
    "<div style='text-align:center; "
    "font-size:20px; "
    "font-weight:500; "
    "color:#666; "
    "margin-top:20px; "
    "margin-bottom:30px;'>"
    "Ayúdanos a seguir mejorando nuestro servicio"
    "</div>",
    unsafe_allow_html=True
)

st.markdown("""
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

<a class="boton"
href="https://impulsa-front.web.app/nps?sap=550018941">
INICIAR ENCUESTA
</a>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="pie">Gracias por confiar en nosotros ❤️</div>',
    unsafe_allow_html=True
)