x = 9
numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == x:
        # ნაპოვნია!
        print(f"პასუხი: {numbers[left]} და {numbers[right]}")
        break  # პასუხის პოვნის შემდეგ შეჩერება
    elif current_sum < x:
        left += 1  # საჭიროა უფრო დიდი რიცხვი
    else:  # current_sum > x
        right -= 1 # საჭიროა უფრო პატარა რიცხვი
