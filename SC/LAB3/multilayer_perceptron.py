import numpy as np 
import pandas as pd 
import math

class SingleLayer :

	def __init__(self):
		pass


	def train(self,X,y, lr = 0.1, num_epochs = 100):
		
		self.X = X
		self.y = y
		self.weights1 = np.random.randn(self.X.shape[1],5)
		self.weights2 = np.random.randn(5,2)
		#self.weights = np.asarray([0.1,0.3])
		self.bias1 = np.random.randn(5,)
		self.bias2 = np.random.randn(1,)

		'''print("Initial Weights: ",self.weights)
		print("Initial threshold: ",self.threshold)
		print("Initial bias: ",self.bias,"\n")'''

		
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


				self.weights = self.adjust_weights(self.weights)
				self.adjust_bias(self.bias)

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

		intermediateValues = np.add(np.matmul(row_i,self.weights1) ,self.bias1)
		intermediateValues = sigmoid_activation(intermediateValues)

		output = np.add(np.matmul(intermediateValues,self.weights2) ,self.bias2)
		output =sigmoid_activation(output)


		#print(intermediateValue)

		if output > 0.5 :
			y=1

		else :
			y=0

		return y

	def sigmoid_activation(self,vector) :

		v_sigmoid = np.vectorize(lambda x : 1 / (1 + math.e**(-x)))

		activated_vector = v_sigmoid(vector)

		return activated_vector

