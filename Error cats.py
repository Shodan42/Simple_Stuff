def howManyCats():
    # validation Loop
    while True:
        try:
            numCats = int(input('How manny cats do you have?: '))
            # Positive int check
            if numCats < 0:
                print('That is not a valid number')
                continue
            return numCats

        # int check
        except ValueError:
            print('That is not a Number please Try Again')


# determines if the amount of cats is too damm high
def isItTooMany(cats):
    if cats >= 4:
        print(f'{cats}!!! thats alot of cats')
    else:
        print('not that many cats')


isItTooMany(howManyCats())
