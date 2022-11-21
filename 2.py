def count (s,c):
    result=0
    for i in range(len(s)):
        if(s[i]==c):
            result+=1
    return result

str1 = input()
str2 = input()
c=str2[-1]
print(count(str1,c))