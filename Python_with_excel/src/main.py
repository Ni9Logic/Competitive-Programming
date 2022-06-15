from openpyxl import load_workbook
import string

def from_pdf_excel():
    #? This is loading the converted pdf file into the program!
    
    #* Invoice
    converted = load_workbook('excel_files/invoice.xlsx')
    invoice = converted.active
    
    #* Copying CNIC
    cnic_Sheet = load_workbook('excel_files/FBR.xlsx')
    cnic = cnic_Sheet.active
    
    #* New Excel File
    new_file = load_workbook('excel_files/sample.xlsx')
    extract = new_file.active
    
    # #* Exported File for CNIC - Not for the first time
    # exported = load_workbook('excel_files/Exported.xlsx')
    # export = exported.active
    
    #! 6 counters will be needed
    #! 1 --> Buyer CNIC
    #! 2 --> Buyer Name 
    #! 3 --> Document Numbers / Invoice Numbers
    #! 4 --> Document Date / Invoice Date
    #! 5 --> Total Quantity --> if 1 X 5 --> ctn qty else pcs qty
    #! 6 --> Sales tax
    
    #* Counters
    table_inc_0 = 1
    buyer_name = 2
    document_date = 2
    invoice_num = 2
    sales_tax = 2
    sales_table_inc = 3    
    quantity_incrementor = 2
    export_quant_incrementor = 2
    
    
    #! Placing Names, Document Invoice Number & Document Invoice Date portion
    for tables in range(1, len(converted.sheetnames) + 1):
        if table_inc_0 + 3 > len(converted.sheetnames) + 1:
            break
        else:
            #? Extracting demo-data from table 1 currently
            invoice = converted[f'Table {table_inc_0}']
            
            #? Distinguishing the dashes from the name 
            if invoice['B1'].value == None and invoice['A1'].value == "Shop Information":
                strings = list(invoice['B2'].value)
                #* This is the fix for the name and address on same line!
                if '\n' in strings:
                    strings = "".join(strings[strings.index('-') + 1:strings.index('\n')])
                else:
                    strings = "".join(strings[strings.index('-') + 1::])
            #* This is the fix for empty values in name.
            elif invoice['B1'].value == None:
                continue
            #* This is the fix for dashes!
            else:
                strings = list(invoice['B1'].value)
                if '\n' in strings:
                    strings = "".join(strings[strings.index('-') + 1:strings.index('\n')])
                else:
                    strings = "".join(strings[strings.index('-') + 1::])
            
           
            
            #? Assigning names from tables by using appropriate incrementing of rows
            extract[f'D{buyer_name}'].value = strings
            
            
            
            #? Assigning document dates & invoices by using appropriate incrementing of rows
            if '\n' in str(invoice['F1'].value) and not invoice['A1'].value == "Shop Information":
                invoice_date = str(invoice['F1'].value)
                invoice_date = list(invoice_date[:invoice_date.index('\n')])
                invoice_date = "".join(invoice_date)

                invoice_number = str(invoice['F1'].value)
                invoice_number = list(invoice_number[invoice_number.index('-') + 1:])
                invoice_number = "".join(invoice_number)
                
                
            elif invoice['A1'].value == "Shop Information" and invoice['B1'].value == None:
                pass
            elif invoice['F1'].value == None or invoice['F2'].value == None:
                continue
            else:
                invoice_date = str(invoice['F1'].value)
                invoice_date = invoice_date[:invoice_date.index('00:')]
                invoice_date = invoice_date.replace('-', '/')
                
                invoice_number = str(invoice['F2'].value)
                invoice_number = list(invoice_number[invoice_number.index('-') + 1:])
                invoice_number = "".join(invoice_number)
                
            #? Assigning invoice date and invoice number from tables by using appropriate incrementing of rows
            extract[f'I{document_date}'].value = invoice_date
            extract[f'H{invoice_num}'].value = int(invoice_number)
                
                

            
            #? 3 out of 6 incrementor
            buyer_name += 1
            document_date += 1
            invoice_num += 1
            
            #? Table incrementor
            table_inc_0 += 3
    
    
    #! Sales Tax Portion
    for sale in range(1, len(converted.sheetnames) + 1):
        while sales_table_inc + 3 <= len(converted.sheetnames) + 3:
            invoice = converted[f'Table {sales_table_inc}']
            sales_table_inc += 3
            sales = invoice['D6'].value
            
            extract[f'O{sales_tax}'].value = sales
            sales_tax += 1
            
    #! Quantity Portion
    for j in range(1, len(converted.sheetnames)):
        while quantity_incrementor + 3 <= len(converted.sheetnames) + 3:
            invoice = converted[f'Table {quantity_incrementor}']

            
            Quantity = 0
            #? This iterates for the product names
            for i in range(2, len(invoice['B'])):
                product_name = invoice[f'B{i}'].value
                if "X 5" in product_name or "x 5" in product_name or "x5" in product_name or "X5" in product_name:
                    Quantity += invoice[f'E{i}'].value
                else:
                    Quantity += invoice[f'F{i}'].value
            
            extract[f'M{export_quant_incrementor}'].value = Quantity
            export_quant_incrementor += 1
            quantity_incrementor += 3
    
    # #TODO --> This portion shall be skipped when the program is running for the first time!
    # #! CNIC Portion
    # CNIC_List = []
    # cnic_inc = 2
    # while cnic[f'D{cnic_inc}'].value != None:
    #     cnic_name = cnic[f'D{cnic_inc}'].value
    #     cnic_number = cnic[f'C{cnic_inc}'].value
    #     CNIC_List.append([cnic_number, cnic_name])
    #     cnic_inc += 1
    # export_inc = 2
    # while export[f'D{export_inc}'].value != None:
    #     name = export[f'D{export_inc}'].value
    #     name = name.replace('G/S', 'GENERAL STORE')
    #     name = name.upper()
    #     for cnics in CNIC_List:
    #         if name in cnics:
    #             extract[f'C{export_inc}'].value = cnics[0]
    #             break
    #     export_inc += 1
        
    
    new_file.save('excel_files/Exported.xlsx')
    
def main():
    from_pdf_excel()
    
    
    
main()