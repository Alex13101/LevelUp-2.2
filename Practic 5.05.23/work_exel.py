import openpyxl

workbook = openpyxl.load_workbook('example1.xlsx')
worksheet = workbook.active

# worksheet['A1'] = 'Name'
# worksheet['B1'] = 'Age'
# worksheet['C1'] = 'City'
#
# worksheet.append(['John', 30, 'New York'])
# worksheet.append(['Jane', 25, 'San Francisco'])

workbook.save('example1.xlsx')

for row in worksheet.iter_rows(values_only=True):
    print(row)
