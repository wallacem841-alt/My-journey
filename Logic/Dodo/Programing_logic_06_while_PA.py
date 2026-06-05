import random

tentativas = 10
senha = random.randint(1, 100)

while tentativas > 0:
    tentativas -= 1

    shot = int(input('Give me a number from 1 to 100: '))

    if shot == senha:
        print(f"You've got it right! The number was {senha}.")
        break
    elif shot > senha:
        print(f'Missed, too high. You have {tentativas} tries left.')
    else:
        print(f'Missed, too low. You have {tentativas} tries left.')

else:
    print(f"You've failed, you reached {tentativas} tries. The right number was {senha}.")