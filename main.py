def call_check (a):
    if a > 50 :
           return  (a - 50 ) * 2.5
    else:
        return 0
def sms_check (b):
    if b > 50 :
        return (b - 50) * 1.5
    else:
        return 0

a = int(input("Введите количество израсходованных минут \n"))
b = int(input("Введите количество израсходованных СМС - сообщений \n"))
base = 150
tax_911 = 4.4
print("Сумма базовой тарификации: " + str(base))
x = float(call_check(a))
y = float(sms_check(b))

if (x > 0) :
    print("Сумма дополнительной тарификации за минуты разговора: " + str(x))
if (y > 0) :
    print("Сумма дополнительной тарификации за СМС-сообщения: " + str(y))
tax = (base + tax_911 + x + y) * 5 / 100
sum = base + x + y + tax_911 + tax

print("Сумма отчислений колл центру: " + str(tax_911))
print("Сумма налога: " + str(round(tax,2)))
print("Общая сумма тарифа: " + str(round(sum,2)))