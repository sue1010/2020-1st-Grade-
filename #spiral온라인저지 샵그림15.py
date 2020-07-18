n = int(input(""))
k = 2
x = ['#']
y = 1


while k <= n:
    if k%4 == 0:
        j = " "*(k-2)
        x.reverse()
        for i in range(2):
            x.append(j)
        x.reverse()
        for d in range(k-1):
            if d == k-2:
                if k == 4:
                    x[d] = "#"+" #"
                else:
                    x[d] = "#"+" "*(k-3)+"#"
                    
            else:
                b = x[d][0:k-2]+"#"
                x[d] = x[d].replace(x[d],b)    
        k+=1

    elif k%4 == 1:
        x[0] = "#"*k
        for i in range(1,k-1):
            x[i] ="  " + x[i]
        k+=1

    elif k%4 == 2:
        if k!=2:
            for i in range(2):
                x.append("#")
        elif k == 2:
            x.append("#")
        for i in range(k):
            if len(x[i]) < k-1:
                x[i] += " "*(k-2)
        for d in range(k):
            a = "#"+x[d][1:]
            x[d] = x[d].replace(x[d],a)
        k+=1

    elif k%4 == 3:
        x[k-2] = "#"*k
        for i in range(k-1):
            while len(x[i]) < k:
                x[i] += " "
        k+=1

for i in range(len(x)):
    print(x[i])
