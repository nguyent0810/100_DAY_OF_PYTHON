from data import vietlott_data
from vietlott_model import Vietlott_Model
from vietlott_machine import Vietlott_Machine
# Guess the Vietlott
vietlott_type = []

for v in vietlott_data:
    vietlott_type.append(Vietlott_Model(v["name"], v["number"]))

vietlott_machine = Vietlott_Machine(vietlott_type)
vietlott_machine.vietlott_processing()
