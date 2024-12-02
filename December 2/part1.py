import sys

def count_safe(levels: list):
    safe_count = 0
    for level in levels:
        direction = 0
        safe_possible = False
        for i in range(0, len(level)):
            if i == 0:
                continue
            elif i == 1:
                if level[1] > level[0] and level[i] - level[i - 1] < 4:
                    direction = 1
                elif level[1] < level[0] and level[i - 1] - level[i] < 4:
                    direction = 0
                else:
                    break
            else:
                if direction == 1 and level[i] > level[i - 1] and level[i] - level[i-1] < 4:
                    safe_possible = True
                elif direction == 0 and level[i] < level[i - 1] and level[i - 1] - level[i] < 4:
                    safe_possible = True
                else:
                    safe_possible = False
                    break
        if safe_possible:
            safe_count += 1
    return safe_count
 
def main():
    levels = []
    with open(sys.argv[1]) as f:
        for line in f:
            level = line.split()
            level_int = []
            for value in level:
                level_int.append(int(value))
            levels.append(level_int)
    print(count_safe(levels))
    
if __name__ == "__main__":
    main()