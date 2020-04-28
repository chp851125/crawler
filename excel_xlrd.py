import xlrd

workbook = xlrd.open_workbook('C:/Users/user/Desktop/test.xls')
print(workbook.sheet_names())  # 查看所有sheet

#獲取Excel工作表
sheets = workbook.sheets() #獲取工作表list
sheet = sheets[0] #通過索引順序獲取
sheet = workbook.sheet_by_index(0) #通過索引順序獲取
sheet = workbook.sheet_by_name(u'sheet1') #通過名稱獲取

'''
#獲取行數和列數
nrows = sheet.nrows #行數
ncols = sheet.ncols #列數
#print(nrows, ncols)
'''

for i in range(sheet.nrows):
    print(sheet.row_values(i))


'''
# 讀取儲存格
cell_11 = sheet.cell_value(0, 0)
cell_21 = sheet.cell_value(1, 0)
# 讀一行
row_3 = sheet.row_values(2)
'''
