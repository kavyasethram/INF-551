#Authors: Kavya Sethuram,Rasika Guru,Roshani Mangalore
import pandas as pd
import random
import numpy as np

if __name__ == "__main__":
    dataframe = pd.read_csv('classification.txt', header=None)
    df = dataframe.values
    weights = [0,0,0,0]

    sum = 0
    eta = 0.01
    count_list = []
    epoch = 0
    while (True):
        loopvar = False
        i = 0
        #epoch = 0
        while(i < len(df)):
            sum = weights[0] +  weights[1]*df[i][0] + weights[2]*df[i][1] + weights[3]*df[i][2]
            if sum < 0:
                if df[i][3] < 0:
                    df[i][4] = df[i][3]
                else:
                    weights[0] += eta * 1
                    weights[1] += eta * df[i][0]
                    weights[2] += eta * df[i][1]
                    weights[3] += eta * df[i][2]
                    epoch = epoch + 1
                    loopvar=True
            elif sum >= 0:
                if df[i][3] > 0:
                    df[i][4] = df[i][3]
                else:
                    weights[0] -= eta
                    weights[1] -= eta * df[i][0]
                    weights[2] -= eta * df[i][1]
                    weights[3] -= eta * df[i][2]
                    epoch = epoch + 1
                    loopvar = True
            count_list.append(epoch)
            i = i+1
        if loopvar == False:
            break
    print(weights)
    np.savetxt("perceptron-output.txt", df, fmt=" %17.15f, %17.15f, %17.15f, %5d,   %5d", delimiter=' ', newline='\n',
               header='                      Data Points                         Label  Prediction')



