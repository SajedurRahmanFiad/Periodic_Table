###############################################################
# IMPORTS
###############################################################

import random
import periodic_table as pt




###############################################################
# INITIALIZE VARIABLES
###############################################################

Name, Number, Mass = {}, {}, {}

for element in pt.ELEMENTS_DATA:
    Name[element] = pt.ELEMENTS_DATA[str(element)]["name"]
for element in pt.ELEMENTS_DATA:
    Mass[element] = pt.ELEMENTS_DATA[str(element)]["atomic-mass"]
for i in range(1, 119):
    Number[i] = list(Name.values())[i-1]




###############################################################
# FUNCTIONS
###############################################################

def GenerateQuiz():
    pattern = random.choice([0, 1])
    ques_symb, ques_name = None, None
    
    if pattern == 1:
        ques_symb = random.choice(list(Name.keys()))
        ans = input("\nWhat is the name of the element " + ques_symb + "?\nAnswer: ")

        if ans.strip().capitalize() == list(Name.values())[list(Name.keys()).index(ques_symb)]:
            print(" Congrats!")
        else:
            print(" Failed!")

    elif pattern == 0:
        ques_name = random.choice(list(Name.values()))
        ans = input("\nWhat is the symbol of " + ques_name + "?\nAnswer: ")

        if ans.strip().capitalize() == list(Name.keys())[list(Name.values()).index(ques_name)]:
            print(" Congrats!")
        else:
            print(" Failed!")


def Ask(times):
    for _ in range(times):
        GenerateQuiz()




###############################################################
# MAIN
###############################################################

Ask(2)
