#!usr/bin/env python
print('Welcome to the Brain Games!')
from brain_games.cly import proverka
name = proverka()
print("Hello,", name)
c = 0
from brain_games.scripts.brain_even import game
from brain_games.scripts.brain_calc import calc
from brain_games.scripts.brain_gcd import nod , findNOD
from brain_games.scripts.brain_progression import gen_progres , game_prog
from brain_games.scripts.brain_prime import is_prime , game_prime
print("Wich game you want to play?")
print("1 - even , 2 - calc , 3 - gcd , 4 - progress , 5 - prime")
ans = int(input())

if ans == 1 :
	
	while c != 3 :
		c = game(name)
		
elif ans == 2 : 
	
	while c != 3 :
		c = calc(name)
		
elif ans == 3 :
	
	while c != 3 :
		c = nod(name)
		
elif ans == 4 :
	
	while c != 3 :
		c = game_prog(name)
	
elif ans == 5 :

	while c != 3 :
		c = game_prime(name)
		
print(input('enter to exit'))