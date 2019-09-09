import pandas as pd 
import numpy as np

class Naive_Bayes() :

	def __init__(self,):
		self.X = None
		self.y = None


	def train(self,X = None, y = None):

		self.X = X
		self.y = y.flatten()
		
		self.num_rows = len(X)

		self.attr_set = self.get_attribute_set(self.X)

		self.class_labels = self.get_attribute_set(self.y)

		'''for i in range(self.num_rows) :
						
									self.P_y_given_X = self.get_classwise_probability(self.X[i,:])'''

	def get_classwise_probability(self, row, label) :

		prob_y = self.class_labels[0][label]*1.0 / self.num_rows



		for i in range(len(self.attr_set)) :

			prob_y_given_xi = self.get_prob_y_given_xi(i,row[i], label)
			#print(prob_y_given_xi,end = ' ')

			prob_y *= prob_y_given_xi


		return prob_y

	def get_label_count(self,sub_column,column_no):
		
		sub_attr_set = list(0 for i in range(self.attr_set[column_no].shape[0]))
		#print(sub_attr_set)

		for i in range(sub_column.shape[0]) :
			sub_attr_set[sub_column[i]] +=1

		return sub_attr_set


	def get_prob_y_given_xi(self, column_no,column_label, y_label):
					
					
						sub_table = self.X[self.y == y_label]
			
						sub_attr_set = self.get_label_count(sub_table[:,column_no], column_no)
			
						num = float(sub_attr_set[column_label])
						den = float(sub_table.shape[0])
			
						prob_y = num/den
						#print(prob_y)

			
						return prob_y

	'''def get_prob_y_given_xi(self, column_no,column_label, y_label):
					
					
					sub_table = self.X[self.y == y_label]
					#print(sub_table)
			
					sub_attr_set = self.get_label_count(sub_table[:,column_no],column_no)
					#print("shape",sub_attr_set.shape)
			
			
					den = len(sub_table)
					num = sub_attr_set[column_label]
			
					prob = num*1.0/den
					print(prob)
			
					return prob'''


		

	def get_attribute_set(self,table, selected_columns = 'all'):

		attr_set = []

		#print(len(table.shape))
		if (len(table.shape)) == 1 :
			table= table.reshape(-1,1)

		#print(table.shape)

		if selected_columns == 'all' :
			columns = list(range(table.shape[1]))

		else :
			columns = selected_columns
		
		for i in columns :

			column = table[:,i]
			_,unique_counts = np.unique(column,return_counts = True)

			attr_set.append(unique_counts)

		return attr_set

	def predict(self, X) :

		y_pred = []
		#print(self.class_labels)

		for i in range(X.shape[0]) :

			high_prob = float('-inf')
			pred_val = 0
			for j in range(self.class_labels[0].shape[0]) :

				#print(i,j)
				temp = self.get_classwise_probability(X[i,:], j)
				#print(temp)

				if temp > high_prob :
					high_prob = temp
					pred_val = j

			y_pred.append(pred_val)

		return y_pred

def accuracy(y_truth, y_pred) :
	count = 0
	for i in range(len(y_pred)) :

		if y_truth[i] == y_pred[i] :
			count +=1

	acc = count*1.0 / len(y_truth)
	return acc


#accuracy = cross_fold_validation(classifier, X,np.asarray(y_enc))


def cross_fold_validation(model, X , y, k = 10):
	

	len_set = X.shape[0] // k
	#print(len_set)
	if X.shape[0] % k == 0 :
		len_rem = len_set
		lim = k

	else :
		len_rem = X.shape[0] % k
		lim = k+1


	init = 0
	fin = len_rem
	acc = []
	for i in range(lim) :

		#print(init,fin)
		val_X = X[init : fin, :]
		train_X = np.concatenate((X[0:init,:], X[fin:,:]) , axis = 0)

		val_y = y[init : fin]
		train_y = np.concatenate((y[0:init], y[fin:]) , axis = None)

		model.train(train_X, train_y)


		y_pred = model.predict(val_X)

		if i == 10 :
			for k in range(len(val_y)) :
				print(val_y[k],y_pred[k]) 

		acc.append(accuracy(val_y,y_pred))




		#print(val_set,"\n\n",train_set,"\n\n")

		init += len_set
		fin += len_set


	return acc





def main() :

	classifier = Naive_Bayes() 

	'''classifier.X = np.asarray([[0,0],[0,1],[1,1],[2,2],[1,1]])
	classifier.y = np.asarray([0,0,0,1,0])

	print(classifier.X,"\n\n", classifier.y,"\n")'''

	#attr_set = classifier.get_attribute_set(classifier.X)
	#class_labels = classifier.get_attribute_set(classifier.y)

	df = pd.read_csv('SPECT.csv')
	df = df.sample(frac =1, random_state = 0)
	y = df.iloc[:,0].values
	X = df.iloc[:,1:].values

	y_enc = []
	for i in y :
		if i == 'Yes' :
			y_enc.append(1)

		else :
			y_enc.append(0)

	#print(y_enc)

	#classifier.train(X, np.asarray(y_enc))
	#print(classifier.attr_set,"\n\n", classifier.class_labels,"\n")

	'''y_pred = classifier.predict(classifier.X)
	#print(classifier.get_label_count(classifier.X[:,1], 1))

	#print('\n',y_pred)

	count = 0
	for i in range(len(y_pred)) :

		if y_enc[i] == y_pred[i] :
			count +=1'''

	#accuracy = cross_fold_validation(classifier, X,np.asarray(y_enc))

	#print(P)

	#print(accuracy)

	acc = cross_fold_validation(classifier,X, np.asarray(y_enc))

	print(np.asarray(acc).mean())

if __name__ == '__main__':
	main()