import xlrd

book = xlrd.open_workbook('usernames.xlsx')

usernames = []

for sheet in book.sheets():  
    for row in range(sheet.nrows):  
        if row > 0: 
            usernames.append(sheet.row(row)[2].value)
       

