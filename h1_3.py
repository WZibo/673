def combine(l1, l2):
    combined_l = []

    min_l = min(len(l1), len(l2))

    # Alternately add elements to a new list
    for i in range(min_l):
        combined_l.append(l1[i])
        combined_l.append(l2[i])

    return combined_l


# Input array, remove redundant [ and ]
user_input1 = input("Enter first list: ").strip('[]')
user_input2 = input("Enter second list: ").strip('[]')


# Convert string to list
list1 = user_input1.split(",")
list2 = user_input2.split(",")

# Merge lists and print results
if len(list1) == len(list2):
    result = combine(list1, list2)
    print(result)
else:
    print("Error, both lists should be equal length!")
