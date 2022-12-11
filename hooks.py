import os
import subprocess
from libqtile import hook, qtile

@hook.subscribe.startup_once
def autostart():
    confd = os.path.expanduser('~/.config/')
    subprocess.Popen([confd + '.screenlayout.sh'])
    subprocess.Popen([confd + '.autorun.sh'])

@hook.subscribe.startup_complete
def assign_groups_to_screens():
    qtile.groups_map["1"].cmd_toscreen(1)
    qtile.groups_map["9"].cmd_toscreen(0)

@hook.subscribe.client_new
def position_static(c):
    # Example rule: the Wallpaper Engine scene window is fixed on the right monitor
    if c.window.get_wm_class()[1] == 'WP':
        c.cmd_static(1, 1920, 56, 1280, 1024)
        
@hook.subscribe.client_managed
def position_floating(c):
    # Position the mixer
    if c.window.get_wm_class()[1] == 'alsamixer':
        c.cmd_set_position_floating(1920 + 1280 - 600 - 8, 40 + 56)
        c.cmd_set_size_floating(600, 320)