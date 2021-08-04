#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите
# соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.
revenue = int(input('Enter the received company`s revenue:'))
costs = int(input('Enter the value of the company`s costs:'))

if revenue > costs:
    print('Congratulations! The company operates with a profit!')
    profit = revenue - costs
    profitability = (profit / revenue) * 100
    print(f'Profitability of your company {profitability:.2f}%')

    employee_num = int(input('Enter the number of employees in the company:'))
    profit_rate = profit / employee_num
    print(f'The company`s profit per employee = {profit_rate:.2f}')
else:
    print('We are sorry, but your company is operating at a loss!')
