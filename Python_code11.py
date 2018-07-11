# 仿照上一個例子，請試著寫數字連乘的遞迴函式，計算出f(10)等於多少。
# sol:
def f(n):
    print('n=',n) #印出目前第幾層
    if n==1:
        return 1
    else:
        return f(n-1)*n
print ('answer=',f(10))