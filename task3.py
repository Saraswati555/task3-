'''#Question 1
num_list = [10,501,22,37,100,999,87,351]
even_num = list(filter(lambda x : x %2 == 0 ,num_list))
odd_num = list(filter(lambda x : x % 2 != 0 , num_list))
print("even number :" ,even_num)
print("odd number :" ,odd_num)

#Question 2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
        return True
        
num_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_list = [num for num in num_list if is_prime(num)]
print("prime List:",prime_list)
print("length:",len(prime_list))

#Question 3
def is_happy(num):
    seen = set()
    while num!=0 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
        return num == 1

num_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_num = list(filter(lambda x : is_happy(x), num_list))
print(happy_num)
print(len(happy_num))

#Question 4
def sum_of(num):
    num_str = str(num)
    return int(num_str[0]) + int(num_str[-1])
print(sum_of(2468))

#Question 6
def find_duplicate(list1 , list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    return list(set1 & set2 & set3)
print(find_duplicate([1,2,3,4,5],[4,5,6,7],[5,6,8,2]))

#Question 7
def non_repeating(nums):
    non_repeat = filter(lambda x : nums.count(x) ==1 , nums )
    return next(non_repeat,None)
print(non_repeating([2,3,3,4,4,3,6,6,5,4,3,2,5,11]))

#Question 8
def find_min(nums):
    if not nums:
        return none
    return min(nums)
print(find_min([4,5,6,7,0,1,2]))

#Question 9
def find_triplet(lst , sum_list):
    n = len(lst)
    for i in range(n):
        for j in range(i+1 , n):
            for k in range(j+1 , n):
                if lst[i] + lst[j] + lst[k] == sum_list:
                    return lst[i] , lst[j] , lst[k]
                return None
print(find_triplet([10, 20, 30, 9] , 59))'''

#Question 10
def sublist_sum(lst):
    for i in range(len(lst)):
        for j in range(i+1 , len(lst)+1):
            sublist = lst[i:j]
            if sum(sublist) == 0:
                return sublist
    return None
print(sublist_sum([4, 2, -3, 1, 6]))