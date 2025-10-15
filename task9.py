numbers = [1, 2, 0, 0, 4, 5]

j = 0  # მაჩვენებელი, სადაც არა-ნულოვანი ელემენტი უნდა ჩავსვათ

# ეტაპი 1: გადავიტანოთ ყველა არა-ნულოვანი ელემენტი დასაწყისში
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[j] = numbers[i]
        j += 1

# ეტაპი 2: დარჩენილი ადგილები შევავსოთ 0-ებით
while j < len(numbers):
    numbers[j] = 0
    j += 1

print(f"შედეგი: {numbers}")
