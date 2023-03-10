def area_of_country(name, area):
    total = 148940000
    per = ""
    per1 = round(area / total *100, 2 )
    per += str(per1)
    per += "%"
    text = name + " is " + per + " of the total world's landmass"
    return text
print(area_of_country("Russia", 17098242))