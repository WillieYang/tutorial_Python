# def comparisation(x, y):
# 	if x == y :
# 		print 'The numbers you have input is equal'
# 	elif x > y:
# 		print 'The %d is bigger than %d' % (x, y)
# 	else:
# 		print 'The %d is smaller than %d' % (x, y)

# print 'Please input two numbers to compare:'
# x = int(raw_input())
# y = int(raw_input())
# l = [x, y]
# comparisation(x, y)

# l = [2, 3, 5, 'sheng', 'yang']
 
# def parameter(a, b, *l, **dic):
# 	print 'int:',a , b, 'l:', l,'dic:', dic
# parameter(1, 3, 5, life = 'sheng', will = 'yang')

def iteration(n):
	if n == 1:
		return 1
	return n * iteration(n-1)

f = iteration(5)
print 'The result is', f