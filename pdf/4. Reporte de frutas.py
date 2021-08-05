# pip install fpdf

from fpdf import FPDF

pdf = FPDF(unit="pt")

page_width = 595
page_height = 842

pdf.add_page()

pdf.set_left_margin(24)
pdf.set_right_margin(24)

pdf.set_font("Times", style="B", size=24)

pdf.cell(0, h=24, txt="Reporte de Frutas", align="C", ln=1)

pdf.ln(48)

pdf.set_font("Times", style="B", size=12)

pdf.cell((page_width - 48) / 3, h=16, txt="Fruta", align="C", border=1, ln=0)
pdf.cell((page_width - 48) / 3, h=16, txt="Peso", align="C", border=1, ln=0)
pdf.cell((page_width - 48) / 3, h=16, txt="Color", align="C", border=1, ln=1)

pdf.set_font("Times", style="", size=12)

pdf.cell((page_width - 48) / 3, h=16, txt="Manzana", align="L", border=1, ln=0)
pdf.cell((page_width - 48) / 3, h=16, txt="60g", align="C", border=1, ln=0)
pdf.cell((page_width - 48) / 3, h=16, txt="Rojo", align="C", border=1, ln=1)

pdf.cell((page_width - 48) / 3, h=16, txt="Mango", align="L", border=1, ln=0)
pdf.cell((page_width - 48) / 3, h=16, txt="80g", align="C", border=1, ln=0)
pdf.cell((page_width - 48) / 3, h=16, txt="Amarillo", align="C", border=1, ln=1)

pdf.ln(24)

pdf.cell(page_width - 48, h=1, txt="", align="C", border=1, ln=1)

pdf.ln(24)

pdf.image("reportes/imagenes/manzana.png", h=128, x=pdf.get_x(), y=pdf.get_y())

pdf.set_font("Arial", style="B", size=16)

pdf.set_y(pdf.get_y() + (128 - 16 * 3) / 2)
pdf.set_x((page_width - 48) / 3)
pdf.cell(0, h=16, txt="Manzana 60g", align="L", border=0, ln=1)
pdf.ln(16)
pdf.set_font("Arial", style="", size=16)
pdf.set_x((page_width - 48) / 3)
pdf.cell(0, h=16, txt="Descripción: Rojo", align="L", border=0, ln=1)
pdf.set_y(pdf.get_y() + (128 - 16 * 3) / 2)

pdf.ln(16)
pdf.cell(page_width - 48, h=1, txt="", align="C", border=1, ln=1)

pdf.ln(24)

pdf.image("reportes/imagenes/mango.png", h=128, x=pdf.get_x(), y=pdf.get_y())

pdf.set_font("Arial", style="B", size=16)

pdf.set_y(pdf.get_y() + (128 - 16 * 3) / 2)
pdf.set_x((page_width - 48) / 3)
pdf.cell(0, h=16, txt="Mango 80g", align="L", border=0, ln=1)
pdf.ln(16)
pdf.set_font("Arial", style="", size=16)
pdf.set_x((page_width - 48) / 3)
pdf.cell(0, h=16, txt="Descripción: Amarillo", align="L", border=0, ln=1)
pdf.set_y(pdf.get_y() + (128 - 16 * 3) / 2)

pdf.ln(16)
pdf.cell(page_width - 48, h=1, txt="", align="C", border=1, ln=1)

pdf.ln(24)

pdf.output("reportes/reporte_frutas.pdf")