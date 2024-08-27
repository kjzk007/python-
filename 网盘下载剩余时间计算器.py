import time

a=input("显示内存（GB）：")
b=input("已经下载（%）：")
c=1-(float(b)/100)
d=float(a)*c*1024*1024/130
e=d/60/60
timestr=time.time()
timestr1=time.ctime(timestr)
timestr2=time.ctime(timestr+d)
print('-'*20)
print("需要{}小时下载完毕".format('%3.3f'%e))
print('现在时间：',timestr1)
print('预计下载完毕时间：',timestr2)
print('-'*20)