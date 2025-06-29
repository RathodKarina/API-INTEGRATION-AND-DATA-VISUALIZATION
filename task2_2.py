import pandas as pd
from fpdf import FPDF
from datetime import datetime

# Load data from CSV
df = pd.read_csv("data.csv")

# Group by department and get average score
summary = df.groupby("City")["Age"].agg(["count", "mean", "min", "max"]).round(2)

# PDF Class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CodTech Internship Report", ln=True, align="C")
        self.ln(5)
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Automated Report Generation", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f'Page {self.page_no()}', align="C")

    def add_summary_table(self, summary):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Department Score Summary", ln=True)
        self.ln(5)

        # Table header
        self.set_font("Arial", "B", 11)
        self.cell(50, 10, "Department", border=1)
        self.cell(30, 10, "Count", border=1)
        self.cell(30, 10, "Average", border=1)
        self.cell(30, 10, "Min", border=1)
        self.cell(30, 10, "Max", border=1)
        self.ln()

        # Table rows
        self.set_font("Arial", "", 11)
        for dept, row in summary.iterrows():
            self.cell(50, 10, dept, border=1)
            self.cell(30, 10, str(row["count"]), border=1)
            self.cell(30, 10, str(row["mean"]), border=1)
            self.cell(30, 10, str(row["min"]), border=1)
            self.cell(30, 10, str(row["max"]), border=1)
            self.ln()

    def add_certificate(self, name, end_date):
        self.add_page()
        self.set_font("Arial", "B", 16)
        self.ln(30)
        self.cell(0, 10, "COMPLETION CERTIFICATE", ln=True, align="C")
        self.ln(20)
        self.set_font("Arial", "", 13)
        message = (
            f"This is to certify that {name} has successfully completed "
            f"the internship at CodTech.\n\nThe internship concluded on {end_date}.\n\n"
            f"We appreciate the dedication and hard work shown during the internship.\n\n"
            f"Best wishes,\nCodTech Team"
        )
        self.multi_cell(0, 10, message, align="C")

# Create PDF report
pdf = PDF()
pdf.add_page()
pdf.add_summary_table(summary)
pdf.add_certificate("Karina Rathod", datetime.today().strftime("%d-%m-%Y"))
pdf.output("Internship_Report.pdf")

print("✅ PDF generated successfully as 'Internship_Report.pdf'")
