'''By Brent Gannetta for Mission Bit'''

# ARE YOU A STUDENT? Don't look at this file while doing this challenge -- it's cheating! If you are curious as to how it works, though, you can look AFTER completing the challenge.









































































































# I SAID NO PEEKING!






















































def craft_pickaxe(grid=[None]):
    '''prints a user friendly message regarding whether the crafting recipe was correct'''
    if grid == [None]:
        print("It looks like you forgot to include the function's parameter. Check the instructions and try again!")
    elif check_grid(grid):
        print("You crafted a Wooden Pickaxe!")
    else:
        print("Your crafting_grid doesn't match the example. Try again!")

































def check_grid(grid): 
    '''checks the contents of the input crafting recipe against the example recipe and returns a bool'''
    example = [
        ["Oak Plank", "Oak Plank", "Oak Plank"],
        ["","Stick",""],
        ["","Stick",""]
    ]
    # check grid has correct number of rows
    if len(grid) != len(example):
        return False
    # check each row has correct number of items
    if len(grid[0]) != len(example[0]) or len(grid[1]) != len(example[1]) or len(grid[2]) != len(example[2]):
        return False
    # check each item in each row using nested loops
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != example[i][j]:
                return False
    return True

if __name__ == "__main__":
    print("Are you trying to cheat?! This file is not meant to be run directly. Please run main.py by pressing the 'Run' button instead!")