#-*- coding: utf-8 -*-
import xlrd


def read_excel(file):
    with open(file, mode='r') as f:
        wb = xlrd.open_workbook_xls(file, formatting_info=True)
        st = wb.sheet_by_index(0)

        cases = []
        for row in range(1,st.nrows):
            temp = []
            for col in range(st.ncols):
                value = st.cell_value(row, col)
                temp.append(value)
            cases.append(temp)

        for c in cases:

            print(c)


file = r'C:\Users\Administrator\Desktop\测试用例生成模板.xls'
read_excel(file)
