Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=int(input("초="))
초=1000000
>>> a=s//3600
>>> b=(s%3600)//60
>>> c=(s%3600)%60
>>> print(str(s)+"초는", str(a)+"시", str(b)+"분", str(c)+"초이다.")
1000000초는 277시 46분 40초이다.
>>> 
