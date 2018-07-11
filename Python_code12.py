# 計算出費氏(Fibonacci)數列 F(20)，公式如下：
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2), when n≥2

#sol:
def F(n):
    print ('n=',n)
    if n==0:
        return 0
    elif n==1:
        return 1    
    else:
        return F(n-1)+F(n-2)    
print ("answer of 費氏數列",F(20))