import random


def get_numbers_ticket(start, end, quantity):
    random_numbers = []

    if (start >= 1 and end <= 1000) and (quantity > 0 and quantity < end) and (quantity <= end - start):
        numbers = list(range(start, end + 1))
        random_numbers = random.sample(numbers, quantity)
        random_numbers.sort()

    return random_numbers

print(f"Ваші лотерейні числа: {get_numbers_ticket(10, 14, 6)}")
