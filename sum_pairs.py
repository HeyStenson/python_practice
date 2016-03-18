# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
# Ex: [1, 4, 8, 7, 3, 15], 8 => [1, 7]


# def sum_pairs(ints, s):
# 	ints_set = set(ints)
# 	result = s
# 	return_arr = []
# 	for x in ints:
# 		diff = result - x
# 		if diff in ints_set:
# 			return_arr.append(x)
# 			return_arr.append(diff)
# 			print return_arr
# 			return return_arr
# 		else:
# 			return None	

from itertools import combinations

def sum_pairs(ints, s):
	return [pair[0] for pair in combinations(ints, 2) if sum(pair) == s]

sum_pairs([1, 4, 8, 7, 3, 15], 8)			