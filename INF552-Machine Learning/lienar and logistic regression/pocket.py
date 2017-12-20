#Authors: Kavya Sethuram, Rasika Guru, Roshani Mangalore
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Reading the datapoints
df_dataset = pd.read_csv('classification.txt',header=None,names=['x1','x2','x3','ignore','labels'])
data_array = np.asarray(df_dataset[['x1','x2','x3']])
output_array = np.asarray(df_dataset[['labels']])


x0 = 1
weights = []
count_list = []
learning_rate = 0.01

# Random Initialization of Weights
for i in range(4):
    weights.append(random.uniform(-1,1))

weight = np.array(weights)

#Calculation of activation function and class prediction

for j in range(7000):
    count = 0

    for i in range(len(data_array)):
        x= np.ones((1,4))
        x[:,1:] = data_array[i]


        activation_func = np.matrix(x)*np.matrix(weight).T

        if activation_func[0][0] > 0:
            predicted_class = 1
        else:
            predicted_class = -1

        if output_array[i] == predicted_class:
            pass
        else:

            count+=1
            if predicted_class == -1:

                weight = weight + (learning_rate)*np.matrix(x)
            else:

                weight = weight - (learning_rate)*np.matrix(x)


    count_list.append(count)

    
# Plotting the misclassifications
x_list = []
for i in range(1,7001,1):
    x_list.append(i)

plt.xlabel('Iterations')
plt.ylabel('Number of Misclassifications')
plt.scatter(x_list,count_list,marker='*')
plt.show()






