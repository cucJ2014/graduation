#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import csv
import pandas

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

#创建浏览器对象
# driver = webdriver.Chrome()
# driver.get("http://www.cosdna.com/chs/product.php?")
#
# driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/form/input").send_keys(u"Facial Treatment Clear Lotion Toner")
#
# # id="su"是百度搜索按钮，click() 是模拟点击
# # driver.find_element_by_id("su").click()
# driver.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/form/button").click()
#
# # 二级页面搜索
# # # ctrl+a 全选输入框内容
# # driver.find_element_by_xpath('//*[@id="q"]').send_keys(Keys.COMMAND, 'a')
# #
# # # ctrl+x 剪切输入框内容
# # driver.find_element_by_xpath('//*[@id="q"]').send_keys(Keys.COMMAND, 'x')
# driver.find_element_by_id("q").clear()
# driver.find_element_by_xpath('//*[@id="q"]').send_keys(u"Ultimate Revival Cream")
# driver.find_element_by_xpath("/html/body/div[1]/main/div/form/button").click()
# driver.find_element_by_css_selector("body > div.layout > main > div > div.d-flex > div.flex-grow-1 > table > tbody > tr:nth-child(1) > td.pl-0 > a").click()


# 打印网页渲染后的源代码
# print(driver.page_source)

# 获取当前页面Cookie
# print(driver.get_cookies())

# ctrl+a 全选输入框内容
# driver.find_element_by_id("q").send_keys(Keys.CONTROL,'a')
#
# # ctrl+x 剪切输入框内容
# driver.find_element_by_id("q").send_keys(Keys.CONTROL,'x')
#
# # 输入框重新输入内容
# driver.find_element_by_id("q").send_keys("test")

# # 模拟Enter回车键
# driver.find_element_by_id("su").send_keys(Keys.RETURN)
#
# # 清除输入框内容
# driver.find_element_by_id("kw").clear()
#
# # 生成新的页面快照
# driver.save_screenshot("test.png")

# 获取当前url
#print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
# driver.quit()

# --------------------------------------------------------------------------------------------------
import time
driver = webdriver.Chrome()
import re
import json
from selenium.common.exceptions import NoSuchElementException
# driver.get("http://www.cosdna.com/chs/product.php?")


# 二级页面搜索
def search_keywords(key_words):
    driver.get("http://www.cosdna.com/chs/product.php?")
    time.sleep(2)
    driver.find_element_by_id("q").clear()
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(key_words)
    driver.find_element_by_xpath("/html/body/div[1]/main/div/form/button").click()
    time.sleep(2)
    try:
        second = driver.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/table/tbody/tr/td[2]/a").text
        second_2 = driver.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/a").text
        print("second    ", second)
        print("second_2    ", second_2)
        if(second!=''):
            driver.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/table/tbody/tr/td[2]/a").click()
            time.sleep(2)
            search_ingredients(key_words)
        elif(second_2!=''):
            driver.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/a").click()
            time.sleep(2)
            search_ingredients(key_words)
    except NoSuchElementException:
        return False
    return True

def wrtie_json_data(data,file):
    json.dump(data,file,ensure_ascii=False)


def search_ingredients(key_words):
    if(driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[1]/h5/span[1]").text == ''):
        time.sleep(1)
        brand = driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[1]/h5/span[1]").text
    else:
        brand = 'None'
        time.sleep(1)
    data = {}
    new_name = driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[1]/h5/span[2]").text
    ing = []  # 保存成份英文名
    ing_chinese = {}  # 保存成份中文名
    effect = []  # 保存每个成份的作用
    acne = []  # 保存置痘的概率：0~5
    irritation =[]  # 保存刺激度：0~5
    safety = []  # 保存安心度：1～10
    element = driver.find_element_by_css_selector('body > div.layout > main > div.container-fluid.mt-4 > div.d-flex.mt-4 > div.flex-grow-1 > table')
    td_content = element.find_elements_by_tag_name("td")  # 进一步定位到表格内容所在的td节点
    time.sleep(2)
    lst = []  # 存储为list
    for td in td_content:
        lst.append(td.text)
    for index, value in enumerate(lst):
        if index % 5 == 0:
            new = re.findall(r"(.*)\n", value)[0]
            ing.append(new)
            chinese = re.findall(r"\n(.*)", value)[0]
            ing_chinese[new] = chinese
        elif index % 5 == 1:  # 作用
            effect.append(value)
        elif index % 5 == 2:
            acne.append(value)
        elif index % 5 == 3:
            irritation.append(value)
        elif index % 5 == 4:
            safety.append(value)
    data['name']=key_words
    data['new_name'] = new_name
    data['brand'] = brand
    data['ingredients'] = ing
    total.append(data)
    # print("lst : ", lst)
    # print("all ingredients are : ", ing)
    # print("all chinese ingredients are : ", ing_chinese)
    # print("effect: ", effect)
    # print("acne: ", acne)
    # print("safety : ", safety)
    # print("==" * 50)
    print("lst : ", len(lst))
    print("all ingredients are : ", len(ing))
    print("all chinese ingredients are : ", len(ing_chinese))
    print("effect: ", len(effect))
    print("acne: ", len(acne))
    print("safety : ", len(safety))

    for j in range(len(safety)):
        tmp = dict()
        tmp['chinese ingredients'] = ing_chinese[ing[j]]
        tmp['effect'] = effect[j]
        tmp['acne'] = acne[j]
        tmp['irritation'] = irritation[j]
        tmp['safety'] = safety[j]
        ing_chinese_new[ing[j]] = tmp

    # print("new_name : ", new_name)
    # print("brand : ", brand)
    # data = pandas.DataFrame(new_name,columns=["new_name"])
    # data.to_csv(file_name,index=False)
    # data_ing = pandas.DataFrame(ing,columns=['ingredients'])
    # print("inng : ", data_ing)
    # data_ing.to_csv(data_ing,index=False)
    # data_brand = pandas.DataFrame(brand,columns=['brand'])
    # data_brand.to_csv(data_brand,index=False)

def write_ingredients_csv(file_name):
    key_list = list(csv_file["name"])
    data = pandas.DataFrame(key_list, columns=['name'])
    data.to_csv(file_name, index=True, index_label='id')


# open the raw dataset
new_datasets_path = "/Users/zhangyujuan/graduation/New_Datasets.json"
json_file = open(new_datasets_path, 'w')
total = []

ingredients_path = "/Users/zhangyujuan/graduation/ingredients.json"
json_file_ingre = open(ingredients_path, 'w')
ing_chinese_new = {}

file_path = "/Users/zhangyujuan/graduation/Dataset-sephora.csv"
csv_file = pandas.read_csv(file_path)

# new data file : data.csv
file_detail_ingredients = 'detail.csv'
file_name = 'ingredients.csv'
ingredients = pandas.read_csv(file_name)
for i,value in enumerate(ingredients['name']):
    print("="*100)
    print("目前正在爬取第  ",i+1," 个" )
    if(search_keywords(value)==True):
        #if i%10 == 0:
        print()
            # wrtie_json_data(ing_chinese_new, json_file_ingre)
            # wrtie_json_data(total, json_file)
    else:
        print("==================== ERROR NUMBER : " , i+1 ,'======================== ')
        continue

print("ing_chinese_new ", ing_chinese_new)
wrtie_json_data(ing_chinese_new, json_file_ingre)
wrtie_json_data(total,json_file)
# crawl content as key_list_name
# for i in key_list:
#
#     write_csv(file_ingredients, key_list)
#     if(search_keywords(i)):
#         pass
#     else:
#         print("ERROR ! the index of error is ",key_list.index(i))