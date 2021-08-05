# pip install fpdf

from fpdf import FPDF

# [Orientación] "P" - vertial o portrait | "L" - horizontal o landscape
# [Unidades] "cm" - centímetros | "mm" - milímetros | "in" - pulgadas | "pt" - puntos
# [Formato] "A4" - casi tamaño carta | "Letter" - tamaño carta | "Legal" - tamaño oficio | "A<x>" - estándar A0, A1, A2, ...

pdf = FPDF(orientation="L", unit="in", format="A4")

pdf.add_page()

pdf.set_font(family="Arial", style="BIU", size=24)

pdf.cell(w=0, h=1, txt="Hello world!", border=1, ln=1, align="C", fill=0, link="https://google.com")

pdf.set_font(family="Times", style="I", size=12)

pdf.cell(w=0, h=1, txt="Hola mundo!", border=0, ln=1, align="R", fill=0, link=None)
pdf.cell(w=0, h=1, txt="¿Cómo estás?", border=0, ln=0, align="R", fill=0, link=None)

pdf.output("reportes/hello_world.pdf")