money_capital: int = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = -1  # Так как последняя итерация будет для money_capital<0
while money_capital >= 0:
    money_capital += salary
    money_capital -= spend
    spend *= (1 + increase)
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
