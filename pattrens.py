''''-----------------------------------------pattren program for pyramid-------------------------------------------------'''

'''for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    for j in range(1,i+1):
         print("*",end=" ")    
    print()'''

'''-------------------------------------------or--------------------------------------------------------------'''

'''rows=int(input("enter the numbr"))
max_width=rows*2
for i in range(1,rows+1):
    stars=' '.join('*'*i)
    leading_spaces=(max_width-len(stars))//2
    print(' '*leading_spaces-stars)'''

'''------------------------------------for right angle triangle-----------------------------------------------'''

'''rows=int(input("enter the numbr"))
max_width=rows*2
for i in range(1,rows+1):
    stars=' '.join('*'*i)
    print(stars)'''
'''------------------------------------------or--------------------------------------------------------------'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=' ')
    print('')    