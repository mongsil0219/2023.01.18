my_name = "sunwoo"
my_age = 24
my_color_eyes = "brown"

print(f"Hello I'm {my_name},I have {my_age} in the earth,{my_color_eyes} is my eye color,")


def make_juice(fruit):
    return f"{fruit}+cup"

def add_ice(juice):
    return f"{juice}+ice"

def add_sugar(iced_juice):
    return f"{iced_juice}+sugar"

juice = make_juice("apple")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

