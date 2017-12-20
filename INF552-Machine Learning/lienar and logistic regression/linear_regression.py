#Authors: Kavya Sethuram, Rasika Guru, Roshani Mangalore
import numpy as np
import pandas as pd

if __name__=="__main__":
    data=pd.read_csv("linear-regression.txt",sep=',',header=None)
    dataarray=np.array(data)

    Y_train=np.array(dataarray)[:,2]
    X=np.array(dataarray)[:,0:2]

    print Y_train
    print X

    #Add new column X0=1 for padding
    n, m = X.shape  # for generality
    X0 = np.ones((n, 1))
    X_train = np.hstack((X0,X))

    weights = np.dot(np.dot(np.linalg.inv(np.dot(X_train.T, X_train)), X_train.T), Y_train)
    weighted_X=np.dot(X_train,weights)

    #print weights on the screen
    print ("weights:")
    print weights
    #to print it on the screen
    print ("weighted X:")
    print weighted_X

    #to write into the file
    with open ("linear-regression-output.txt","w") as outfile:
        outfile.write('\tX1\t\t\t\tX2\t\t\tY\t\t\tPredicted_Y\n')
        for i in range(3000):
            outfile.write(str(X[i])+"\t"+str(Y_train[i])+"\t"+str( [i])+"\n")





    