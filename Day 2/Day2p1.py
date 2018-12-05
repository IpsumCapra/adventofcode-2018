f = open("input.txt", "r");
contents = f.readlines();
a = 0;
b = 0;
for x in contents:
    ac = False;
    bc = False;
    for i in set(x):
        if x.count(i) == 2 and ac == False:
            a+=1;
            ac = True;
        if x.count(i) == 3 and bc == False:
            b+=1;
            bc = True;
print(a*b);
