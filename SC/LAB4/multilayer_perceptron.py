import pandas as pd 
import numpy as np 

from sklearn.metrics import accuracy_score

def cross_fold_validation(model,X,y, k = 10) :

	part_length = X.shape[0]//k

	init = 0
	fin = part_length
	acc = []
	i = 0
	while fin <= X.shape[0] :

		#print(init,fin)
		val_X = X[init : fin, :]
		train_X = np.concatenate((X[0:init,:], X[fin:,:]) , axis = 0)

		val_y = y[init : fin]
		train_y = np.concatenate((y[0:init], y[fin:]) , axis = None)

		model.train(train_X, train_y,0.1,500)


		y_pred = model.predict(val_X)
		print(y_pred)

		acc.append(accuracy_score(y_pred,val_y))

		print(init,fin,i)

		if i == k-2 :
			init+=part_length
			fin = X.shape[0]
			i+=1
			
		else:
			init+=part_length
			fin+=part_length
			i+=1

	return np.asarray(acc)

class MLP :

	def __init__(self) :
		pass

	def init_weights_bias(self, num_input_nodes,num_hidden_nodes):
		
		self.W1 = np.random.randn(num_input_nodes,num_hidden_nodes)
		self.W2 = np.random.randn(num_hidden_nodes, 1)
		self.b1 = np.random.randn(1,num_hidden_nodes)
		self.b2 = np.random.randn(1,1)
		self.sigmoid_vect = np.vectorize(self.sigmoid)
		self.lr =0.9

	def sigmoid(self, x):
		return 1.0 / (1+np.exp(-x))


	def train(self, X, y, lr = 0.1, num_epochs = 1000):

		self.X = X
		self.y = y
		self.lr = lr
		self.init_weights_bias(X.shape[1],X.shape[1]*2)
		
		for i in range(num_epochs):
			
			for j in range(X.shape[0]) :

				y_pred = self.forward_prop(X[j,:])
				self.back_prop(X[j,:],y_pred,y[j])


	def forward_prop(self,inp) :

		input_layer = inp.reshape(1,-1)

		#print(self.b1)
		hidden_layer = np.matmul(input_layer,self.W1)+self.b1
		hidden_layer = self.sigmoid_vect(hidden_layer)
		#print("hidden_layer:\n",hidden_layer)

		output_layer = np.add(np.matmul(hidden_layer,self.W2),self.b2)
		output_layer = self.sigmoid_vect(output_layer)
		#print("\noutput_layer:\n",output_layer)
		output_layer = np.where(output_layer >=0.5 , 1,0)

		return output_layer

	def back_prop(self, input_layer, y_pred, y_target):
		
		#Output layer error
		output_err = y_pred*(1-y_pred)*(y_target - y_pred)
		output_err = output_err.reshape(1,-1)
		#print("output_err\n",output_err)

		#Hidden Layer error
		hidden_layer = np.add(np.matmul(input_layer,self.W1),self.b1)
		hidden_output = self.sigmoid_vect(hidden_layer)
		#print("hidden_output\n",hidden_output)
		hidden_err = hidden_output*(1 - hidden_output)*np.matmul(self.W2,output_err).T
		#print("hidden_err\n",hidden_err)

		#Updating W2 weights
		output_x,output_y = np.meshgrid(output_err,hidden_output)
		delta_w2 = self.lr*output_x*output_y
		#print("delta_w2\n",delta_w2)
		self.W2 = self.W2 + delta_w2
		#print(self.W2)


		#Updating W1 weights
		output_x,output_y = np.meshgrid(hidden_err,input_layer)
		delta_w1 = self.lr*output_x*output_y
		#print("delta_w1\n",delta_w1)
		self.W1 = self.W1 + delta_w1
		#print(self.W1)

		#Updating b2
		delta_b2 = self.lr*output_err
		self.b2 = self.b2+delta_b2
		#print("updated b1\n",self.b1)

		#Updating b1
		delta_b1 = self.lr*hidden_err
		self.b1 = self.b1+delta_b1
		#print("updated b2\n",self.b2)

	def predict(self,X):
		
		y_pred = np.empty((0,))
		for i in range(X.shape[0]) :

			y = self.forward_prop(X[i,:])
			y_pred = np.append(y_pred,y)

		return y_pred


if __name__ == '__main__':
	main()

def main():
		
	classifier = MLP()

	dataset = pd.read_csv('SPECT.csv')
	dataset = dataset.sample(frac = 1,random_state =0)
	inputs = dataset.iloc[:,1:].values
	outputs = dataset.iloc[:,0].values

	from sklearn.preprocessing import LabelEncoder
	label_enc = LabelEncoder()
	outputs = label_enc.fit_transform(outputs)
	outputs = outputs.reshape(-1,1)

	'''classifier.init_weights_bias(3,2)
	print(classifier.W1.shape)
	print(classifier.W2.shape)
	print(classifier.b1.shape)
	print(classifier.b2.shape)'''

	'''classifier.W1 = np.asarray([[0.2, -0.3],[0.4, 0.1],[-0.5, 0.2]])
	classifier.W2 = np.asarray([[-0.3] ,[-0.2]])
	classifier.b1 = np.asarray([[-0.4,0.2]])
	classifier.b2 = np.asarray([[0.1]])'''

	#inp = np.asarray([1,0,1])
	#y_target = np.asarray([1])
	#y_pred = classifier.forward_prop(inp,)
	#classifier.back_prop(inp,y_pred,y_target)

			
	'''classifier.train(inputs,outputs)

	y_pred = classifier.test(inputs)
	#print(y_pred)
	from sklearn.metrics import accuracy_score
	acc = accuracy_score(outputs,y_pred)
	print(acc)'''

	accuracy =  cross_fold_validation(classifier,inputs,outputs)
	print(accuracy.mean())
