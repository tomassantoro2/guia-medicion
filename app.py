import streamlit as st
from fpdf import FPDF
import datetime

st.set_page_config(page_title="Generador de Guía de Medición", layout="centered")

st.title("📏 Generador de Guía de Medición")
st.write("Completa los datos y descarga la guía en PDF.")

# --- FORMULARIO ---
with st.form("formulario"):
    codigo = st.text_input("Código de producto")
    nombre = st.text_input("Nombre del producto")
    altura = st.text_input("Altura (cm)")
    ancho = st.text_input("Ancho (cm)")
    largo = st.text_input("Largo (cm)")
    observaciones = st.text_area("Observaciones")
    fecha = st.date_input("Fecha", datetime.date.today())

    generar = st.form_submit_button("Generar PDF")

# --- PDF ---
if generar:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Guía de Medición", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 8, txt=f"Fecha: {fecha}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 8, txt=f"Código del producto: {codigo}", ln=True)
    pdf.cell(200, 8, txt=f"Nombre: {nombre}", ln=True)
    pdf.cell(200, 8, txt=f"Altura: {altura} cm", ln=True)
    pdf.cell(200, 8, txt=f"Ancho: {ancho} cm", ln=True)
    pdf.cell(200, 8, txt=f"Largo: {largo} cm", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 8, txt=f"Observaciones:\n{observaciones}")

    filename = f"guia_{codigo}.pdf"
    pdf.output(filename)

    with open(filename, "rb") as f:
        st.download_button("⬇ Descargar PDF", f, file_name=filename)
