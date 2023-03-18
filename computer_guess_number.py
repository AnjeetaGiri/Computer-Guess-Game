import random
def computer_guess(n):
    low=1
    high=n
    feedback=''
    while feedback!="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} is too high(h),too low(l) or correct(c)")
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"We have guessed the number correctly:{guess}") 
computer_guess(20)           









