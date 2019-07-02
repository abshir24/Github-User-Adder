# This file handles parsing through the excel file and retrieving all of the usernames from that file

import xlrd

# for those using a mac without excel the file extensions should be xlsx instead of xls
# Download the file from teams and place it in this directory
# MAKE SURE THE FILE IS IN THIS DIRECTORY!
filename = xlrd.open_workbook('usernames.xlsx')

usernames = []

for sheet in filename.sheets():  
    for row in range(sheet.nrows):  
        if row > 0: 
            usernames.append(sheet.row(row)[2].value)
       
