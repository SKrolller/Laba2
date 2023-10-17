def lim_max(nums, limit):
    max_val = 1  # устанавливаем максимальное значение как 1

    for num in nums:
        if num < limit and num > max_val:
            max_val = num

    return max_val

# Пример
nums = (10, 20, 30, 40, 50, 60, 70, 80, 100)
limit = 60  # ограничения
result = lim_max(nums, limit)
print(result)  # Выведет 50

def temp_cat(temp):
    if temp < -30:
        return 0  # Холодно
    elif temp < 0:
        return 1  # Прохладно
    elif temp < 15:
        return 2  # Зябко
    elif temp < 25:
        return 3  # Тепло
    else:
        return 4  # Жарко

# Примеры использования
temp1 = -30
temp2 = 10
temp3 = 30

print(temp_cat(temp1))
print(temp_cat(temp2))
print(temp_cat(temp3))

def del_rep(nums):
    # Удаляем дубликат
    unique_nums = set(nums)
    # Сортируем уникальные числа и возвращаем результат как перечень
    return sorted(list(unique_nums))
num = [1, 2, 1, 2, 3, 1, 2, 3, 4]
result = del_rep(num)
print(result)  # Выведет: [1, 2, 3, 4]

