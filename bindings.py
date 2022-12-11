from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal

mod = "mod4"
fileman = "dolphin"
terminal = "kitty" #guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod],              "Left",     lazy.layout.left(),         desc="Move focus to left"),
    Key([mod],              "Right",    lazy.layout.right(),        desc="Move focus to right"),
    Key([mod],              "Down",     lazy.layout.down(),         desc="Move focus down"),
    Key([mod],              "Up",       lazy.layout.up(),           desc="Move focus up"),
    #Key([mod],              "space",    lazy.layout.next(),         desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],     "Left",     lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"],     "Right",    lazy.layout.shuffle_right(),desc="Move window to the right"),
    Key([mod, "shift"],     "Down",     lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"],     "Up",       lazy.layout.shuffle_up(),   desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],   "Left",     lazy.layout.grow_left(),    desc="Grow window to the left"),
    Key([mod, "control"],   "Right",    lazy.layout.grow_right(),   desc="Grow window to the right"),
    Key([mod, "control"],   "Down",     lazy.layout.grow_down(),    desc="Grow window down"),
    Key([mod, "control"],   "Up",       lazy.layout.grow_up(),      desc="Grow window up"),
    Key([mod],              "n",        lazy.layout.normalize(),    desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],     "Return",   lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([mod],              "Tab",      lazy.next_layout(),         desc="Toggle between layouts"),
    Key([mod],              "q",        lazy.window.kill(),         desc="Kill focused window"),
    Key([mod],              "Space",    lazy.window.toggle_floating(), desc="Toggle floating state of the window"),
    Key([mod, "control"],   "r",        lazy.reload_config(),       desc="Reload the config"),
    Key([mod, "control"],   "q",        lazy.shutdown(),            desc="Shutdown Qtile"),
    
    Key(["mod1"], "Shift_L",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Switch to the next keyboard layout"),
            
    # Spawn stuff
    Key([mod],  "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod],  "e",
        lazy.spawn(fileman),
        desc="Launch file manager"),
    Key([mod],  "d",
        lazy.spawn("rofi -show drun -theme themes/drun.rasi"),
        desc="Show the apps launcher"),
    Key([mod],  "x",
        lazy.spawn(".local/bin/rofi-power-menu"),
        desc="Show the shutdown/logout menu"),
    Key([],     "Print",
        lazy.spawn("scrot --focused 'Arch-Qtile-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$HOME/Pictures'"),
        desc="Take a screenshot of the active window"),
        
    Key([mod, "shift"],   "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

# Drag floating layouts.
mouse = [
    Drag([mod],     "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag([mod],     "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod],    "Button2",
        lazy.window.bring_to_front()
    ),
]
