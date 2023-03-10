def cm_gridMove(pathString, startPoint = (0, 0)):
 
    row = startPoint[0]
    col = startPoint[1]
    pathString = pathString.lower()
    for dir in pathString:
        if dir == 'n':
            row += 1
        elif dir == 's':
            row -= 1
        elif dir == 'e':
            col += 1
        elif dir == 'w':
            col -= 1
            
    return (row, col)
    
def cm_pointOnPath(pathString, point, startPoint = (0,0)):
    x = startPoint[0]
    y = startPoint[1]
    if pathString == '' and point == (0,0):
        return True
    for i in range(0, len(pathString)):
        if pathString[i] == 'n' or pathString[i] == 'N':
            x += 1
            startPoint = (x,y)
            if startPoint == point:
                return True
        elif pathString[i] == 's' or pathString[i] == 'S':
            x -= 1
            startPoint = (x,y)
            if startPoint == point:
                return True
        elif pathString[i] == 'e' or pathString[i] == 'E':
            y += 1
            startPoint = (x,y)
            if startPoint == point:
                return True
        elif pathString[i] == 'w' or pathString[i] == 'W':
            y -= 1
            startPoint = (x,y)
            if startPoint == point:
                return True
        
    return False

def cm_generatePath(endPoint, startPoint =(0,0)):
    V = endPoint[0] - startPoint[0]
    H = endPoint[1] - startPoint[1]
    path = ''
    if V > 0:
        for i in range(0, V):
            path += 'n'
    else:
        for i in range(0, V, -1):
            path += 's'
    if H > 0:
        for i in range(0, H):
            path +=  'e'
    else:
        for i in range(0, H, -1):
            path +=  'w'
    return path 
        
def cm_reversePath(pathString, reTrace = True):
    Np = ''
    if reTrace == True:
        if pathString == 'news':
                Np += 'news'
        else: 
            for i in range(-1, -len(pathString)-1, -1):
                if pathString[i] == 'n':
                    Np += 's'
                elif pathString[i] == 's':
                    Np += 'n'
                elif pathString[i] == 'w':
                    Np += 'e'
                elif pathString[i] == 'e':
                    Np += 'w'
    else:
        V = 0
        H = 0
        for i in range(0, len(pathString)):
            if pathString[i] == 'n':
                V += 1
            elif pathString[i] == 's':
                V -= 1
            if pathString[i] == 'e':
                H += 1
            elif pathString[i] == 'w':
                H -= 1
        
        if V > 0:
            for i in range(0, V):
                Np += 's'
        else:
            for i in range(0, V, -1):
                Np += 'n'
        if H > 0:
            for i in range(0, H):
                Np +=  'w'
        else:
            for i in range(0, H, -1):
                Np +=  'e'
        
    return Np


print(cm_reversePath('swswswwwn', reTrace = True))