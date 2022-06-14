from openpyxl import Workbook, load_workbook
import PyPDF2 as PDF

def from_excel():
    wb = load_workbook('excel_files/FBR_Working.xlsx')
    ws = wb.active
    
    
    
    aB = Workbook()
    aB.title = 'new_Data'
    active_sheet_ab = aB.active
    active_sheet_ab['A1'].value = 'CNIC'
    
    counter = 0
    for i in range(1, 100):
        if ws[f'C{i}'].value == None:
            break
        else:
            active_sheet_ab[f'A{i}'] = ws[f'C{i}'].value
            counter += 1
            
            
    print(counter)
    
    for i in range(1, 100):
        if active_sheet_ab[f'A{i}'].value == None:
            break
        else:
            print((active_sheet_ab[f'A{i}'].value, ws[f'C{i}'].value))
            counter += 1
    
    
    
    aB.save('excel_files/loaded.xlsx')
    wb.save('excel_files/FBR_Working.xlsx')
def from_pdf():
    converted = load_workbook('excel_files/hamza-converted.xlsx')
    active_sheets = converted.active
    print(len(converted.sheetnames))

def learn_read_pdf():
    pdf_file = open('excel_files/hamza.pdf', 'rb')
    reader = PDF.PdfFileReader(pdf_file)
    page1 = reader.getPage(0)
    print(reader.numPages)
    a = page1.extract_text()
    print(a)
    
def main():
    learn_read_pdf()
    
    
    
main()