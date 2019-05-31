import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)
product = tf.mul(x1,x2)


with tf.session() as sess:
    output = sess.run(product)
    print(output)
