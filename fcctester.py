def apply_discount(price, discount):
    if type(price) != int and type(price) != float:
        return f"The price should be a number"
    if price <= 0:
        return f"The price should be greater than 0"
    else:
        pass
    if type(discount) != int and type(discount) != float:
        return f"The discount should be a number"
    if discount not in range(0, 100):
        return f"The discount should be between 0 and 100"
    else:
        discount /= 100
    price = price - (price * discount)
    return price

print(apply_discount(200, 50))
        

full_dot = '●'
empty_dot = '○'



def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) < 1:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if ' ' in name:
        return "The character name should not contain spaces"
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if strength + intelligence + charisma > 7:
        return "The character should start with 7 points"
    return f"{name} STR {full_dot * (strength)}{empty_dot * (10 - strength)}\n INT {full_dot * (intelligence)}{empty_dot * (10 - intelligence)}\n CHA {full_dot * (charisma)}{empty_dot * (10 - charisma)}"

print(create_character('david', "", 3, 4))
print(create_character('david', 0, 3, 4))
print(create_character('david', 1, 3, 5))
