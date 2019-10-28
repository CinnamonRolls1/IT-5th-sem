import random
import math
from csv import reader

def compute_mem_matrix(m,x,clusters,curr):
	res=[]
	sum=0
	for i in range(len(x)):
		U=0
		
		if x[i]==curr[i]:
			U=1
		else:
			ans=0
			flag=True
			for c in clusters:
				if x[i]==clusters[c][i]:
					U=0
					flag=False
					break
				ans+=pow((abs(x[i]-curr[i])/abs(x[i]-clusters[c][i])),(2/(m-1)))
			if flag:
				U=1/ans
				#print(U)
		res.append((U,x[i]))
		sum+=U

	return [res,sum]

def compute_cluster_center(m,U_X):
	U=[]
	X=[]
	for i in U_X:
		U.append(i[0])
		X.append(i[1])
	num=0
	den=0
	for i in range(len(U)):
		#print(U[i]," ",X[i])
		num+=(pow(U[i],m)*X[i])
		den+=pow(U[i],m)
	c=num/den
	return c

def cMean(clusters,dataset,m):
	prev={'Yes':clusters['Yes'],'No':clusters['No']}
	final_cluster={'Yes':[],'No':'No'}
	arr=['No' for i in range(len(dataset))]
	epoch=1
	for i in range(500):
		cluster_Y=[]
		cluster_N=[]
		#print(epoch)
		for i in range(len(dataset)):
			if dataset[i]==clusters['Yes']:
				arr[i]='Yes'
				ans=[(1,dataset[i][j]) for j in range(len(dataset[i]))]
				#print(ans)
				cluster_Y.append(ans)
				continue
			elif dataset[i]==clusters['No']:
				arr[i]='No'
				ans=[(1,dataset[i][j]) for j in range(len(dataset[i]))]
				#print(ans)
				cluster_N.append(ans)
				continue

			c1=compute_mem_matrix(m,dataset[i],clusters,clusters['Yes'])
			c2=compute_mem_matrix(m,dataset[i],clusters,clusters['No'])

			if c1[1]>c2[1]:
				arr[i]='Yes'
				cluster_Y.append(c1[0])

			else:
				arr[i]='No'
				cluster_N.append(c2[0])
		res_Y=[]
		res_N=[]
		for j in range(len(cluster_Y[0])):
			U_X=[]
			for i in range(len(cluster_Y)):
				U_X.append(cluster_Y[i][j])
			res_Y.append(compute_cluster_center(m,U_X))
		clusters['Yes']=res_Y

		for j in range(len(cluster_N[0])):
			U_X=[]
			for i in range(len(cluster_N)):
				U_X.append(cluster_N[i][j])
			res_N.append(compute_cluster_center(m,U_X))

		clusters['No']=res_N
		#print(clusters)
		if clusters['Yes']==prev['Yes'] and clusters['No']==prev['No']:
			return arr
		prev={'Yes':clusters['Yes'],'No':clusters['No']}
		epoch+=1
		

	return arr

def remove_index(dataset):
	brr=[]
	for i in dataset:
		brr.append(i.pop(0))
	return [dataset,brr]

def load_csv(filename):
	dataset=[]
	with open(filename,'r') as file:
		csv_reader=reader(file)
		for row in csv_reader:
			dataset.append(row)
	dataset.pop(0)
	return dataset

def main():
	k=2
	m=2
	filename='SPECTF.csv'
	dataset=load_csv(filename)
	random.shuffle(dataset)
	clusters={}
	res=[]
	# for i in dataset:
	# 	if i[0]=="Yes":
	# 		res.append(list(i))
	# 		break
	# for i in dataset:
	# 	if i[0]=="No":
	# 		res.append(list(i))
	# 		break
	res1=random.sample(dataset,2)
	for i in res1:
		res.append(list(i))
	

	res[0].pop(0)
	res[1].pop(0)
	for i in range(len(res[0])):
		res[0][i]=float(res[0][i].strip())
		res[1][i]=float(res[1][i].strip())

	clusters={'Yes':res[0],'No':res[1]}
	crr=remove_index(dataset)
	dataset=crr[0]

	for i in range(len(dataset[0])):
		for row in dataset:
			row[i]=float(row[i].strip())

	brr=crr[1]
	final_cluster=cMean(clusters,dataset,m)
	acc=0
	tp=0
	fp=0
	tn=0
	fn=0
	for i in range(len(dataset)):
		print(brr[i]," ",final_cluster[i])
		if brr[i]==1:
			if brr[i]==final_cluster[i]:
				tp += 1
			else:
				fp += 1
		else:
			if brr[i] == final_cluster[i]:
				tn += 1
			else:
				fn += 1
			
	print("TP\tFP\tTN\tFN")
	print(tp,"\t",fp,"\t",tn,"\t",fn)
	conf= [tp,fp,tn,fn]

	acc = (conf[0]+conf[2])/(conf[0]+conf[2]+conf[1]+conf[3])
		
	acc=acc/len(dataset)*100
	if acc<50:
		acc=100-acc
		conf[0],conf[1]=conf[1],conf[0]
		conf[2],conf[3]=conf[3],conf[2]
	

	print('Accuracy is ' + str(acc*100) + '%')
	recall = conf[0]/(conf[0]+conf[3])
	precision = conf[0]/(conf[0]+conf[1])
	print('Recall is ' + str(recall*100) + '%')
	print('Precision is ' + str(precision*100) + '%')
if __name__ == '__main__':
	main()