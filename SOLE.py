import random
import numpy as np

min_int = int(input("минимум диапазона чисел: "))
max_int = int(input("максимум диапазона чисел: "))
unknowns = int(input("количество неизвестных: "))
expressions = int(input("количество уравнений: "))

print()

convert = lambda x: 1 if x==True else -1

def fmt(sgn_arr, arr):
	cnv = lambda x: '+' if x==1 else '-'
	fst_cnv = lambda x: ' ' if x==1 else '-'
	row_len = ((np.array((np.unique(sgn_arr,axis=0)).shape[:1]))[0])
	for i in range(row_len):
		print(fst_cnv(sgn_arr[i][0]), 'x1', '', end='')
		for j in range(len(sgn_arr[0])-1):
			print(cnv(sgn_arr[i][j+1]), 'x' + str(j+2), '', end='')
		for k in range(len(arr[0])):
			print('=', arr[i][k], end='')
		print()
list_of_unknowns = np.array([random.randint(min_int,max_int+1) for i in range(unknowns)])
matrix_sgn_sl = np.array([[convert(random.choice([True, False])) for j in range(unknowns)] for i in range(expressions)])
while ((np.array((np.unique(matrix_sgn_sl,axis=0)).shape[:1]))[0]) != ((np.array(matrix_sgn_sl.shape[:1]))[0]):
	matrix_sgn_sl = np.array([[convert(random.choice([True, False])) for j in range(unknowns)] for i in range(expressions)])

sl_sum_res = np.sum((list_of_unknowns * matrix_sgn_sl), axis=1, keepdims=True)

fmt(matrix_sgn_sl, sl_sum_res)

input("if u rdy for answ, press enter")
print(list_of_unknowns)
input()
