from libqtile import layout

config = {
    'border_focus': "#FF0000",
    'border_normal': "#000000",
    'border_width': 0,
    'margin': 8,
    'single_border_width': 0,
    'single_margin': 8,
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(**config),
    # layout.Matrix(),
    # layout.MonadTall(**config),
    # layout.MonadWide(**config),
    # layout.RatioTile(),
    layout.Tile(**config),
    layout.VerticalTile(**config),
    # layout.TreeTab(**config),
    # layout.Zoomy(),
]
