from libqtile.config import Group, ScratchPad, DropDown
from libqtile.core.manager import Qtile
from typing import Callable

group_names_main = "1234"
group_names_second = "90"

def go_to_group(name: str) -> Callable:
    def _inner(qtile: Qtile) -> None:
        if len(qtile.screens) == 1:
            qtile.groups_map[name].cmd_toscreen()
            return
        if name in group_names_second:
            qtile.focus_screen(0)
            qtile.groups_map[name].cmd_toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].cmd_toscreen()
    return _inner

groups = [Group(i) for i in group_names_main + group_names_second]

from bindings import mod, keys
from libqtile.config import Key
from libqtile.lazy import lazy

for i in groups:
    keys.extend([
        # mod + letter of group = switch to group
        Key([mod],          i.name,
            #lazy.group[i.name].toscreen(),
            lazy.function(go_to_group(i.name)),
            desc="Switch to group {}".format(i.name),
        ),
        # mod + shift + letter of group = move focused window to group
        # add argument 'switch_group=True' to switch to that group
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)
        ),
    ])

groups.extend([
    ScratchPad("r", [
        DropDown("term", "kitty"),
    ]),
])

keys.extend([
    Key([mod], "r", lazy.group["r"].dropdown_toggle("term")),
])