#!/usr/bin/env python3

import argparse
from sudoku import Sudoku

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sudoku solver')

    parser.add_argument('--create-input-file', type=bool, required=False, default=False,
                        help='This flag creates template for sudoku to solve.')
    parser.add_argument('--path', '-p', type=str, required=False, default='sudoku.txt',
                        help='Path of input or output file.')

    args = parser.parse_args()

    if args.create_input_file:
        template = Sudoku.create_template()

        with open(args.path, 'w') as f:
            f.write(template)
    else:
        with open(args.path, 'r') as f:
            input_board = f.read()

        sudoku = Sudoku(input_board=input_board)
        sudoku.solve()
        print(str(sudoku))