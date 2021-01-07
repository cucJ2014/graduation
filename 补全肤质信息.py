from py2neo import *
import json
import re
from re import search

def write_json(file_path,data):
    with open(file_path, 'a') as f:    #在代码当前目录生成一个data.json的文件
        json.dump(data, f)

def read_json(file_path):
    with open(file_path, 'r') as f:  # 读取当前目录的json文件并解码成python数据
        data = json.load(f)
        print(data)
        return data

file_path = '/Users/zhangyujuan/graduation/finally.json'
file_data = read_json(file_path)

file_A_path = 'A.json'
file_B_path = 'B.json'

for i in file_data:
    if file_data[i]["details"]:
        # print(file_data[i]["details"])
        write_json(file_A_path, file_data[i])
    else:
        write_json(file_A_path, file_data[i])

# 嘻嘻
