fibonacci_num = [1, 1]

# First 100 elements
for i in range(2, 100):
    # The next number is the sum of the previous two numbers
    next_fibonacci = fibonacci_num[i-1] + fibonacci_num[i-2]
    fibonacci_num.append(next_fibonacci)


for i in range(0, 100, 5):
    print(fibonacci_num[i:i+5])
