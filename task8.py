x = 7
numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1
count = 0  # მრიცხველი

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == x:
        count += 1    # ვიპოვეთ წყვილი, გავზარდოთ მრიცხველი
        left += 1     # გადავდივართ შემდეგ წყვილზე
        right -= 1    # გადავდივართ შემდეგ წყვილზე
    elif current_sum < x:
        left += 1     # საჭიროა უფრო დიდი რიცხვი
    else:  # current_sum > x
        right -= 1    # საჭიროა უფრო პატარა რიცხვი

print(f"წყვილების რაოდენობა: {count}")
