from fpdf import FPDF

pdf = FPDF("P", "in", "A4")
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(1, 1, 'Hello World!')
pdf.ln()
width = 8.3
x = (width - 4) / 2
pdf.image("reportes/graficas/g1.png", x=x, w=4, h=4)
pdf.set_font('Arial', 'I', 11)
pdf.cell(0, 1, 'Descripción de la imagen', 1)
pdf.output('reportes/test.pdf', 'F')