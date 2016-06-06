import random
import time
length = 10000
def generate():
	array = [random.randint(1, 1000000) for _ in range (length)]
	return array

def bubbleSort(array):
	for passnum in range(len(array)-1, 0, -1):
		for i in range(passnum):
			if array[i] > array[i+1]:
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
start_time = time.time()
array = generate()
print("--- %s seconds to generate ---" % (time.time() - start_time))
start_time = time.time()
bubbleSort(array)
print("--- %s seconds to sort ---" % (time.time() - start_time))
