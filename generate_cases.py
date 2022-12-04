# coding=gbk
import xmindparser
import xlwt


class ReadXmind:
    def __init__(self, path):
        self.path = path

    def read_xmind(self):
        x = xmindparser.xmind_to_dict(self.path)[0]['topic']['topics']
        return x

    def handle_data(self):
        data = self.read_xmind()

        cases = []
        for case in data:
            condi = case['title']
            for topic in case['topics']:
                ts = topic['topics']
                for i in range(len(ts)):
                    v = ts[i]['title']
                    c = condi + v
                    cases.append(c)
        return cases

    def write_to_excel(self):
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('case', cell_overwrite_ok=True)

        cases = self.handle_data()
        for c in cases:
            sheet.write(cases.index(c), 1, c)

        wb.save(r'C:\Users\Administrator\Desktop\gouwuche.xls')


if __name__ == '__main__':
    path = r'C:\Users\Administrator\Desktop\购物车.xmind'
    rx = ReadXmind(path)
    rx.write_to_excel()