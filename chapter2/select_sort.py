'''
Created on 2019年4月8日

@author: admin
'''


def select_sort_asc(arr):
    """ 选择排序 升序排列 """
    for i in range(len(arr)):
        key = arr[i]
        for j in range(i + 1, len(arr)):
            if key > arr[j]:
                key, arr[j] = arr[j], key
        arr[i] = key
    return arr


def select_sort_desc(arr):
    """ 选择排序 降序排列 """
    for i in range(len(arr)):
        key = arr[i]
        for j in range(i + 1, len(arr)):
            if key < arr[j]:
                key, arr[j] = arr[j], key
        arr[i] = key
    return arr


def main():
    arr_list = [10,34,213,23,4,3,5,56,66,41,13,2,11]
    print("原始数组:"+str(arr_list))
    arr_asc = select_sort_asc(arr_list)
    print("升序排列:"+str(arr_asc))
    arr_desc = select_sort_desc(arr_list)
    print("降序排列:"+str(arr_desc))
    

if __name__ == '__main__':
    main()