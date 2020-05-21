'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr: list):
    # store tallies in dict object
    counts: dict = {}
    # increment tallies
    for i in arr:
        counts[i] = counts.get(i, 0) + 1
    # return single ton 
    for v in counts:
        if counts[v] == 1:
            return v

    print(counts) 



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")