from frattlesnake import frattlesnake, Familiar

def main():
    frattlesnake.init()
    frattlesnake.login("onweb")

    fam = Familiar.mine()

    if fam is None:
        print("No active familiar")
        return

    print(f"\033[1m{fam.race} (named \"{fam.nickname}\")\033[0m")
    print("=======")
    print(f"Hatchling: {fam.hatchling.name}")
    print(f"Weight: {fam.weight}lbs")
    print(f"Experience: {fam.experience}")

    print("Also, for fun, your last encounter was " + frattlesnake.get("lastEncounter"))

main()