from django.test import TestCase

#import part2.matrix as matrix
#import part2.keplermodule as keplermodule
#import part2.entropy as entropy
import matrix, keplermodule, entropy, edfmodule, csvmodule, ripsermodule
import numpy
import random
# Create your tests here.

def randomMatrix(height,length):
    return numpy.array([[random.randint(1,101) for i in range(length)] for i in range(height)])

def randomEntropyMatrix(height):
    return numpy.array([(lambda x : [x,x+random.randint(1,101)])(random.randint(1,101)) for i in range(height)])

class MatrixTestCase(TestCase):
    def setUp(self):
        self.m = randomMatrix(3,10)

    def test_len(self):
        self.assertEqual(len(matrix.corrMatrix(self.m)), len(self.m))
        self.assertEqual(len(matrix.distMatrix(self.m)), len(self.m[0]))

class KMTestCase(TestCase):
    def setUp(self):
        self.m = randomMatrix(3,10)
        self.dist = matrix.distMatrix(self.m)
        self.mapper = keplermodule.getMapper()
    def test(self):
        projected_data = self.mapper.fit_transform(self.dist)
        graph = self.mapper.map(projected_data)
        self.mapper.visualize(graph)

class EntropyTestCase(TestCase):
    def setUp(self):
        self.m = randomEntropyMatrix(random.randint(1,101))
    def test(self):
        entropy.entropy(self.m)


if __name__ == '__main__':
    '''
    a = edfmodule.readEDF('sample.edf')
    mat = edfmodule.edfToMatrix(a)
    dist = matrix.distMatrix(mat[:,:10])
    mapper = keplermodule.getMapper()
    projected_data = mapper.fit_transform(dist)
    graph = mapper.map(projected_data)
    mapper.visualize(graph)
    '''
    a = edfmodule.readEDF('sample.edf')
    mat = edfmodule.edfToMatrix(a)
    dist = matrix.corrMatrix(mat)
    rips = ripsermodule.getRips()
    diagrams = rips.fit_transform(dist, distance_matrix = True)
    print(diagrams)
    rips.plot(diagrams)
    import matplotlib.pyplot as plt
    plt.savefig("rips.svg")

