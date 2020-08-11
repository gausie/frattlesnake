from typing import Optional, Union
from dataclasses import dataclass

from .kolmafia import km
from .Item import Item

@dataclass
class Familiar:
    id: int
    name: str
    image: str
    hatchling: Item

    @staticmethod
    def get_by_id(id: int) -> Optional["Familiar"]:
        if id == -1:
            return None

        hatchling_id = km.FamiliarDatabase.getFamiliarLarva(id)
        hatchling = Item.get(hatchling_id)

        if hatchling is None:
            raise Exception(f"Hatching {hatchling_id} not recognised")

        return Familiar(id=id,
                        name=km.FamiliarDatabase.getFamiliarName(id),
                        image=km.FamiliarDatabase.getFamiliarImage(id),
                        hatchling=hatchling)

    @staticmethod
    def get_by_name(name: str) -> Optional["Familiar"]:
        return Familiar.get_by_id(km.FamiliarDatabase.getFamiliarId(name))

    @staticmethod
    def get(key: Union[int, str]) -> Optional["Familiar"]:
        if isinstance(key, int):
            return Familiar.get_by_id(key)
        elif isinstance(key, str):
            return Familiar.get_by_name(key)

    @staticmethod
    def mine() -> Optional["Familiar"]:
        return Familiar.get(km.KoLCharacter.getFamiliar().getId())

    @staticmethod
    def enthroned() -> Optional["Familiar"]:
	    return Familiar.get(km.KoLCharacter.getEnthroned().getId())

    @staticmethod
    def bjorned() -> Optional["Familiar"]:
	    return Familiar.get(km.KoLCharacter.getBjorned().getId())

    def use(self) -> bool:
        km.KoLmafiaCLI.DEFAULT_SHELL.executeCommand("familiar", self.name)
        return True

    def have(self) -> bool:
        return km.KoLCharacter.findFamiliar(self.id) is not None