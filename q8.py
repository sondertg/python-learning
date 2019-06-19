# Question:
# Write a program that accepts a comma separated sequence of words as input
# Prints the words in a comma-separated sequence  after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

a = [x for x in input().split(',')]

a.sort()

print(','.join(a))
