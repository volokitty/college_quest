from expressions import expressions

def is_command_correct(command):
	if command not in command_list:
		print()	

def ten_to_five(number):
	number = int(number)
	new_number = ''
	while number > 0:
		new_number = str(number % 5) + new_number
		number //= 5
	return new_number

def five_to_ten(number):
	pass
