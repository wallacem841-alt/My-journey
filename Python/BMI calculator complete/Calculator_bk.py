BMI_TABLE = [
    (0,    18.5, "thinness"),
    (18.5,  25,   "normal"),
    (25,    30,   "overweight"),
    (30,    35,   "obese_I"),
    (35,    40,   "obese_II"),
    (40,    float('inf'), "obese_III"),
]

'''weight_input = 75
height_input = 171'''


def number_treatment(weight_input, height_input):
    try:
        weight = int(weight_input)
        height = int(height_input) / 100
    except ValueError:
        return "nan"
    
    if height == 0 or weight == 0:
        return "0_division"
    
    return weight/(height**2)

'''bmi = number_treatment(weight_input, height_input)
print(bmi)'''

def bmi_category(bmi):
    if bmi < 0:
        return "negative"

    for low, high, label in BMI_TABLE:
        if low < bmi < high:
            return label

    return "unknown"

'''bmi = bmi_category(bmi)
print(bmi)'''