
# Given an array containing None values fill in the None values with most recent non none value
# non None value in the array 
array1 = [1,None,2,3,None,None,5,None]

def solution(array):
    cached = 0            #stores latest value of not none
    appendedArray = []    #stores new list values that is appended after iteration and if else checking
    for i in nums: 
        if i is not None:    
            appendedArray.append(i)
            cached = i
        else:
            appendedArray.append(cached)
    return appendedArray

solution(array1)
