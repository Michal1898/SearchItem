import time
def search(lst,x):
    #start = time.time()
    for idx, item in enumerate(lst):
        if item == x:
            end = time.time()

            return idx
    return -1
def binary_search_iter(lst, x):
    #start_time = time.time()
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = int((start+end)/2)
        if lst[mid] == x:

            return mid
        if x > lst[mid]:
            start = mid + 1
        if x < lst[mid]:
            end = mid - 1
    return -1
def binary_search_rec(lst, key, start = 0, end = None):
    #start_time = time.time()
    if end == None:
        end = len(lst) - 1
    if start <= end:
        mid = int((start+end)/2)
        if lst[mid] == key:

            return key
        elif lst[mid] > key:
            return binary_search_rec(lst, key, start, mid - 1)
        else: #lst[mid] < key
            return binary_search_rec(lst, key, mid + 1, end)
    else: # key not found
        return -1
test_lst = range(100000000)#[2, 3, 4, 5, 10, 11, 40]
x = 9999999
start_time = time.time()
for a in range(100):
    result = search(test_lst,x)
print('Proste prochazeni cas: {} s'.format(time.time()-start_time))

# if result != -1:
#     print("Method 1: Element is present at index {}".format(result))
# else:
#     print("Method 1: Element is not present in array")
# Function call
start_time = time.time()
for a in range(100):
    result = binary_search_iter(test_lst, x)
print('Binarni vyhledavani iteraci: {} s'.format(time.time()-start_time))

# if result != -1:
#     print("Binarni vyhledavani iteraci: Element is present at index {}".format(result))
# else:
#     print("Method 2: Element is not present in array")
start_time = time.time()
for a in range(100):
    result = binary_search_rec(test_lst, x)
print('Binarni vyhledavani rekurzi: {} s'.format(time.time()-start_time))

# if result != -1:
#     print("Method 3: Element is present at index {}".format(result))
# else:
#     print("Method 3: Element is not present in array")
