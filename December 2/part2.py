import sys

def count_safe(levels: list[list[int]]):
    safe_count = 0
    for level in levels:
        if check_level(level):
            safe_count += 1
        elif check_damper(level):
            safe_count += 1    
    return safe_count

def check_damper(level: list[int]):
    for i in range(0, len(level)):
        amended_level = level
        amended_level = level[:i] + level[i + 1:]
        if check_level(amended_level):
            return True
    return False

def check_level(level: list[int]):
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
                if direction == 1 and level[i] > level[i - 1] and level[i] - level[i - 1] < 4:
                    safe_possible = True
                elif direction == 0 and level[i] < level[i - 1] and level[i - 1] - level[i] < 4:
                    safe_possible = True
                else:
                    safe_possible = False
                    break
    return safe_possible

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