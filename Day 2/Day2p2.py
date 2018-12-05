f = open("input.txt", "r");
contents = f.readlines();
for line in contents:
    b = [];
    for x in line:
        b.append(x);
    for y in contents:
        a = 0;
        d = 0;
        for z in y:
            if b[a] != z:
                d+=1;
            a+=1;
        if d == 1:
            print(x,y);
            
