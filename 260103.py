##txt = input('영어로 문자열을 입력해주세요. :')
##
##i = 0
##common=''
##while i < len(txt):
##    count = 1
##    if txt[i] not in common:
##        for j in range(i+1,len(txt)):
##            if txt[i] == txt[j]:
##                count += 1
##        common += (txt[i] +':' +str(count)+'\n')
##    i += 1
##
##print(f'{common}')

##mylist = [3,6,9]
##strlist=list('이샘코딩학원')
##
##print(mylist[0])
##print(mylist[:3])
##print(mylist[-1])

##mylist = [3,6,9]
##del mylist[2]
##print(mylist)

##doublelist=[1, [2,3], [4,[5,6]]]
####print(doublelist[0])
####print(doublelist[1][0])
####print(doublelist[2][0])
####print(doublelist[2][1][0])
##
##print(len(doublelist))

##num_list = [10,20,30,40,50]
##print('num_list :',num_list)
##print('num_list의 길이 :',len(num_list))

##test_list = ['하나',2,3.0]
##print(test_list[0],type(test_list[0]))
##print(test_list[1],type(test_list[1]))
##print(test_list[2],type(test_list[2]))

##sample = [1,1,2,3,5,8,13,21,34,55,89,144]
##
##print(sample[1])
##print(sample[-1])
##print(sample)
##print(sample[0:len(sample)])
##print(sample[::-1])

##txt = list('테스트 중')
##print(txt)
##
##txt[4]='끝'
##print(txt)

##sample=[]
##sample1 = list()
##
##sample2 = list('예시문장입니다.')
##
##print(sample)
##print(sample2[2:4])
##print(sample2[1:5:2])

##phone = [[1,2,3],[4,5,6],[7,8,9],['#',0,'*']]
##
##print(phone)
##print(phone[0])
##print(phone[1])
##print(phone[2])
##print(phone[3])
##print(phone[0][0])
##print(phone[1][1])

##mylist = [3,6,9]
##mylist.append(12)
##print(mylist)

##mylist = [3,6,9]
##mylist.insert(0,0)
##print(mylist)
##
##mylist = [3,6,9]
##mylist.remove(6)
##print(mylist)

##mylist = [3,6,9]
##n=mylist.pop(0)
##print(n)

##mylist=[86, '안녕', 2.01]
##print(mylist.index('안녕'))

##mylist=[86, '안녕', 2.01]
##print(mylist.pop(1))

##test=[1,2,3]
##print(test[2])
##
##test.append(4)
##print(test)
##
##del test[1]
##print(test)

##animals=['고양이','너구리','강아지','사자']
##search = input('동물 이름을 입력하세요 :')
##
##if search in animals:
##    print('해당 동물이 리스트에 있습니다.')
##else:
##    print('해당 동물이 리스트에 없습니다.')

##test = [1,2,3]

####test[3] = 4
##test.insert(0,5)
##print(test)

##test.remove(2)
##print(test)

##temp = test.pop(2)
##print(test.pop(2), test)

##num_list=[3,4,5,6,7]
##print('리스트 안에',num_list,'이 있습니다.')

##data_list=[]
##count = 1
##
##while count<=3:
##    data=input('데이터를 입력해주세요 : ')
##    data_list.append(data)
##    count += 1
##print(data_list)

##alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
##print(alphabet)
##
##char_6=alphabet.pop(6)
##print(char_6)
##print(alphabet)

##alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
####
####index_ch = alphabet.index('B')
####print(index_ch,alphabet[index_ch])
##
##ch = input('알파벳을 입력하세요')
##index_ch = alphabet.index(ch)
##print(ch,'는',index_ch + 1,'번째 알파벳', sep='')

##string=input('문자열을 입력해주세요 : ')
##print(string[::-1])

##num_list=[]
##
##for i in range(1, 100+1):
##    num_list.append(i)
##print(num_list)
    
##num_list=[]
##
##for i in range(1, 100+1):
##    num_list.append(i)
##    if i==1 or (i != 2 and i % 2 == 0):
##        num_list.remove(i)
##
##print(num_list)

##num_list=[]
##
##for i in range(1, 100+1):
##    num_list.append(i)
##    if i==1 or (i != 2 and i % 2 == 0):
##        num_list.remove(i)
##    for j in num_list:
##        if j !=3 and j % 3 == 0:
##            num_list.remove(j)
##
##print(num_list)

##num_list=[]
##
##for i in range(1, 100+1):
##    num_list.append(i)
##    if i==1 or (i != 2 and i % 2 == 0):
##        num_list.remove(i)
##    for j in num_list:
##        if j !=3 and j % 3 == 0:
##            num_list.remove(j)
##    for k in num_list:
##        if k !=5 and k % 5 == 0:
##            num_list.remove(k)
##
##print(num_list)

##num_list=[]
##del_num=[]
##
##for n in range(2, 100+1):
##    num_list.append(n)
##    for k in range (2, n):
##        if n % k == 0 and n not in del_num:
##            del_num.append(n)
##            
##for i in del_num:
##    i_index=num_list.index(i)
##    del num_list[i_index]
##
##print(num_list)
          
##num_list=[]
##
##
##for i in range(2, 100+1):
##    num_list.append(i)
##
##for k in num_list:
##    for j in range(k+1,100+1):
##        if j % k == 0 and j in num_list:
##            num_list.remove(j)
##
##print(num_list)          

List=[]
while True:
    menu=input('1. 추가 2. 삭제 3. 확인 4. 종료 : ')
    if menu == '1':
        string=input('추가할 문자열을 입력해주세요')
        List.append(string)

    if menu == '4':
        break
    else:
        continue


















































































































































































































