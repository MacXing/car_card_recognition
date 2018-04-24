import tensorflow as tf
import tensorlayer as tl
import os


def load_image():
    for root, dirs, files in os.walk(r"H:\毕业论文\car_recognition\image", topdown=False):
        for name in files:
            print(os.path.join(root, name))


def cnn_network():
    sess = tf.InteractiveSession()
    X_train, y_train, X_val, y_val, X_test, y_test = load_image()
    x = tf.placeholder(tf.float32,shape=[500,120,256],name='x')
    y_ = tf.placeholder(tf.float64,shape=[1],name='y_')
    #构建网络
    network = tl.layers.InputLayer(inputs=x,name='input_layer')
    network = tl.layers.Conv2dLayer(network,32,(5,5),(1,1),act=tf.nn.relu(),padding="SAME",name="cnn1")
    network = tl.layers.MaxPool2d(network,(2,2),(2,2),padding="SAME",name = "pool1")
    network = tl.layers.Conv2dLayer(network,64,(5,5),(1,1),act=tf.nn.relu(),padding="SAME",name="conn2")
    network = tl.layers.MaxPool2d(network,(2,2),(2,2),padding="SAME",name="pool2")
    network = tl.layers.FlattenLayer(network,name="flatten")
    network = tl.layers.DropoutLayer(network,keep=0.5,name="drop1")
    network = tl.layers.DenseLayer(network,256,act=tf.nn.relu(),name="relu1")
    network = tl.layers.DropoutLayer(network,name="drop2")
    network = tl.layers.DenseLayer(network,2,act=tf.identity(),name="output")
    #定义损失函数
    y = network.outputs
    cost = tl.cost.cross_entropy(y,y_,name="cost")
    correct_prediction = tf.equal(tf.arg_max(y, 1), y_)
    acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    y_op = tf.arg_max(tf.nn.softmax(y), 1)

    # 定义优化器
    train_param = network.all_params
    train_op = tf.train.AdamOptimizer(learning_rate=0.0001, use_locking=False).minimize(cost, var_list=train_param)

    # tensorboard
    acc_summ = tf.summary.scalar('acc', acc)
    cost_summ = tf.summary.scalar('cost', cost)
    summary = tf.summary.merge_all()
    writer = tf.summary.FileWriter('./logs')
    writer.add_graph(sess.graph)

    # 初始化参数
    tl.layers.initialize_global_variables(sess)

    # 列出模型信息
    network.print_layers()
    network.print_params()

    # 训练模型
    tl.utils.fit(sess, network, train_op, cost, X_train, y_train, x, y_,
                 acc=acc, batch_size=512, n_epoch=100, print_freq=10,
                 X_val=X_val, y_val=y_val, eval_train=False, tensorboard=True)

    # 评估
    tl.utils.test(sess, network, acc, X_test, y_test, x, y_, batch_size=None, cost=cost)

    # 保存模型
    tl.files.save_npz(network.all_params, name='model.npz')
    sess.close()
if __name__ == '__main__':
    x = tf.placeholder(tf.float32, shape=[500, 120, 256], name='x')
    print(x)
