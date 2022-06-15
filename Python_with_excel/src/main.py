from openpyxl import Workbook, load_workbook

def from_pdf_excel():
    #? This is loading the converted pdf file into the program!
    
    #* Invoice
    converted = load_workbook('excel_files/hamza-converted.xlsx')
    invoice = converted.active
    
    #* Copying CNIC
    cnic_Sheet = load_workbook('excel_files/FBR.xlsx')
    cnic = cnic_Sheet.active
    
    #* New Excel File
    new_file = load_workbook('excel_files/sample.xlsx')
    extract = new_file.active
    
    #! 6 counters will be needed
    #! 1 --> Buyer CNIC
    #! 2 --> Buyer Name 
    #! 3 --> Document Numbers / Invoice Numbers
    #! 4 --> Document Date / Invoice Date
    #! 5 --> Total Quantity --> if 1 X 5 --> ctn qty else pcs qty
    #! 6 --> Sales tax
    
    
    table_inc_0 = 1
    buyer_name = 2
    document_date = 2
    invoice_num = 2
    sales_tax = 2
    
    #? Pasting all the names from invoices
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
            
    
    
    #? Sales Tax also done!
    sales_table_inc = 3    
    for sale in range(1, len(converted.sheetnames) + 1):
        while sales_table_inc + 3 <= len(converted.sheetnames) + 3:
            invoice = converted[f'Table {sales_table_inc}']
            sales_table_inc += 3
            sales = invoice['D6'].value
            
            extract[f'O{sales_tax}'].value = sales
            sales_tax += 1
            
    new_file.save('excel_files/Exported.xlsx')
  
    
def main():
    from_pdf_excel()
    
    
    
main()