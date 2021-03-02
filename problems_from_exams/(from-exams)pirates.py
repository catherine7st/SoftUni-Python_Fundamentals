command = input()
my_gold = 0
killed_citizens = 0
cities = []

while not command == 'Sail':
    command = input()

    target_city, population, target_gold = command.split("||")



    if command == 'Sail':
        command_2 = input()

        while not command_2 == 'End':
            events = command_2.split("=>")

            if events[0] == 'Plunder':
                if events[2] or events[3] == 0:
                    print(f"{events[1]} has been wiped off the map!")
                    continue
                else:
                    cities.append(events[1])
                    killed_citizens += events[2]
                    my_gold += events[3]
                    print(f"{events[1]} plundered! {events[3]} gold stolen, {events[2]} citizens killed.")
            elif events[0] == 'Prosper':
                town = events[1]
                gold = int(events[2])

                if gold < 0:
                    print("Gold added cannot be a negative number!")
                else:





            command_2 = input()

