# Day 1 05.03.23
# https://leetcode.com/problems/longest-common-prefix/
# Find Commomn Prefix

#strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
m = 1
word = strs[0]
while m<len(strs):
    for i in range(0,len(word)):
        if strs[m].startswith(word):
            break
        else:
            word = word[:-1]
    m+=1
    if word == '':
        break
print(word)