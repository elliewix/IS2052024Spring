hours_i_worked = 10
my_pay_rate = 15

# generally, we would try this first
# but not dealing with overtime stuff

my_weekly_pay = hours_i_worked * my_pay_rate

# print(my_weekly_pay)

# let's add some logic to deal with overtime

# dealing with hours
what_is_overtime = 40
hours_i_worked = 50
my_overtime_hours = hours_i_worked - what_is_overtime
# not bad, but will always have the value of what_is_overtime
my_base_hours = hours_i_worked - my_overtime_hours
# dealing with pay
my_pay_rate = 15
my_overtime_rate = my_pay_rate * 1.5

# let's just get some math going, presuming that OT is happening
# base_pay = my_base_hours * my_pay_rate
# ot_pay = my_overtime_hours * my_overtime_rate
# print(base_pay, ot_pay, base_pay + ot_pay)

# print(my_overtime_rate)

# prev one presumed ot was happening, lets add logic
# to automatically adjust

what_is_overtime = 40
hours_i_worked = 20
# this will work, but it's not checking other stuff
# if hours_i_worked > what_is_overtime:
#     print("you worked overtime!")
# else:
#     print("You worked regular time")

what_is_overtime = 40
hours_i_worked = 10000

if hours_i_worked > (7 * 24):
    print("error")
elif hours_i_worked > what_is_overtime:
    print("you worked overtime")
else:
    print("you worked regular time")