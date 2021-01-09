# volokitty

from instruction import *
from core import *

print(INSTRUCTION)

while True:
	text = input('>>> ')

	if text == 'q':
		break

	try:
		tokens = str_to_tokens(text)
		args = list(map(int, tokens[1:]))

		command = { 'func': headers[tokens[0]], 'args': args }

		result = command['func'](*command['args'])
		print(result)
	except:
		print('Error')
