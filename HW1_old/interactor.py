code = int(input())
interactor = int(input())
checker = int(input())

def module(code, interactor, checker):
	if interactor == 0:
		if code != 0:
			result = 3
		else:
			result = checker
	elif interactor == 1:
		result = checker
	elif interactor == 4:
		if code != 0:
			result = 3
		else:
			result = 4
	elif interactor == 6:
		result = 0
	elif interactor == 7:
		result = 1
	else:
		result = interactor
	return result

print(module(code, interactor, checker))
