# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import scipy.spatial.distance as dist
import tests


def corrMatrix(m):
    return numpy.corrcoef(m)
def distMatrix(m, metric = 'euclidean'):
    _metric = metric
    if _metric not in ['braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation', 'cosine', 'dice', 'euclidean', 'hamming', 'jaccard', 'jensenshannon', 'kulsinski', 'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']:
        raise ValueError("invalid distance algorithm") 
    return dist.squareform(dist.pdist(m.transpose(), metric = _metric))


def splitMatrix(m, window, overlap = 0):
    '''
        # for correlation matrix
        if window != 0 and window < len(m):
            raise ValueError("window must be >= the number of rows of input matrix")
    '''

    cols = len(m[0]) 
    step = window - overlap
    windows = 1 + (cols - window) // step

    for i in range(windows):
        tmp = m[:,window*i - overlap*i : window*(i+1) - overlap*i]
        yield tmp  





#TODO: alert user that overlap is invalid to correct overlap
    # change overlap rules
    #change window dynamic

if __name__ == '__main__':
   # m = randomMatrix(3,10)
    #print(tmp)
    #print(m)
    #print(corrMatrix(m)) #funziona
    #print(distMatrix(m)) #funziona?

    '''
    for i in corrMatrix(m):
        print(i)
    '''
    #print(next(distMatrix(m, type='canberra')))
    
    '''
    for i in distMatrix(m,window=10):
        print(i)
   

    m = tests.randomMatrix(3,10)
    print(m)
    for i in distMatrix(m,window=3, overlap = 0):
        pass
    '''