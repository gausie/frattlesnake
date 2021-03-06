from typing import Any
from enum import Enum

class Modifier(Enum):
    AbsorbAdventures = "Absorb Adventures"
    AbsorbStats = "Absorb Stats"
    AccessoryDrop = "Accessory Drop"
    AdditionalSong = "Additional Song"
    Adventures = "Adventures"
    AdventureUnderwater = "Adventure Underwater"
    AttacksCanTMiss = "Attacks Can't Miss"
    Avatar = "Avatar"
    BaseRestingHp = "Base Resting HP"
    BaseRestingMp = "Base Resting MP"
    BonusRestingHp = "Bonus Resting HP"
    BonusRestingMp = "Bonus Resting MP"
    BoozeDrop = "Booze Drop"
    Breakable = "Breakable"
    Brimstone = "Brimstone"
    CandyDrop = "Candy Drop"
    Class = "Class"
    Cloathing = "Cloathing"
    Clowniness = "Clowniness"
    ColdDamage = "Cold Damage"
    ColdImmunity = "Cold Immunity"
    ColdResistance = "Cold Resistance"
    ColdSpellDamage = "Cold Spell Damage"
    ColdVulnerability = "Cold Vulnerability"
    CombatRate = "Combat Rate"
    CombatRateUnderwater = "Combat Rate (Underwater)"
    CrimbotOutfitPower = "Crimbot Outfit Power"
    CriticalHit = "Critical Hit"
    CriticalHitPercent = "Critical Hit Percent"
    DamageAbsorption = "Damage Absorption"
    DamageReduction = "Damage Reduction"
    DbCombatDamage = "DB Combat Damage"
    DiscoStyle = "Disco Style"
    DrippyDamage = "Drippy Damage"
    DrippyResistance = "Drippy Resistance"
    DropsItems = "Drops Items"
    DropsMeat = "Drops Meat"
    Effect = "Effect"
    EffectDuration = "Effect Duration"
    Equalize = "Equalize"
    EquipsOn = "Equips On"
    Experience = "Experience"
    ExperienceMuscle = "Experience (Muscle)"
    ExperienceMysticality = "Experience (Mysticality)"
    ExperienceMoxie = "Experience (Moxie)"
    ExperiencePercentMuscle = "Experience Percent (Muscle)"
    ExperiencePercentMysticality = "Experience Percent (Mysticality)"
    ExperiencePercentMoxie = "Experience Percent (Moxie)"
    ExperienceFamiliar = "Experience (familiar)"
    Fairy = "Fairy"
    FamiliarDamage = "Familiar Damage"
    FamiliarEffect = "Familiar Effect"
    FamiliarTuningMysticality = "Familiar Tuning (Mysticality)"
    FamiliarTuningMoxie = "Familiar Tuning (Moxie)"
    FamiliarTuningMuscle = "Familiar Tuning (Muscle)"
    FamiliarWeightHidden = "Familiar Weight (hidden)"
    FamiliarWeight = "Familiar Weight"
    FishingSkill = "Fishing Skill"
    FloorBuffedMoxie = "Floor Buffed Moxie"
    FloorBuffedMuscle = "Floor Buffed Muscle"
    FoodDrop = "Food Drop"
    FourSongs = "Four Songs"
    FreePull = "Free Pull"
    Fumble = "Fumble"
    GearDrop = "Gear Drop"
    Generic = "Generic"
    HatDrop = "Hat Drop"
    HoboPower = "Hobo Power"
    HotDamage = "Hot Damage"
    HotImmunity = "Hot Immunity"
    HotResistance = "Hot Resistance"
    HotSpellDamage = "Hot Spell Damage"
    HotVulnerability = "Hot Vulnerability"
    HpRegenMax = "HP Regen Max"
    HpRegenMin = "HP Regen Min"
    Initiative = "Initiative"
    InitiativePenalty = "Initiative Penalty"
    ItemDrop = "Item Drop"
    ItemDropSporadic = "Item Drop (sporadic)"
    ItemDropPenalty = "Item Drop Penalty"
    Jiggle = "Jiggle"
    KruegerandDrop = "Kruegerand Drop"
    LastsUntilRollover = "Lasts Until Rollover"
    Leprechaun = "Leprechaun"
    LookLikeAPirate = "Look like a Pirate"
    Luck = "Luck"
    ManaCost = "Mana Cost"
    ManaCostCombat = "Mana Cost (combat)"
    MaximumHooch = "Maximum Hooch"
    MaximumHp = "Maximum HP"
    MaximumHpPercent = "Maximum HP Percent"
    MaximumMp = "Maximum MP"
    MaximumMpPercent = "Maximum MP Percent"
    MaximumPP = "Maximum PP"
    MeatBonus = "Meat Bonus"
    MeatDrop = "Meat Drop"
    MeatDropSporadic = "Meat Drop (sporadic)"
    MeatDropPenalty = "Meat Drop Penalty"
    MinstrelLevel = "Minstrel Level"
    MonsterLevel = "Monster Level"
    Moxie = "Moxie"
    MoxiePercent = "Moxie Percent"
    MoxieControlsMp = "Moxie Controls MP"
    MoxieLimit = "Moxie Limit"
    MoxieMayControlMp = "Moxie May Control MP"
    MpRegenMax = "MP Regen Max"
    MpRegenMin = "MP Regen Min"
    Muscle = "Muscle"
    MusclePercent = "Muscle Percent"
    MuscleLimit = "Muscle Limit"
    Mysticality = "Mysticality"
    MysticalityPercent = "Mysticality Percent"
    MysticalityLimit = "Mysticality Limit"
    NeverFumble = "Never Fumble"
    NonstackableWatch = "Nonstackable Watch"
    NoPull = "No Pull"
    OffhandDrop = "Offhand Drop"
    OthelloSkill = "Othello Skill"
    PantsDrop = "Pants Drop"
    PickpocketChance = "Pickpocket Chance"
    PoolSkill = "Pool Skill"
    PlumberStat = "Plumber Stat"
    PlumberPower = "Plumber Power"
    PvPFights = "PvP Fights"
    RandomMonsterModifiers = "Random Monster Modifiers"
    RangedDamage = "Ranged Damage"
    RangedDamagePercent = "Ranged Damage Percent"
    Raveosity = "Raveosity"
    ReduceEnemyDefense = "Reduce Enemy Defense"
    RestingHp = "Resting HP"
    RestingHPPercent = "Resting HP Percent"
    RestingMp = "Resting MP"
    RestingMPPercent = "Resting MP Percent"
    RolloverEffect = "Rollover Effect"
    RolloverEffectDuration = "Rollover Effect Duration"
    RubeeDrop = "Rubee Drop"
    ShirtDrop = "Shirt Drop"
    SingleEquip = "Single Equip"
    SixgunDamage = "Sixgun Damage"
    Skill = "Skill"
    SleazeDamage = "Sleaze Damage"
    SleazeImmunity = "Sleaze Immunity"
    SleazeResistance = "Sleaze Resistance"
    SleazeSpellDamage = "Sleaze Spell Damage"
    SleazeVulnerability = "Sleaze Vulnerability"
    SlimeHatesIt = "Slime Hates It"
    SlimeResistance = "Slime Resistance"
    Smithsness = "Smithsness"
    SoftcoreOnly = "Softcore Only"
    Sombrero = "Sombrero"
    SombreroBonus = "Sombrero Bonus"
    SongDuration = "Song Duration"
    SpellCritical = "Spell Critical"
    SpellCriticalPercent = "Spell Critical Percent"
    SpellDamage = "Spell Damage"
    SpellDamagePercent = "Spell Damage Percent"
    SpookyDamage = "Spooky Damage"
    SpookyImmunity = "Spooky Immunity"
    SpookyResistance = "Spooky Resistance"
    SpookySpellDamage = "Spooky Spell Damage"
    SpookyVulnerability = "Spooky Vulnerability"
    SprinkleDrop = "Sprinkle Drop"
    StatTuning = "Stat Tuning"
    StenchDamage = "Stench Damage"
    StenchImmunity = "Stench Immunity"
    StenchResistance = "Stench Resistance"
    StenchSpellDamage = "Stench Spell Damage"
    StenchVulnerability = "Stench Vulnerability"
    SupercoldResistance = "Supercold Resistance"
    Surgeonosity = "Surgeonosity"
    Synergetic = "Synergetic"
    Unarmed = "Unarmed"
    UnderwaterFamiliar = "Underwater Familiar"
    Variable = "Variable"
    Volleyball = "Volleyball"
    WarBearArmorPenetration = "WarBear Armor Penetration"
    WaterLevel = "Water Level"
    WeakensMonster = "Weakens Monster"
    WeaponDamage = "Weapon Damage"
    WeaponDamagePercent = "Weapon Damage Percent"
    WeaponDrop = "Weapon Drop"
    WikiName = "Wiki Name"

    def parse_value(self, value: Any) -> Any:
        if self is Modifier.Effect:
            from .Effect import Effect
            return Effect(value)
        if self is Modifier.MeatDrop:
            return float(value) / 100
        if self is Modifier.EffectDuration:
            return int(value)

        return value

