#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import csv
from py2neo import *


# 将B_result数据补充到B.json
def read_csv(file_path):
    with open(file_path) as f:
        label_file = csv.reader(f)
        data = []
        for online in label_file:
            data.append(online)
        return data

def create_csv(path,data1):
    with open(path,'a+') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data1)


def get_city_code(str_c):
    city_code_csv_file="/Users/zhangyujuan/graduation/recommendation/city_code_csv.csv"
    with open(city_code_csv_file) as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
        for i in range(len(column)):
            if str_c in column[i][1]:
                return column[i][1],column[i][0]
        else:
            return 0
# city_name, city_id = get_city_code("汕头")
def get_weather(city_name, city_id):
    ak = 'HELaVmuS91N8z1IjE9i3m2uAVFWGMVBU' #你的ak
    url = 'http://api.map.baidu.com/weather/v1/?district_id=%d&data_type=all&ak=%s'%(int(city_id),ak)
    a = requests.get(url).json()
    result = a['result']['forecasts'][0]
    rh = a['result']['now']['rh']
    text = a['result']['now']['text']
    date = result['date'] #当天日期
    text_day = result['text_day'] #白天天气
    text_night = result['text_night'] #晚上天气
    high_temp = result['high'] #当天最高温度℃
    low_temp = result['low'] #当天最低温度℃
    wc_day = result['wc_day'] #风力
    wd_day = result['wd_day'] #风
    weather={}
    weather["日期"]=date
    weather["城市名称"]=city_name
    weather["天气"]=text
    weather["白天天气"]=text_day
    weather["晚上天气"]=text_night
    weather["最高温度"]=high_temp
    weather["最低温度"] =low_temp
    weather["湿度"] =rh
    weather["风力"] =wc_day
    weather["风"] = wd_day
    if weather:
        return weather
    else:
        return 0

def skintype_input():
    print("=-*-="*10)
    input_num = input("请输入肤质序号：\n"
                     "    1. 干性 \n"
                     "    2. 油性 \n"
                     "    3. 混合 \n"
                     "    4. 正常 \n")
    if int(input_num)<5 and int(input_num)>0:
        return dict_skin_type[int(input_num)]
    return skintype_input()


def sensitive_input():
    print("=-*-="*10)
    input_num = input("是否为敏感肌：\n"
                     "    1. 是 \n"
                     "    2. 否 \n")
    if int(input_num)<3 and int(input_num)>0:
        return int(input_num)
    return sensitive_input()


def service_input():
    print("=-*-="*10)
    input_num = input("请选择待服务内容：\n"
                     "    1. 查推荐 \n"
                     "    2. 查搭配 \n")
    if int(input_num)<3 and int(input_num)>0:
        return int(input_num)
    return service_input()

def type_re_input():
    print("=-*-="*10)
    input_list = list(map(int,input("请选择待推荐的种类序号，按逗号分割，（如 2,3,4）：：\n"
                     "    0. 无，默认推荐 \n"
                     "    1. 洗面奶 \n"
                     "    2. 护肤水 \n"
                     "    3. 乳液/面霜 \n"
                     "    4. 精华 \n"
                     "    5. 眼霜 \n"
                     "    6. 防晒 \n"
                      ).strip().split(",")))
    if input_list:
        return input_list
    return type_re_input()

def type_match_input():
    print("=-*-="*10)
    input_list = list(map(int,input("请选择待搭配的种类序号，按逗号分割，（如 1,2,3）：\n"
                     "    1. 洗面奶 \n"
                     "    2. 护肤水 \n"
                     "    3. 乳液/面霜 \n"
                     "    4. 精华 \n"
                     "    5. 眼霜 \n"
                     "    6. 防晒 \n"
                      ).strip().split(",")))
    if input_list:
        return input_list
    return type_match_input()

def city_input():
    print("=-*-="*10)
    input_string = input("请输入所在城市：\n")
    if input_string:
        return input_string
    return city_input()

def function_input():
    print("=-*-="*10)
    input_list = list(map(int,input("请输入功能需求：\n"
                     "    1. 保湿（默认） \n"
                     "    2. 美白 \n"
                     "    3. 去皱 \n"
                     "    4. 收敛 \n"
                     "    5. 祛痘 \n"
                      )))
    if input_list:
        return input_list[0]
    return function_input()

def price_input(type_list):
    print("=-*-="*10)
    input_list = []
    print("请依次输入价格需求：\n")
    for i in type_list:
        j = str(i)
        words = dict_type[j] + ' 价格 ¥ ：'
        line = float(input(words))
        input_list.append(line)

    if input_list:
        return input_list
    return price_input(type_list)

def match_name_input(type_list):
    print("=-*-="*10)
    input_list = []
    print("请依次输入待搭配产品名称：\n")
    for i in type_list:
        j = str(i)
        words = dict_type[j] + ' 名称 ：'
        line = input(words)
        input_list.append(line)
    if input_list:
        return input_list
    return match_name_input(type_list)


# city = "汕头"
# name,id = get_city_code(city)
# weather = get_weather(name,id)
# print(weather)

dict_type = {}
dict_type["0"] = "待推荐"
dict_type["1"] = "洗面奶"
dict_type["2"] = "护肤水"
dict_type["3"] = "乳液/面霜"
dict_type["4"] = "精华"
dict_type["5"] = "眼霜"
dict_type["6"] = "防晒"

# dict_match_type = {}
# dict_match_type["1"] = "洗面奶"
# dict_match_type["2"] = "护肤水"
# dict_match_type["3"] = "乳液/面霜"
# dict_match_type["4"] = "精华"
# dict_match_type["5"] = "眼霜"
# dict_match_type["6"] = "防晒"

dict_skin_type = {"1":"Dry","2":"Oily","3":"Combination","4":"Normal","5":"Sensitive"}
dict_type_eng = {"1":"Cleanser","2":"Toner","3":"Cream","4":"Serum","5":"EyeCream","6":"Sunscreen"}

def user_input():
    skin_type = skintype_input()
    sensitive_num = sensitive_input()
    service_num = service_input()
    if service_num==1:
        # 推荐种类
        re_list = type_re_input()
        re_list_name = []
        # 换成英文列表
        for i in re_list:
            re_list_name.append(dict_type_eng[i])
        city = city_input()
        function_num = function_input()
        if re_list[0]==0: # 如果包含默认推荐，那就依据所有的价格，推荐三种方案
            price_list = price_input([1,2,3,4,5,6])
        else:
            price_list = price_input(re_list)
        # print("skin_num : ",skin_num)
        # print("sensitive_num : ",sensitive_num)
        print("service_num : ",service_num)
        print("re_list : ",re_list)
        print("city: ", city)
        print("function_num : ", function_num)
        print("price_list : ", price_list)
    else:
        match_list = type_match_input()
        match_name_list = match_name_input(match_list)
        # print("skin_num : ",skin_num)
        # print("sensitive_num : ",sensitive_num)
        print("service_num : ",service_num)
        print("match_list : ",match_list)
        print("match_name_list : ", match_name_list)





graph = Graph("bolt://localhost:7687/neo4j", username="neo4j", password='123456')
matcher = NodeMatcher(graph)
matcher_relationship = RelationshipMatcher(graph)


# 按照价格、种类、肤质，在每个种类中，筛选出符合用户预期的产品
# 返回值：result = {"name":price}
# def search_single(single,single_price,skin_type):
#     up_price = single_price+5
#     down_price = single_price-5
#     single_list_1 = list(matcher.match(single).where("_.price <= "+str(up_price)).order_by("_.price"))
#     single_list_2 = list(matcher.match(single).where("_.price >= "+str(down_price)).order_by("_.price"))
#     # single_list = list(matcher.match(single, price__gt=1))
#                        # and("_.price >= "+str(down_price)))
#     single_list = list(set(single_list_1) & set(single_list_2))
#     # for i in single_list:
#     #     print(i["price"],i["name"])
#     print("筛选之前的长度： ", len(single_list))
#
#     result = {}
#     if single_list:
#         for i in single_list:
#             findnode = matcher.match(single,name=i["name"]).first()
#             findskintype = matcher.match("Skintype", name=skin_type).first()
#             a = list(graph.match((findnode,findskintype), r_type='suitsfor'))
#             if a:
#                 result[i["name"]] = i["price"]
#                 # print(i["price"], i["name"])
#         print("筛选之后的长度： ",len(result))
#
#         # 检测是否有环，推理是否存在不合理的场景
#         b = list(graph.run('match (a:'+ single + ')-[r:hasIngredient]->(x)<-[rr:`in conflict with`]-(b:Skintype{name:"'+
#                       skin_type+'"})<-[rrr:suitsfor]-(a) return a.name'))
#         if b:
#             for i in b:
#                 if i["a.name"] in result:
#                     del result[(i["a.name"])]
#         print("二次筛选之后的长度： ",len(result))
#         # for i in result:
#         #     print(result[i],i)
#         return result
#     else:
#         return 0

def search_single(single,single_price,skin_type,sensitive):
    up_price = single_price+5
    down_price = single_price-5
    single_list_1 = list(matcher.match(single).where("_.price <= "+str(up_price)).order_by("_.price"))
    single_list_2 = list(matcher.match(single).where("_.price >= "+str(down_price)).order_by("_.price"))
    single_list = list(set(single_list_1) & set(single_list_2))
    # for i in single_list:
    #     print(i["price"],i["name"])
    print("1、根据【价格、种类】筛选后的长度： ", len(single_list))  # 按价格筛选之后的结果

    result = {}
    if single_list:
        for i in single_list:
            findnode = matcher.match(single,name=i["name"]).first()
            findskintype = matcher.match("Skintype", name=skin_type).first()
            # 判断当前【节点】是否适合 当前【肤质】
            a = list(graph.match((findnode,findskintype), r_type='suitsfor'))  # 适合其他肤质的节点
            if a:  # 适合的话，再判断是否适合敏感肌：
                if sensitive==1:
                    findskintype2 = matcher.match("Skintype", name="Sensitive").first()
                    # 判断当前【节点】是否适合【敏感肌】
                    c = list(graph.match((findnode,findskintype2), r_type='suitsfor'))  # 适合敏感肤质的节点
                    if c:
                        result[i["name"]] = i["price"]
                else:  # 如果不是敏感肌，只是其他正常肌肤，直接保存该节点。
                    result[i["name"]] = i["price"]
                # print(i["price"], i["name"])
        print("2、根据【肤质】筛选后的长度： ",len(result))

        if sensitive==1:
            d = list(graph.run(
                'match (a:' + single + ')-[r:hasIngredient]->(x)<-[rr:`in conflict with`]-(b:Skintype{name:"' +
                'Sensitive' + '"})<-[rrr:suitsfor]-(a) return a.name'))
            if d:
                for i in d:
                    if i["a.name"] in result:
                        del result[(i["a.name"])]
            print("3、根据【敏感肌】环路判断后的长度： ", len(result))

        b = list(graph.run('match (a:'+ single + ')-[r:hasIngredient]->(x)<-[rr:`in conflict with`]-(b:Skintype{name:"'+
                      skin_type+'"})<-[rrr:suitsfor]-(a) return a.name'))  # 检测是否有环，推理是否存在不合理的场景
        if b:
            for i in b:
                if i["a.name"] in result:
                    del result[(i["a.name"])]
        print("3、最终：根据【肤质环路】判断后的长度： ",len(result))
        # for i in result:
        #     print(result[i],i)
        return result
    else:
        return 0
search_list = search_single("Toner", 36, "Oily",1)
print(search_list)


# 每个产品之间是否可达。
def item2item(item1,type1,item2,type2) -> bool:

    match_item2item = 'MATCH (n:Ingredients{name:"'+item1+'"}),(m:Ingredients{name:"'+item2+'"}) ' \
                  'with n, m ' \
                  'match (p:'+type1+')-[r:hasIngredient]->(n),(q:'+type2+')-[rr:hasIngredient]->(m) ' \
                  'return n,m,r,rr,p,q'

    match_item2item_inconflict = 'match (p:'+type1+'{name:"'+item1+'"})-[r:hasIngredient]->(n:Ingredients),' \
                                 '(q:'+type2+'{name:"'+item2+'"})-[rr:hasIngredient]->(m:Ingredients) ' \
                                 'with n,m,r,rr,p,q match (n)-[k:`in conflict with`]-(m) ' \
                                 'return n,m,r,rr,p,q,k'

    a = list(graph.run(match_item2item_inconflict))
    if a:
        return False
    return True
        # print(a)
        # print(len(a))
        # print(a[0]["n"]["chinese"])


re_list = [1,2,3] # 洗面奶 水 霜
re_list_name = []
# 换成英文列表
for i in re_list:
    re_list_name.append(dict_type_eng[str(i)])

price_list = [15.0,25.0,30.0]
skin_type = "Sensitive"
sensitive_BOOL = 1

# 测试代码
# def item2item(item1,type1,item2,type2) -> bool:
#     if item1[0]=="洗面奶1" and item2=="水2":
#         return False
#     elif item1[0]=="水1" and item2=="霜1":
#         return False
#     return True
# result = recall(["a","b","c"],[15,20,25],"Oily",1)


def recall(re_list_name,price_list,skin_type,sensitive_BOOL):
    single_list = []  # 存储每一个类别的字典，每个字典里头是name和price
    for i in range(len(re_list_name)):  # 水、乳、霜
        if sensitive_BOOL==1:
            single_dict = search_single(re_list_name[i],price_list[i],"Sensitive")
            single_list.append(single_dict)
        else:
            single_dict = search_single(re_list_name[i], price_list[i], skin_type)
            single_list.append(single_dict)


    # single_list = [{"洗面奶1":10,"洗面奶2":13},{"水1":20,"水2":22,"水3":24},{"霜1":24,"霜2":22}]
    group = [[]]
    new_group = [[]]
    if len(single_list)>1:
        count = 0
        for d in single_list:
            group=new_group.copy()
            new_group=[]
            for g in group:
                for item in d:

                    length = len(group)
                    if length>1:
                        type1_index=group.index(g)
                        if(item2item(g[0],re_list_name[count],item,re_list_name[count])):
                            new_group.append(g+[item])
                    else:
                        new_group.append([item])
            count+=1
    return new_group

# result = item2item("Clarifying Lotion 4","Toner","Refreshing Cleanser","Cleanser")
# result = recall(re_list_name,price_list,skin_type,sensitive_BOOL)
# print(len(result))
# print(result)





