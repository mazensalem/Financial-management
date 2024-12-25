from reportlab.pdfgen import canvas 

def get_name_location():
    pass


def savepdf(startdate, enddate, totalgained, totalspend, count):
    lines = [ 
f"from {startdate} to {enddate} ",
f"total transaction number: {count}",
f"total revenue gained: {totalgained}",
f"total amount spend: {totalspend}",
f"profit gained: {totalgained - totalgained}" 
    ]
    get_name_location()
    filename = "report.pdf"
    pdf = canvas.Canvas(filename)
    text = pdf.beginText(40, 680) 
    text.setFont("Courier", 18)
    
    for line in lines: 
        text.textLine(line) 
        
    pdf.drawText(text) 

    pdf.save()


savepdf("hi", "hi", 90, 60, "hi")
    