def candies(s):
    if len(s) <= 1:
        return -1
    else:
        s.sort()
        base = s[-1]
        total = 0
        for x in s:
            if x < base:
                diff = base - x
                total += diff
        print total    
        return total   

candies([5,8,6,4])            