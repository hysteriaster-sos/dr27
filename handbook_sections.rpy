## The four pages of the handbook.
##
## Each page is a heading, one line of framing, and a scrollable body. They are
## used from handbook.rpy, so they hold no state of their own.

screen hb_page_students():

    vbox:
        xpos 54
        ypos 46
        xsize 1470
        spacing 16

        text "Student profiles" style "hb_section"
        text "Six names on the register. Two have been spoken to." style "hb_lead"

        viewport:
            ysize 820
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                xsize 1440
                spacing 20

                for s in hb_students:

                    frame:
                        style "hb_card"
                        xsize 1400

                        hbox:
                            spacing 28

                            fixed:
                                xsize 250
                                ysize 380

                                if s["portrait"]:
                                    add s["portrait"]:
                                        yalign 1.0
                                else:
                                    frame:
                                        style "hb_monogram"
                                        xsize 250
                                        ysize 380

                                        text s["initial"] style "hb_monogram_text"

                            vbox:
                                xsize 1060
                                spacing 6

                                text s["name"] style "hb_name"
                                text s["talent"] style "hb_talent"
                                text s["birthday"] style "hb_meta"

                                null height 10

                                for p in s["paragraphs"]:
                                    text p style "hb_body"


screen hb_page_evidence():

    vbox:
        xpos 54
        ypos 46
        xsize 1470
        spacing 16

        text "Evidence log" style "hb_section"
        text "Written up by staff. An entry appears once the room has been walked." style "hb_lead"

        viewport:
            ysize 820
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                xsize 1440
                spacing 26

                for e in hb_evidence:

                    hbox:
                        spacing 26

                        if e["shot"]:
                            fixed:
                                xsize 160
                                ysize 90

                                add e["shot"]:
                                    yalign 0.0
                        else:
                            frame:
                                style "hb_thumb_empty"
                                xsize 160
                                ysize 90

                        vbox:
                            xsize 1200
                            spacing 6

                            hbox:
                                spacing 18

                                text e["ref"] style "hb_ref"
                                text e["title"] style "hb_entry_title"

                            text e["where"] style "hb_meta"

                            if e["body"]:
                                null height 6
                                text e["body"] style "hb_body"


screen hb_page_map():

    vbox:
        xpos 54
        ypos 46
        xsize 1470
        spacing 16

        text "Map system" style "hb_section"
        text "Floor plans as the office holds them. Rooms are listed under each floor." style "hb_lead"

        viewport:
            ysize 820
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                xsize 1440
                spacing 44

                for f in hb_floors:

                    hbox:
                        spacing 30

                        if f["plan"]:
                            add f["plan"]
                        else:
                            add Null(width=576)

                        vbox:
                            xsize 780
                            spacing 4

                            text f["label"] style "hb_floor"
                            text f["caption"] style "hb_meta"

                            null height 12

                            for rm in f["rooms"]:

                                text rm["name"] style "hb_room"
                                text rm["note"] style "hb_room_note"

                                null height 8


screen hb_page_rules():

    vbox:
        xpos 54
        ypos 46
        xsize 1470
        spacing 16

        text "School rules" style "hb_section"
        text "Nine rules, posted in every room. Rule seven explains the rest." style "hb_lead"

        viewport:
            ysize 820
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                xsize 1440
                spacing 22

                for r in hb_rules:

                    hbox:
                        spacing 26

                        text r["number"] style "hb_rule_number"

                        vbox:
                            xsize 1300
                            spacing 4

                            text r["text"] style "hb_body"

                            if r.get("amendment"):
                                null height 8
                                text r["amendment"] style "hb_amendment"
