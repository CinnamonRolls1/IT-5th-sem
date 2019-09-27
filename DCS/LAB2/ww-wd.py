

def waitDie(p_l):
	current=p_l[0]
	print("Process 0 holds the resource.")
	for i in range(1,len(p_l)):
		print("Process", i,"requests the resource.")
		if p_l[i]>current:
			print("Process ", i, "waits for completion of process")
			current=p_l[i]
			print("Process", i," holds the resource." )
		else:
			print("Process ", i, "is killed.")

def woundWait(p_l):
	current=p_l[0]
	print("Process 0 holds the resource.")
	for i in range(1,len(p_l)):
		print("Process", i,"requests the resource.")
		if p_l[i]>current:
			print("Process ",i, "is forced to be rolled back.")

		else:
			print("Process ", i ,"is forced to wait until resource is available.")
			current=p_l[i]
			print("Process ", i, "holds the resource.")

def main():
	proc_lens=[3,5,1,2,3]
	print("-------------wait die---------------")
	waitDie(proc_lens)
	print("------------wound wait--------------")
	woundWait(proc_lens)

if __name__ == '__main__':
	main()