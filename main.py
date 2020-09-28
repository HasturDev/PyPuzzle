from Introduction import Introduction
from beginner_tests.test import starter_test

if __name__ == "__main__":
    print('''Thank you for using PyPuzzle.\n
      If you have any questions then just use "Introduction(list)" and you will see a list of puzzles.\n
      type "Introduction(Puzzle Name)" and information about a puzzle will be given to you.\n''')
    Introduction("list")

    def some_function(x):
        x += 1
        return x
    something = some_function(3)

    starter_test(something)
    