## The Monopad.
##
## A case file the school writes, not a tool the player owns. Read-only by
## design: no notes, no counters, no editing. The story fills it.
##
## Opens on H at any point in the story, or from the Monopad button in the
## quick menu. Closes on H, Escape, the right mouse button, or Close.
##
## Where things live:
##   handbook_data.rpy     the contents, one dict per student, entry, rule, floor
##   handbook_sections.rpy the four pages
##   handbook_styles.rpy   type, colour and spacing
##
## Add a dict to the data file and the pages pick it up.

define handbook_hotkey_key = "K_h"

define hb_font_display = "fonts/doctor_punk.otf"

define hb_font_body = "fonts/elegant_typewriter/ELEGANT TYPEWRITER Regular.ttf"

define hb_sections = [
    ("students", "Student profiles"),
    ("evidence", "Evidence log"),
    ("map", "Map system"),
    ("rules", "School rules"),
]


init python:
    if "handbook_hotkey" not in config.overlay_screens:
        config.overlay_screens.append("handbook_hotkey")


screen handbook_hotkey():
    key handbook_hotkey_key action If(renpy.get_screen("handbook") is None, Show("handbook"), Hide("handbook"))


screen handbook():

    modal True
    zorder 150

    default section = "students"

    key "game_menu" action Hide("handbook")

    add Solid("#0b0b0f")

    ## The rail. Section names come from hb_sections so the order lives in one
    ## place, next to the pages that answer them.
    frame:
        style "hb_rail"
        xpos 0
        ypos 0
        xsize 340
        ysize 1080

        vbox:
            xpos 38
            ypos 54
            xsize 264
            spacing 0

            text "ROSARY HILL" style "hb_kicker"
            text "HANDBOOK" style "hb_title"

            null height 16

            text "Property of the school office. Staff write the entries." style "hb_note"

            null height 48

            vbox:
                style_prefix "hb_nav"
                spacing 2

                for sid, name in hb_sections:
                    textbutton name action SetScreenVariable("section", sid)

            null height 46

            text "H closes this file." style "hb_footnote"

    vbox:
        style_prefix "hb_close"
        xpos 1690
        ypos 44

        textbutton "Close" action Hide("handbook")

    frame:
        style "hb_page"
        xpos 340
        ypos 0
        xsize 1580
        ysize 1080

        if section == "students":
            use hb_page_students
        elif section == "evidence":
            use hb_page_evidence
        elif section == "map":
            use hb_page_map
        else:
            use hb_page_rules
