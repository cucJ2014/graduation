# import re
# mystr = '今天的天气真好，天气真的好'
#
# pattern = re.compile('真')
# res = pattern.search(mystr)
# print(res)
#
# # search结果
# # <_sre.SRE_Match object; span=(3, 5), match='天气'>
# # 只有一个结果，返回的是Match object，可以用search[0]得到该字符串
#
# find = re.findall(pattern, mystr)
# print(find)

# import csv
#
# def create_csv(path,data1,data2):
#     with open(path,'a+') as f:
#         csv_write = csv.writer(f)
#         title = ["epcho","loss","acc"]
#         csv_write.writerow(title)
#         for i in range(len(data1)):
#             tmp = []
#             tmp.append(i+1)
#             tmp.append(data1[i])
#             tmp.append(data2[i])
#             csv_write.writerow(tmp)
#
#
# loss_list = [1.2222,3.4444,2.3333,6.2222]
# acc_list = [0.9999,0.8888,0.7777,0.6666]
#
# file_path = 'lala.csv'
# create_csv(file_path,loss_list,acc_list)

