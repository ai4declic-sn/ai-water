import pickle
from time import sleep

import pandas as pd
import stqdm
import streamlit as st
from PIL import Image
from stqdm import stqdm
from streamlit_option_menu import option_menu


@st.cache_resource
def load_model():
    with open("assets/model.pkl", "rb") as f:
        return pickle.load(f)


st.set_page_config(
    page_title="Open Knowledge Senegal", page_icon="🇸🇳", initial_sidebar_state="expanded"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#FF4C1B"},
}

# Loading assets
img_banner = Image.open("assets/images/laptop_realistic_2.jpg")
img_banner2 = Image.open("assets/images/ias-logo.png")
img_rwanda = Image.open("assets/images/ias-logo.png")


def home_page():
    st.write("""# Système d'inspection de l'eau""", unsafe_allow_html=True)
    st.image(img_banner)

    st.write(
        """<h2>Le Problème</h2>
    <p>L'accès à l'eau potable est un défi crucial dans de nombreuses parties du monde, y compris au Rwanda. La prédiction de la qualité de l'eau est importante pour garantir la disponibilité d'une eau sûre et propre pour la boisson, l'agriculture et d'autres usages. Cependant, les méthodes traditionnelles de prédiction de la qualité de l'eau sont souvent longues et coûteuses, et elles peuvent ne pas fournir des informations précises et opportunes. Pour relever ce défi, le chapitre rwandais d'Omdena a lancé un projet pour développer un système automatisé de prédiction de la qualité de l'eau utilisant l'apprentissage automatique.</p> """,
        unsafe_allow_html=True,
    )

    st.write(
        """<h2>Objectifs du projet</h2> <p>L'objectif principal du chapitre rwandais d'Omdena dans ce projet est de développer un modèle d'apprentissage automatique précis et efficace capable de prédire la qualité de l'eau à partir d'une gamme de paramètres tels que la conductivité électrique de l'eau, la quantité de carbone organique en ppm, la quantité de trihalométhanes en μg/L, et la turbidité. Le modèle sera entraîné sur un large ensemble de données historiques sur la qualité de l'eau et sera conçu pour fournir des prédictions sur la qualité de l'eau.</p> """,
        unsafe_allow_html=True,
    )
    st.image(Image.open("assets/images/accuracy.png"))


def about_page():
    st.write("""<h1>Project background</h1>""", unsafe_allow_html=True)
    st.image(img_banner2)
    st.write(
        """
    """,
        unsafe_allow_html=True,
    )


def model_section():
    st.write(
        """<h1>Prédire la qualité de l'eau</h1>
    <p>Entrez ces valeurs des paramètres pour savoir si la qualité de l'eau est potable ou non.</p><hr>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        ColourTCU = st.number_input(
            label="Colour (TCU)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider0",
        )
        TurbidityNTU = st.number_input(
            label="Turbidity (NTU)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider1",
        )
        pH = st.number_input(
            label="pH", min_value=0.0, max_value=1000.0, step=50.0, format="%f", key="test_slider2"
        )
        ConductivityuS = st.number_input(
            label="Conductivity (uS/cm)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider3",
        )
        TotalDissolvedSolids = st.number_input(
            label="Total Dissolved Solids (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider4",
        )
        TotalHardness = st.number_input(
            label="Total Hardness (mg/l as CaCO3)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider5",
        )

    with col2:
        Aluminium = st.number_input(
            label="Aluminium (mg/l)",
            min_value=0.0,
            max_value=1000.5,
            step=50.1,
            format="%f",
            key="test_slider6",
        )
        Chloride = st.number_input(
            label="Chloride (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider7",
        )
        Iron = st.number_input(
            label="Iron (mg/l)",
            min_value=0.0,
            max_value=1000.5,
            step=50.1,
            format="%f",
            key="test_slider8",
        )
        Sodium = st.number_input(
            label="Sodium (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider9",
        )
        Sulphate = st.number_input(
            label="Sulphate (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider10",
        )
        Zinc = st.number_input(
            label="Zinc (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider11",
        )

    with col3:
        Magnesium = st.number_input(
            label="Magnesium (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider12",
        )
        Calcium = st.number_input(
            label="Calcium (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider13",
        )
        Potassium = st.number_input(
            label="Potassium (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider14",
        )
        Nitrate = st.number_input(
            label="Nitrate (mg/l)",
            min_value=0.0,
            max_value=1000.0,
            step=50.0,
            format="%f",
            key="test_slider15",
        )
        Phosphate = st.number_input(
            label="Phosphate (mg/l)",
            min_value=0.0,
            max_value=1000.2,
            step=50.1,
            format="%f",
            key="test_slider16",
        )
        st.write("<br>", unsafe_allow_html=True)
        predict_button = st.button("  Predict Water Quality  ")

    dataframe = pd.DataFrame(
        {
            "Colour (TCU)": [ColourTCU],
            "Turbidity (NTU)": [TurbidityNTU],
            "pH": [pH],
            "Conductivity (uS/cm)": [ConductivityuS],
            "Total Dissolved Solids (mg/l)": [TotalDissolvedSolids],
            "Total Hardness (mg/l as CaCO3)": [TotalHardness],
            "Aluminium (mg/l)": [Aluminium],
            "Chloride (mg/l)": [Chloride],
            "Total Iron (mg/l)": [Iron],
            "Sodium (mg/l)": [Sodium],
            "Sulphate (mg/l)": [Sulphate],
            "Zinc (mg/l)": [Zinc],
            "Magnesium (mg/l)": [Magnesium],
            "Calcium (mg/l)": [Calcium],
            "Potassium (mg/l)": [Potassium],
            "Nitrate (mg/l)": [Nitrate],
            "Phosphate (mg/l)": [Phosphate],
        }
    )

    if predict_button:
        model = load_model()
        result = model.predict(dataframe)
        for _ in stqdm(range(50)):
            sleep(0.015)
        if result[0] == 1.0:
            st.error("This Water Quality is Non-Potable")
        else:
            st.success("This Water Quality is Potable")


def contributors_page():
    st.write(
        """

            """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.image(img_rwanda)
    selected = option_menu(
        menu_title=None,
        options=["Home", "Check Water Quality", "About", "Contributors"],
        icons=["house", "droplet", "info-circle", "people"],
        styles=css_style,
    )

if selected == "Home":
    home_page()


elif selected == "Check Water Quality":
    model_section()

elif selected == "About":
    about_page()

elif selected == "Contributors":
    contributors_page()
