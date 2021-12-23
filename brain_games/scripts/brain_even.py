def game(name):
	import random
	c = 0
	print("Answer 'yes' if the number is even, otherwise answer 'no'.")
	while c != 3 and c >= 0:
		ans = ''
		number = random.randint(1,100)
		print("Qwestion:",number)
		ans = input('Your answer ')
		if number % 2 == 1 and ans == 'no' :
			print('Correct')
			c += 1
		elif number % 2 == 0 and ans == 'yes' :
			print('Correct')
			c += 1
		else : 
			print("Let's try again,",name)
			return 0
	if c == 3 :
		print("Congratulations,",name)
		return c
	
		
	
		
