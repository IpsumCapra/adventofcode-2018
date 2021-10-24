# Read input.txt, split into lines.
f = open("input.txt", "r");
contents = f.readlines();

# Algorithm to find the common letters between two lines.
for line in contents:
    b = [];
    for x in line:
        b.append(x);
    for y in contents:
        a = 0;
        d = 0;
        # Count common letters.
        for z in y:
            if b[a] != z:
                d+=1;
            a+=1;
        # If there is only one mismatch, print it.
        if d == 1:
            print(x,y);
            
