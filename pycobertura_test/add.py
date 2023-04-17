def add(a, b):
    return a + b


def badNameing():
    BadVariable = 1
    return BadVariable

def not_covered_function_in_main_branch():
    return

def is_even(i: int):
    return i//2 == 0

def is_fruit(s: str):
    """
    A multiline uncovered feature
    """
    if s == "orange":
        return True
    if s == "grape":
        return True
    if s == "apple":
        return True
