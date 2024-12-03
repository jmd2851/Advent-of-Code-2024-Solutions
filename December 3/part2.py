import regex

program = ""
with open ("input.txt") as f:
    for line in f:
        program += line.strip()
results = []
sum = 0
pos = 0
while pos < len(program):
    if pos != 0:
        pos = program.find("do()", pos)
        if pos == -1:
            break
        else:
            pos += 4
        
    endpos = program.find("don't()", pos)
    if endpos == -1:
        endpos = len(program)
    results = regex.findall("mul\\(\\d*,\\d*\\)", program, pos=pos, endpos=endpos)
    
    for result in results:
        comma = result.find(",")
        product = int(result[4:comma]) * int(result[comma+1:-1])
        sum += product
    pos = endpos

print(sum)
