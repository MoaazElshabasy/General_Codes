name ="May, the F0urth, Be with Y0u:"
l = []
l2 = []
new = ""
temp = ""
sc = ".,:;"
dic = []
c=0
for i in range(len(name)):

    if name[i].isspace() and temp != '':
        l.append(temp + " ")
        c +=1
        temp =  ""
    elif i == len(name)-1 and not((name[i] not in sc) and (name[i].isalpha or name[i].isnumeric) or name[i].isspace()) :
        l.append(temp + " ")
        c+=1
        temp1 = (name[i], c)
        dic.append(temp1)
    elif i == len(name)-1:
        temp += name[i]
        l.append(temp)
        c +=1
        temp =  "" 
    elif (name[i] not in sc) and (name[i].isalpha or name[i].isnumeric) :
        if not(name[i].isspace()):
            temp += name[i]
    else:
        c+=1
        temp1 = (name[i], c)
        dic.append(temp1)
        
j = -1
if " " in l:
    l.remove(" ")
while j != -len(l) -1:
    l2.append(l[j] + " ")
    j-=1

for k in range(len(dic)):
    l2.insert(dic[k][1], dic[k][0] + " ")
for h in range(len(l2)):
    new += l2[h]
print(new)

