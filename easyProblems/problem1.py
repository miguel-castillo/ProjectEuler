endpoint = 999
firstMultiple = 3
secondMultiple = 5
sumOfMultiples = 0
sumOf3 = 0
for x in range(1000):
    if x % firstMultiple == 0 or x % secondMultiple == 0:
        sumOfMultiples += x

# The running time of the above code will take O(n)
# it can be made faster with the following code


def sum_of_multiples(n, m):
    num_of_multiples = m // n
    sum_multiples = n * num_of_multiples * (num_of_multiples + 1) // 2
    return sum_multiples


total_sum = sum_of_multiples(3, 999) + sum_of_multiples(5, 999) - sum_of_multiples(15, 999)
print(total_sum)

# The run time of the code above is O(1)
