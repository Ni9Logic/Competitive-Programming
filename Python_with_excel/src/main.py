from openpyxl import Workbook, load_workbook


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
def from_pdf_excel():
    converted = load_workbook('excel_files/hamza-converted.xlsx')
    active_sheets = converted.active
    
    counter = 0
    for total_sheets in range(1, len(converted.sheetnames) + 1):
        active_sheet = converted[f'Table {total_sheets}']
        counter += 1
    print(len(converted.sheetnames), counter)
        
    
    
def main():
    from_pdf_excel()
    
    
    
main()