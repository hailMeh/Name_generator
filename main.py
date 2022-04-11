import random
import sys

name_list = ['John', 'Peter', 'David', 'Max', 'Alfred', 'Jack', 'James', 'Robert', 'Kirk', 'Woody']
surname_list = ['Addison', 'Armstrong', 'Bell', 'Carter', 'Clarke', 'Hall', 'Mason', 'Oxley', 'Quimby', 'Walsh']
print('Hello, It\'s name generator!')


def name_generator(list_of_names, list_of_surnames):
    random_name = random.choice(list_of_names)
    random_surname = random.choice(list_of_surnames)
    user_choice = input(
        'if you want to create a random name and surname: \n write - make \n if you want to quit: \n write - exit\n')
    if user_choice == 'make':
        print("\nGenerated - {} {}\n".format(random_name, random_surname), file=sys.stderr)
        name_generator(list_of_names, list_of_surnames)
    elif user_choice == 'exit':
        print('See you soon!')
        exit()
    elif user_choice != 'exit' and user_choice != 'make':
        print('Your word is not make or exit to continue, try again ')
        name_generator(list_of_names, list_of_surnames)


name_generator(name_list, surname_list)
