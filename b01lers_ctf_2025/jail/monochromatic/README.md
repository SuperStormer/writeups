JUMP\_\* opodes don't check bounds, so you can jump out of bounds to a bytecode gadget. `find_gadgets.py` finds gadgets that allow you to call `exec(input())` given the appropriate co_names.
