import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##TODO memory leaks
def getDataFrameFromText(path, index = 0, delim = ','):
    return pd.read_csv(path, index_col = index, sep = delim)

def plotDF(data):
    plt.plot(data)
    plt.savefig('test.png')

def getMatrixFromDataFrame(data):
    return data.values

'''
def plotCSV(path):
    df = pd.read_csv(path, index_col=0)
    csvToMatrix(df)
    plt.plot(df)
    plt.show()

def plotTXT(path, delimiter):  ##todo skip first
    data = np.genfromtxt(path,delimiter=delimiter,skip_header = 1)
    plt.plot(data[:,1:])
    plt.show()
def csvToMatrix(data):
    print(data.values)
def txtToMatrix():
    pass

'''


if __name__ == '__main__':
    #data = np.genfromtxt('hw_25000.csv',delimiter=',')
    #plt.plotfile('hw_25000.csv',(0,1,2))
    #df = pd.read_csv('hw_25000.csv', index_col=0)
    #plotCSV('hw_25000.csv')
    #plotTXT('hw_25000.csv',',')
    print(getMatrixFromDataFrame(getDataFrameFromText('hw_25000.csv',0,',')))
    plotDF(getDataFrameFromText('hw_25000.csv',0,','))
