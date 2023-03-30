ticket = int(input('введите количество билетов:\n'))
s = []
price = [0, 990, 1390]
for i in range(1, ticket + 1):
    age = int(input('введите возраст:\n'))
    if age < 18:
        s.append(price[0])
    elif 18 < age < 25:
        s.append(price[1])
    else:
        s.append(price[2])
if ticket > 3:
    s = sum(s) - sum(s) * 0.1
    print('Общая сумма к оплате: ', int(s))
else:
    print('Общая сумма к оплате: ', sum(s))
