from fpdf import FPDF


def main():
    name = input("What is your name? ")
    name =  name + " took CS50"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 36)
    pdf.cell(h=50, text="CS50 Shirtificate", center=True, align="C")
    pdf.image("shirtificate.png", x="C", y=60)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(h=250, text=name, center=True, align="C")
    pdf.output("shirtificate.pdf")
    


if __name__ == "__main__":
    main()
