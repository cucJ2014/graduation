# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:12:37 2019

@author: cm
"""


import os
import sys
pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import numpy as np
import tensorflow as tf
from classifier_multi_label_textcnn.networks import NetworkAlbertTextCNN
from classifier_multi_label_textcnn.classifier_utils import get_feature_test, id2label, get_features_test
from classifier_multi_label_textcnn.hyperparameters import Hyperparamters as hp
 
          

class ModelAlbertTextCNN(object,):
    """
    Load NetworkAlbert TextCNN model
    """
    def __init__(self):
        self.albert, self.sess = self.load_model()
    @staticmethod
    def load_model():
        with tf.Graph().as_default():
            sess = tf.Session()
            with sess.as_default():
                albert = NetworkAlbertTextCNN(is_training=False)
                saver = tf.train.Saver()  
                sess.run(tf.global_variables_initializer())
                checkpoint_dir = os.path.abspath(os.path.join(pwd,hp.file_model))
                print(checkpoint_dir)
                ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
                saver.restore(sess, ckpt.model_checkpoint_path)
        return albert, sess

MODEL = ModelAlbertTextCNN()
print('Load model finished!')


def get_label(sentence):
    """
    Prediction of the sentence's label.
    """
    feature = get_feature_test(sentence)
    fd = {MODEL.albert.input_ids: [feature[0]],
          MODEL.albert.input_masks: [feature[1]],
          MODEL.albert.segment_ids:[feature[2]],
          }
    prediction = MODEL.sess.run(MODEL.albert.predictions, feed_dict=fd)[0]

    print(prediction)


    return [id2label(l) for l in np.where(prediction==1)[0]]

# np.where()[0] 表示行的索引；
# —— np.where()[1] 则表示列的索引；


if __name__ == '__main__':
    # Test
    sent3 = "糖昆布, 糖海带 丙烯酰二甲基牛磺酸铵/VP 共聚物 苯氧乙醇, 苯氧基乙醇, 二苯氧基乙醇 聚乙二醇-8 茶 聚硅氧烷-11 二氧化钛 欧洲板栗 柠檬油精, 柑橘皮粹取, 苎烯 玻尿酸钠, 透明质酸钠, 玻璃酸钠 芳樟醇, 沈香醇 乙基己基甘油 甘油, 丙三醇 聚乙烯 棕榈酰低聚肽, 棕榈酰寡肽 水 小麦 去甲二氢愈创木酸 胆甾醇 葡萄柚, 柚子, 柚 薰衣草, 真正薰衣草 聚山梨醇酯 80, 聚山梨醇酯-80 磷脂质, 磷脂 氯苯甘醚 酵母, 酵母菌胞溶产物, 酵母提取 锯叶棕 乙酰葡萄糖氨, 乙酰葡糖胺 咖啡因 글리세릴폴리메타크릴레이트 维他命C磷酸镁盐, 维他命C磷酸镁, ... 二氢茉莉酮酸甲酯 南欧丹参, 快乐鼠尾草 异戊二醇 环戊硅氧烷, 聚硅氧化合物, 十甲基环五硅氧烷, ... 硅灵, 地美司康, 二甲基硅酮, 二甲硅油, ... 丁二醇, 1, 3-丁二醇 醋酸盐维他命E, 醋酸生育酚酯, 生育酚醋酸酯, ... "
    sent2 = "胶原蛋白, 胶原 水 棕榈酸异辛酯, 棕榈酸乙基己酯, 棕榈酸盐 稻糠提取 辛酸/癸酸三酸甘油酯, 辛酸/癸酸甘油三酯, ... 甘油, 丙三醇 鲸蜡硬脂基聚硅氧烷, 鲸蜡硬脂基聚甲基硅氧烷 硅灵, 地美司康, 二甲基硅酮, 二甲硅油, ... 棕榈醇, 鲸蜡硬脂醇 苹果果提取 暂无 聚山梨醇酯 60, 聚山梨醇酯-60 甘油葡糖苷 聚甘油-2 硬脂酸酯 暂无 胶原氨基酸类 神经酰胺 3 水飞蓟果提取 向日葵提取 迷迭香叶提取 生育醇, 生育酚, 维他命E, 维生素E, ... 肌肽 硬脂酰谷氨酸钠 辛乙二醇, 辛甘醇, 1, 2-辛二醇 丙烯酰二甲基牛磺酸铵/VP 共聚物 乙基己基甘油 己二醇 柠檬酸 卵燐脂, 卵磷脂, 磷脂酰胆硷 氢氧化钠 植酸钠 叔丁醇, t-丁醇 明串球菌/萝蔔根发酵产物滤液 苯氧乙醇, 苯氧基乙醇, 二苯氧基乙醇 クエン酸トリエチル 香兰素, 香草醛 水杨酸戊酯 乙酸苄酯 北非雪松树皮油 苯乙醇 紫罗酮 芳樟醇, 沈香醇 "
    print(get_label(sent2))