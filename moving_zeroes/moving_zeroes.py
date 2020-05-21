'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr: list):
	# since beginning must be non zero, we 
    index: int = 0
    # iterate thru list, if we find a non zero element
    # we swap it to index, which is the beginning then increment index
    for i in range(len(arr)):
    	elem = arr[i]
    	if elem != 0:
    		arr[i], arr[index] = arr[index], arr[i]
    		index += 1 


    return arr 

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]
    # [0, 3, 1, 0, -2]
    

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")