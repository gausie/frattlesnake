from frattlesnake import Item, ModifierType

def main():
    meat_drop_food = [
       item
       for item in Item.all()
       if item.effect and any(m.type == ModifierType.MeatDrop for m in item.effect.modifiers) and item.fullness is not None
    ]

    for item in meat_drop_food:
        print(item.name)

main()
