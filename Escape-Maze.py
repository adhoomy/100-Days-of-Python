# this code is the solution to the maze at:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == False:
    while right_is_clear() == True:
        turn_right()
        move()
    while right_is_clear() == False and front_is_clear() == False:
        turn_left()
    if front_is_clear() == True:
        move()