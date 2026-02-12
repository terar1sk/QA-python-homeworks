def sum_numbers(s: str) -> int:
    try:
        nums = s.split(",")
        total = 0
        for n in nums:
            total += int(n)
        return total
    except ValueError:
        raise


data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


for item in data:
    try:
        print(sum_numbers(item))
    except ValueError:
        print("Не могу это сделать!")