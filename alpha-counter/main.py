def count_letters(word):
    """شمارش تعداد هر حرف در یک کلمه"""
    letter_count = {}

    for char in word.lower():
        if char.isalpha():  # فقط حروف الفبا
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count


# دریافت ورودی از کاربر
word = input("یک کلمه وارد کنید: ")
result = count_letters(word)

print(f"\nدیکشنری شمارش حروف کلمه '{word}':")
print(result)

# نمایش زیباتر
print("\nنمایش جزئیات:")
for letter, count in result.items():
    print(f"حرف '{letter}': {count} بار")