def repeatedString(s, n):
    if(s.count('a')==len(s)):
        return n
    
    l=len(s)
    q=n//l
    c=s.count('a')
    return q*c+(s.count('a',0,(n%l)))
