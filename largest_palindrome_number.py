# Find the largest palindrome made from the product of two 3-digit numbers.
def largest_palindrome_num():
    lst=[]
    for i in range(100,999):
        for j in range(100,999):
            if str(i*j)==str(j*i)[::-1]:
                lst.append(i*j)
    return max(lst)
            

res=largest_palindrome_num()
print(res)