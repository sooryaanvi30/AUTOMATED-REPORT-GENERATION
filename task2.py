from fpdf import FPDF
import pandas as pd

# Sample Data Analysis Task: Read CSV and analyze sales data
DATA_FILE = r"C:\Users\User\Desktop\engineering\INTERNSHIP-PYTHON\sample_data.csv"

# Read the data from a file (assuming a CSV for this example)
try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    print("Data file not found. Please ensure the file path is correct.")
    exit()

# Analyze the data (simple summary statistics)
sales_summary = df.describe()

total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()

# PDF Report Generation
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Sales Data Analysis Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def add_text(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, text)
        self.ln(5)

    def add_table(self, dataframe):
        self.set_font('Arial', 'B', 10)
        for col in dataframe.columns:
            self.cell(40, 10, col, 1, 0, 'C')
        self.ln()
        
        self.set_font('Arial', '', 10)
        for index, row in dataframe.iterrows():
            for cell in row:
                self.cell(40, 10, str(cell), 1, 0, 'C')
            self.ln()

# Create PDF
pdf = PDFReport()
pdf.add_page()
pdf.add_title('Sales Data Summary')

pdf.add_text(f'Total Sales: ${total_sales:,.2f}')
pdf.add_text(f'Average Sales: ${average_sales:,.2f}')

pdf.add_title('Statistical Summary')
pdf.add_table(sales_summary.reset_index())

# Save PDF
pdf_output_file = r"C:\Users\User\Desktop\engineering\INTERNSHIP-PYTHON\sales_report.pdf"
pdf.output(pdf_output_file)

print(f'Report generated and saved as {pdf_output_file}.')
