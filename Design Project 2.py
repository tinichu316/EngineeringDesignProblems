#Develop a Madlib game

#repeatedly prompt player for certain verbs/nouns/adjectives
#finally, print the story.

#let's make it prompt the user for a couple of verbs, nouns, and adjectives, say 3 each.

import sys
import random

verbs = []
nouns = []
adjs = []

noVerbs = 0
noNouns = 0
noAdjs = 0

inp1 = input("How many verbs would you like to input?\n"
"Please enter 1-10. ")
    
inp2 = input("How many nouns would you like to input? ")

inp3 = input("How many adjectives would you like to input? ")

if inp1.isdigit() and inp2.isdigit() and inp3.isdigit():
    noVerbs = int(inp1)
    noNouns = int(inp2)
    noAdjs = int(inp3)
else:
    print("Those aren't numbers!")
    sys.exit()
    
    
for i in range(noVerbs):
    current = input("(%d/%d) Please enter a verb. " %(i + 1, noVerbs))
    verbs.append(current)
    
for i in range(noNouns):
    current = input("(%d/%d) Please enter a noun. " %(i + 1, noNouns))
    nouns.append(current)

for i in range(noAdjs):
    current = input("(%d/%d) Please enter an adjective. " %(i + 1, noAdjs))
    adjs.append(current)
    
def selectMainCharacter(): #selects one to be mentioned more than the others
    lucky = random.randrange(0, noNouns, 1)
    return nouns.pop(lucky)
    
def getNoun():
    lucky = random.randrange(0, noNouns - 1, 1)
    return nouns[lucky]

def getVerb():
    lucky = random.randrange(0, noVerbs, 1)
    return verbs[lucky]

def getAdj():
    lucky = random.randrange(0, noAdjs, 1)
    return adjs[lucky]

mainChar = selectMainCharacter()


#story has 3 noun, verb, and adjective slots.
story = """
Once upon a time, there was a %s who always %s %s pudding.
One day, %s showed up, went ahead and %s %s!
However, %s did not like that so %s %s the %s skating rink!
Now %s, %s went and %s %s instead.
""" %(mainChar, getVerb(), getAdj(),
      getNoun(), getVerb(), getNoun(),
      mainChar, mainChar, getVerb(), getAdj(),
      getAdj(), getNoun(), getVerb(), mainChar
      )

#Mainnoun, verb, adj, 
#noun, verb, noun, 
#Mainnoun, Mainnoun, verb, adj, 
#adj, noun, verb, Mainnoun

print("Er.. this seems wrong but... here's your story: \n", story)