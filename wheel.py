### The Wheel
### Randomly select a brother/pledge to assign a task
### Usage: python3 wheel.py [-b | -p]
### -b: Brothers only
### -p: Pledges only
### no arg: Both bros and pledges

from random import randint
import sys

def main(args):
	names = []
	if (len(args) == 1):
		#bros and pledges
		f = open('brothers.txt')
		names = f.readlines()
		f.close()
		f2 = open('pledges.txt')
		names.extend(f2)
		f2.close()
	elif (len(args) > 1):
		if (args[1] == '-b'):
			#brothers only
			f = open('brothers.txt')
			names = f.readlines()
			f.close()
		elif (args[1] == '-p'):
			#pledges only
			f = open('pledges.txt')
			names = f.readlines()
			f.close()

	length = len(names)
	index = randint(0, length - 1)
	theChosenOne = names[index]
	print(theChosenOne)

if __name__ == '__main__':
	main(sys.argv)