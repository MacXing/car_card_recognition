import numpy as np
import os
import random
from scipy.misc import imread
import string
from sklearn import svm
import time
classfies = []

def get_labels():
    dict_labels = {}
    list_labels = []
    for i in range(10):
        dict_labels[i] = i
    for word in string.ascii_uppercase:
        dict_labels[word] = word
    dict_labels["川"] = 'zh_cuan'
    dict_labels["鄂"] = 'zh_e'
    dict_labels["赣"] = 'zh_gan'
    dict_labels["甘"] = 'zh_gan1'
    dict_labels["贵"] = 'zh_gui'
    dict_labels["桂"] = 'zh_gui1'
    dict_labels["黑"] = 'zh_hei'
    dict_labels["沪"] = 'zh_hu'
    dict_labels["冀"] = 'zh_ji'
    dict_labels["津"] = 'zh_jin'
    dict_labels["京"] = 'zh_jing'
    dict_labels["吉"] = 'zh_jl'
    dict_labels["辽"] = 'zh_liao'
    dict_labels["鲁"] = 'zh_lu'
    dict_labels["蒙"] = 'zh_meng'
    dict_labels["闽"] = 'zh_min'
    dict_labels["宁"] = 'zh_ning'
    dict_labels["青"] = 'zh_qing'
    dict_labels["琼"] = 'zh_qiong'
    dict_labels["陕"] = 'zh_shan'
    dict_labels["苏"] = 'zh_su'
    dict_labels["晋"] = 'zh_sx'
    dict_labels["皖"] = 'zh_wan'
    dict_labels["湘"] = 'zh_xiang'
    dict_labels["新"] = 'zh_xin'
    dict_labels["豫"] = 'zh_yu'
    dict_labels["渝"] = 'zh_yu1'
    dict_labels["粤"] = 'zh_yue'
    dict_labels["云"] = 'zh_yun'
    dict_labels["藏"] = 'zh_zang'
    dict_labels["浙"] = 'zh_zhe'
    for value in dict_labels.values():
        list_labels.append(value)

    return dict_labels,list_labels

def open_dir():
    global classfies
    for root, dirs, filename in os.walk('D:\workspace\EasyPR-python\data\easypr_train_data\chars', topdown=False):
        for dir in dirs:
            classfies.append(dir)


def init_data():
    open_dir()
    a = random.choice(classfies)
    # print(a)
    dict_labels,list_labels = get_labels()
    # print(len(list_labels))
    for index,label in enumerate(list_labels):
        if label == a:
            y = index
    for root,_,filename in os.walk(os.path.join(r'D:\毕业论文\car_recognition\chars',a),topdown=False):
        name = random.choice(filename)
        # print(name)
        x = imread(os.path.join(root,name))
        # print(os.path.join(root,name))

        return x,y

def create_svm(dataMat, dataLabel, decision='ovr'):
    clf = svm.SVC(decision_function_shape=decision)
    clf.fit(dataMat, dataLabel)
    return clf
def train():
    tbasePath = "Mnist-image\\test\\"
    tcName = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tst = time.clock()
    allErrCount = 0
    allErrorRate = 0.0
    allScore = 0.0
    for tcn  in tcName:
        testPath = "Mnist-image\\test\\" + tcn
        #print("class " + tcn + " path is: {}.".format(testPath))
        tflist = get_file_list(testPath)
        #tflist
        tdataMat, tdataLabel = read_and_convert(tflist)
        print("test dataMat shape: {0}, test dataLabel len: {1} ".format(tdataMat.shape, len(tdataLabel)))

        #print("test dataLabel: {}".format(len(tdataLabel)))
        pre_st = time.clock()
        preResult = clf.predict(tdataMat)
        pre_et = time.clock()
        print("Recognition  " + tcn + " spent {:.4f}s.".format((pre_et-pre_st)))
        #print("predict result: {}".format(len(preResult)))
        errCount = len([x for x in preResult if x!=tcn])
        print("errorCount: {}.".format(errCount))
        allErrCount += errCount
        score_st = time.clock()
        score = clf.score(tdataMat, tdataLabel)
        score_et = time.clock()
        print("computing score spent {:.6f}s.".format(score_et-score_st))
        allScore += score
        print("score: {:.6f}.".format(score))
        print("error rate is {:.6f}.".format((1-score)))
        print("---------------------------------------------------------")


    tet = time.clock()
    print("Testing All class total spent {:.6f}s.".format(tet-tst))
    print("All error Count is: {}.".format(allErrCount))
    avgAccuracy = allScore/10.0
    print("Average accuracy is: {:.6f}.".format(avgAccuracy))
    print("Average error rate is: {:.6f}.".format(1-avgScore))
# def SVM(X,W,b):
#     X = tf.reshape(X,[-1,20*20])
#     return tf.nn.softmax(tf.matmul(X,W)+b)

# def train(do_train):
#     W = tf.Variable(tf.zeros([20*20,67]))
#     b = tf.Variable(tf.zeros([67]))
#     X = tf.placeholder(tf.float32,[20,20])
#     _y = tf.placeholder(tf.float32,[67,1])
#     _pred = SVM(X,W,b)
#     loss = -tf.reduce_sum(_y*tf.log(_pred))
#     optm = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)
#     sess = tf.Session()
#     saver = tf.train.Saver()
#     sess.run(tf.initialize_all_variables())
#     if do_train ==0:
#         epochs = 1000
#         for epoch in range(epochs):
#             x,y = init_data()
#             y_data = np.zeros([67,1])
#             y_data[y] = 1
#             # x = x.reshape([20,20])
#             sess.run(optm,feed_dict={X:x,_y:y_data})
#             if epoch % 10==0:
#                 loss = sess.run(loss,feed_dict={X:x,_y:y_data})
#                 print("Epoch: %d/%d,Loss: %f"%(epoch,epochs,loss))

if __name__ == '__main__':
    train()

