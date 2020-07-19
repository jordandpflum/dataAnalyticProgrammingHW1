import re


file = open('Santa.txt','r')
santa = file.read()
out_list = []
for line in santa:
    santa.rstrip()
    out_list = santa.split('\n')
out_list.remove('')

file.close()


g=0
a_list = []
for i in out_list:
    a_list.append(re.findall('\S+\s?',out_list[g]))
    #print(re.findall('\S+\s',out_list[g]))
    #print(a_list)
    g +=1

l=0
new_list = []
for i in range(0,len(a_list)):
    p=0
    while p <= len(a_list[l])-3:
        new_list.append(a_list[l][p]+a_list[l][p+1]+a_list[l][p+2])
        p += 1
    l += 1

out_dict = {}

u=0
for i in range(0,len(new_list)):
    out_dict[new_list[u]] = 1
    u += 1
print(out_dict)
