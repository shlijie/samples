
from __future__ import print_function

# python 3.6
# tensorflow 2.0.0
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import numpy
import matplotlib.pyplot as plt
rng = numpy.random

# Parameters
learning_rate = 0.001
training_epochs = 10000
display_step = 100

# Training Data
train_X = numpy.asarray([1,2,3,4,5,6,7,8,9,10,11])
# train_X = numpy.asarray([2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])
train_Y = numpy.asarray([0.52,9.36,33.6,191,362,571,912.17,1207,1682,2135,2684])
n_samples = train_X.shape[0]

# tf Graph Input
X = tf.compat.v1.placeholder("float")
Y = tf.compat.v1.placeholder("float")

# Set model weights
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")
W_2 = tf.Variable(rng.randn(), name="weight_2")
# W_3 = tf.Variable(rng.randn(), name="weight_3")

# Construct a linear model
pred = tf.add(tf.multiply(X, W), b)
pred = tf.add(tf.multiply(tf.pow(X, 2), W_2), pred)
# pred = tf.add(tf.multiply(tf.pow(X, 3), W_3), pred)

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
# Gradient descent
#  Note, minimize() knows to modify W and b because Variable objects are trainable=True by default
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
# init = tf.global_variables_initializer()
init = tf.compat.v1.global_variables_initializer()

# Start training
with tf.compat.v1.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "W_2=", sess.run(W_2), "b=", sess.run(b))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    # print("Training cost=", training_cost, "W=", sess.run(W),  "W_2=", sess.run(W_2),  "W_3=", sess.run(W_3), "b=", sess.run(b), '\n')
    print("Training cost=", training_cost, "W=", sess.run(W),  "W_2=", sess.run(W_2), "b=", sess.run(b), '\n')
    pred2020 = 12*12*W_2 + 12*W + b
    print("predict 2020", pred2020)

    # Graphic display
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    # plt.plot(train_X, sess.run(W) * train_X + train_X ** 2 * sess.run(W_2) + train_X ** 3 * sess.run(W_3) + sess.run(b), label='Fitted line')
    plt.plot(train_X, sess.run(W) * train_X + train_X ** 2 * sess.run(W_2) + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()
