import random

class Vietlott_Machine:
    def __init__(self, vietlott_model):
        self.vietlott_model = vietlott_model
        self.number = 0

    def vietlott_processing(self):       
        for i in self.vietlott_model:
            self.number += 1
            print(f"Option {self.number}: {i.name}")
        choice = int(input(f"Select options: 1 or 2\n"))
        self.vietlott_generate (choice)

    def vietlott_generate(self, choice):
        if choice == 1:
            selected_model = self.vietlott_model[0]
        elif choice == 2:
            selected_model = self.vietlott_model[1]
        else:
            print("Invalid choice. Please try again!")
            return
        generate_number = []
        for i in range(6):
            random_number = random.randint(1, selected_model.number)
            if random_number in generate_number:
                random_number = random.randint(1, selected_model.number)
            else:    
                generate_number.append(random_number)
        result = self.construct_string(generate_number)
        print(f"The suggested number for today is: {result}. Good luck!")

    def construct_string(self, number_list):
        result = ""
        for idx, val in enumerate(number_list):
            if idx == len(number_list) - 1:
                result += f"{val}"
            else:
                result += f"{val} - "
        return result
