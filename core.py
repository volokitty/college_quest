str_to_tokens = lambda string: string.split()

def five(number):
	new_number = ''
	while number > 0:
		new_number = str(number % 5) + new_number
		number = number // 5
	return int(new_number)

def decimal(number):
	number = str(number)
	length = len(number)
	decimal = 0
	
	for i in range(0, length):
		decimal = decimal + int(number[i]) * (5 ** (length - i - 1))
	
	return int(decimal)

def my_sum(*args):
	args = list(map(decimal, args))		

	return five(sum(args))

my_sub = lambda *args: five(decimal(args[0]) - decimal(my_sum(*args[1:])))

headers = { '+': my_sum, '-': my_sub, 'five': five, 'decimal': decimal }
