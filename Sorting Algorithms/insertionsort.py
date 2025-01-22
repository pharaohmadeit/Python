# coding: utf-8
import numpy as np
from utilities import print_pass
def insertion_sort(data):
    for next in range(1, len(data)):
        insert = data[next]
        move_item = next
        while move_item > 0 and data[move_item -1] > insert:
            data[move_item] = data[move_item - 1]
            move_item -= 1
        data[move_item] = insert
        print_pass(data, next, move_item)
        
def main():
    data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
    print(f'Unsorted array: {data}\n')
    insertion_sort(data)
    print(f'\nSorted array: {data}\n')
    
if __name__ == '__main__':
    main()
    
