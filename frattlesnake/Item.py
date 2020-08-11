from typing import Optional, Union
from dataclasses import dataclass

from .kolmafia import km

@dataclass
class Item:
    id: int
    name: str
    description: str
    image: str

    @staticmethod
    def get_by_id(id: int) -> Optional["Item"]:
        if id == -1:
            return None

        return Item(id=id,
                    name=km.ItemDatabase.getDisplayName(id),
                    description=km.ItemDatabase.getDescriptionId(id),
                    image=km.ItemDatabase.getImage(id))

    @staticmethod
    def get_by_name(name: str) -> Optional["Item"]:
        return Item.get_by_id(km.ItemDatabase.getItemId(name))

    @staticmethod
    def get(key: Union[int, str]) -> Optional["Item"]:
        if isinstance(key, int):
            return Item.get_by_id(key)
        elif isinstance(key, str):
            return Item.get_by_name(key)

    def eat(self, quantity=1, silent=False) -> bool:
        command = "eat" + ("silent" if silent else "")
        km.KoLmafiaCLI.DEFAULT_SHELL.executeCommand(command, "{} {}".format(quantity, self.name))
        return km.UseItemRequest.lastUpdate == ""

    def drink(self, quantity=1, silent=False) -> bool:
        command = "drink" + ("silent" if silent else "")
        km.KoLmafiaCLI.DEFAULT_SHELL.executeCommand(command, "{} {}".format(quantity, self.name))
        return km.UseItemRequest.lastUpdate == ""

