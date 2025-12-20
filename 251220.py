##for num in range(1,100):
##    if num > 55:
##        break
##    print(num, end=' ')

##for num in range(7):
##    power = 2**num
##    if power > 64:
##        break
##    print(power, end=' ')

##sum_odd = 0
##for i in range(1,1000,2):
##    if i % 13 == 0:
##        continue
##    print(i, end=' ')
##    sum_odd += i
##    if sum_odd > 500:
##        break

##odd = 1
##for num in range(1,20):
##    if num % 2 == 0:
##        continue
##    odd *= num
##    print(f'{num} = {odd}')

##num = int(input('숫자를 입력해주세요'))
##for i in range(2,100):
##    num_i = num ** i
##    if num_i > 10000:
##        break
##    print(num_i, end=' ')


##num = int(input('숫자를 입력해주세요: '))
##a=''
##
##for i in range(1,num+1):
##    if num % i == 0:
##        a += str(i) + ' '
##print(f'{num}의 약수: {a}')

##multiple = 3
##
##for i in range(1,200):
##    if i % 15 == 0:
##        continue
##    if multiple == 3 and i % multiple == 0:
##        print(i, end=' ')
##        multiple = 5
##    if multiple == 5 and i % multiple == 0:
##        print(i, end=' ')
##        multiple =3
##    if i > 100:
##        break

##today_luck_num =''
##
##for i in range(1,100+1):
##    if len(today_luck_num.split()) == 5:
##        break
##    if i % 3== 0 :
##        if '7' in str(i):
##            today_luck_num += str(i) + ' '
##print(today_luck_num)

##for num in range(97,104):
##    print(chr(num))

##text = 'ABCDEFG'
##for character in text:
##    print(ord(character))

####text = 'HelloPython'
####
####for character in text:
####    if character.isupper():
####        print(character.lower(),end=' ')
####    elif character.islower():
####        print(character.upper(),end=' ')
##        
##text = 'Hello World How are you doing today?'
##vowels = 'aeiouAEIOU'
##count = 0
##
##for char in text:
##    if char in vowels:
##        count += 1
##
##print(f'모음의 개수 : {count}')

##text = 'abcdefghijklmnopqrstuvwxyz'
##shift = 3
##
##shifted_text=''
##
##for character in text:
##    if character.isalpha():
##        shifted_char = chr((ord(character)+shift))
##        shifted_text += shifted_char
##print(shifted_text)

##num = int(input('숫자를 입력하세요: '))
##sum_num = 0
##
##for i in range(1,num+1):
##    sum_num += i
##
##print(f'합산: {sum_num}')

##text = input('문장을 입력하세요: ')
##count=0
##
##for char in text:
##    if char.isnumeric():
##        count += 1
##print(f'숫자의 개수: {count}')

##text = 'abcdefghijklmnopqrstuvwxyz'
##
##for char in text:
##    if ord(char) % 2 != 0:
##        print(f'{ord(char)}({char})', end=' ')
##    else:
##        print(f'{char}({ord(char)})', end=' ')
        
##text = input('문장을 입력하세요: ')
##shifted_text = ''
##count=0
##vowels='aeiouAEIOU'
##
##for char in text:
##    if char in vowels:
##        shifted_char =char.replace(char,'*')
##        shifted_text += shifted_char
##        count += 1
##    else:
##        shifted_text += char
##
##print(f'''변환된 문장: {shifted_text}
##바뀐 모음의 개수: {count}''')

password=''

import random

while True:
    if len(password)<6:
        num1 = random.randint(0,9)
        num2 = random.randint(65,91)
        password += str(num1)
        password += chr(num2)
    else:
        break

print(password)
                         

    










































































































































