import json
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
from operator import truediv
application_start =  True



def sudduction_check_dc(abbility_s_str,abbility_s_dex,abbility_s_wis,abbility_s_cha):
    # this Fucntion both calculates the Ablility modifires of acharacter and adds it up as Dificulty Class
    base_DC = 12
    DC = abbility_s_str + abbility_s_dex + abbility_s_wis + abbility_s_cha + base_DC
    print(f"{DC}")

def sudduction_check(attacker,defender):


def chr_info(x):



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
while application_start:
    with open('Playerdatabase.json') as file:
        chr_data = json.load(file)
        """" chr_data stand for character data, when calling formation information, chr_data must be called."""

    print("Made by Discord user trigoli also known as Josh")
    print("wish to give credit to the dungeon master, Dede who has hosted game for me twice and who I")
    print("Had the privalige of also being her Dungeon master")
    print(f" the character options you have are {chr_data}")
    attacker = input("input Charater who is engaining in romance")
    defender = input("input target you wish to flirt with")
