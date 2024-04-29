def print_space(n, l):
    space = n - l
    for i in range(space):
        print(" ", end="")

def print_stars(n):
    for i in range(n):
        print("* ", end="")
    print()

def generate_nums(n):
    length = 2 * n - 1
    nums = []
    for i in range(n):
        nums.append(i + 1)
    for i in range(n, length):
        nums.append(2 * n - i - 1)
    return nums

def main():
    n = 5
    nums = generate_nums(n)
    for num in nums:
        print_space(n, num)
        print_stars(num)

if __name__ == "__main__":
    main()
