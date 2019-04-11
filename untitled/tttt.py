import requests
import xlrd
from collections import OrderedDict
import json
import sys

# reload(sys)


def Excel_to_json(file):
    wb = xlrd.open_workbook(file)

    convert_list = []
    sh = wb.sheet_by_index(0)
    title = sh.row_values(0)  # 表头，json文件的key
    print(title)
    # for rownum in range(1, sh.nrows):
    #     rowvalue = sh.row_values(rownum)
    #     single = OrderedDict()  # 有序字典
    #     for colnum in range(0, len(rowvalue)):
    #         print("key:{0}, value:{1}".format(title[colnum], rowvalue[colnum]))
    #         single[title[colnum]] = rowvalue[colnum]
    #     convert_list.append(single)
    #
    # j = json.dumps(convert_list)
    #
    # with open("file.json", "w", encoding="utf8") as f:
    #     f.write(j)

if __name__ == '__main__':
    Excel_to_json('animal_sounds_v2.csv')