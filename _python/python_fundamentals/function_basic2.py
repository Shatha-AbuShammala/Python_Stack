#countdown 
def countdown(num):
    return list(range(num, -1, -1))

#print and return 
def print_and_return(lst):
    print(lst[0])
    return lst[1]

#First Plus Length
def first_plus_length(lst):
    return lst[0] + len(lst)

#Values Greater than Second
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False

    new_list = []
    for val in lst:
        if val > lst[1]:
            new_list.append(val)

    print(len(new_list))
    return new_list

#length and value 
def length_and_value(size, value):
    return [value] * size


print(countdown(5))
print(print_and_return([1, 2]))
print(first_plus_length([1,2,3,4,5]))
print(values_greater_than_second([5,2,3,2,1,4]))
print(length_and_value(4, 7))