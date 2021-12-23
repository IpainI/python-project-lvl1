def is_prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count > 2 or num == 1:
        return False
    else : 
        return True
def game_prime(name):
	import random
	ff = True
	c = 0
	print('Answer "yes" if given number is prime. Otherwise answer "no".')
	while c != 3:
		a = random.randint(1,50)
		print("Question:",a)
		ans = input('Your answer: ')
		ff = is_prime(a)
		if ff == True and ans == 'yes' : 
			c += 1 
			print('Correct!')
		elif ff == False and ans == 'no' :
			c += 1 
			print('Correct!')
		else :
			print("Let's try again,",name)
			return 0
	if c == 3 :
	    print("Congratulations,",name)
	    return c