# Introduction

These are a series of coding challenges given in an introductory Python programming course.

#### Challenge 1:
Design a function that calculates two-stage forward kinematics. The function takes four inputs, the length of the two arms, and the angle from one arm to the line of action of the other arm (or the ground).

#### Challenge 2:
Design a MadLibs game that prompts the user for various verbs, nouns, and adjectives.
The story is hard coded and does not vary on the amount of information placed in (although it is based on 3 of each verb, noun, and adjective).

As a bonus, each user defined word is randomly selected from the total number that they made (so technically they can enter as many words as they want).

Further, one of the nouns is repeated in an attempt to make the story seem more cohesive.

#### Challenge 3:
Design a function that determines the status of a nuclear power plant based on parameters such as temperature, radiation leak level, water leve, and tsunami height and then determine the appropriate responses based on a decision tree.

This challenge simply involves the use of if statements to determine the correct alert setting, then multiple if statements to determine the correct response.

The latter half of the code was designed as to prompt the user for an input each time a check, such as for electrical power, was requried. This in turn resulted in repeated lines of code in different function trees as the decision tree invovled initially responding in the same manner as a lower level alert. For example, the response to a red alert would be first to apply yellow alert response conditions.

This repetition could be removed by replacing the yellow alert and orange alert protocols with a function and then calling the appropriate function based on the user inputted alert level.
