import math
import sklearn.preprocessing
import sklearn.cluster
import sklearn.mixture
import kmapper
import ripser
import json
import matplotlib.pyplot as plt
import numpy as np
from os.path import join
import edfmodule
import matrixmodule


class FiltrationAnalysis:
    '''
    class FiltrationChoice(Enum):
        VIETORIS_RIPS = 'Vietoris Rips Filtration'
        CLIQUE_WEIGHTED_RANK = 'Clique Weighted Rank Filtration'
    '''
    type = 'Vietoris Rips Filtration'
    max_homology_dimension = 1
    max_distances_considered = math.inf
    coeff = 2
    do_cocycles = False
    n_perm = None

    result = None
    plot = None

    # TODO: matrix is raw
    def execute(self, matrix, start_point=None, end_point=None):
        ## dist matrix metric!
        if self.type == 'Vietoris Rips Filtration':
            matrix = matrixmodule.distMatrix(matrix)
        elif self.type == 'Clique Weighted Rank Filtration':
            matrix = matrixmodule.corrMatrix(matrix)
        image_path = 'test_image.svg'
        rips = ripser.Rips(maxdim=self.max_homology_dimension, thresh=self.max_distances_considered, coeff=self.coeff,
                           do_cocycles=self.do_cocycles, n_perm=self.n_perm, verbose=False)
        result = rips.fit_transform(matrix, distance_matrix=True)
        rips.plot(result)
        plt.savefig(image_path)
        result = [l.tolist() for l in result]
        self.result = json.dumps(result)
        self.plot = 'test_image.svg'



class MapperAnalysis:
    scalers = {
        'None': None,
        'MinMaxScaler': sklearn.preprocessing.MinMaxScaler(),
        'MaxAbsScaler': sklearn.preprocessing.MaxAbsScaler(),
        'RobustScaler': sklearn.preprocessing.RobustScaler(),
        'StandardScaler': sklearn.preprocessing.StandardScaler()
    }

    clusterers = {
        'K-Means': sklearn.cluster.KMeans(),
        'Affinity propagation': sklearn.cluster.AffinityPropagation(),
        'Mean-shift': sklearn.cluster.MeanShift(),
        'Spectral clustering': sklearn.cluster.SpectralClustering(),
        'Agglomerative clustering': sklearn.cluster.AgglomerativeClustering(),
        'DBSCAN': sklearn.cluster.DBSCAN(min_samples=3),
        'Gaussian mixtures': sklearn.mixture.GaussianMixture(),
        'Birch': sklearn.cluster.Birch()
    }
    # TODO: Inserire parametri
    '''
    class ProjectionChoice(Enum):
        SUM = 'sum'
        MEAN = 'mean'
        MEDIAN = 'median'
        MAX = 'max'
        MIN = 'min'
        STD = 'std'
        DIST_MEAN = 'dist_mean'
        L2NORM = 'l2norm'
        KNN_DISTANCE = 'knn_distance_n'  # TODO knn_distance, add scikit classes

    class ScalerChoice(Enum):
        NONE = 'None'
        MINMAXSCALER = 'MinMaxScaler'
        MAXABSSCALER = 'MaxAbsScaler'
        ROBUSTSCALER = 'RobustScaler'
        STANDARDSCALER = 'StandardScaler'

    class ClustererChoice(Enum):
        KMEANS = 'K-Means'
        AFFINITYPROPAGATION = 'Affinity propagation'
        MEANSHIFT = 'Mean-shift'
        SPECTRALCLUSTERING = 'Spectral clustering'
        AGGLOMERATIVE = 'Agglomerative clustering'
        DBSCAN = 'DBSCAN'
        GAUSSIANMIXTURES = 'Gaussian mixtures'
        BIRCH = 'Birch'
    '''
    # fit_transform parameters; not implemented : scaler params, scikit projections
    projection = 'std'
    scaler = 'StandardScaler'

    # map parameters; not implemented : clusterer params, cover limits
    
    use_original_data = True
    clusterer = 'K-Means'
    cover_n_cubes = 10
    cover_perc_overlap = 0.5
    graph_nerve_min_intersection = 1
    remove_duplicate_nodes = False

    graph = None


    # TODO: matrix is raw
    def execute(self, matrix):
        matrix = matrixmodule.distMatrix(matrix)
        mapper = kmapper.KeplerMapper()
        mycover = kmapper.Cover(n_cubes=self.cover_n_cubes, perc_overlap=self.cover_perc_overlap)
        mynerve = kmapper.GraphNerve(min_intersection=self.graph_nerve_min_intersection)
        original_data = matrix if self.use_original_data else None
        projected_data = mapper.fit_transform(matrix, projection=self.projection,
                                              scaler=MapperAnalysis.scalers[self.scaler], distance_matrix=False)
        graph = mapper.map(projected_data, X=original_data, clusterer=MapperAnalysis.clusterers[self.clusterer],
                           cover=mycover, nerve=mynerve, precomputed=False,
                           remove_duplicate_nodes=self.remove_duplicate_nodes)
        output_graph = mapper.visualize(graph, save_file=True)
        self.graph = output_graph


def ripsertest():
    a = edfmodule.readEDF('sample.edf')
    mat = edfmodule.edfToMatrix(a)
    m = next(matrixmodule.splitMatrix(mat, window = 1000, overlap = 0))
    t = FiltrationAnalysis()
    t.execute(m)

def kmappertest():
    a = edfmodule.readEDF('sample.edf')
    mat = edfmodule.edfToMatrix(a)
    m = next(matrixmodule.splitMatrix(mat, window = 1000, overlap = 0))
    t = MapperAnalysis()
    t.execute(m)

if __name__ == '__main__':
    kmappertest()