# Open the file 'input.txt' in read mode.
f = open("input.txt", "r");

# Store the contents as a list of the lines of the file.
contents = f.readlines();

# Add up the number in each line into one variable.
a = 0;
for line in contents:
    a += int(line);

# Print the final result.
print(a);
