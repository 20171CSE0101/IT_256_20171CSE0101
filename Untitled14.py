#!/usr/bin/env python
# coding: utf-8

# In[4]:


input_string = "Data Science"
frequencies = {}
count=0

for char in input_string:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# Show Output
print("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))

for i in range(0, len(input_string)):
    if (input_string[i] != ' '):
        count = count + 1;

    # Displays the total number of characters present in the given string
print("Total number of characters in a string: " + str(count));


# In[2]:


def check_isogram(str1):
    return len(str1) == len(set(str1.lower()))

print(check_isogram("w3resource"))
print(check_isogram("w3r"))
print(check_isogram("Python"))
print(check_isogram("Java"))


# In[1]:


import string

alphabet = set(string.ascii_lowercase)


def ispangram(string):
    return set(string.lower()) >= alphabet


# Driver code
string = "The quick brown fox jumps over the lazy dog"
if (ispangram(string) == True):
    print("Yes")
else:
    print("No")


# In[2]:


n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()


# In[3]:


def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

print(is_anagram('anagram','nagaram'))
print(is_anagram('cat','rat'))


# In[4]:


# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = "ATTACKATONCE"
s = 4
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))


# In[5]:


import sys

A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

            # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i])


# In[6]:


nlist = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]
print('List has the items: ', nlist)
searchItem = int(input('Enter a number to search for: '))
found = False
for i in range(len(nlist)):
    if nlist[i] == searchItem:
        found = True
        print(searchItem, ' was found in the list at index ', i)
        break
if found == False:
    print(searchItem, ' was not found in the list!')


# In[7]:


num = list(range(10))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum)) # <- This is the issue.
    previousNum=i


# In[8]:


st=input("Enter a string:")
n=int(input("Enter a number:"))
op=st[n+1:len(st)]
print(op)
test_str = "Python"

# Printing original string
print("The original string is : " + test_str)

# Removing char at pos 3
# using loop
new_str = ""

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

    # Printing string after removal
print("The string after removal of i'th character : " + new_str)


# In[ ]:





# In[ ]:




