input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = {}
for div in divisors:
    count = 0
    for num in input_list:
        if num % div == 0:
            count += 1
    result[div] = count

print(result)
