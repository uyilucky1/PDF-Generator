import pandas as pd
from fpdf import FPDF

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 21, 200, 21)

    pdf.ln(250)
    pdf.set_font(family='Times', style='B', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')
    for a in range(row['Pages'] - 1):
        pdf.add_page()


pdf.output('output.pdf')
