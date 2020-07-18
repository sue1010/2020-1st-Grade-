def runlength(s):
    result = ""
    size = len(s)
    last = s[0]
    count = 1
    i = 1
    while i < size:
        if s[i] == s[i-1]:
            count += 1
        else:
            result += str(count) + s[i-1]
            count = 1
        i += 1
    result += str(count) + s[i-1]
    return result

s = input("압축할 문자열을 입력하시오: ")
output = runlength(s)
print("압축된 문자열: ", output)
