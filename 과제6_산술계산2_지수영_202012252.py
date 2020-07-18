import random
score = 0

for i in range(10):
    x = random.randrange(1,10)
    y = random.randrange(10,100)
    list = ['*', '-', '+']
    listA = random.choice(list)
    a = "%d%s%d" %(y,listA,x)
    answer = int(input(str(a)+'='))
    a = eval(a)
    if a==answer:
        score = score + 10
   
print("점수 = ", score)
