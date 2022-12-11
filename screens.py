from libqtile import bar, widget
from libqtile.config import Screen

mainbar = bar.Bar(
    [
        widget.CurrentLayoutIcon(
            scale=0.8
        ),
        widget.GroupBox(
            highlight_method="block",
        ),
        widget.TextBox("|",
            foreground="#d75f5f",
        ),
        widget.WindowName(),
        widget.Prompt(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox("asrifox",
            foreground="#d75f5f",
        ),
        widget.KeyboardLayout(
            configured_keyboards=['us', 'ru typewriter'],
            display_map={
                'us': 'us',
                'ru typewriter': 'ru',
            },
        ),
        widget.Systray(),
        widget.Clock(
            format="%Y-%m-%d %a %H:%M:%S",
        ),
    ],
    24,
    margin=[8,8,0,8],
    background = "#00000000",
    
    #border_width=[8, 8, 8, 8],  # Draw top and bottom borders
    #border_color=["00000000", "00000000", "00000000", "00000000"]
)

screens = [
    Screen(
        top=mainbar,
        wallpaper = "/home/asriel/Pictures/wallpapers/1190273.png",
        wallpaper_mode = "fill"
    ),
]
