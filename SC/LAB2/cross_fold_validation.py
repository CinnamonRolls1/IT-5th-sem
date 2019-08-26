from sklearn.metrics import accuracy_score
import numpy as np

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

	return acc







	