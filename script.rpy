init python:
    def dismiss_callback():
        renpy.play("text.mp3")
        return True
    config.say_allow_dismiss = dismiss_callback


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

    n "Students from all over the world gather right here, in front of the school's gates. I'm sure they all have hope in their eyes for a bright future as they look up at such a school."

    n "I stand there for a while, before taking a long breath to settle myself. I don't know what this school has in store for me. But it never hurts to be prepared for the worst-case scenarios." 

    n "Of course, I don't think I could've ever fully prepared myself for what came next."

    n05 "My name is {color=#bf9000}{b}Lythan{/b}{/color}. I'm a pretty average student for someone standing in front of such a prestigious school."

    n05 "I don't think there's anything overly memorable about me. I just like to write stories, and hope to publish a book of my own one day."

    n05 "Back to the topic at hand though .." 

    d "One tentative step, another follows suit."
    
    show school_corrupted with dissolve

    d "You barely make it past the gates when your vision begins to swim."

    n05 "Ugh.. my head.."

    scene black with fade 

    n05 "..."

    n ".. ow.. "

    scene rhs with dissolve
    show classroom 

    n "ow, ow, ow. My head is killing me.."

    n05 ".. What- what the..?"

    d "You wake up somewhere dark and unfamiliar. It almost looks like a classroom. But, it's not one that you recognise."

    n05 "How.. did I..? When did I..?"

    n "Get a grip. I can't just stutter my way through this. "
    d "You look around the room for anything that might tell you definitively where you are, or how you got there. "

    n "Huh? Is that.. a person..? Maybe I should approach them.. they might know something. "

    call screen classroom

    return


label ezra_1:
    play sound transition
    pause 0.3
    show n04
    with dissolve

    n ".. Isn't this how the first victims usually die in horror movies?"

    n "Whatever. It's not like I'm actually in a horror movie."

    show n05 nerv at player

    n05 "Hey. Do you know where we are?" 


    n04 "..." 

    n05 "..."
    hide n05 nerv

    n04 "..."

    n05 "I'll take that as a 'no'. I'm Lythan."

    n "Introducing myself is probably the best course of action. Maybe it'll help her trust me more." 

    show n04 question

    n04 ".. Ezra." 

    n05 "... Sorry?"

    n04 "My name is Ezra."

    n05 "Oh. Well, I'd say 'nice to meet you' but that's not exactly true. I mean- it's nice to meet you. But this place is kind of... not it."
    
    show n04 smile

    d "She chuckles. She seems to be a little less on edge."

    n05 "So.. uhm.. do RHS students usually hang around empty-and-possibly-abandoned classrooms?"

    show n04 question
    d "She shakes her head slowly. She opens her mouth to say something but quickly closes it again"
    show n04

    show n05 at player    
    n05 "Something on your mind?"
    hide n05

    n04 ".. The classroom door is unlocked"

    show n05 pensive at player  
    play sound sfx_dull
    n "Ah. Now I feel like an idiot for not trying that first."

    show n05 nerv at player  
    n05 "Great! Let's get out of here then! No point in moping around in a place like this, right?"
    hide n05 nerv
    
    d "You turn to look at Ezra as you make your way to the door. But, she's still standing there."

    n05 "Ezra? You coming?"

    d "She's silent for a long while. She looks like she just wants to go home."

    d "She doesn't say anything as she walks closer, ducking her head down and staring at the floor in front of her as she walks."

    show school_cool with fade

    show n04 arm away with dissolve
    d "The two of you spend some time wandering around the school. You've tried to start conversation, but Ezra seems less willing to speak now that you're out of the classroom."

    n05 ".. Wasn't there.. some kind of thing in the hall?" 

    n04 ".. Was there?" 

    d "You exchange a glance. You don't even know what time it is." 

    n05 "Hmm.. my memory is still kind of hazy. I can't really remember things."

    n04 ".. My memory isn't the best either.. sorry.." 

    n05 "It's okay! That just means that we'll figure things out together! Nothing wrong with that." 

    n05 "Let's just try to find the hall for now, maybe we'll bump into some more people along the way." 


    show schoolhall_entrance with fade

    n05 "Damn, this school is big. I feel like we've been looping this area for-"

    n "You notice a flicker of something in the distance."
    play sound sfx_point

    n "Is that another student? Come to think of it, this school is pretty empty for such a prestigious institution. " 

    n "Maybe I should approach her? Or… I don't even know if she's a threat to me or not. "

    call screen prehall

label kirsten_1:
    pause 0.3
    show n01 at happy with dissolve 
    play sound sfx_charm

    n01 "Oh! More students! Are you two the last?" 

    n05 "I think so? I didn't really see anyone else walking around." 

    show n01 cookie
    n01 "Hmm.. It's whatever, come on." 

    n05 "Uh.. where, exactly?" 

    show n01 -cookie
    n01 "The hall, of course! It was everywhere on those posters." 

    n "Posters? Did I read one? I remember something about the hall.. but, not entirely. "

    n01 "I'm Kirsten. The Ultimate Baker."

    n05 "Oh! Right! I'm the Ultimate Author. I think that's what my letter said." 

    show n01 smug
    n01 "You think?" 

    return

