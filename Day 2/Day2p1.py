# Open input.txt in readmode, split into individual lines.
f = open("input.txt", "r");
contents = f.readlines();

a = 0;
b = 0;

# Find all occurences of 2 or 3 letters inside of an input line, increment a and b.
for x in contents:
    ac = False;
    bc = False;
    for i in set(x):
        # Two occurunces of a character.
        if x.count(i) == 2 and ac == False:
            a+=1;
            ac = True;
        # Three occurences of a character.
        if x.count(i) == 3 and bc == False:
            b+=1;
            bc = True;
#Print the result.
print(a*b);
