##for out in range(1,6):
##    for blank in range(out,6):
##        print(' ',end='')
##    for star in range(1,out+1):
##        print('*',end='')
##    print()

##for out in range(1,6):
##    for blank in range(1,out+1):
##        print(' ',end='')
##    for star in range(out,6):
##        print('*',end='')
##    print()

##for out in range(1,6):
##    for blank1 in range(out,6):
##        print(' ',end='')
##    for star in range(1,2*out):
##        print('*',end='')
##    print()

##for out in range(1,6):
##    for blank1 in range(out,6):
##        print(' ',end='')
##    for star1 in range(1,2*out):
##        print('*',end='')
##    print()
##print('*'*11)
##for out in range(5,0,-1):
##    for blank2 in range(out,6):
##        print(' ',end='')
##    for star2 in range(2*out-1,0,-1):
##        print('*',end='')
##    print()

##s='PYTHON'
##for y in range(len(s)):
##    for x1 in range(len(s) - y - 1):
##        print(' ',end='')
##    for x2 in range(2*y+1):
##        print(s[x2 % len(s)], end='')
##    print()

##s='시간을달려서'
##n=len(s)
##for y in range(n):
##    for x in range(n):
##        if y <= x and y <= n-1-x or y >= x and y >= n-1-x:
##            print(s[x],end='')
##        else:
##            print(' ',end='')
##    print()

##s='테두리를만들자'
##n=7
##for y in range(n):
##    for x in range(n):
##        if y == 0 or y==n-1 or x==0 or x==n-1:
##            print(s[(x+y)%len(s)],end='')
##        else:
##            print('  ',end='')
##    print()

##s='빙글빙글돌아가는파이썬'
##n=15
##for y in range(n):
##    for x in range(n):
##        min_dist = min(y,x,n-1-y,n-1-x)
##        print(s[min_dist % len(s)], end=' ')
##    print()

##s1 = '파이썬은 즐거워'
##s2 = '파이썬은 재밌어'
##common=''
##for letter1 in s1:
##    for letter2 in s2:
##        if letter1 == letter2 and letter1 not in common:
##            common += letter1
##print(f'공통 문자: {common}')

##s='AABBBCCCC'
##compressed = ''
##i=0
##while i < len(s):
##    count = 1
##    for j in range(i + 1, len(s)):
##        if s[j] == s[i]:
##            count += 1
##        else:
##            break
##    if count > 1:
##        compressed += str(count) + s[i]
##    else:
##        compressed += s[i]
##    i += count
##print(f'압축된 문자열: {compressed}')

##s= 'ABABABABABA'
##pattern='ABA'
##
##for i in range(len(s) - len(pattern) + 1):
##    match = True
##    for j in range(len(pattern)):
##        if s[i+j] != pattern[j]:
##            match = False
##            break
##    if match:
##        print(f'패턴 발견 위치 : {i}')

txt = input('영어로 문자열을 입력해주세요. :')

i = 0
common=''
while i < len(txt):
    count = 1
    if txt[i] not in common:
        for j in range(i+1,len(txt)):
            if txt[i] == txt[j]:
                count += 1
                common += txt[i] +':' +str(count)
    else:
        continue
    i += 1

print(f'{common}')
















































































































