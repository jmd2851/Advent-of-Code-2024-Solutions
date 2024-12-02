from typing import List
import sys

def similarity(list_a: List, list_b: List):
    overall_similarity = 0
    for a_item in list_a:
        count_in_b = 0
        for b_item in list_b:
            if b_item == a_item:
                count_in_b += 1
        overall_similarity += count_in_b * a_item
    return overall_similarity

def main():
    list_a = []
    list_b = []
    with open(sys.argv[1]) as f:
        for line in f:
            items = line.split()
            list_a.append(int(items[0]))
            list_b.append(int(items[1]))
    print(similarity(list_a, list_b))

if __name__ == "__main__":
    main()