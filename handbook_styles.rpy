## Type, colour and spacing for the handbook.
##
## Every colour here is one already in gui.rpy: white for body, the gold for
## headings, the muted maroon for the rail, the hover pink for the one line
## that is an amendment rather than a rule.

style hb_rail is frame:
    background Solid("#1b0010")
    padding (0, 0)


style hb_page is frame:
    background None
    padding (0, 0)


style hb_kicker is gui_text:
    font hb_font_display
    size 24
    color "#bf9000"


style hb_title is gui_text:
    font hb_font_display
    size 66
    color gui.accent_color


style hb_note is gui_text:
    font hb_font_body
    size 22
    color gui.idle_small_color


style hb_footnote is gui_text:
    font hb_font_body
    size 20
    color gui.idle_small_color


style hb_section is gui_text:
    font hb_font_display
    size 46
    color gui.accent_color


style hb_lead is gui_text:
    font hb_font_body
    size 24
    color gui.idle_small_color


style hb_card is frame:
    background Solid("#150710")
    padding (26, 22)


style hb_monogram is frame:
    background Solid("#1b0010")
    padding (0, 0)


style hb_monogram_text is gui_text:
    font hb_font_display
    size 120
    color "#7a003d"
    xalign 0.5
    yalign 0.5


style hb_name is gui_text:
    font hb_font_display
    size 44
    color gui.accent_color


style hb_talent is gui_text:
    font hb_font_display
    size 26
    color "#bf9000"


style hb_meta is gui_text:
    font hb_font_body
    size 22
    color gui.idle_small_color


style hb_body is gui_text:
    font hb_font_body
    size 25
    color gui.text_color


style hb_ref is gui_text:
    font hb_font_display
    size 30
    color "#bf9000"


style hb_entry_title is gui_text:
    font hb_font_display
    size 30
    color gui.accent_color


style hb_thumb_empty is frame:
    background Solid("#1b0010")
    padding (0, 0)


style hb_floor is gui_text:
    font hb_font_display
    size 36
    color "#bf9000"


style hb_room is gui_text:
    font hb_font_body
    size 24
    color gui.text_color


style hb_room_note is gui_text:
    font hb_font_body
    size 22
    color gui.idle_small_color


style hb_rule_number is gui_text:
    font hb_font_display
    size 34
    color "#bf9000"


style hb_amendment is gui_text:
    font hb_font_body
    size 22
    color gui.hover_color


style hb_nav_button is button:
    background None
    padding (0, 12)


style hb_nav_button_text is button_text:
    font hb_font_body
    size 26
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.hover_color
    insensitive_color gui.insensitive_color


style hb_close_button is button:
    background None
    padding (0, 0)


style hb_close_button_text is button_text:
    font hb_font_body
    size 26
    idle_color gui.idle_color
    hover_color gui.hover_color
