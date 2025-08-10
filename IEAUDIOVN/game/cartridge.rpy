# Game cartridge section script (expanded with full dialogue and audio cues)

define you = Character('You', color = "#ffffff")
define mom = Character('Mom', color = "#6999ff")
define dog = Character('Dog', color = "#b700ff")
define madong = Character('Hansum Madong', color = "#22ff04")
define maddie = Character('Maddie', color = "#8c00ff")
define narrator = Character(None, what_color="#979797", what_italic=True)

label cartridge_start:
    # Start nostalgic background music
    play music "audio/bgm_nostalgic.mp3" fadein 2.0 volume 0.3
    
    you "I found this old cartridge with the stuff she left for me."
    you "It's the dating sim we used to play as kids: Precious Endearing Elitist Academy."
    you "P.E.E. academy..."
    pause 1
    you "Did I keep the save file?"
    play sound "audio/sfx_game_startup.mp3"

    scene bg madong
    with fade
    show madong
    madong "People mingling, heart's a tingling, oh this warm feeling!"
    madong "Oh you're so sugoiiii, won't you be my boy!"
    you "…"
    pause 1
    you "Oh my god"
    madong "Been a long time babygirl!"
    madong "Sure I'm only an inch tall…"
    madong "But I got a lotta love to give to this long-distance relationship."
    madong "Standing at 1 inch tall, it's the handsomest of them all: Handsum Madong~"
    you "Haha bro how'd they ever greenlight this?"
    you "We actually played this every day for like, a full YEAR back in highschool."
    madong "Shawtycakes… you're making me blush~"
    play sound "audio/sfx_kiss.wav"
    narrator "Hansum blows you a kiss"
    you "Very disturbing."
    pause 1
    you "Wouldn't have spent my senior year any other way."
    narrator "Hansum continues to look at you longingly, with a tinge of sadness in his eyes"
    you "If I..."
    pause 1
    you "If I could go back."
    you "What would I say to her?"
    you "…"
    pause 1
    you "Where would I even start?"
    narrator "Your thoughts are interrupted when all of a sudden, your vision blurs drastically."
    with hpunch
    you "Ugh I've been awake too long…"
    pause 1
    you "???"
    you "It looks like Hansum's right in front of me…"
    you "Ew."
    madong "Babylove, you seem quite unwell…"
    madong "Your file's quite old. Surely there are other games you can play?"
    narrator "Lost in thought, Hansum stares you down intently."
    madong "Oh, I see."
    madong "You still have the final chapter to complete."
    madong "But… I suppose you wouldn't want to continue without your player 2."
    madong "..."
    madong "For my two loyal fans…"
    madong "I guess I could do something"

    # Next day prompt effect - transition to night scene
    hide madong
    scene black with fade
    pause 0.5
    show text "{size=30}{color=#ffffff} The Next day...{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    pause 0.5

    # Add night ambience and slow music change
    hide madong
    scene bg night with dissolve
    narrator "Deep into the night, the weight of the still air in your bedroom seems to have suddenly shifted."
    narrator "The cool air brushes against your face, letting you take in each breath with ease."
    narrator "You feel at home."
    play sound "audio/sfx_firework.wav"
    narrator "In the distance, you hear a faint whistle ripping through the air."
    narrator "The gentle sound fades into the night, eventually dragging into a complete silence."
    narrator "Finally,"
    narrator "As if the sky couldn't hold it in any longer"
    play sound "audio/sfx_firework.wav"
    pause 0.5
    play sound "audio/sfx_firework.wav"
    pause 0.3
    play sound "audio/sfx_firework.wav"
    pause 1.0
    narrator "You hear the loud scattering sound of fireworks."
    narrator "Your eyes still closed, the sound echoes through the room as you enjoy the cold sensation of the tiled floor."
    narrator "…"
    narrator "The cold floor…"
    narrator "Weren't you on your mattress?"
    narrator "Something's off. Even from the sound of it, your room is bigger than it's supposed to be."
    narrator "You open your eyes"
    scene bg festival with dissolve
    you "...what"
    narrator "You're no longer in your room, but in a classroom that looks like it was ripped straight out of an anime."
    narrator "You stand up and try to make sense of your environment."
    narrator "As you walk towards the window on your right, you notice school festival decorations displayed throughout the room like flyers, signs, banners…"
    narrator "And finally, outside the window, you see a crowd of students sitting on the field, watching the firework show."
    narrator "However strange, the setting is not unfamiliar to you. It's…"
    you "Oh my god I'm in P.E.E. Academy"
    show maddie festival 
    maddie "What, did you just realize the acronym now???"
    play sound "audio/sfx_laughter.wav"
    narrator "Maddie erupts in light laughter"
    pause 0.5
    narrator "That voice.. It's"
    pause 0.5
    narrator "It's her."
    pause 1.0
    $ renpy.say(narrator, "{cps=20}Your breath trembles.{/cps}")
    
    # Add variable for tracking
    $ met_maddie = True

    menu:
        "{color=#8c00ff}Maddie?{/color}":
            jump cartridge_maddie
        "{color=#ffffff}I've missed you{/color}":
            jump cartridge_missed
        "{color=#22ff04}Let's finish the game{/color}":
            jump cartridge_finish

label cartridge_maddie:
    show maddie festival confused
    you "M-Maddie? Is it really you?"
    maddie "Huh? Yeah? Of course I'm.. me??? haha"
    maddie "Girl you sound weird, you okay?"
    you "..."
    pause 0.5
    show maddie festival smiling
    you "Yeah. Yeah I'm fine haha."
    you "just… messing with you"
    narrator "Though you only see her 'player 2' icon, you know it's her. You'd recognize that voice even as a whisper in a screaming crowd."
    maddie "Okay dude, no more kidding around, I wanna finish the game before sundown haha"
    jump cartridge_choice

label cartridge_missed:
    show maddie festival
    you "..."
    pause 0.3
    maddie "??"
    maddie "Why're you so quiet?"
    you "Do you…"
    pause 0.5
    you "Did you still think of me?"
    you "Do you…"
    you "Do you wanna finish the game?"
    show maddie festival smiling
    maddie "Yeahh I feel like if we don't finish it like, now, we'll keep procrastinating."
    maddie "C'mon, let's go!"
    jump cartridge_choice

label cartridge_finish:
    show maddie festival smiling
    maddie "Okay, let's go!"
    narrator "You spend the night joking around with Maddie, laughing like when you were just kids."
    narrator "For the first time in forever, you're finally home."
    stop music fadeout 3.0
    scene black with fade
    pause 1.0
    narrator "Filled with joy, you laugh yourself awake."
    jump ending_scene

label cartridge_choice:
    menu:
        "{color=#ffffff}I've missed you{/color}":
            jump cartridge_finish
        "{color=#22ff04}Let's finish the game{/color}":
            jump cartridge_finish
        "{color=#8c00ff}Maddie?{/color}":
            jump cartridge_maddie