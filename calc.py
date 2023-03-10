def calculator(txt):

    l = []
    temp1 = []
    temp2 = []
    temp = ""
    for i in range(len(txt)):
        if txt[i].isnumeric():
            temp += txt[i]
        else:
            if temp.isnumeric():
                temp = int(temp)
            temp1 = temp

            l.append(temp1)
            temp1 = []
            temp2 = txt[i]
            l.append(temp2)
            temp2 = []
            temp =""
        if i+1 == len(txt):
            if temp.isnumeric():
                temp = int(temp)
            temp1 = temp
            l.append(temp1)
            temp1 = []
            temp =""
        
    print(l)
    temp3 = 0
    while len(l) > 1:
        if "*" in l and "/" in l:
            if l.index("*") < l.index("/"):
                k = l.index("*")
                temp3 = l[k-1] * l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
                k = l.index("/")
                temp3 = l[k-1] / l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
        #if "/" in l:
            else:
                k = l.index("/")
                temp3 = l[k-1] / l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
                k = l.index("*")
                temp3 = l[k-1] * l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
        elif "*" in l:
            k = l.index("*")
            temp3 = l[k-1] * l[k+1]
            l[k-1] = temp3
            l.remove(l[k])
            if k+1 != len(l):
                l.remove(l[k])
            else:
                l.pop()
            print(l)
        elif "/" in l:
            k = l.index("/")
            temp3 = l[k-1] / l[k+1]
            l[k-1] = temp3
            l.remove(l[k])
            if k+1 != len(l):
                l.remove(l[k])
            else:
                l.pop()
            print(l)
        if "+" in l and "-" in l:
            if l.index("+") < l.index("-"):
                k = l.index("+")
                temp3 = l[k-1] + l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
                k = l.index("-")
                temp3 = l[k-1] - l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
        #if "/" in l:
            else:
                k = l.index("/")
                temp3 = l[k-1] / l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
                k = l.index("*")
                temp3 = l[k-1] * l[k+1]
                l[k-1] = temp3
                l.remove(l[k])
                if k+1 != len(l):
                    l.remove(l[k])
                else:
                    l.pop()
                print(l)
        elif "+" in l:
            k = l.index("+")
            temp3 = l[k-1] + l[k+1]
            l[k-1] = temp3
            l.remove(l[k])
            if k+1 != len(l):
                l.remove(l[k])
            else:
                l.pop()
            print(l)
        elif "-" in l:
            k = l.index("-")
            temp3 = l[k-1] - l[k+1]
            l[k-1] = temp3
            l.remove(l[k])
            if k+1 != len(l):
                l.remove(l[k])
            else:
                l.pop()
            print(l)

    return l[-1]