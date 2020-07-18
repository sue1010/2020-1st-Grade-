import random


tries = 0


print('안녕하세요? 이름이 어떻게 되시나요?')
name = input()


number = random.randint(1, 100)
print(name + '님, 제가 지금 1부터 100 사이의 정수를 생각하고 있습니다.')


while tries < 10:
    guess = int(input('맞춰보세요:'))
    tries = tries + 1

    if guess < number:
        print('너무 낮습니다!')

    if guess > number:
        print('너무 높습니다!')

    if guess == number:
        break


if guess == number:
    print(name + '님, 잘 하셨어요!');
    
