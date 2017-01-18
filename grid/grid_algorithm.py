import time

n = 20

def brute_force(row, col):
	if row == 0 or col == 0:
		return 1
	return calc_num_paths(row-1, col) + calc_num_paths(row, col-1)

def clever_formula(size):
	answer = 2
	for i in range(size+1, 2*size):
		answer *= i
	for i in range(1, size):
		answer //= i
	return answer

if __name__ == "__main__":
	# for i in range(1, n):
	# 	start = time.time()
	# 	#print("Iteration {0}, Answer: {1}, Time: {2} seconds".format(i, calc_num_paths(i, i), time.time() - start))
	# 	#rint("Iteration {0}, Answer: {1}, Time: {2} seconds".format(i, formula(i), time.time() - start))
	# 	#print("Iteration {0}, Equal? : {1}, Time: {2} seconds".format(i, calc_num_paths(i, i) == formula(i), time.time() - start))
	# 	
	print(clever_formula(20))