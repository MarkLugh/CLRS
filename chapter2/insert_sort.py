'''
Created on 2019年4月8日

@author: admin
'''


def insert_sort_asc(arr):
    if type(arr) != list:
        print("请输入int数组")
        return
        
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1       
        arr[j+1] = key 
       
    return arr


def insert_sort_desc(arr):
    if type(arr) != list:
        print("请输入int数组")
        return
        
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1       
        arr[j+1] = key 
       
    return arr 
        

def main():
    arr_list = [10,314,23,123,34,23,5,56,66,41,13,2,1]
    print("原始数组:"+str(arr_list))
    arr_asc = insert_sort_asc(arr_list)
    print("升序排列:"+str(arr_asc))
    arr_desc = insert_sort_desc(arr_list)
    print("降序排列:"+str(arr_desc))
    

if __name__ == '__main__':
    main()
