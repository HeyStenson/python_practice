# given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. a being 1, b being 2, etc. 
# alphabet_position("The sunset sets at twelve o' clock.") 
# returns: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
import re

def alphabet_position(text):
    # text = text.translate(None, ' ')
    text = re.sub('\W+','', text)
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    to_index = [alpha.index(char.lower()) for char in text]
    return " ".join(str(num) for num in to_index)

# Failed hard on this one. A good answer was:
def alphabet_position(text):
  	return " ".join(str(ord(char)-ord("a")+1) for char in text.lower() if char.isalpha()) 