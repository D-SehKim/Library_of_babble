import random

def main():
    seed_input = random.randrange(1,1000)
    print(create_random_seed(seed_input))

def create_random_seed(seed_input):
    '''
    Takes any number as seed input and creates a seed based on the input given, 
    hypothetically no two seeds can be alike
    '''
    random.seed(seed_input)
    return random.random()


if __name__ == "__main__":
    main()