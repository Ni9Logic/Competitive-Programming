from openpyxl import Workbook, load_workbook


def main():
    sheet = load_workbook('excel_files/hamza-converted.xlsx')
    
    
    for i in range(491, 710):
        ss = sheet[f'Table {i}']
        ss.title = f'Table {i - 1}'
        
    sheet.save('excel_files/hamza-converted.xlsx')
        
main()