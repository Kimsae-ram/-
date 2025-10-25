##str1= '파이썬 문자열을 골라보자'
##print(str1[0])
##print(str1[4])
##print(str1[9])
##print(str1[2])
##print(str1[6])
##print(str1[12])

##str2='이샘코딩학원'
##print(str2[1:3])
##print(str2[2:])
##print(str2[:2])
##print(str2[::2])
##print(str2[::-2])

##word='문자열과 인덱스'
##print(word[0])
##print(word[3])
##print(word[5])
##print(word[-1])

##snack='떡볶이 순대 튀김'
##setmenu = snack[0] + snack[4] +snack[7]
##print(setmenu)

##word = '부분만 바꾸려고 하면 에러가 나요'
##print(word)
##word[0]='수'

##word='새로 만들어 덮어 쓰기는 가능'
##print(word)

##word='슬라이싱으로 다양하게 문자를 잘라봅시다'
##print(word[0:4])
##print(word[7:9])
##print(word[5:])
##print(word[:12])
##print(word[::3])
##print(word[::-3])

##song= '록도닳 고르마 이산두백 과물해동'
##reverse = song[::-1]
##print(reverse)

##song = '동해물과 백두산이 마르고 닳도록'
##part_song=song[:4]
##print(part_song)
##part_song=song[5:13]
##print(part_song)
##part_song=song[14:]
##print(part_song)

##str='가나다라마바사1234567'
##print(str[1::2])

##str='100123-4567890'
##print(str[2:6])

##str1='타파에벅서이썬스나짱만스'
##print(str1[11]+str1[0]+str1[3]+str1[7]+str1[2]+str1[4]+str1[10]+str1[8])

##song='동해물과 백두산이 마르고\n닳도록\n하느님이 보우하사\n우리나라 만세.\n무궁화 삼천리 화려 강산\n대한 사람, 대한으로\n길이 보전하세.'
##print(song[33:35])
##print(song[68:70])

##song='동해물과 백두산이 마르고\n닳도록\n하느님이 보우하사\n우리나라 만세.\n무궁화 삼천리 화려 강세\n대한 사람, 대한으로\n길이 보전하세.'
##print(song)

##song='동해물과 백두산이 마르고\n닳도록\n하느님이 보우하사\n우리나라 만세.\n무궁화 삼천리 화려 강산\n대한 사람, 대한으로\n길이 보전하세.'
##print(song[:47]+'강세')
##print(song[51:])

##str1='파이썬, c언어, HTML/CSS, JAVA'
##logic1='파이썬' in str1
##print(logic1)
##logic2='c#' in str1
##print(logic2)

##poison='이 파이썬 문장에는 독이 있어'
##print('독' in poison)
##print('약' not in poison)

##number=12345678
##print(1 in number)

##number='12345678'
##print(1 in number)
##number='12345678'
##print('1' in number)

##message='다른 연산자끼리 섞어쓰는 것도 가능해'
##print('연산자' in message[2:10])
##print('연산자' not in '정말 다양한 방법으로' + '연산자를 쓸 수 있어')

##string='문자열 함수 & 문자열 함수'
##print(string.find('자열'))
##print(string.find('함수'))
##print(string.rfind('자열'))
##print(string.rfind('함수'))

##string='hellopython'
##number='12345'
##print(string.isalpha())
##print(string.isnumeric())
##print(number.isalpha())
##print(number.isnumeric())

##string='hello python'
##number='12345'
##print(string.isalpha())
##print(string.isnumeric())
##print(number.isalpha())
##print(number.isnumeric())

##bab = '국밥 컵밥 초밥 김밥 비빔밥'
##print('가장 앞에 있는 밥은 ' + str(bab.find('밥')) +'번째!')
##print('가장 마지막에 있는 밥은 ' +str(bab.rfind('밥')) +'번째!')

##eng='funnypython'
##kor='신나는파이썬'
##blank='B L A N K'
##print(eng.isalpha())
##print(kor.isalpha())
##print(blank.isalpha())

##num='20240505'
##date='2024.05.05'
##print(num.isnumeric())
##print(date.isnumeric())

##bean='강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다.'
##print('첫번째 완두콩은 ' +str(bean.find('완두콩'))+'번째에 있습니다.')
##print('두번째 완두콩은 '+ str(bean.rfind('완두콩'))+'번째에 있습니다.')

##bean='강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다.'
##print(bean[bean.find('완두콩'):24])
##print(bean[bean.rfind('강낭콩'):50])

##ID=input('이메일을 입력해주세요')
##print(ID[:ID.find('@')])

##string='문자열_함수는_참_다양해요'
####split_string=string.split('_')
####print(split_string)
##string = string.replace('다양해','멋져')
##print(string)

##string='Python Upper Lower'
##print(string.upper())
##print(string.lower())

##dessert = '초코케이크 녹차마카롱 모카라떼'
##cake, macaron, coffee= dessert.split(' ')
##print('[오늘 먹을 간식 목록]')
##print('케이크 :', cake)
##print('마카롱 :', macaron)
##print('커피 :', coffee)

##n1, n2=input('int 둘 입력: ').split()
##print(n1)
##print(n2)
##print(n1+n2)
##print(int(n1)+int(n2))

##a,b,c = input('알파벳 셋 입력 :').split()
##print(c,b,a,sep='>')

##r1, r2 =input('float 둘 입력 :').split()
##r1=float(r1)
##r2=float(r2)
##print(r1*r2)

##message='대공원에 봄 벚꽃 놀이는 낮 봄 벚꽃 놀이보다 밤 봄 벚꽃 놀이니라.'
##print(message.replace('벚꽃','개나리'))

##win='windowXP'
##update=win.replace('XP','11')
##print(update+'로 업데이트 되었습니다.')

##japangi='이 자판기 안에는 포도맛 사이다, 포도맛 쥬스, 포도맛 슬러쉬가 있습니다.'
##taste=input('무슨 맛 자판기로 바꿀까요 :')
##print(japangi.replace('포도',taste))
        
##message = input('영어로 문장을 적어주세요: ')
##print(message.upper())
##print(message.lower())

##message='abcD 1234 !!@@'
##trans=message.upper()
##print(trans)

##phone1, phone2, phone3=input('전화번호 입력 :').split('-')
##print(phone1)
##print(phone2)
##print(phone3)

##file=input('파일명을 입력해주세요:')
##print(file+ '파일을' +file.replace('jpg','png')+'파일로 변경했습니다.')

##message='Hello Python, Hello String!'
##print(message.upper())
##print(message.lower())

##string = '이 문장안에 있는 글자 수는 몇개일까요?'
##print(len(string))

##string='파이썬 {0}번 복습하기'.format(10)
##print(string)
##string2=f'문자열도 {10:5.2f}번 복습하기'
##print(string2)





















































































































































