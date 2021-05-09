# Opening dialogue to determine which rate card is being used

def start():

    # Select rate card A or B
    print(" Are you using rate card A or rate card B?")
    rate_choice = input("> ")

    if rate_choice == "a":
        card_a()
    elif rate_choice == "b":
        card_b()
    else:
        print("\n Sorry, that's not one of the options. Please choose between rate card A or B.\n")
        start()


def card_a():

    # First let's calculate rate card 'A'

    #  Retrieve the variables

    pots = int(input(" How Many pots? "))
    chambers = int(input(" How Many chambers? "))
    cabinets = int(input(" How Many cabinets? "))
    road_trench = int(input(" How Many Meters of road trench? "))
    verge_trench = int(input(" How Many Meters of verge trench? "))

    # Confirm the numbers are correct

    print(f"\n So you have {pots} pots, \n {chambers} chambers, \n {cabinets} cabinets, \n {road_trench} meters of road trench \n and {verge_trench} meters of verge trench.\n")

    def card_a_rates(*args):
        cabinet_cost = cabinets * 1000
        pot_cost = pots * 100
        chamber_cost = chambers * 200
        road_trench_cost = road_trench * 100
        verge_trench_cost = verge_trench * 50
        return cabinet_cost + pot_cost + chamber_cost + road_trench_cost + verge_trench_cost

    print("\n Is this correct? Type y or n")
    a_totals = input("> ")

    if a_totals == "y":
        print(
            f"\n Using rate card A this will cost £{card_a_rates(pots, chambers, cabinets, road_trench, verge_trench)}.")
    else:
        print("\n Okay, let's get those numbers again.\n")
        start()


def card_b():

    # First let's calculate rate card 'B'

    #  Retrieve the variables

    pots = int(input(" How Many pots? "))

    # Add pot distances from the cabinet using a list of values

    pot_distance = [int(x) for x in input(
        "\n How far is each pot from the cabinet in metrers?\n Please separate each value with a space. ").split()]
    chambers = int(input(" How Many chambers? "))
    cabinets = int(input(" How Many cabinets? "))
    road_trench = int(input(" How Many Meters of road trench? "))
    verge_trench = int(input(" How Many Meters of verge trench? "))

    # Confirm the numbers are correct

    print(f"\n So you have {pots} pots, \n these pots are {pot_distance} meters away from the cabinet,\n {chambers} chambers, \n {cabinets} cabinets, \n {road_trench} meters of road trench \n and {verge_trench} meters of verge trench.\n")

    def card_b_rates(*args):
        cabinet_cost = cabinets * 1200
        pot_cost = sum(pot_distance) * 20
        chamber_cost = chambers * 200
        road_trench_cost = road_trench * 80
        verge_trench_cost = verge_trench * 40
        return cabinet_cost + pot_cost + chamber_cost + road_trench_cost + verge_trench_cost

    print(" Is this correct? Type y or n")
    b_totals = input("> ")

    if b_totals == "y":
        print(
            f"\n Using rate card B this will cost £{card_b_rates(pots, chambers, cabinets, road_trench, verge_trench)}.")
    else:
        print(" Okay, let's get those numbers again.\n")
        start()


start()
