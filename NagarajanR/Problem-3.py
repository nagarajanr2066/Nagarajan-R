def generate_series(a):
    series = []
    for i in range(1, a + 1):
        if i % 2 == 1:
            series.append(i)
    return series

# Example usage
print(generate_series(1))  # Output: [1]
print(generate_series(2))  # Output: [1]
print(generate_series(3))  # Output: [1, 3]
print(generate_series(4))  # Output: [1, 3]
print(generate_series(5))  # Output: [1, 3, 5]
print(generate_series(6))  # Output: [1, 3, 5]
