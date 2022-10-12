# first get all lines from file
with open('preproinsulin-seq.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

lines = [line.replace("ORIGIN", "") for line in lines]
lines = [line.replace("61", "") for line in lines]
lines = [line.replace("//", "") for line in lines]
lines = [line.replace("1", "") for line in lines]

# finally, write lines in the file
with open('preproinsulin-seq-clean.txt', 'w') as f:
    f.writelines(lines)
