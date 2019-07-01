# This file handles parsing through the excel file and retrieving all of the usernames from that file

import xlrd

# for those using a mac without excel the file extensions should be xlsx instead of xls
book = xlrd.open_workbook('FILENAME.xls')

usernames = []

for sheet in book.sheets():  
    for row in range(sheet.nrows):  
        if row > 0: 
            usernames.append(sheet.row(row)[2].value)
       

