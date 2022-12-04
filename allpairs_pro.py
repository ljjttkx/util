import functools
import xlrd

functools.reduce(lambda x,y: x-y, [1,2,3,4])


class AllpairsPro:
    def __init__(self, path):
        self.path = path

    def get_excel(self):
        wb = xlrd.open_workbook_xls(self.path)
        sheet = wb.sheet_by_index(0)
        ncols = sheet.ncols

        datas = []
        for col in range(ncols):
            temp = []
            for row in range(1, sheet.nrows):
                value = sheet.cell(row, col).value
                temp.append(value)
            datas.append(temp)
        return datas

    def reduce_data(self):
        data_list = self.get_excel()
        mutex_list = functools.reduce(self.excute_mutual_exclusion, data_list)
        print(mutex_list)

    def excute_mutual_exclusion(self1, condi1, condi2):
        return condi1 + condi2


if __name__ == '__main__':
    path = r'C:\Users\Administrator\Desktop\正交.xls'
    ap = AllpairsPro(path)
    ap.reduce_data()