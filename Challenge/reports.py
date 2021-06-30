#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    report.build(["<h1>Processed Updated on {}</h1><br></br><br></br>".format(title), paragraph])
    return report
