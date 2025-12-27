##key_list=['name','hp','mp','level']
##value_list=['기사',200,30,5]
##character={}
##character[key_list[0]] = value_list[0]
##character[key_list[1]] = value_list[1]
##character[key_list[2]] = value_list[2]
##character[key_list[3]] = value_list[3]
##print(character)

##for num1 in range(2):
##    print('바깥쪽 반복문')
##    for num2 in range(3):
##        print('안쪽 반복문')

##for num1 in range(0,4):
##    print(f'안쪽 : {num1}')
##    for num2 in range(0,num1):
##        print(f'\t 바깥쪽 : {num2}')
##    print('='*20)

##cnt=0
##
##for y in range(1,6):
##    for x in range(1,6):
##        cnt += 1
##    print(cnt)

##for y in range(5):
##    sentence=''
##    for x in range(5):
##        sentence += str(y)
##    print(sentence)

##for hour in range(1,13):
##    for minute in range(1,61):
##        print(f'{hour}시 {minute}분')

##for y in range(1,5):
##    pyramid=''
##    for x in range(y):
##        pyramid += str(y)
##    print(pyramid)

##for day in range(1,8):
##    print(f'{day}일차')
##    for time in range(1,4):
##        if time ==1:
##            print('아침', end='')
##        if time ==2:
##            print('낮', end='')
##        if time == 3:
##            print('밤')

##i=1
##txt=''
##
##while i < 4:
##    j=1
##    txt += f'{i}학년'
##    while j < 6:
##        txt += f'{j}반'
##        j += 1
##    i+=1
##    txt += '\n'
##
##print(txt)

##num = 10
##cnt = 0
##
##for y in range(1,num+1):
##    for x in range(1,num+1):
##        cnt += 1
##        print(cnt, end='')
##    print()

##num = int(input('숫자를 입력해 주세요: '))
##cnt=0
##
##for y in range(1, num+1):
##    for x in range(1,y):
##        cnt += 1
##        print(cnt, end='')
##    print()

##for y in range(5):
##    for x in range(5):
##        print(chr(ord('A')+x+y),end='')
##    print()

##string='abcd'
##
##for y in range(len(string)):
##    for x in range(y, len(string)):
##        print(string[y:x+1])

##num=0
##
##for i in range(1,6+1):
##    for j in range(1,5+1):
##        num += 1
##        print(f'{num*10}', end=' ')
##    print()


##for x in range(1,6):
##    print(chr(ord('A')+(x-1))*x)
##print()
##num = 0

##for x in range(1,5+1):
##    for y in range(0,x):
##        print(chr(ord('A')+x+y-1), end='')
####        num += 1
##    print()
##

##for i in range(1,10):
##    print(2,'*',i,'=',2*i)
##
##for i in range(1,10):
##    print('2* %d = %d' % (i,2*i))
##
##for i in range(1,10):
##    print('{0}*{1}={2}'.format(2,i,2*i))

##for i in range(1,10):
##    print('{0} * {1} = {2}'.format(2,i,2*i))
##
##for i in range(1,10):
##    print('{0} * {1} = {2}'.format(3,i,3*i))
##
##for i in range(1,10):
##    print('{0} * {1} = {2}'.format(4,i,4*i))
##
##for i in range(1,10):
##    print('{0} * {1} = {2}'.format(5,i,5*i))

##for dan in range(2,10):
##    for i in range(1,10):
##        print('{0} * {1} = {2}'.format(dan,i,dan*i))


##for dan in range(2,10):
##    print('======={0}단======='.format(dan))
##    for i in range(1,10):
##        print('{0} * {1} = {2}'.format(dan,i,dan*i))

##for dan in range(2,10):
##    for i in range(2,10):
##        print(f'{dan:d} * {i:d} = {dan*i:-2d}',end = ' ')
##    print()

##for dan in range(2,10):
##    for i in range(1,10):
##        if i % 2==0:
##            continue
##        print(f'{dan:2d} * {i:2d} = {dan*i:-3d}', end = ' ')
##    print()


##from_dan = int(input('몇 단 부터? : '))
##to_dan = int(input('몇 단 까지? : '))
##
##for dan in range(from_dan, to_dan+1):
##    for i in range(1,10):
##        print(f'{dan} * {i} = {dan*i}')
##    print()

##column = int(input('몇 개씩? : '))
##to_dan = int(input('몇 단 까지? : '))
##
##for i in range(1,10):
##    for dan in range(2, to_dan+1):
##        if dan < (2 + column):
##        print(f'{dan} * {i} = {dan*i}', end='\t')
##        if dan >= 2 + column:
##            print()
##    print()

##column = int(input('몇 개씩? : '))
##to_dan = int(input('몇 단 까지? : '))
##
##for i in range(1, 10):
##    for dan in range(2, 2 + column):
##        print(f'{dan:2d} * {i:2d} = {dan*i:2d}', end='  ')
##    print()
##print()
##for i in range(1, 10):
##    for dan in range(2 + column, to_dan + 1):
##        print(f'{dan:2d} * {i:2d} = {dan*i:2d}', end='  ')
##    print()

##to_dan = int(input('몇 단 까지? : '))
##
##for dan in range(2,to_dan + 1):
##    for su in range(1,10):
##        for dan_2 in range(dan,dan+5):
##            print(f'{dan:2d}*{su:2d} = {dan*su:-3d}', end='  ')
##        print()
##    print()

##column = int(input('몇 개씩? : '))
##to_dan = int(input('몇 단 까지? : '))
##
##for dan_2 in range(0,column):
##    for dan in range(2,to_dan + 1):
##        for su in range(1,10):
##            print(f'{dan:2d}*{su:2d} = {dan*su:-3d}', end='  ')
##        print()
##    print()


##to_dan = int(input('몇 단 까지? : '))
##
##for dan in range(2,to_dan + 1,5):
##    for su in range(1,10):
##        for dan_2 in range(dan,dan+5):
##            if dan_2 > to_dan:
##                break
##            print(f'{dan_2:2d}*{su:2d} = {dan_2*su:-3d}', end='  ')
##        print()
##    print()

##for i in range(1,6):
##    print('*',end='')

##for i in range(1,6):
##    for j in range(1,6):
##        print('*',end='')
##    print()
    
##for i in range(1,6):
##    for j in range(1,i+1):
##        print('*',end='')
##    print()

##for i in range(1,6):
##    for j in range(i,6):
##        print('*',end='')
##    print()

##for out in range(1,6):
##    for blank in range(out,6):
##        print(' ',end='')
##    for star in range(1,out+1):
##        print('*',end='')
##    print()

for out in range(1,6):
    for blank in range(1,out+1):
        print(' ',end='')
    for star in range(out,6):
        print('*',end='')
    print()





















































































































































































