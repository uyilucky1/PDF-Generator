import base64

import streamlit as st
import pandas as pd
from fpdf import FPDF


def generate_pdf(df):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)

    for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=24)
        pdf.set_text_color(10, 100, 10)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Set Footer
        pdf.ln(265)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(10, 180, 10)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R')
        for a in range(row['Pages'] - 1):
            pdf.add_page()

            # Set Footer
            pdf.ln(277)
            pdf.set_font(family='Times', style='I', size=8)
            pdf.set_text_color(10, 180, 10)
            pdf.cell(w=0, h=12, txt=row['Topic'], align='R')
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)

    return pdf


def main():
    st.markdown('<h1 style="color: red;">PDF Generator App</h1>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        if st.button("Generate PDF"):
            pdf = generate_pdf(df)
            output_file_path = 'output.pdf'
            pdf.output(output_file_path)
            st.success(f"PDF generated successfully!")

            # Display a link to download the PDF
            st.markdown(get_download_link(output_file_path), unsafe_allow_html=True)


def get_download_link(file_path):
    """Generates a download link for the given file."""
    with open(file_path, "rb") as file:
        data = file.read()
    b64_data = base64.b64encode(data).decode()
    return f'<a href="data:application/pdf;base64,{b64_data}" download="output.pdf">Click here to download the file</a>'


if __name__ == "__main__":
    main()
