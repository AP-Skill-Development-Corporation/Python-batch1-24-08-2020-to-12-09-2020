def leapyears(s,e):
    for year in range(s,e+1):
        if year%400==0 or (year%100!=0 and year%4==0):
            print(year,end=" ")
        else:
            pass
        
def duplicates(li):#[12,12,13,14,13]--->[12,13,14]
    li1=[] #12,13,14
    for i in li: #12,12,13,14,13
        if i not in li1:
            li1.append(i)
    print(li1)
        