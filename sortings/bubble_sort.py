import random

def bubble_sort(array):

    for index, value in enumerate(array):

        if index + 1 == len(array):
            
            break
        
        if array[index + 1] < value:

            array.remove(value)
            array.insert(index + 2, value)
    
    
    last_num = array[0]

    for value in array[1:]:
        
        if value < last_num:

            return bubble_sort(array)
        
        last_num = value
    
    return array



if "__main__" == __name__:
    a = list(range(1, 10))
    random.shuffle(a)

    print(a)
    print(bubble_sort(a))