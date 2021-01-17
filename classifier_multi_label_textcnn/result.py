# # -*- coding: utf-8 -*-
# import numpy as np  # 导入numpy包
# from sklearn.model_selection import KFold  # 从sklearn导入KFold包
#
# #输入数据推荐使用numpy数组，使用list格式输入会报错
# def K_Flod_spilt(K,fold,data,label):
#     '''
#     :param K: 要把数据集分成的份数。如十次十折取K=10
#     :param fold: 要取第几折的数据。如要取第5折则 flod=5
#     :param data: 需要分块的数据
#     :param label: 对应的需要分块标签
#     :return: 对应折的训练集、测试集和对应的标签
#     '''
#     split_list = []
#     kf = KFold(n_splits=K)
#     for train, test in kf.split(data):
#         split_list.append(train.tolist())
#         split_list.append(test.tolist())
#     train,test=split_list[2 * fold],split_list[2 * fold + 1]
#     return  data[train], data[test], label[train], label[test]  #已经分好块的数据集

# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:42:07 2019

@author: cm
"""

import os
# os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
import numpy as np
import tensorflow as tf
from classifier_multi_label_textcnn.networks import NetworkAlbertTextCNN
from classifier_multi_label_textcnn.classifier_utils import get_features,get_features_test
from classifier_multi_label_textcnn.hyperparameters import Hyperparamters as hp
from classifier_multi_label_textcnn.utils import select, time_now_string

pwd = os.path.dirname(os.path.abspath(__file__))
MODEL = NetworkAlbertTextCNN(is_training=False)

# Get data features
input_ids, input_masks, segment_ids, label_ids = get_features_test()
num_train_samples = len(input_ids)
indexs = np.arange(num_train_samples)
num_batchs = int((num_train_samples - 1) / hp.batch_size) + 1  # 800 / 64 = 13
print('Number of batch:', num_batchs)

# Set up the graph
saver = tf.train.Saver(max_to_keep=hp.max_to_keep)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Load model saved before
# MODEL_SAVE_PATH = os.path.join(pwd, hp.file_save_model)
checkpoint_dir = os.path.abspath(os.path.join(pwd,hp.file_model))
print(checkpoint_dir)
ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
# ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
if ckpt and ckpt.model_checkpoint_path:
    saver.restore(sess, ckpt.model_checkpoint_path)
    print('Restored model!')

print('Load model finished!')
# print("indexs : ", indexs)

loss_list = []
accuracy_list = []
with sess.as_default():
    # Tensorboard writer
    # writer = tf.summary.FileWriter(hp.logdir, sess.graph)
    for i in range(hp.num_train_epochs):
        # np.random.shuffle(indexs)

        for j in range(num_batchs):
            # Get ids selected
            i1 = indexs[j * hp.batch_size:min((j + 1) * hp.batch_size, num_train_samples)]
            # Get features
            input_id_ = select(input_ids, i1)
            input_mask_ = select(input_masks, i1)
            segment_id_ = select(segment_ids, i1)
            label_id_ = select(label_ids, i1)

            # Feed dict
            fd = {MODEL.input_ids: input_id_,
                  MODEL.input_masks: input_mask_,
                  MODEL.segment_ids: segment_id_,
                  MODEL.label_ids: label_id_}

            accuracy, loss = sess.run([MODEL.accuracy, MODEL.loss], feed_dict=fd)

            # loss_list.append(loss)
            accuracy_list.append(accuracy)
            print('Time:%s, Epoch:%s, Batch number:%s/%s, Loss:%s, Accuracy:%s' % (
            time_now_string(), str(i), str(j), str(num_batchs), str(loss), str(accuracy)))
    print('Train finished')
avg_acc = sum(accuracy_list) / num_batchs
print(avg_acc)












