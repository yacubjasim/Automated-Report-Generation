import pandas as pd
from fpdf import FPDF

df = pd.read_csv("data.csv")

total_students = len(df)
average_score = df['Score'].mean()
max_score = df['Score'].max()
min_score = df['Score'].min()
top_student = df.loc[df['Score'].idxmax()]['Name']
low_student = df.loc[df['Score'].idxmin()]['Name']

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Score Report", ln=1, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_statistics(self, total, avg, max_s, min_s, top, low):
        self.set_font("Arial", "", 12)
        self.ln(10)
        self.cell(0, 10, f"Total Students: {total}", ln=1)
        self.cell(0, 10, f"Average Score: {avg:.2f}", ln=1)
        self.cell(0, 10, f"Highest Score: {max_s} (by {top})", ln=1)
        self.cell(0, 10, f"Lowest Score: {min_s} (by {low})", ln=1)

    def add_table(self, dataframe):
        self.set_font("Arial", "B", 12)
        self.cell(60, 10, "Name", border=1)
        self.cell(40, 10, "Score", border=1)
        self.ln()
        self.set_font("Arial", "", 12)
        for _, row in dataframe.iterrows():
            self.cell(60, 10, str(row["Name"]), border=1)
            self.cell(40, 10, str(row["Score"]), border=1)
            self.ln()

pdf = PDFReport()
pdf.add_page()
pdf.add_statistics(total_students, average_score, max_score, min_score, top_student, low_student)
pdf.ln(10)
pdf.cell(0, 10, "Individual Scores", ln=1)
pdf.add_table(df)
pdf.output("report.pdf")  

print("✅ PDF generated as 'report.pdf'")




