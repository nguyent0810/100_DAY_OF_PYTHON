from turtle_garden import Turtles
from race import Race
from data import colors, y_positions

new_race = Race()
turtles = Turtles().list_turtles(6)


user_bet = new_race.get_user_choice()
if user_bet:
    new_race.is_race_on = True
while new_race.is_race_on:
    new_race.race_processor(turtles, user_bet)