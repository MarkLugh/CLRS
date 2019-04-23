# coding:utf-8
'''
Created on 2019年4月12日

@author: admin
'''

def merge():
	pass


def merge_sort_asc(arr_list, start, end, temp):
	pass


def merge_sort_desc(arr_list):
	pass


def main():
	arr_list = [10,314,23,123,34,23,5,56,66,41,13,2,1]
	print("原始数组:"+str(arr_list))
	temp = [len(arr_list)]
	arr_asc = merge_sort_asc(arr_list, 0, len(arr_list), temp)
	print("升序排列:"+str(arr_asc))
	arr_desc = merge_sort_desc(arr_list)
	print("降序排列:"+str(arr_desc))

if __name__ == '__main__':
	main()

