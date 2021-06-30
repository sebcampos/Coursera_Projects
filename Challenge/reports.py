#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    report.build([Paragraph("<h1>Processed Updated on {}</h1><br></br><br></br>".format(title)), Paragraph(paragraph])])
    return report
