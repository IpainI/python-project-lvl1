def calc(name):
	import random
	c = 0 
	print("What is the result of the expression?")
	while c != 3 :
		
		znak = random.randint(1,3)
		if znak == 1 :
			z = '+'
			a = random.randint(1,40)
			b = random.randint(1,40)
			d = a + b
		elif znak == 2 :
			z = '-'
			a = random.randint(1,40)
			b = random.randint(1,40)
			d = a - b
		elif znak == 3 :
			z = '*'
			a = random.randint(1,20)
			b = random.randint(1,20)
			d = a * b
		print("Question:",a,z,b)
		ans = int(input('Your ansver '))
		if ans == d :
			print('Correct!')
			c += 1 
		else : 
			print("Let's try again,",name)
			return 0
	if c == 3 :
		print("Congratulations,",name)
		return c