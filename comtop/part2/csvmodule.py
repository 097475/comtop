import matplotlib.pyplot as plt
import pandas as pd

##TODO memory leaks
def getDataFrameFromText(path, index = 0, delim = ',', header_index = 0):
    return pd.read_csv(path, index_col = index, sep = delim, header = header_index)

def plotDF(df):
    df.plot()
    plt.savefig('test.svg')  ##inserire path

def getMatrixFromDataFrame(df):
    return df.values

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
    #df.plot()
    #plt.show()
    #plotCSV('hw_25000.csv')
    #plotTXT('hw_25000.csv',',')


    print(getMatrixFromDataFrame(getDataFrameFromText('hw_25000.csv',0,',',0)))
    plotDF(getDataFrameFromText('hw_25000.csv',0,',',0))
