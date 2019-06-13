'''
python implement of search algorithms.
'''

def binary_search(data, find):
    '''
    binary search of a sorted list.
    '''
    start = 0
    stop = len(data)-1

    while(stop>=start):
        mid = int((start + stop)/2)
        if(find == data[mid]):
            print('the index is {}'.format(mid))
            break
        elif(find<data[mid]):
            stop = mid-1
        else:
            start = mid+1
    else:
        print('the data is not in the list.')