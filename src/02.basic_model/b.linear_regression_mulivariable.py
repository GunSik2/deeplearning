# Multi variable linear regression
# Hypothesis: H(x) = W * X
# Cost Fun.: cost(w,b) = Sum(H(x) - y)^2 * 1/m
# Gradient descent: W := W - alpah * 1/m * Sum((W*x - y) * x)


import tensorflow as tf
import numpy as np

# Parameters
learning_rate = 0.1     # learning rate, alpha

# training data
train_X = [[1, 1, 1, 1, 1],       # for b
     [1., 0., 3., 0., 5.],  # x1
     [0., 2., 0., 4., 0.]]  # x2
train_Y = [1, 2, 3, 4, 5]

# tf Graph Input
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# Set model weights: initial value (w, b)
W = tf.Variable(tf.random_uniform([1, len(train_X)], -1., 1.))

# Hypothesis: Linear model
hypothesis = tf.matmul(W, X)

# Cost function: Mean squared error
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost) # goal is minimize cost

# Initializing the variables
init = tf.initialize_all_variables()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # fit the line
    for step in range(1000):
        sess.run(optimizer,  feed_dict={X: train_X, Y: train_Y})
        if step % 20 == 0:
            print(step, sess.run(cost, feed_dict={X: train_X, Y: train_Y}), sess.run(W))

    # learns best fit is w: [0 1 1]
    print(sess.run(hypothesis, feed_dict={X: [[1], [3], [1]]}))
