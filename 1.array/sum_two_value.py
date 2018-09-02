def find_sum_of_two(A, val):
    hash_table = set()
    for i in A:
        if val - i in hash_table:
            return True
        hash_table.add(i)
    return False


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [55,23,26,2,18,78,23,8,2,3]
    qq = find_sum_of_two(a, 11)
    print(b)

if __name__ == "__main__":
    main()