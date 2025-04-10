def adding_medals(row):
    "This function calculates the sum of all medals "
    "achieved by a country in a tournament and returns the total value."
    
    total_medals = row["Gold"] + row["Silver"] + row["Bronze"]
    return total_medals