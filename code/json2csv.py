import json
import csv

def csv_json():
    # 1.分别 读、创建文件
    json_fp = open("../data/edge.json", "r",encoding='utf-8')
    csv_fp = open("../data/paper2person.csv", "w",encoding='utf-8',newline='')
    # 2.提出表头和表的内容
    data_list = json.load(json_fp)
    sheet_title = data_list[0].keys()
    sheet_data = []
    for data in data_list:
        sheet_data.append(data.values())
    # 3.csv 写入器
    writer = csv.writer(csv_fp)
    # 4.写入表头
    writer.writerow(sheet_title)
    # 5.写入内容
    writer.writerows(sheet_data)
    # 6.关闭两个文件
    json_fp.close()
    csv_fp.close()

csv_json()
