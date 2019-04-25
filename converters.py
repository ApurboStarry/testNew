def lbs_to_kg(weight):
    try:
        return int(weight) * 0.45
    except ValueError:
        print("Invalid Weight")


def kg_to_lbs(weight):
    try:
        return weight / 0.45
    except ValueError:
        print("Invalid Weight")



