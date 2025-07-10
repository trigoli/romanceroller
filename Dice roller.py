import random
from tabnanny import check

r_number = random.randrange(1,100)
print(r_number)




def roll(dice):
    match dice:
        case "d_six":
            return random.randrange(1,6)
        case "d_eight":
            return random.randrange(1,8)
        case "d_ten":
            return random.randrange(1,10)
        case "d_twelve":
            return random.randrange(1,12)
        case _:
            raise ValueError(f"{dice} Not an valid number of sided dice")



def romance_encounter(d, a):
    # for stats in d:
    print(d)
    print(a)





def assault_encounter(athletics_A):
    print(athletics_A)
    """"
    athletics_B =
    Acrobatics_B =
 
    """

