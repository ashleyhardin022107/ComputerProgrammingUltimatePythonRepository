def make_abc():
    result = ["a", "b", "c"]
    return result

print("make_abc: ")
print(make_abc())


def equal_edges(items):
    first = items[0]
    last = items[-1]

    if first == last:
        return True
    else:
        return False

print("equal_edges: ")  
print([1, 5, 7, 1], equal_edges([1, 5, 7, 1]))
print([2, 4, 6, 8], equal_edges([2, 4, 6, 8]))


def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    middle1 = list1[1]
    middle2 = list2[1]
    last1 = list1 [2]
    last2 = list2[2]
    
    if first1 == first2 or first1 == last2 or first2 == first1 or first2 == last1:
        return True
    else:
        return False

print("common_edge: ")
print([1, 2, 3], [1, 3, 2], common_edge([1, 2, 3] , [1, 3, 2]))
print([2, 4, 6], [4, 5, 6], common_edge([2, 4, 6] , [4, 5, 6]))
print([1, 2, 3], [4, 5, 6], common_edge([1, 2, 3] , [4, 5, 6]))


def all_the_same(list):
    first = list[0]
    middle = list[1]
    last = list[2]
    
    if first == middle and first == last and middle == last:
        return True
    else:
        return False

print("all_the_same: ")
print([1, 2, 3], all_the_same([1, 2, 3]))
print([5, 5, 5], all_the_same([5, 5, 5]))


def all_unique(list):
    first = list[0]
    middle = list[1]
    last = list[2]
    
    if first == middle or first == last or middle == last:
        return False
    else:
        return True

print("all_unique: ")
print([1, 2, 3], all_unique([1, 2, 3]))
print([5, 5, 5], all_unique([5, 5, 5]))
print([1, 1, 3], all_unique([1, 1, 3]))


def increasing(list):
    first = list[0]
    middle = list[1]
    last = list[2]
    
    if last > middle and middle > first:
        return True
    else:
        return False

print("increasing: ")
print([1, 2, 3], increasing([1, 2, 3]))
print([3, 2, 1], increasing([3, 2, 1]))


def all_true(list):
    if list[0] == True and list[1] == True and list[2] == True:
        return True
    else:
        return False

print("all_true: ")
print([True, True, False], all_true([True, True, False]))


def mostly_true(list):
    if list[0] == True and list[1] == True or list[0] == True and list[2] == True or list[1] == True and list[2] == True:
        return True
    else:
        return False

print("mostly_true: ")
print([True, False, True], mostly_true([True, False, True]))
print([False, False, False], mostly_true([False, False, False]))

