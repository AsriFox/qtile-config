import os
import subprocess
from libqtile import hook, qtile

@hook.subscribe.startup_once
def autostart():
    confd = os.path.expanduser('~/.config/')
    subprocess.Popen([confd + '.autorun.sh'])

@hook.subscribe.client_new
def position_static(c):
    # Example rule: the Wallpaper Engine scene window is fixed on the right monitor
    if c.window.get_wm_class()[1] == 'WP':
        c.cmd_static(0, 0, 0, 1920, 1080)
        
@hook.subscribe.client_managed
def position_floating(c):
    # Position the mixer
    if c.window.get_wm_class()[1] == 'alsamixer':
        c.cmd_set_position_floating(1920 - 600 - 8, 40)
        c.cmd_set_size_floating(600, 320)
