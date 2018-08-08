hour0,minute0=map(int,input().split())
hour1,minute1=map(int,input().split())
h0=(hour0*60)+minute0
t0=(hour1*60)+minute1
t1=h0-t0
h1=t1//60
t1%=60
print(h1,t1,sep=" ")






