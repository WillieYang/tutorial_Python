def comparisation(x, y):
	if x == y :
		print 'The numbers you have input is equal'
	elif x > y:
		print 'The %d is bigger than %d' % (x, y)
	else:
		print 'The %d is smaller than %d' % (x, y)

print 'Please input two numbers to compare:'
x = int(raw_input())
y = int(raw_input())
comparisation(x, y)

