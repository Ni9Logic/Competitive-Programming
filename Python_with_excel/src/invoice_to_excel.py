from linecache import cache
from openpyxl import load_workbook
from timeit import default_timer

class invoicee:
    def __init__(self):
        self.buyer_name = ''
        self.buyer_cnic = ''
        self.invoice_date = ''
        self.invoice_number = 0
        self.total_quantity = 0
        self.ValueAfterTax = 0
        self.NTN = 0
        
        
def insert_dash(string, index):
    return string[:index] + '-' + string[index:]

def program():
    Invoice_objects = []
    
    print("Opening Excel files this may take few seconds...")
    # * Invoice
    converted = load_workbook('excel_files/invoice.xlsx')
    invoice_sheet = converted.active
    
    # * File to export
    export_sheet = load_workbook('excel_files/sample.xlsx')
    to_export_sheet = export_sheet.active
    
    sheet_divider = 1
    #? Creating Objects...
    print("Creating Objects...")
    invoice = invoicee()
    for tables in range(1, len(converted.sheetnames) + 1):
        invoice_sheet = converted[f'Table {tables}']
        cell_value_A1 = invoice_sheet['A1'].value
        
        if cell_value_A1 == None: #! --> Sales Tax
            invoice.ValueAfterTax = invoice_sheet['D6'].value
        elif 'Name' in cell_value_A1: #! --> Name, cnic, invoice_date, invoice_number
                buyer_name = list(invoice_sheet['B1'].value)
                if '\n' in buyer_name:
                    buyer_name = "".join(buyer_name[buyer_name.index('-') + 1:buyer_name.index('\n')])
                else:
                    buyer_name = "".join(buyer_name[buyer_name.index('-') + 1::])

                # ? Assigning names from tables by using appropriate incrementing of rows
                buyer_name = buyer_name.upper()
                invoice.buyer_name = buyer_name
                invoice.buyer_name = invoice.buyer_name.replace('G/S', 'GENERAL STORE')
                invoice.buyer_name = invoice.buyer_name.replace('S/S', 'SUPER STORE')
                invoice.buyer_name = invoice.buyer_name.replace('C/C', 'CASH AND CARRY')
                invoice.buyer_name = invoice.buyer_name.replace('K/S', 'KARYANA STORE')
                invoice.buyer_name = invoice.buyer_name.replace('G.STORE', 'GENERAL STORE')
                invoice.buyer_name = invoice.buyer_name.replace('C&C', 'CASH AND CARRY')
                invoice.buyer_name = invoice.buyer_name.replace(' GS', 'GENERAL STORE')
                invoice.buyer_name = invoice.buyer_name.replace('GS', 'GENERAL STORE')
                invoice.buyer_name = invoice.buyer_name.replace('Cash & Carry', 'CASH AND CARRY')
                invoice.buyer_name = invoice.buyer_name.replace('Cash & carry', 'CASH AND CARRY')
                invoice.buyer_name = invoice.buyer_name.replace('cash & carry', 'CASH AND CARRY')
                
                # ? Assigning CNIC
                buyer_cnic = str(invoice_sheet['B4'].value)
                if '_' in buyer_cnic:
                    buyer_cnic = buyer_cnic.replace('_', '-')
                elif '-' not in buyer_cnic and '_' not in buyer_cnic:
                    buyer_cnic = insert_dash(buyer_cnic, 5)
                    buyer_cnic = insert_dash(buyer_cnic, 13)
                    
                invoice.buyer_cnic = buyer_cnic
                
                
                # ? Assigning Dates
                if "Date" not in str(invoice_sheet['F1'].value):
                    if '\n' in str(invoice_sheet['F1'].value):
                        date = str(invoice_sheet['F1'].value)
                        date = list(date[:date.index('\n')])
                        date = "".join(date)
                        invoice.invoice_date = date
                    else:
                        date = str(invoice_sheet['F1'].value)
                        date = list(date[:date.index('00:')])
                        date = "".join(date)
                        date = date.replace('-', '/')
                        year = date[:4:]
                        day = date[8:]
                        date = date.replace(day, '!')
                        date = date.replace(year, day)
                        date = date.replace('!', year)
                        date = date.replace(' ', '')
                        invoice.invoice_date = date
                else:
                    if '\n' in str(invoice_sheet['G1'].value):
                        date = str(invoice_sheet['G1'].value)
                        date = list(date[:date.index('\n')])
                        date = "".join(date)
                        invoice.invoice_date = date
                    else:
                        date = str(invoice_sheet['G1'].value)
                        date = list(date[:date.index('00:')])
                        date = "".join(date)
                        date = date.replace('-', '/')
                        year = date[:4:]
                        day = date[8:]
                        date = date.replace(day, '!')
                        date = date.replace(year, day)
                        date = date.replace('!', year)
                        date = date.replace(' ', '')
                        invoice.invoice_date = date
                
                # ? Assigning Invoice Numbers
                if "Date" not in str(invoice_sheet['F1'].value):
                    if '\n' in str(invoice_sheet['F1'].value):
                        number = str(invoice_sheet['F1'].value)
                        number = list(number[number.index('-') + 1:])
                        number = "".join(number)
                        invoice.invoice_number = number
                    else:
                        number = str(invoice_sheet['F2'].value)
                        number = list(number[number.index('-') + 1:])
                        number = "".join(number)
                        invoice.invoice_number = number
                else:
                    if '\n' in str(invoice_sheet['G1'].value):
                        number = str(invoice_sheet['G1'].value)
                        number = list(number[number.index('-') + 1:])
                        number = "".join(number)
                        invoice.invoice_number = number
                    else:
                        number = str(invoice_sheet['G2'].value)
                        number = list(number[number.index('-') + 1:])
                        number = "".join(number)
                        invoice.invoice_number = number
                
                #? Assigning NTN
                if '\n' in str(invoice_sheet['B2'].value):
                    NTN = str(invoice_sheet['B2'].value)
                    NTN = list(NTN[NTN.index('\n') + 1:])
                    invoice.NTN = NTN
                else:
                    NTN = str(invoice_sheet['B2'].value)
                    invoice.NTN = NTN
                    
                        
        elif 'Product Code' in cell_value_A1: #! --> Quantity
            for product_i in range(2, len(invoice_sheet['B'])): #? This will iterate it through the product names.
                product_name = invoice_sheet[f'B{product_i}'].value
                if "X 5" in product_name or "x 5" in product_name or "x5" in product_name or "X5" in product_name:
                    invoice.total_quantity += invoice_sheet[f'E{product_i}'].value
                else:
                    invoice.total_quantity += invoice_sheet[f'F{product_i}'].value
        else: #! --> Sales meme invoice & shop information
            continue
        
        #* Important
        sheet_divider = (sheet_divider % 3) + 1  
        if sheet_divider == 1:
            Invoice_objects.append(invoice)
            invoice = invoicee()



    #? Exporting the object's values into the excel file...
    print("Generating the third excel file...")
    rows = 2
    for i in range(0, len(Invoice_objects)):
        if Invoice_objects[i].buyer_cnic == '0--' or Invoice_objects[i].buyer_cnic == 'None':
            continue
        to_export_sheet[f'D{rows}'].value = Invoice_objects[i].buyer_name
        if '-' in Invoice_objects[i].buyer_cnic:
            Invoice_objects[i].buyer_cnic = Invoice_objects[i].buyer_cnic.replace('-', '')
        to_export_sheet[f'C{rows}'].value = Invoice_objects[i].buyer_cnic
        to_export_sheet[f'H{rows}'].value = int(Invoice_objects[i].invoice_number)
        to_export_sheet[f'I{rows}'].value = Invoice_objects[i].invoice_date
        to_export_sheet[f'M{rows}'].value = Invoice_objects[i].total_quantity
        to_export_sheet[f'O{rows}'].value = Invoice_objects[i].ValueAfterTax
        
        rows += 1
        
        
        
    export_sheet.save("excel_files/Exported_v2.xlsx")
    

def main():
    start = default_timer()
    program()
    stop = default_timer()
    
    total = stop - start
    
    print(f"Your program took total of {total} seconds to complete...")
    
    
main()