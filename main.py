import pandas as pd
from fpdf import FPDF


df = pd.read_csv('topics.csv')
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


pdf.output('output.pdf')
