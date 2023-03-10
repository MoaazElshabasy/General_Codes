def updateContact(info, name):
    b = False
    for key in contacts:
        if key == info:
            b = True
            break
        else:
            b = False
    contacts.update({info:name})
    return b

def findName(info):
    if info in contacts.keys():
        return info in contacts.keys() , contacts.get(info)
    else:
        return False , ""  

def findContact(partName):
    L = list()
    partName = partName.lower()


    for i in contacts.keys():
        c = 0

        contacts[i] = contacts[i].lower()

        for x in range(0, len(contacts[i])):
            if partName[c].upper() == contacts[i][x].upper(): 
                c += 1
                if c == len(partName):
                    L.append((i,contacts[i]))
                    break
            else: c = 0
    return L
    

def deleteContact(value):
    count = 0
    for key in range(0,len(contacts)):
        for key in contacts:
            if value == key:
                del contacts[value]
                count += 1
                break
            elif value == contacts[key]:
                contacts.pop(key)
                count += 1
                break
    return count

