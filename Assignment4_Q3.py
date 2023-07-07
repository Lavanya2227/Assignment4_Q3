#Square the elements of a list using map() function.

def square_num(n):
   return n*n
num = list(map(int,input("Enter your list: ",).split()))
print("original list: ",num)
result= map(square_num,num)
print("Square of the given list: ", list(result))
