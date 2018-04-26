import numpy as np
import os
import random

classfies = []
classfies_index = []

def open_dir():
    global classfies
    for root, dirs, filename in os.walk('D:\workspace\EasyPR-python\data\easypr_train_data\chars', topdown=False):
        for dir in dirs:
            classfies.append(dir)


def init_data():
    open_dir()
    a = random.choice(classfies)
    print(os.path.join(r'D:\workspace\EasyPR-python\data\easypr_train_data\chars',a))



if __name__ == '__main__':
    init_data()
