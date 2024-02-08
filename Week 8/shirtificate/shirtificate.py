from fpdf import FPDF

def getName():
    name = input("Name: ")
    return name

def createPDF(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(left = 0, top = 10)
    pdf.set_font("times", "B", size = 48)
    pdf.cell(txt = "CS50 Shirtificate\n", align = "C", w = 225, h = 40)
    pdf.ln(40)
    pdf.image("shirtificate.png")
    pdf.set_font("times", "B", size = 28)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(txt = f"{name} took CS50", align = "C", w = 215, h = -280)
    pdf.output("shirtificate.pdf")

def main():
    name = getName()
    createPDF(name)

main()