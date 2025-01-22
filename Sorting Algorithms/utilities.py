# coding: utf-8
"""Utility function for printing a pass of the insertionsort.py and selectionsort.py algorithms."""

def print_pass(data, pass_number, index):
    label = f'after pass {pass_number}: '
    print(label, end='')
    print('  '.join(str(d) for d in data[:index]), end='  ' if index != 0 else '')
    print(f'{data[index]}* ', end='')
    print('  '.join(str(d) for d in data[index + 1:len(data)]))
    print(f'{" " * len(label)}{"-- " * pass_number}')
    
