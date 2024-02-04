hours_i_worked = 50
my_regular_pay_rate = 15
my_overtime_rate = my_regular_pay_rate * 1.5
# print(my_regular_pay_rate, my_overtime_rate)
my_overtime_hours = hours_i_worked - 40
# print(40 * my_regular_pay_rate, my_overtime_hours * my_overtime_rate)
my_base_pay = 40 * my_regular_pay_rate
my_ot_pay = my_overtime_hours * my_overtime_rate

# print(my_base_pay + my_ot_pay)

hours_i_worked = 20
# my_regular_pay_rate = 15
what_is_overtime = 40

# if hours_i_worked > what_is_overtime:
#     print("you worked overtime")
# else:
#     print("you worked regular time")

hours_i_worked = 20
# my_regular_pay_rate = 15
what_is_overtime = 40

# if hours_i_worked > (7 * 24):
#     print("error")
# elif hours_i_worked > what_is_overtime:
#     print("worked overtime")
# else:
#     print("regular hours")

hours_i_worked = 20
# my_regular_pay_rate = 15
what_is_overtime = 40

if hours_i_worked > (7*24):
    print("error")
else:
    # print("value looks good")
    if hours_i_worked > what_is_overtime:
        print("worked overtime")
    else:
        print("regular time")