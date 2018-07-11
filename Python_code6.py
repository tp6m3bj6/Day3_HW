# 數字連乘遞迴函數

n=int(input("請輸入n:"))
def f(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,'*',j,'=',i*j,sep='',end='\t')
        print('')
f(n)
