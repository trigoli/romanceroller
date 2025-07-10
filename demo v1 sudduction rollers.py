import json
import random
from typing import List, Union
""""

Created By Trigoli, For Dede, the goddes Of the nine moons, Breaker of Swords. Wetter then all Ever pretty, massive slut.

as an dungeon master,
I want to automate our romance mini-game,
to make it more accesslibe and record them the stats or follplay purpeces


As an dungeon master,
the I need to have the abbilty to quicky add new characters.
So that this use interchangeble between diffrent games

As an dungeon master.

first there is the sucuction check. DC calculated 12 +  STR + WEX + WIS + CHA Modifiers
DC is calulated By Defenders.
Attackers need to check if their traints are postive.
"""
#from operator import truediv
application_start =  True


# Banner message

banner_message =  (
    str("Made by Discord user trigoli also known as Josh"),
    str("wish to give credit to the dungeon master, Dede who has hosted game for me twice and who I"),
    str("Had the privalige of also being her Dungeon master")

)



# dice roller
def roll(dice):
    x = dice.lower()
    match x:
        case "d_six" | "d6":
            return random.randrange(1,6)
        case "d_eight" | "d8":
            return random.randrange(1,8)
        case "d_ten" | "d10":
            return random.randrange(1,10)
        case "d_twelve" | "d12":
            return random.randrange(1,12)
        case "d_twenty" | "d20":
            return random.randrange(1,20)
        case _:
            raise ValueError(f"{dice} Not an valid number of sided dice")







def sudduction_check_dc(abbility_s_str,abbility_s_dex,abbility_s_wis,abbility_s_cha):
    # this Fucntion both calculates the Ablility modifires of acharacter and adds it up as Dificulty Class
    base_dc = 12
    dc = abbility_s_str + abbility_s_dex + abbility_s_wis + abbility_s_cha + base_dc
    print(f"{dc}")


def sudduction_check(soother, crush: str) -> str:
    att = soother["id"]
    add = crush["id"]
    print(att)
    print(add)



def chr_info(playercharacters):
    for pc in playercharacters["player_characters"]:
        print()
        print(f"{pc['id']}: {pc['name']}")
        print(f"Acrobatics: {pc['acrobatics']}")
        print()


def ability_mod(score: int) -> int:
    #source
    """" player hand book
    “To determine an ability modifier without consulting the table,
    subtract10 from the ability score and then divide the result by 2 (round down).”

    this function has to be used to calculate the ability modifier out of Json too insure future proofing.
    """
    if not 1 <= score <= 30:
        raise ValueError("Ability score must be between 1 and 30.")
    return (score - 10) // 2


# script starts running from this point off.

print(banner_message)

while application_start:
    with open('Playerdatabase.json') as file:
        chr_data = json.load(file)

        """" chr_data stand for character data, when calling formation information, chr_data must be called."""
    print("Made by Discord user trigoli also known as Josh")
    print("wish to give credit to the dungeon master, Dede who has hosted game for me twice and who I")
    print("Had the privalige of also being her Dungeon master")
    print(f" the character options you have are TBT")
    print("You have four options, option 1: show list of characters ")
    print("You have four options, option 2: have romance")
    print("You have four options, option 3: see add characters to list")
    print("You have four options, option 6: to roll dice")
    print("You have four options, option 4: explain rules of Character romance, Brought to you by Dede")
    menu_optrion = input("Insert Option... :")
    if menu_optrion == "1":
        chr_info(chr_data)
    elif menu_optrion == "2":
        a = input("Insert ID attacker...")
        d = input("Insert Name defender...")
        sudduction_check(a,d)
    elif menu_optrion == "6":

        amount_of_dice = input("Insert Amount of dice..").lower()
        dice_roll = roll(amount_of_dice)
        print(dice_roll)


    else:
        print("You have entered wrong option")


    #attacker = input("input Charater who is engaining in romance")
    #defender = input("input target you wish to flirt with")
