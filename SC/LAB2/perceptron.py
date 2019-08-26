import numpy as np 
import pandas as pd 
import random
from sklearn.metrics import accuracy_score

from cross_fold_validation import cross_fold_validation

class Perceptron() :

	def __init__(self):
		pass

	def train(self, X, y,lr = 0.1,num_epochs = 100):

		self.X = X
		self.y = y
		self.wts = np.random.randn(self.X.shape[1],)

		self.threshold = random.uniform(-1,1)
		self.bias = random.uniform(-1,1)


		print("Weights: ",self.wts)
		print("Bias: ",self.bias)
		print("Threshold: ",self.threshold)

		
		for i in range(num_epochs) :

			for j in range(X.shape[0]) :
				row_i = X[j,:]
				ground_val = self.y[j]
				predicted_val = self.prediction_i(row_i)

				error = ground_val - predicted_val

				correction_term = error*lr

				self.threshold = np.subtract(self.threshold, np.multiply(lr,np.subtract(ground_val,predicted_val)))
				self.wts = np.add(self.wts,np.multiply(row_i,correction_term))


	def predict(self, X):
		y_pred = np.empty(0)
		
		for i in range(X.shape[0]):
			row_i = X[i,:]
			y_i = self.prediction_i(row_i)
			y_pred = np.append(y_pred,y_i)

		return y_pred

	def prediction_i(self, row_i):
		y = None
		intermediate = np.matmul(row_i,self.wts) + self.bias
		if intermediate > self.threshold :
			y=1
		else:
			y=0
		return y



ds = pd.read_csv('SPECTF.csv')
ds = ds.sample(frac = 1,random_state =0)
X = ds.iloc[:,:-1].values
y = ds.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()
y = label_enc.fit_transform(y)

model = Perceptron()

accuracy = cross_fold_validation(model,X,np.asarray(y))


print("\nAccuracy:", np.asarray(accuracy).mean())
