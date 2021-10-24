# Open 'input.txt' in read mode.
f = open("input.txt", "r");

# Store the lines of the file in a list.
contents = f.readlines();

a = 0;
al = [];

# Find the number that is the sum of a subset of all numbers, and also inside of the list.
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
    
