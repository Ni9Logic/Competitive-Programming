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
    #? This is loading the converted pdf file into the program!
    converted = load_workbook('excel_files/hamza-converted.xlsx')
    
    #? New Excel file in which data will be extracted from the old excel file!
    New_Excel = Workbook()
    New_Excel.title = "Hamza's Converted"
    
    #? Current workspace to new excel file's active sheet.
    nwa = New_Excel.active
    
    #? Setting rows
    nwa['A1'].value = 'Name'
    nwa['B1'].value = 'CNIC'
    
    #? Counters for incrementing rows
    nwa_counter = 2
    nwb_counter = 2
    noooo = 1
    
    for tables in range(1, len(converted.sheetnames) + 1):
        if noooo + 3 >= len(converted.sheetnames):
            break
        else:
            #? Extracting demo-data from table 1 currently
            active_sheet = converted[f'Table {noooo}']
            
            #? Assigning names from tables by using appropriate incrementing of rows
            nwa[f'A{nwa_counter}'].value = active_sheet['B1'].value
            nwa_counter += 1
                    
            #? Assigning CNIC from table by using appropriate incrementing of rows
            nwa[f'B{nwb_counter}'].value = active_sheet['D4'].value
            nwb_counter += 1
            
            noooo += 3
  
    New_Excel.save('excel_files/new_excels.xlsx')
    
def main():
    from_pdf_excel()
    
    
    
main()