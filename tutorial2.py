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
 
def parameter(*l, **dic):
	print 'l', l,'dic', dic
parameter(1, 3, 5, life = 'sheng', will = 'yang')