from django.test import TestCase
from . import matrix
from . import keplermodule
import numpy
import random
# Create your tests here.

def randomMatrix(height,length):
    return numpy.array([[random.randint(1,101) for i in range(length)] for i in range(height)])

class MatrixTestCase(TestCase):
    def setUp(self):
        self.m = randomMatrix(3,10)

    def test_len(self):
        self.assertEqual(len(next(matrix.corrMatrix(self.m))), len(self.m))
        self.assertEqual(len(next(matrix.distMatrix(self.m))), len(self.m[0]))

class KMTestCase(TestCase):
    def setUp(self):
        self.m = randomMatrix(3,10)
        self.dist = next(matrix.distMatrix(self.m))
    def test(self):
        projected_data = keplermodule.mapper.fit_transform(self.dist)
        graph = keplermodule.mapper.map(projected_data)
        keplermodule.mapper.visualize(graph)

