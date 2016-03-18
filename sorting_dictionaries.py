# Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary.

# In this kata you will create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

# The list must be sorted by the value and be sorted largest to smallest.

def sort_dict(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)