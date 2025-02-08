# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: P SOORYA SHENOY

INTERN ID: CT12ONS

DOMAIN: PYTHON PROGRAMMING

DURATION: 8 WEEKS

MENTOR: NEELA SANTHOSH

This Python script is cross-platform and can be executed on any system that supports Python, including Windows, macOS, and Linux. It is particularly useful for businesses and developers who need to automate report generation from data files like CSVs. Applications for this task include sales analytics reporting, financial data summaries, and any task that requires formatted PDF reporting. By leveraging the power of libraries like `fpdf`, the solution minimizes human effort in creating structured and presentable reports.

How the Code Works

1. Reading Data from a CSV File: 
   The program reads data from a CSV file using Python's built-in `csv` library. The file path for the CSV is stored in the `DATA_FILE` variable. The CSV file contains structured information, such as sales records with columns for `Date`, `Product`, `Sales`, and `Region`. The data is parsed and processed line by line.

2. Data Analysis:  
   Basic analysis is performed on the dataset:
   - Total sales are computed by summing the `Sales` column values.
   - Average sales are calculated by dividing the total sales by the number of records.

3. Generating a PDF Report: 
   The script uses the `fpdf` library to create a well-formatted PDF report. `fpdf` is a lightweight and easy-to-use Python library for generating PDF documents. It supports various layout customizations, such as text formatting, table generation, and image embedding.
   - A title and subtitle are added to the PDF using `pdf.set_font()` and `pdf.cell()` methods.
   - Data records are displayed as table rows in the report, where each record from the CSV file is printed on a separate line.
   - The total and average sales statistics are summarized at the end of the report.

4. Saving the PDF Report:
   The `output()` method of `fpdf` saves the generated PDF file as `sales_report.pdf`. By default, the file is saved in the same directory where the script is executed.

Key Features of `fpdf`
- **Text and Font Control:** The script uses `pdf.set_font()` to customize the font type and size.
- **Table Representation:** Data from the CSV file is printed line by line using `pdf.cell()`.
- **Automatic Page Breaks:** When content overflows, `fpdf` automatically creates a new page.
- **Flexible Output:** The report can be easily formatted and customized further, including adding headers, footers, and images.

Applications
1. Sales and Financial Reporting:  Businesses can automate the generation of daily, weekly, or monthly sales reports.
2. Data Summarization:  This solution is ideal for creating summaries from sensor data, IoT devices, or any structured data files.
3. Academic Projects:   Students and researchers can utilize this for report generation in machine learning or data science projects.
4. Customized Business Reports:   Automating invoicing, performance dashboards, or operational summaries.

output
![Image](https://github.com/user-attachments/assets/361427dd-3ba3-49e3-a9ce-ace1411587ab)
