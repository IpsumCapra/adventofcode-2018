f = open("input.txt", "r");
contents = f.readlines();
a = 0;
for line in contents:
    a += int(line);

print(a);
