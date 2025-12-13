##import random
##
##answer=random.randint(1,1000)
##print(answer)
##
##
##count=0
##
##while True:
##    number=int(input('1 ~ 1000 사이 숫자를 입력해주세요.'))
##    if number > answer:
##        print('더 낮은 숫자가 정답입니다.')
##        count += 1
##    elif number < answer:
##        print('더 높은 숫자가 정답입니다.')
##        count += 1
##    else:
##        count += 1
##        print('정답입니다.')
##        print(f'현재 입력 횟수 {count}')
##        break

##import random
##
##count = 0
##
##while True:
##    number = random.randint(0,999)
##    if number < 10:
##        print(number)
##        break
##    elif 10 <= number <= 99:
##        if number // 10 != number % 10:
##            print(number)
##            break
##    elif 100 <= number <= 999:
##        if number // 100 != (number % 100 // 10) and (number % 100 // 10) != number % 10 and number // 100 != number % 10:
##            print(number)
##            break
##    else:
##        count += 1


##import random
##
##answer = random.randint(100,999)
##answer_str=str(answer)
##print(answer)
##
##strike = 0
##ball = 0
##
##while True:
##    guess=input('세 자리 숫자를 입력해주세요 :')
##    if guess != answer_str:
##        if guess[0] == answer_str[0]:
##            strike += 1
##            if answer_str[0] in guess[1:]:
##                ball -= 1
##        else:
##            if guess[0] in answer_str:
##                ball += 1
##        if guess[1] == answer_str[1]:
##            strike += 1
##            if answer_str[1] == guess[0] or  answer_str[1] == guess[2]:
##                ball -= 1
##        else:
##            if guess[1] in answer_str:
##                ball += 1
##        if guess[2] == answer_str[2]:
##            strike += 1
##            if answer_str[2] in guess[:2]:
##                ball -= 1
##        else:
##            if guess[2] in answer_str:
##                ball += 1
##        print(f'{strike} strike, {ball} ball')
##        strike = 0
##        ball = 0
##    else:
##        if guess[0] == answer_str[0]:
##            strike += 1
##            if answer_str[0] in guess[1:]:
##                ball -= 1
##        else:
##            if guess[0] in answer_str:
##                ball += 1
##        if guess[1] == answer_str[1]:
##            strike += 1
##            if answer_str[1] == guess[0] or  answer_str[1] == guess[2]:
##                ball -= 1
##        else:
##            if guess[1] in answer_str:
##                ball += 1
##        if guess[2] == answer_str[2]:
##            strike += 1
##            if answer_str[2] in guess[:2]:
##                ball -= 1
##        else:
##            if guess[2] in answer_str:
##                ball += 1
##        print(f'''{strike} strike, {ball} ball
##정답!''')
##        break

##for i in range(1,11):
##    print('안녕',i,'번째')
    
##for i in range(10, 0, -1):
##    print(i,end=' ')

##total = 0
##
##for i in range(1,101):
##    total += i
##
##print(total)

##for i in range(5,100+1,5):
##    print(i, end=' ')

##total=0
##
##for i in range(3,100,3):
##    total += i
##
##print(f'3의 배수의 합: {total}')

##for i in range (1,11):
##    if i % 2 == 0:
##        print('짝수번 안녕')
##    else:
##        print('홀수번 안녕')

##first_num = int(input('시작값 입력: '))
##last_num = int(input('끝값 입력: '))
##
##for i in range(first_num, last_num+1):
##    if i % 2 == 0:
##        print('짝수: ',i)
##    else:
##        print('홀수: ',i)

##print('시작값 입력: ')
##first_num = int(input())
##
##print('끝값 입력: ')
##last_num = int(input())
##
##for i in range(first_num,last_num+1):
##    if i % 2 == 0:
##        print('짝수: ',i)
##    else:
##        print('홀수: ',i)

##first_num= int(input('시작 값 입력: '))
##last_num= int(input('끝 값 입력: '))
##
##for i in range(first_num, last_num+1):
##    if i % 15 == 0:
##        print(i, end=' ')

##for num in range(1,100):
##    if num > 55:
##        break
##    print(num, end=' ')

##for num in range(7):
##    power = 2**num
##    if power > 64:
##        break
##    print(power, end=' ')

##sum_odd=0
##
##for i in range(1, 1000, 2):
##    if i % 13 == 0:
##        continue
##    print(i, sum_odd,  end=' ')
##    sum_odd += i
##    if sum_odd > 500:
##        break

##odd =1
##for num in range(1,20):
##    if num % 2 == 0:
##        continue
##    odd *= num
##    print(f'{num} = {odd}')

num = int(input('숫자를 입력해주세요'))


for i in range(2,100):
    temp=num**i
    if temp > 10000:
        break
    print(temp)





































































































