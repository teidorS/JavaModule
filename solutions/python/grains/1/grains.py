# 1 => 1; 2 => 2; 3 => 4; 4 => 8
# 1 * 2 

TOTAL_SQAURES = 64

def square(number):
    if 1 <= number <= TOTAL_SQAURES:
        if number == 1:
            return 1
        return 2 ** (number - 1)
    else:
        raise ValueError(f"square must be between 1 and {TOTAL_SQAURES}")
    
        


def total():
    sum = 0
    for i in range(2, TOTAL_SQAURES + 1):
        sum += 2 ** (i - 1)
    return sum + 1
