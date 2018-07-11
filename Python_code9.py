def maker(n):
    def action(x):
        r = n ** x
        return r
    return action 
        
h = maker(9)
print(h(5))


#def maker(n):
#     return lambda x: n ** x
    
#h = maker(9)
#print(h(5))