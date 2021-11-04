def flatten_array(arr):
    '''Takes in a 3 dimensional array
        and returns a flattened array 
        taking the first element of each
        array followed by the second and the third.
        [[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]] => [a1,b1,c1,a2,b2,c2,a3,b3,c3]]
    '''
    
    flattened_array = []
    # set the array length to the length of the first inner array
    arr_len = len(arr[0])
    # check to make sure it is a 3d array
    if len(arr) < 3:
        print("Please pass in a 3 dimensional array with equal lengths.")
    # check to see if all internal arrays are of the same length
    elif any(len(lst) != arr_len for lst in arr[1:]):
        print("Please make sure that the inner arrays are the same lengths.")
    else:
        a = arr[0]
        b = arr[1]
        c = arr[2]
        # iterate and append the first value from each inner array
        for i in range(arr_len):
            flattened_array.append(a[i])
            flattened_array.append(b[i])
            flattened_array.append(c[i])
        print(flattened_array)
        return flattened_array


flatten_array([[0,1,2],[3,4,5],[6,7,8]])