f = open("input.txt", "r");
contents = f.readlines();
a = 0;
al = [];
for line in contents:
    c = [];
    for x in line:
        c.append(x)
        a += int(line);
        if a in al:
            print(a);
            found = True;
            break;
        else:
            al.append(a);
    c+=1;
    print("Try ",c);
    
