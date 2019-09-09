import pandas as pd 
import numpy as np 
from sklearn.metrics import accuracy_score
from NB import Naive_Bayes

class GA_FeatureSelection :

	def __init__(self) :
		self.max_acc = float('-inf')
		self.best_can = None


	def initialization(self,sample_set):
		self.N = 20
		population = np.empty((0,sample_set.shape[0]))
		#print(population.shape)
		for i in range(self.N) :
			individual = np.round(np.random.random(sample_set.shape[0])).reshape(1,-1)
			#print(individual.shape)
			population = np.append(population,individual,axis=0)
			population = population.astype(dtype=bool)
		return population

	
	def update_rank(self,accuracies,ranks):
		ranks = np.append(ranks,0)

		for i in range(accuracies.shape[0]) :

			if accuracies[i] > accuracies[-1] :
				ranks[i]+=1
			else :
				ranks[-1]+=1

		return ranks

	def fitness_function(self,X,y):
		classifier = Naive_Bayes()
		classifier.train(X,y)
		y_pred = classifier.predict(X)
		accuracy = accuracy_score(y,y_pred)
		return accuracy
		

	def fitness_eval(self,population,X,y) :
		
		#evaluating fitness
		accuracies = np.empty((0,))
		ranks = np.empty((0,))
		for i in range(self.N) :
			#print(population[i,:])
			X_select = X[:,population[i,:]]
			acc=self.fitness_function(X_select,y)
			accuracies = np.append(accuracies,acc)
			ranks = self.update_rank(accuracies,ranks)
			#print(X_select.shape)
			#print(accuracies)
			#print(ranks)
			#print()
		if self.max_acc < np.max(accuracies):
			self.max_acc = np.max(accuracies)
			self.best_can = population[np.argmax(accuracies),:]

		#print(accuracies)

		self.fitness = 1.5*ranks

		return [self.fitness,accuracies]




	def search(self,key,arr):
		
		for i in range(arr.shape[0]) :
			if key < arr[i] :
				return i
		


	def selection(self,population,fitness,sel_rate=0.25) :
		probabilities =fitness/np.sum(fitness)
		#print(probabilities)
		self.cumulative = np.empty((0,))
		current = 0

		for i in range(probabilities.shape[0]) :
			current += probabilities[i]
			self.cumulative = np.append(self.cumulative,current)

		#print(self.cumulative,"\n")
		#print(self.binSearch(0.005,fitness))
		num_candidates=round(sel_rate*population.shape[0])
		candidates=np.empty((0,population.shape[1]))
		for i in range(num_candidates) :
			candidates = np.append(candidates,self.search(np.random.random(),self.cumulative))

		return candidates.astype(int)
		

	def crossover(self,candidate1,candidate2,population) :
		

		candidate1 = population[candidate1,:]
		candidate2 = population[candidate2,:]
		choice = np.round(np.random.random(candidate1.shape))
		offspring = np.where(choice==0,candidate1,candidate2).reshape(1,-1)

		return offspring


	def get_newPopulation(self,candidates,population):
		
		newPopulation = np.empty((0,population.shape[1]))
		for i in range(self.N):
			if i in candidates :
				candidate1=i
				candidate2=int(np.random.choice(candidates[np.where(candidates!=i)]))
				newPopulation = np.append(newPopulation,self.crossover(candidate1,candidate2,population),axis=0)

			else :
				newPopulation= np.append(newPopulation,population[i,:].reshape(1,-1),axis=0)

		return newPopulation.astype(bool)





	def mutation(self,candidate,mut_rate=0.1) :
		mutate = np.random.choice(np.arange(candidate.shape[0]),round(mut_rate*candidate.shape[0]),replace=False)
		#print(mutate)
		mutated = np.copy(candidate)
		mutated[mutate] = 1- mutated[mutate]
		return mutated

	def evolution(self,X,y) :


		best_candidate = None
		best_candidate_fitness = float("-inf")
		population= self.initialization(np.arange(X.shape[1]))
		for i in range(20) :
			evalued=self.fitness_eval(population,X,y)
			fitness=evalued[0]
			probs=evalued[1]
			candidates = self.selection(population,fitness)
			#print("Selected candidates:", candidates)
			current_best_candidates_fitness=np.max(fitness[candidates])
			if current_best_candidates_fitness > best_candidate_fitness :
				best_candidate_fitness = current_best_candidates_fitness
				best_candidate = population[np.argmax(fitness[candidates]),:]
			population = self.get_newPopulation(candidates,population)
			#print(population)
			#print("fitness=",fitness)

			for j in range(population.shape[0]) :
				population[j,:]=self.mutation(population[j,:])
				print(population[j,:].astype(int),probs[j])
			print('-----: iter', i, ":-----")

		
		return best_candidate,best_candidate_fitness



dataset = pd.read_csv('SPECT.csv')
dataset = dataset.sample(frac = 1,random_state =0)
inputs = dataset.iloc[:,1:].values
outputs = dataset.iloc[:,0].values
#print(inputs.shape)

from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()
outputs = label_enc.fit_transform(outputs)
outputs = outputs.reshape(-1,1)
		

optimizer  = GA_FeatureSelection()
'''print(optimizer.initialization(np.arange(inputs.shape[1])))
#print("\n\n")
fitness=optimizer.fitness_eval(optimizer.population,inputs,outputs)
candidates = optimizer.selection(optimizer.population ,fitness)
print(candidates,"\n")
new_population =optimizer.get_newPopulation(candidates,optimizer.population)
print(new_population)'''
#print(optimizer.mutation(new_population[0,:]))
candidate,fitness = optimizer.evolution(inputs,outputs)
#print(fitness)
print("Final candidates:",optimizer.best_can)
#print(optimizer.fitness_function(inputs[:,candidate[:]],outputs))
print("Accuracy:", optimizer.max_acc)





