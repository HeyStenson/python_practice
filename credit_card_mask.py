# Dear god.
# Mine: 

def maskify(cc):
	cc_arr = list(cc)
	last_four = None
	masked = []
	if len(cc) > 4:
		last_four = ('').join(cc_arr[-4:])
		del cc_arr[-4:]
		for item in cc:
			item = 'x'
			masked.append(item)
		masked.append(last_four)
		masked = ('').join(masked)
		print masked
		return masked	
	else:
		print cc
		return cc
			
# The real way:
def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:] 

maskify("198383775616")	     	