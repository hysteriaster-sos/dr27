init:
    # basics
    $ config.window_title = 'DR27'

    #characters
    $ n = Character (_narrator, what_color="#00ffff")
    $ d = Character(_narrator, what_color="#00ff00")
    $ n01 = Character('Kirsten')
    $ n02 = Character('Aster')
    $ n03 = Character('Zoe')
    $ n04 = Character('Ezra')
    $ n05 = Character('Lythan')
    $ n11 = Character('Zach')

label splashscreen:
    scene black
    show text "merry christmas everyone :3" with fade
    $ renpy.pause(1.0)
    hide text with fade
    return



label start:

    $ save_name = "Prologue"
    scene school_cool with fade

    n "Rosaryhill School, also known as 'RHS', has been standing proud for hundreds of years."

    n "The school has seen the rise of countless {color=#bf9000}{b}'ultimate'{/b}{/color} students, each one seemingly just as-if not more successful than the last."

    n "Students from all over the world gather right here, in front of the school's gates. I'm sure they all have hope in their eyes for a bright future as they look up at such a school.}"

    n "I stand there for a while, before taking a long breath to settle myself. I don't know what this school has in store for me. But it never hurts to be prepared for the worst-case scenarios." 

    n "Of course, I don't think I could've ever fully prepared myself for what came next."

    show 06_default with dissolve

    n05 "My name is {color=#bf9000}{b}Lythan{/b}{/color}. I'm a pretty average student for someone standing in front of such a prestigious school."

    n05 "I don't think there's anything overly memorable about me. I just like to write stories, and hope to publish a book of my own one day."

    n05 "Back to the topic at hand though .." 

    scene black with fade

    d "One tentative step, another follows suit. You barely make it past the gates when your vision begins to swim."

    n05 "Ugh.. my head.."

    n05 "..."

    n ".. ow.. "

    scene classroom with dissolve

    n "ow, ow, ow. My head is killing me.."

    n05 ".. What- what the..?"

    d "You wake up somewhere dark and unfamiliar. It almost looks like a classroom. But, it's not one that you recognise."

    n05 "How.. did I..? When did I..?"

    n "Get a grip. I can't just stutter my way through this. "
    d "You look around the room for anything that might tell you definitively where you are, or how you got there. "

    n "Huh? Is that.. a person..? Maybe I should approach them.. they might know something. "

    call screen classroom

    return

transform sprite_entrance:
    on show:
        yzoom 0.25 yanchor 1.0
        easein_bounce 0.75 yzoom 1.0
    on hide:
        easeout 0.3 alpha 0.0 yoffset 40

screen classroom():
    modal True
    imagebutton:
        xpos 1381
        ypos 960
        focus_mask True
        idle Transform("04_stand.png",zoom= 0.3)
        hover Transform("04_stand.png",zoom= 0.3)
        at sprite_entrance
        action Jump("talk_to_ezra")

label talk_to_ezra:
    pause 0.3
    show 06_default
    show 05_default
    with dissolve

    n ".. Isn't this how the first victims usually die in horror movies?"

    n "Whatever. It's not like I'm actually in a horror movie."

    show 06_nervsmile

    n05 "Hey. Do you know where we are?" 

    n04 "..." 

    show 06_sweat

    n05 "..."

    n04 "..."

    n05 "I’ll take that as a 'no'. I’m Lythan."

    n "Introducing myself is probably the best course of action. Maybe it’ll help her trust me more." 

    show 05_openmouth

    n04 ".. Ezra." 

    return
