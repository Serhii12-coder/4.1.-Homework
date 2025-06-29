List1 = [0,1,2,3,4,5,0,0,6,0,7,0,9];
length = len(List1) # Це є 13
List2 = List1.copy()

n = 0
while n < len(List2):
    if  List2[n] == 0:
        List2.pop(n)
    else:
        n = n + 1

m = len(List2)
while m < length:
    List2.append(0)
    m = m + 1

print(List1)
print(List2)