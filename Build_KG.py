#!/usr/bin/env python
# -*- coding:utf-8 -*-
import py2neo

# =========================================== 1. 转换成Cypher语言 创建1362个结点 ===========================================
# import json
# import re
#
# def write_json(file_path,data):
#     with open(file_path, 'w') as f:    #在代码当前目录生成一个data.json的文件
#         json.dump(data, f)
#
# def read_json(file_path):
#     with open(file_path, 'r') as f:  # 读取当前目录的json文件并解码成python数据
#         data = json.load(f)
#         print(data)
#         return data
#
# dataset_path = '/Users/zhangyujuan/graduation/finally.json'
# test_path = '/Users/zhangyujuan/graduation/test2.json'
# f = open('test.txt','a')
# data = read_json(dataset_path)
# for x in data:
#
#     name_index = str(x).replace(" ",'').replace("-",'').replace("+","")
#     pattern = "\w+"
#     b = re.findall(pattern, name_index)[0]
#     line = "CREATE (" + name_index + ":" + data[x]["class"] + "{" + "name:" + '"' + str(x) + '"' + "," + "brand:" + '"' \
#            + data[x]["brand"] + '"' + "," + "rating:" + str(data[x]["rating"]) + "," + "love:" + str(data[x]["love"]) + \
#            "," + "price:" + str(data[x]["price"]) + "," + "URL:" + '"' + data[x]["URL"] + '"' + "," + "how_to_use:" + '"' + data[x]["how_to_use"] \
#            + '"' + "," + "new_name:" + '"' + data[x]["new_name"] + '"' + "})"
#     print(line)
#     f.write('\n')
#     f.write(line)
# f.close()

# =========================================== 2. 创建成份结点 ===========================================================

# import json
# import re
#
# def write_json(file_path,data):
#     with open(file_path, 'w') as f:    #在代码当前目录生成一个data.json的文件
#         json.dump(data, f)
#
# def read_json(file_path):
#     with open(file_path, 'r') as f:  # 读取当前目录的json文件并解码成python数据
#         data = json.load(f)
#         print(data)
#         return data
#
# dataset_path = '/Users/zhangyujuan/graduation/ingredients.json'
# test_path = '/Users/zhangyujuan/graduation/test2.json'
# f = open('2-ingredients-cypher.txt','a')
# data = read_json(dataset_path)
# for x in data:
#
#     name_index = str(x).replace(" ",'').replace("-",'').replace("+","").replace(".","").replace("%","")
#     pattern = "[A-Za-z]"
#     b = re.findall(pattern, name_index)[0]
#     line = "CREATE (" + name_index + ":" +"Ingredients" + "{" + "name:" + '"' + str(x)+'"' + ','+ "chinese:" + '"' + data[x]["chinese"]\
#            + '"' + ',' + "effcet:" + '"' + data[x]["effect"] + '"' + ',' + "acne:"+'"' + str(data[x]["acne"])+'"'+','+"irritation:" \
#            + '"' + data[x]["irritation"] + '"' + ',' + "safety:" + '"' + data[x]["safety"] + '"' + "})"
#     print(line)
#     f.write('\n')
#     f.write(line)
# f.close()


# =========================================== 2. 创建成份结点 ===========================================================
# from py2neo import *
# import json
#
# def write_json(file_path,data):
#     with open(file_path, 'w') as f:    #在代码当前目录生成一个data.json的文件
#         json.dump(data, f)
#
# def read_json(file_path):
#     with open(file_path, 'r') as f:  # 读取当前目录的json文件并解码成python数据
#         data = json.load(f)
#         print(data)
#         return data
#
# graph = Graph("bolt://localhost:7687/neo4j", username="neo4j", password='123456')
# matcher = NodeMatcher(graph)
#
# dataset_path = '/Users/zhangyujuan/graduation/finally.json'
#
# # dataset_path = '/Users/zhangyujuan/graduation/test3.json'
# data = read_json(dataset_path)
# for x in data:
#     ingre_lst = data[x]["ingredients"]
#     print(len(ingre_lst))
#     a = graph.nodes.match(data[x]["class"], name=x).first()
#     for i in ingre_lst:
#         b = graph.nodes.match("Ingredients", name=i).first()
#         if a and b:
#             r = Relationship(a, "hasIngredient", b)
#             graph.create(r)
#
# # # 建立已有结点的关系
# # a_have=graph.nodes.match("Person",name="Alice").first()
# # b_have=graph.nodes.match("Person",name="Bob").first()
# # rel_a=Relationship(a_have,"likes",b_have)
# # graph.create(rel_a)
# #
# # # 查找目前所有的关系
# # find_re = RelationshipMatcher(graph)
# # find_r_list = list(find_re.match())
# # for i in find_r_list:
# #     print(i)
# # # 删除目前所有的关系
# #
# # i = 0
# # while i<30:
# #     relationship = graph.match_one(r_type='hasIngredient')
# #
# #     graph.delete(relationship)
# #     i+=1
# =========================================== 3. 创建肤质关系 ===========================================================
# # "details": ["Normal", "Dry", "Combination", "Oily"]
# from py2neo import *
# import json
#
# def write_json(file_path,data):
#     with open(file_path, 'w') as f:    #在代码当前目录生成一个data.json的文件
#         json.dump(data, f)
#
# def read_json(file_path):
#     with open(file_path, 'r') as f:  # 读取当前目录的json文件并解码成python数据
#         data = json.load(f)
#         print(data)
#         return data
#
# graph = Graph("bolt://localhost:7687/neo4j", username="neo4j", password='123456')
# matcher = NodeMatcher(graph)
#
# dataset_path = '/Users/zhangyujuan/graduation/finally.json'
#
# # dataset_path = '/Users/zhangyujuan/graduation/test3.json'
# data = read_json(dataset_path)
# for x in data:
#     details_lst = data[x]["details"]
#     print(len(details_lst))
#     a = graph.nodes.match(data[x]["class"], name=x).first()
#     for i in details_lst:
#         b = graph.nodes.match("Skintype", name=i).first()
#         if a and b:
#             r = Relationship(a, "suitsfor", b)
#             graph.create(r)

# =========================================== 4. 创建成份的作用关系 ===========================================================
# # 美白：Whitening
# # 保湿：Moisturizing
# # 除皱：Anti-wrinkle
# # 滋润：Moisten
# # 收敛：Porerefining
#
from py2neo import *
import json
import re
from re import search

def write_json(file_path,data):
    with open(file_path, 'w') as f:    #在代码当前目录生成一个data.json的文件
        json.dump(data, f)

def read_json(file_path):
    with open(file_path, 'r') as f:  # 读取当前目录的json文件并解码成python数据
        data = json.load(f)
        print(data)
        return data

graph = Graph("bolt://localhost:7687/neo4j", username="neo4j", password='123456')
matcher = NodeMatcher(graph)

dataset_path = '/Users/zhangyujuan/graduation/ingredients.json'

# dataset_path = '/Users/zhangyujuan/graduation/test4.json'
data = read_json(dataset_path)
pattern_Moisturizing =re.compile("保湿")
pattern_Whitening =re.compile("美白")
pattern_Moisten =re.compile("滋润")
pattern_Anti =re.compile("抗氧化")
pattern_wrinkle =re.compile("除皱")
pattern_Porerefining =re.compile("收敛")

pattern_flavor =re.compile("香精")
pattern_Ethoxyquim =re.compile("防腐剂")

for x in data:
    if data[x]["effect"]:
        if pattern_Moisturizing.search(data[x]["effect"]):
            print(data[x]["effect"], ": ", "保湿")
            a = graph.nodes.match("Ingredients", name=x).first()
            b = graph.nodes.match("Function", name="Moisturizing").first()
            if a and b:
                r = Relationship(a, "haseffect", b)
                graph.create(r)

        if pattern_Whitening.search(data[x]["effect"]):
            print(data[x]["effect"], ": ", "美白")
            a = graph.nodes.match("Ingredients", name=x).first()
            b = graph.nodes.match("Function", name="Whitening").first()
            if a and b:
                r = Relationship(a, "haseffect", b)
                graph.create(r)

        if pattern_Moisten.search(data[x]["effect"]):
            print(data[x]["effect"], ": ", "滋润")
            a = graph.nodes.match("Ingredients", name=x).first()
            b = graph.nodes.match("Function", name="Moisten").first()
            if a and b:
                r = Relationship(a, "haseffect", b)
                graph.create(r)

        if pattern_Anti.search(data[x]["effect"]) or pattern_wrinkle.search(data[x]["effect"]):
            print(data[x]["effect"],": ","抗氧化  除皱")
            a = graph.nodes.match("Ingredients", name=x).first()
            b = graph.nodes.match("Function", name="Anti-wrinkle").first()
            if a and b:
                r = Relationship(a, "haseffect", b)
                graph.create(r)

        if pattern_Porerefining.search(data[x]["effect"]):
            print(data[x]["effect"], ": ", "收敛")
            a = graph.nodes.match("Ingredients", name=x).first()
            b = graph.nodes.match("Function", name="Porerefining").first()
            if a and b:
                r = Relationship(a, "haseffect", b)
                graph.create(r)
        if pattern_flavor.search(data[x]["effect"]):
            print(data[x]["effect"], ": ", "收敛")
            a = graph.nodes.match("Ingredients", name=x).first()
            b = graph.nodes.match("Flavor", name="Porerefining").first()
            if a and b:
                r = Relationship(a, "haseffect", b)
                graph.create(r)

# =========================================== 4. 创建成份的作用关系 ===========================================================