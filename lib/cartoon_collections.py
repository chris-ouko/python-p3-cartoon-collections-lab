def roll_call_dwarves(dwarf_names):
    for index, name in enumerate(dwarf_names):
        print(f"{index + 1}. {name}")

def summon_captain_planet(planeteer_calls):
    return [f"{call.capitalize()}!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        pass
        if snack in cheeses:
            return snack
    return None