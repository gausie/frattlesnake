from typing import Union

from .kolmafia import km

class Item:
    id: int

    def __init__(self, key: Union[str, int]):
        if isinstance(key, str):
            key = int(km.ItemDatabase.getItemId(key))

        if key == -1:
            return None

        self.id = key

    @property
    def name(self) -> str:
        return km.ItemDatabase.getDisplayName(self.id)

    @property
    def description(self) -> str:
        return km.ItemDatabase.getDescriptionId(self.id)

    @property
    def image(self) -> str:
        return km.ItemDatabase.getImage(self.id)

    def eat(self, quantity=1, silent=False) -> bool:
        command = "eat" + ("silent" if silent else "")
        km.KoLmafiaCLI.DEFAULT_SHELL.executeCommand(command, "{} {}".format(quantity, self.name))
        return km.UseItemRequest.lastUpdate == ""

    def drink(self, quantity=1, silent=False) -> bool:
        command = "drink" + ("silent" if silent else "")
        km.KoLmafiaCLI.DEFAULT_SHELL.executeCommand(command, "{} {}".format(quantity, self.name))
        return km.UseItemRequest.lastUpdate == ""

