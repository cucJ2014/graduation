import json

def write_json(file_path,data):
    with open(file_path, 'w') as f:    #在代码当前目录生成一个data.json的文件
        json.dump(data, f)

def read_json(file_path):
    with open(file_path, 'r') as f:  # 读取当前目录的json文件并解码成python数据
        data = json.load(f)
        print(data)
        return data

test_1_path = '/Users/zhangyujuan/graduation/test.json'
data1 = read_json(test_1_path)
# print(data1["GENIUS Liquid Collagen"]["details"])


test_2_path = '/Users/zhangyujuan/graduation/test2.json'
data2 = read_json(test_2_path)

for x in data1:
    if x in data2:
        data2[x]["details"] = data1[x]["details"]

print("=="*88)
print(data2)

save_file = 'b.json'
write_json(save_file,data2)