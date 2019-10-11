

def waitDie(p_l):
	current=p_l[0]
	unfinished = []
	print("P",current[0] ,"holds the resource.")
	for i in range(1,len(p_l)):
		print("P", p_l[i][0],"requests the resource.")
		if p_l[i][1]<current[1]:
			print("P", p_l[i][0], "waits for completion of process")
			current=p_l[i]
			print("P", p_l[i][0]," holds the resource." )
		else:
			print("P", p_l[i][0], "is killed.")
			unfinished.append(p_l[i])

	print("P", current[0], "finishes execution.")
	return unfinished


def WD(p_l) :
	unfinished = list(p_l)
	while True :
		current = waitDie(unfinished)
		if current == [] :
			break

		unfinished = current

def WW(p_l) :
	unfinished = list(p_l)
	while True :
		current = woundWait(unfinished)
		if current == [] :
			break

		unfinished = current


# def waitDieStack(p_l):
# 	procs=[[i,p_l[i]] for i in range(len(p_l))]
# 	current=procs[0]
# 	print("P 0 holds the resource.")
# 	# while procs!=[]:
# 	for i in range(10):
# 		val = procs.pop(0)
# 		print("P", val[0],"requests the resource.")
# 		if val[1]<current[1]:
# 			print("P ", val[0], "waits for completion of process")
# 			print(val)
# 			print(current)
# 			print(procs)
# 			procs.remove(current)
# 			current=val
# 			print("P", val[0]," holds the resource." )
		
# 		else:
# 			print("P ", val[0], "is killed.")
# 			print(val)
# 			print(current)
# 			print(procs)
# 			procs.append(val)

def woundWait(p_l):
	current=p_l[0]
	unfinished = []
	# print(p_l)
	print("P",current[0] ,"holds the resource.")
	for i in range(1,len(p_l)):
		print("P", p_l[i][0],"requests the resource.")
		if p_l[i][1]<current[1]:
			
			print("P", current[0], "is killed.")
			unfinished.append(current)
			current=p_l[i]
			print("P", current[0]," holds the resource." )
		
		else:
			
			print("P", p_l[i][0], "is forced to wait until resource is available.")
			current=p_l[i]
			print("P", current[0], "holds the resource.")

	# print("P", current[0], "finishes execution.")
	return unfinished


# def woundWait(p_l):
# 	current=p_l[0]
# 	cur=0
# 	unfinished = []
# 	print("P 0 holds the resource.")
# 	for i in range(1,len(p_l)):
# 		print("P", i,"requests the resource.")
# 		if p_l[i]<current:
# 			print("P",cur, "is killed.")
# 			cur=i
# 			current=p_l[i]
# 			print("P", cur, "holds the resource.")

# 		else:
# 			print("P", i ,"is forced to wait until resource is available.")
# 			current=p_l[i]
# 			cur=i
# 			print("P", i, "holds the resource.")


def main():
	procs=[[0,3],[1,5],[2,1],[3,2],[4,3]]
	# proc_lens=[3,5,1,2,3]
	print("-------------WAIT DIE---------------")
	WD(procs)
	print("------------WOUND WAIT--------------")
	WW(procs)

if __name__ == '__main__':
	main()