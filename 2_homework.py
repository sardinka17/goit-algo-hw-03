import random

def get_numbers_ticket(min, max, quantity):
    random_numbers = []
    if (min >= 1 and max <= 1000) and (quantity > 0 and quantity < max):
        numbers = list(range(min, max + 1))
        random_numbers = random.sample(numbers, quantity)
        random_numbers.sort()

    return random_numbers

print(f"Ваші лотерейні числа: {get_numbers_ticket(1, 1000, 7)}")