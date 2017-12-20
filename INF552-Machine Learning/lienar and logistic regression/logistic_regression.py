#Authors: Kavya Sethuram,Rasika Guru, Roshani Mangalore
import numpy as np
import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("classification.txt", sep=',', header=None)
    dataarray = np.array(data)

    Y_train = np.array(dataarray)[:,4]
    X = np.array(dataarray)[:, 0:3]

    # Add new column X0=1
    n, m = X.shape  # for generality
    X0 = np.ones((n, 1))
    X_train = np.hstack((X0, X))
    epochs=7000
    gradient=np.zeros(4)
    weights=np.random.rand(X_train.shape[1])
    le=0.01
    for value in range(epochs):
        for i in range(len(Y_train)):
            denominator= 1+np.exp(np.dot(np.dot(X_train[i],weights.T),Y_train[i]))
            gradient= gradient + (np.dot(Y_train[i],X_train[i])/denominator)
        gradient=-(gradient/len(Y_train))
        weights=weights-(le*gradient)
        weighted_x=np.dot(X_train,weights.T)
        #print "weighted_x"
        #print np.shape(weighted_x)
        #print weighted_x

    probability=(np.exp(weighted_x))/(1+np.exp(weighted_x))
    probability[probability > 0.5] = 1
    probability[probability < 0.5] = -1


    with open ("logistic-regression-weights.txt","w") as outfile:
        outfile.write('\tX1\t\t\tX2\t\t\t\tX3\t\t\tWeightedX\n')
        for i in range(2000):
            outfile.write(str(X[i])+"\t"+str(weighted_x[i])+"\n")

    with open ("logistic-regression-prediction.txt","w") as predfile:
        predfile.write('\tX1\t\t\tX2\t\t\t\tX3\t\tY\t\tYpred\n')
        for i in range(2000):
            #predfile.write(str(X[i])+"\t"+str(Y_train[i])+"\t"+str(probability[i])+"\n")
            predfile.write('{:10s} {:3s}  {:7s}'.format(str(X[i])+"\t",str(Y_train[i])+"\t",str(probability[i]))+"\n")
    #Compute the Accuracy of Logistic Regression Method
    count = 0.0
    for i in range (len(Y_train)):
        if probability[i]==Y_train[i]:
            count+=1
    accuracy=(count/len(Y_train))*100
    print accuracy




