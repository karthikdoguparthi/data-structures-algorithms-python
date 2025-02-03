'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

odd_num=[]

n=int(input("Enter max number: "))
for i in range (1,n):
  if i%2==1:
    odd_num.append(i)

print("Odd Numbers: ", odd_num)
