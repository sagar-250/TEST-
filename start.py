def add(n,m):
    return m+n
def factorial(n):
    r=1
    for i in range(n):
        r*=i+1   
    return r
def mix(n):
    l=add(n,2*n)
    p=factorial(l)
    j=p*10
    import pdb;pdb.set_trace() 
    return j*p/l
        
h=mix(2)        
print(h)