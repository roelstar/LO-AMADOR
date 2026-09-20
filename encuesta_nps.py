import streamlit as st
import base64

st.set_page_config(
    page_title="Encuesta Dismerca",
    page_icon="🏍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# FUNCIÓN PARA MOSTRAR LOS LOGOS
# ============================================================

def imagen_base64(ruta):
    with open(ruta, "rb") as archivo:
        return base64.b64encode(archivo.read()).decode()

logo_auteco = imagen_base64("logo3.png")
logo_dismerca = imagen_base64("logo4.png")

# ============================================================
# ESTILO
# ============================================================

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
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    padding: 35px 20px 40px 20px;
    box-sizing: border-box;
}

/* ============================================================
   ENCABEZADO RESPONSIVE
   ============================================================ */

.encabezado {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 35px;
    margin: 0 auto;
    box-sizing: border-box;
}

.logo-empresa {
    width: 150px;
    height: auto;
    max-width: 22%;
    object-fit: contain;
}

.titulo-centro {
    flex: 1;
    min-width: 0;
    text-align: center;
    font-size: clamp(32px, 5vw, 42px);
    font-weight: 900;
    color: #17345f;
    line-height: 1.1;
}

.sede {
    text-align: center;
    font-size: clamp(19px, 3vw, 22px);
    font-weight: 500;
    color: #666;
    margin-top: 10px;
}

/* ============================================================
   MENSAJE INFERIOR
   ============================================================ */

.mensaje-inferior {
    width: 100%;
    text-align: center;
    font-size: clamp(18px, 3vw, 20px);
    font-weight: 500;
    color: #666;
    margin-top: 25px;
    margin-bottom: 30px;
    line-height: 1.4;
}

/* ============================================================
   TARJETA
   ============================================================ */

.tarjeta {
    width: 100%;
    box-sizing: border-box;
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
    box-sizing: border-box;
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

/* ============================================================
   CELULARES
   ============================================================ */

@media (max-width: 600px) {

    .block-container {
        padding: 25px 15px 30px 15px;
    }

    .encabezado {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
    }

    .logo-empresa {
        width: 110px;
        max-width: 40%;
    }

    .titulo-centro {
        order: 3;
        flex-basis: 100%;
        font-size: 34px;
        line-height: 1.08;
        margin-top: 8px;
    }

    .sede {
        font-size: 20px;
        margin-top: 8px;
    }

    .mensaje-inferior {
        font-size: 19px;
        margin-top: 22px;
        margin-bottom: 25px;
    }

    .tarjeta {
        padding: 30px 20px;
        border-radius: 24px;
    }

    .pregunta {
        font-size: 25px;
    }

    .descripcion {
        font-size: 18px;
    }

    .aviso {
        font-size: 18px;
        padding: 18px 14px;
    }

    .aviso-titulo {
        font-size: 22px;
    }

    .opcion {
        font-size: 22px;
    }

    .boton {
        font-size: 23px;
        padding: 21px 10px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# ENCABEZADO
# ============================================================

st.markdown(f"""
<div class="encabezado">

    <img
        src="data:image/png;base64,{logo_auteco}"
        class="logo-empresa"
    >

    <div class="titulo-centro">

        Tu experiencia nos importa

        <div class="sede">
            Sede Lo Amador
        </div>

    </div>

    <img
        src="data:image/png;base64,{logo_dismerca}"
        class="logo-empresa"
    >

</div>
""", unsafe_allow_html=True)


# ============================================================
# MENSAJE INFERIOR
# ============================================================

st.markdown("""
<div class="mensaje-inferior">
    Ayúdanos a seguir mejorando nuestro servicio
</div>
""", unsafe_allow_html=True)


# ============================================================
# TARJETA PRINCIPAL
# ============================================================

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


# ============================================================
# PIE
# ============================================================

st.markdown(
    '<div class="pie">Gracias por confiar en nosotros ❤️</div>',
    unsafe_allow_html=True
)