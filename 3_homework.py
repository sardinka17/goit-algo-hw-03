import re

def normalize_phone(phone_number):
    pattern = r"[^\d]"
    replacement = ""
    normalized_phone = re.sub(pattern, replacement, phone_number)

    pattern = r"^(380|80|0)"
    replacement = "+380"
    normalized_phone = re.sub(pattern, replacement, normalized_phone)

    if normalized_phone.startswith("+") == False:
        normalized_phone = f"+{normalized_phone}"
    
    return normalized_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "972545379039",
    "+972545379039"
]

print(f"{raw_numbers}")

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(f"\nНормалізовані номери телефонів для SMS-розсилки:{sanitized_numbers}\n")