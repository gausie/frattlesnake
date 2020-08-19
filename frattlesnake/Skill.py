from functools import cached_property
from typing import Optional, Union

from .kolmafia import km
from .Effect import Effect


class Skill:
    id: int

    def __init__(self, key: Union[str, int]):
        if isinstance(key, str):
            key = int(km.SkillDatabase.getSkillId(key))

        self.id = key

    @cached_property
    def name(self) -> str:
        return km.SkillDatabase.SkillDatabase(self.id)

    @cached_property
    def type(self) -> str:
        return km.SkillDatabase.getSkillTypeName(self.id)

    @cached_property
    def level(self) -> int:
        return km.SkillDatabase.getSkillLevel(self.id)

    @cached_property
    def image(self) -> str:
        return km.SkillDatabase.getSkillImage(self.id)

    @cached_property
    def training_cost(self) -> int:
        return km.SkillDatabase.getSkillPurchaseCost(self.id)

    @cached_property
    def class(self) -> str:
        return km.SkillDatabase.getSkillCategory(self.id)

    @cached_property
    def libram(self) -> bool:
        return km.SkillDatabase.isLibramSkill(self.id)

    @cached_property
    def passive(self) -> bool:
        return km.SkillDatabase.isPassive(self.id)

    @cached_property
    def buff(self) -> bool:
        return km.SkillDatabase.isBuff(self.id)

    @cached_property
    def combat(self) -> bool:
        return km.SkillDatabase.isCombat(self.id)

    @cached_property
    def song(self) -> bool:
        return km.SkillDatabase.isSong(self.id)

    @cached_property
    def expression(self) -> bool:
        return km.SkillDatabase.isExpression(self.id)

    @cached_property
    def walk(self) -> bool:
        return km.SkillDatabase.isWalk(self.id)

    @cached_property
    def summon(self) -> bool:
        return km.SkillDatabase.isSummon(self.id)

    @cached_property
    def permable(self) -> bool:
        return km.SkillDatabase.isPermable(self.id)

    @cached_property
    def effect(self) -> Optional[Effect]:
        effect_name = km.UneffectRequest.skillToEffect(self.name)

        return None if effect_name is None else Effect(effect_name)

    @cached_property
    def effect_duration(self) -> int:
        return km.SkillDatabase.getEffectDuration(self.id)