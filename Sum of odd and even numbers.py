def sum_odd_and_even(lst):
    even = []
    odd = []
    temp1 = 0
    temp2 = 0
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            even.append(lst[i])
        elif lst[i]%2 == 1:
            odd.append(lst[i])
    for j in range(len(even)):
        temp1 += even[j]
    for k in range(len(odd)):
        temp2 += odd[k]
    return [temp1,temp2]
