## Map menu (hub)
##
## A school map the player returns to between rooms. Pick a room, play it, and
## the room sends you back here. Rooms can be replayed.
##
## Works with or without the background: drop a 1920x1080 image at
## images/school_map.png and the hotspots sit on top. Without it the screen runs
## on a plain dark background.
##
## To add a room, add one dict to map_locations. "rect" is (x, y, width, height)
## in 1920x1080 space. "jump" is the label played for that room, or None to show
## the room dimmed and not clickable.
##
## Setup:
##   - Enter the map the first time with:  jump map_hub
##   - End every room label with:          jump map_hub
##   - Set map_exit_label to the label that follows the map section. The Leave
##     button appears once it is set.
##
## The player can also open the map at any time with the keyboard shortcut below
## (M by default). Escape or a right-click closes it.

define map_locations = [
    {"name": "School Gates", "rect": (150, 640, 380, 210), "jump": None},
    {"name": "Classroom", "rect": (1010, 300, 420, 240), "jump": "talk_to_ezra"},
]

## Label the story continues to when the player leaves the map. Leave empty to
## hide the Leave button while the map is still the main screen.
define map_exit_label = ""

## Key that opens the map from anywhere in the story. M is unused by Ren'Py's
## default keymap. Change this to any free key for a different shortcut.
define map_hotkey_key = "K_m"

## True while the map was opened by the shortcut, so the Leave button shows even
## before map_exit_label is set.
default map_from_hotkey = False


init python:

    if "map_hotkey" not in config.overlay_screens:
        config.overlay_screens.append("map_hotkey")

    def open_map():
        if renpy.context()._menu:
            return
        if renpy.get_screen("map_menu"):
            return

        renpy.store.map_from_hotkey = True
        try:
            renpy.call_in_new_context("map_hub")
        finally:
            renpy.store.map_from_hotkey = False


screen map_hotkey():
    key map_hotkey_key action Function(open_map)


## Rooms are replayed, so control always comes back here.
label map_hub:
    call screen map_menu
    $ map_choice = _return
    if map_choice is not None:
        jump map_choice
    if map_exit_label:
        jump map_exit_label
    return


screen map_menu():

    tag menu
    modal True
    zorder 50

    key "game_menu" action Return(None)

    if renpy.loadable("images/school_map.png"):
        add "images/school_map.png"
    else:
        add Solid("#0b0b0f")

    label "Rosaryhill School" style "map_title"

    text "Select a location" style "map_hint"

    if map_from_hotkey or map_exit_label:
        textbutton _("Leave"):
            style "return_button"
            action Return(None)

    for loc in map_locations:
        $ hx, hy, hw, hh = loc["rect"]
        textbutton loc["name"]:
            style "map_hotspot"
            xpos hx
            ypos hy
            xysize (hw, hh)
            action If(loc["jump"], Return(loc["jump"]))


style map_title is gui_text:
    xalign 0.5
    ypos 40
    size 54
    color gui.accent_color


style map_hint is gui_text:
    xalign 0.5
    ypos 110
    size 30
    color gui.idle_small_color


style map_hotspot is button:
    idle_background Frame("gui/button/slot_idle_background.png", Borders(15, 15, 15, 15))
    hover_background Frame("gui/button/slot_hover_background.png", Borders(15, 15, 15, 15))
    insensitive_background Frame("gui/button/slot_idle_background.png", Borders(15, 15, 15, 15))
    padding (24, 18, 24, 18)


style map_hotspot_text is button_text:
    xalign 0.5
    yalign 0.5
    size 40
    idle_color gui.accent_color
    hover_color gui.hover_color
    insensitive_color gui.insensitive_color
