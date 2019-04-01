# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import scipy.spatial.distance as dist


def corrMatrix(m, window = 0, overlap = 0):
##aggiustare overlap quando c'è il resto
    def _corrMatrix(m, window = 0, overlap = 0):
        ##exception for negative window and overlap
        if window < 0:
            raise ValueError("window must be >= 0")
        if window != 0 and window < len(m):
            raise ValueError("window must be >= the number of rows of input matrix")
        if window > len(m[0]):
            raise ValueError("window must be <= the number of columns of input matrix")
        if overlap < 0:
            raise ValueError("overlap must be >= 0")
            
        windows,remainder = divmod(len(m[0]),window)
        cols = len(m[0])
        step = window - overlap
        if (cols - window) % step != 0:  ##invalid overlap, reset overlap to step=1
            overlap = window - 1
            windows = 1 + cols - window
        else:
            windows = 1 + (cols - window) // step

        for i in range(windows):
            tmp = m[:,window*i - overlap*i : window*(i+1) - overlap*i]
            yield numpy.corrcoef(tmp)  

    if window > 0:
        _corrMatrix(m,window,overlap)
    else:
        return numpy.corrcoef(m)

def distMatrix(m,window = 0, overlap = 0, type = 'euclidean'):
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html#scipy.spatial.distance.pdist
    def _distMatrix(m, window = 0, overlap = 0, type = 'euclidean'):
        if window > len(m[0]):
            raise ValueError("window must be <= the number of columns of input matrix")
        if window < 0:
            raise ValueError("window must be >= 0")
        if overlap < 0:
            raise ValueError("overlap must be >= 0")
        if type not in ['braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation', 'cosine', 'dice', 'euclidean', 'hamming', 'jaccard', 'jensenshannon', 'kulsinski', 'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']:
            raise ValueError("invalid distance algorithm") 

        windows,remainder = divmod(len(m[0]),window)
        cols = len(m[0])
        step = window - overlap
        if (cols - window) % step != 0:  ##invalid overlap, reset overlap to step=1
            overlap = window - 1
            windows = 1 + cols - window
        else:
            windows = 1 + (cols - window) // step

        for i in range(windows):
            tmp = m[:,window*i - overlap*i : window*(i+1) - overlap*i]
            yield dist.squareform(dist.pdist(tmp.transpose(), metric = type))

    if window > 0:
        _distMatrix(m,window,overlap,type)   
    else:     
        return dist.squareform(dist.pdist(m.transpose(), metric = type))


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
    '''
    