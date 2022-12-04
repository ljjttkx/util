#-*- coding: utf-8 -*-
from faker import Faker
import pandas as pd


class FakerData:
    def __init__(self, locale):
        self.faker = Faker(locale)

    def getRamdom(self, type, count):
        list = []
        for i in range(count):
            rdata = getattr(self.faker, type)()
            list.append(rdata)
        return list

    def write_to_excel(self, file, sheet, type, count):
        try:
            data = self.getRamdom(type, count)
            df = pd.DataFrame({type: data})

            with pd.ExcelWriter(file) as writer:
                df.to_excel(writer, sheet_name=sheet, index=False)

        except FileNotFoundError:
            print('文件不存在')


if __name__ == '__main__':
    faker = FakerData(locale='zh_CN')
    '''
        中文随机类
        https://faker.readthedocs.io/en/master/locales/zh_CN.html#faker-providers-date-time
        name, address, phone_number, date, text, random_int, words
        locale可修改英文en
    '''
    # faker.getRamdom('words', 10)
    file = r'C:\Users\Administrator\Desktop\test.xls'
    faker.write_to_excel(file, 'Sheet1', 'name', 100)
