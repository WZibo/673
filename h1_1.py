def mul_table():

    # Print column header
    print("\t", end='')
    for n in range(1, 13):
        print(f"{n}\t", end='')
    print()

    # Print multiplication table
    for n in range(1, 13):
        # Print line header
        print(f"{n}\t", end='')
        for m in range(1, 13):
            print(f"{n*m}\t", end='')
        print()


mul_table()
