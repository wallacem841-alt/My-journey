User_n = input('Give me an integer: ')

# Try to convert the input to an integer
try:
    User_n = int(User_n)
except ValueError:
    print("Not an integer, dummy")
else:
    Odd_even = User_n % 2

    if User_n < 0 and Odd_even == 0:
        print('This integer is negative and even')
    elif User_n < 0 and Odd_even == 1:
        print('This integer is negative and odd')
    elif User_n >= 0 and Odd_even == 1:
        print('This integer is positive and odd')
    elif User_n >= 0 and Odd_even == 0:
        print('This integer is positive and even')
    else:
        print('WTF did you do?')

# Get user input for height and weight
User_height = input('Give me your height(cm): ')

User_weight = input('Give me your weight(Kg): ')

try:
    # Convert inputs to floats
    User_height = float(User_height)
    User_weight = float(User_weight)
except ValueError:
    print('not a number, dummy')
else:
    # Convert height from cm to meters
    User_height = User_height / 100

    # Calculate BMI
    bmi = User_weight / (User_height**2)

    # Determine BMI category and print appropriate message
    if bmi < 16 and bmi >= 0:
        print('Severe Thinness, You better go around with some weights or you gon go flying')
    elif bmi == 16:
        print('Moderate Thinness, fuuu! did you went flying?')
    elif bmi > 16 and bmi <= 18.5:
        print('Mild Thinness, better hold onto something or you might blow away!')
    elif bmi > 18.5 and bmi <= 25:
        print('Normal, enjoy it while it lasts, you doornob')
    elif bmi > 25 and bmi <= 30:
        print('Overweight, time to back away from the buffet! Slowly fatso')
    elif bmi > 30 and bmi <= 35:
        print("Obese Class I, the scale called and said 'one at a time, please!'")
    elif bmi > 35 and bmi <= 40:
        print("Obese Class II, when's the last time you saw your toes?")
    elif bmi > 40:
        print("Obese Class III, My 600-lb Life called, they've found their next contendent")
    else:
        print("you've put a negative number didn't you? dum dum")


'''Classification	BMI range - kg/m2
Severe Thinness	< 16
Moderate Thinness	16 - 17
Mild Thinness	17 - 18.5
Normal	18.5 - 25
Overweight	25 - 30
Obese Class I	30 - 35
Obese Class II	35 - 40
Obese Class III	> 40'''