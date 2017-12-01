# a script to print the contents of a dict

some_dict = {"Sam": 25, "Peter": 26, "Tom": 47, "Alice": 3}

def print_dict(dictionary):
	for k, v in dictionary.items():
		print('\n{}: {}'.format(k, v))	

print_dict(some_dict)
