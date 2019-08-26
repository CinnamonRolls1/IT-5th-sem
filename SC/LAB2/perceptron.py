import numpy as np 
import pandas as pd 
import random
from sklearn.metrics import accuracy_score

from cross_fold_validation import cross_fold_validation

class Perceptron() :

	def __init__(self):
		pass

	def train(self, X, y,lr = 0.1,num_epochs = 100):

		#Initializing model parameters
		self.X = X
		self.y = y
		self.weights = np.random.randn(self.X.shape[1],)
		#self.weights = np.asarray([0.1,0.3])
		self.threshold = random.uniform(-1,1)
		self.bias = random.uniform(-1,1)
		#self.bias =0

		print("Weights: ",self.weights)
		print("Threshold: ",self.threshold)
		print("Bias: ",self.bias,"\n")

		
		for i in range(num_epochs) :

			for j in range(X.shape[0]) :
				row_i = X[j,:]
				ground_val = self.y[j]
				predicted_val = self.prediction_i(row_i)

				error = ground_val - predicted_val

				correction_term = error*lr
				

				#print('error',error)
				#print('correction_term',correction_term)
				#print('row',row_i)
				#print("old_weights: ",self.weights,'\n')


				self.weights = np.add(self.weights,np.multiply(row_i,correction_term))
				self.threshold = np.subtract(self.threshold, np.multiply(lr,np.subtract(ground_val,predicted_val)))

				#print('predicted_val',predicted_val)
				#print("Weights: ",self.weights, "\nThreshold:", self.threshold,"\n\n")





	def predict(self, X):
		y_pred = np.empty(0)
		
		for i in range(X.shape[0]) :

			row_i = X[i,:]

			y_i = self.prediction_i(row_i)
			y_pred = np.append(y_pred,y_i)


		return y_pred

	def prediction_i(self, row_i):
		y = None

		intermediateValue = np.matmul(row_i,self.weights) + self.bias
		#print(intermediateValue)

		if intermediateValue > self.threshold :
			y=1

		else:
			y=0

		return y



'''X = np.asarray([[0,0],[0,1],[1,0],[1,1]])
y = np.asarray([0,1,1,0])

print(X,"\n")
print(np.reshape(y,(-1,1)),"\n\n")

classifier = Perceptron()
classifier.train(X,y,0.2,1)
y_pred = classifier.predict(X)
#print('\n',classifier.threshold)	
print(y_pred)'''

dataset = pd.read_csv('IRIS.csv')
dataset = dataset.sample(frac = 1,random_state =0)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()
y = label_enc.fit_transform(y)

'''print(X.shape)
print(y.shape)

classifier = Perceptron()
classifier.train(X,y,num_epochs = 500)

y_pred = classifier.predict(X)

print(accuracy_score(y,y_pred))'''

classifier = Perceptron()

accuracy = cross_fold_validation(classifier,X,np.asarray(y))


print("Accuracy:", np.asarray(accuracy).mean())
