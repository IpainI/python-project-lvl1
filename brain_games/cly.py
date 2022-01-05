import prompt


def user_name() -> object:
	name = prompt.string('May I have your name? ')
	print('Hello,{}'.format(name))
	return name
