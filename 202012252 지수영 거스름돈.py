Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> money = int(input("투입한 돈:"))
투입한 돈:5000
>>> price = int(input("물건 값:"))
물건 값:3220
>>> change = money-price
>>> print("거스름돈:", change)
거스름돈: 1780
>>> coin500s = change//500
>>> coin100s = (change%500)//100
>>> coin50s = ((change%500)%100)//50
>>> coin10s = (((change%500)%100)%50)//10
>>> print("500원 동전의 개수:", coin500s)
500원 동전의 개수: 3
>>> print("100원 동전의 개수:", coin100s)
100원 동전의 개수: 2
>>> print("50원 동전의 개수:", coin50s)
50원 동전의 개수: 1
>>> print("10원 동전의 개수:", coin10s)
10원 동전의 개수: 3
>>> 