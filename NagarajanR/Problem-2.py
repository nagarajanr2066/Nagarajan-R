def generate_series(a):
    series = []
    for i in range(1, a + 1):
        series.append(2 * i - 1)
    return series

# Example usage
print(generate_series(1))  # Output: [1]
print(generate_series(2))  # Output: [1, 3]
print(generate_series(3))  # Output: [1, 3, 5]
print(generate_series(4))  # Output: [1, 3, 5, 7]
