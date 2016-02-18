# You're given a list of comparable elements:

# heights = [Integers or Floats]
# Your job is to check whether for any x all successors are greater or equal to x.
# is_monotone([1,1,2]) == True
# is_monotone([1])     == True
# is_monotone([3,2,1]) == False

def is_monotone(heights):
	return sorted(heights) == heights

# tried the pattern:
# for idx, item in enumerate(arr)
# but had trouble figuring out how to make it work for me

 	    
