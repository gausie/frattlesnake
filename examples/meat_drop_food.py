from frattlesnake import frattlesnake, Item, Modifier

def main():
    frattlesnake.login("onweb")

    base_meat = 250

    meat_drop_food = [
       item
       for item in Item.all()
       if item.effect and item.effect.modifier(Modifier.MeatDrop, 0) > 0 and item.fullness is not None
    ]

    for item in meat_drop_food:
        effective = item.effect.modifier(Modifier.MeatDrop) * item.modifier(Modifier.EffectDuration)
        print(f"{item.name} is worth {effective * base_meat}")
        print(f"{item.price()} for 1, {item.price(quantity=5)} for 5")

main()
