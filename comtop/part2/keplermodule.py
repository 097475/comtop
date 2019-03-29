# Import the class
import kmapper as km

# Some sample data
from sklearn import datasets
data, labels = datasets.make_circles(n_samples=1, noise=0.03, factor=0.3)

print(data)

