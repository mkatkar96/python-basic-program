'''Data Structure-1.searchuing
                  2.sorting

                  definations
                  1.serching - serching is the process ofof finding desired elemnts in a set of items such as list ,array,
                  ,linkedlist,tree or graph.

                  2.sorting - array means arranging perticulaar collection of items in a perticular manner.


*searchin and its types*


1.Linear search -

pos = -1
def linearsearch(list,n):
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()["pos"] = i
            return True
    return False
list = [2,5,3,6,7,4]
print(list)
n = int(input("enter element you want to search fro list="))
if linearsearch(list,n):
    print("element fond at",pos+1)
else:
    print("not found")


2.binary search -

pos = -1
def search(list,n):
     l =0
     u =len(list)-1
     while l <= u:
         mid = (l+u) //2
         if list[mid] == n:
             globals()["pos"] = mid
             return True
         else:
             if list[mid] < n:
                 l = mid+1
             else:
                 u = mid
     return False
list = [1,2,3,4,5,6,7,8,9,99,123]
print(list)
n = int(input("enter element to be searched = "))
if search(list,n):
    print("element found at",pos+1)
else:
    print("elemnt not found")



*SORTING -


1.Bubble sort-

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [1,2,3,4,5,6,55,22,47,68,9,99,123]
sort(nums)
print(nums)


2.Selection sort-'''

def sort(nums):
    for i in range (len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


nums = [1, 2, 3, 4, 5, 6, 55, 22, 47, 68, 9, 99, 123]
sort(nums)
print(nums)