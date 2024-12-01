from typing import List
import sys

def list_distance(list_a: List, list_b: List):
    if len(list_a) != len(list_b):
        print("Lists not equal length")
        return False
    list_a.sort()
    list_b.sort()
    distances = []
    for i in range (0, len(list_a)):
        distances.append(abs(list_a[i] - list_b[i]))
    total_distance = 0
    for distance in distances:
        total_distance += distance
    return total_distance

def main():
    list_a = []
    list_b = []
    with open(sys.argv[1]) as f:
        for line in f:
            items = line.split()
            list_a.append(int(items[0]))
            list_b.append(int(items[1]))
    print(list_distance(list_a, list_b))

if __name__ == "__main__":
    main()