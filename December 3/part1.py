import regex

program: list[str] = []
with open ("input.txt") as f:
    for line in f:
        program.append(line.strip())
results = []
for line in program:
    results += regex.findall("mul\\(\\d*,\\d*\\)", line)

sum = 0
for result in results:
    comma = result.find(",")
    product = int(result[4:comma]) * int(result[comma+1:-1])
    sum += product

print(sum)
