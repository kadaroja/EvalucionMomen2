import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
uploaded_file = st.file_uploader("Cargar archivo 'educacion.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("static/datasets/educacion.csv")

st.title("Análisis de Datos de Educación en Colombia")
st.dataframe(df)

st.sidebar.header("Filtros")
nivel_educativo = st.sidebar.multiselect(
    "Nivel educativo", df["Nivel educativo"].unique()
)
carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())
institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

df_filtrado = df.copy()
if nivel_educativo:
    df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
if carrera:
    df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
if institucion:
    df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

st.dataframe(df_filtrado)


if not df_filtrado.empty:
    st.subheader("Estadísticas Descriptivas")
    st.write(df_filtrado.describe())


    # Conteo de estudiantes por nivel educativo
    st.subheader("Conteo de Estudiantes por Nivel Educativo")
    st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

    st.subheader("Distribución de la Edad")
    plt.hist(df_filtrado["Edad"], bins=10, alpha=0.7)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de la Edad")
    st.pyplot(plt)
else:
    st.write("No hay datos para mostrar con los filtros seleccionados.")

