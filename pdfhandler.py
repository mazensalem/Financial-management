from reportlab.pdfgen import canvas 
from tkinter import filedialog

def get_name_location(parent):
    file = filedialog.asksaveasfilename(
        filetypes=[("pdf file", ".pdf")],
    defaultextension=".pdf", parent=parent)
    return file


def savepdf(startdate, enddate, totalgained, totalspend, count, parent):
    lines = [ 
f"from {startdate} to {enddate} ",
f"total transaction number: {count}",
f"total revenue gained: {totalgained}",
f"total amount spend: {totalspend}",
f"profit gained: {int(totalgained) - int(totalspend)}" 
    ]
    filename = get_name_location(parent)
    pdf = canvas.Canvas(filename)
    text = pdf.beginText(40, 680) 
    text.setFont("Courier", 18)
    
    for line in lines: 
        text.textLine(line) 
    pdf.drawText(text) 
    pdf.showPage()

    pdf.save()

    