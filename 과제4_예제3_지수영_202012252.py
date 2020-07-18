import time
now = time.time()
thisYear = int(1970+now//(365*24*3600))
a= "올해는 %d년 입니다." %thisYear
print(a)
age = int(input("몇 살이신지요?"))
b = age+2050-thisYear
c = "2050년에는 %d살 이시군요." %b
print(c)

