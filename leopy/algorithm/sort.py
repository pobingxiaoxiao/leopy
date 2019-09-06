'''
collection of all sort algorithm.
'''

def select_sort(data):
    '''
    selection sort.
    O(n^2)
    '''
    data = list(data)
    result = []
    while(len(data)!=0):
        result.append(data.pop(__find_minimum_index(data)))
    return result
        
def quick_sort(array):
    '''
    quick sort.
    '''
    array = list(array)
    if(len(array)<2):
        return array
    else:
        base = array[0]
        smaller = [i for i in array[1:] if i<base]
        greater = [i for i in array[1:] if i>base]
        sorted = quick_sort(smaller)+ [base] + quick_sort(greater)
        return sorted

def __find_minimum_index(data):
    minimum = data[0]
    minimum_index = 0
    for index in range(len(data)):
        if data[index] < minimum:
            minimum = data[index]
            minimum_index = index
    return minimum_index

if __name__ == '__main__':
    unsorted = [1,4,3,8,2]
    sorted_data = select_sort(unsorted)
    print('unsorted data is', unsorted)
    print('sorted data is:',sorted_data)
