# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character('You', color = "#ffffff")
define mom = Character('Mom', color = "#6999ff")
define dog = Character('Dog', color = "#b700ff")
define madong = Character('Hansum Madong', color = "#22ff04")
define maddie = Character('Maddie', color = "#8c00ff")
define narrator = Character(None, what_color="#979797", what_italic=True)

default shake_dialogue = False
default shakes = 0

# snowglobe made with dandruff
label snowglobe:

    play music "audio/bgm_winter.mp3" fadein 1.0 volume 0.4
    voice "MC/line5.mp3" 
    you "This is… kinda disgusting."

    scene bg snowglobe
    with fade

    narrator "The edges of your lips crease up, and for the first time in a while, you can’t help but crack into a smile."
    voice "MC/line6.mp3" 
    you "When we were kids, she kept talking about how much she wanted to play in the snow."

    show bg philippines
    with fade

    voice "MC/line7.mp3" 
    you "We waited for it all year but, turns out we don’t have that kind of weather in the Philippines."

    voice "MC/line8.mp3" 
    you "So, I guess my 5-year-old brain thought making a gross snowglobe with my dandruff was the next best thing…"

    scene bg snowglobe
    with fade

    $ shakes = 0;
    while shakes < 4:
        menu:
            "Shake the snowglobe":
                $ shakes += 1
                if shakes == 3 and not shake_dialogue:
                    $ shake_dialogue = True
                    play sound "audio/sfx_snowglobe.mp3" volume 0.2
                    narrator "You shake the snowglobe."
                    narrator "Are you done?"
                else:
                    play sound "audio/sfx_snowglobe.mp3" volume 0.2
                    narrator "You shake the snowglobe."
    jump snowglobe_broken

label snowglobe_broken:
    play sound "audio/sfx_leak.mp3" volume 0.2
    narrator "The snowglobe leaks the viscous liquid out of itself, rapidly pouring it all over your floor."
    voice "MC/line9.mp3"
    you "Oh- oh my god"
    narrator "You scramble to find something to wipe it with, but in your hurry…"
    stop sound fadeout 0.5

    show black
    play sound "audio/sfx_thud.mp3" volume 0.5
    narrator "You slip."


    scene black with fade
    pause 0.5
    show text "{size=30}{color=#ffffff} The Next Day...{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    pause 0.5

label next_day:
    scene bg bedroom
    with fade

    voice "MC/line10.mp3"
    you "I know I should’ve just like, called or something."
    voice "MC/line11.mp3"
    you "Maddie wouldn’t have told me she was sick but–"
    voice "MC/line12.mp3"
    you "I know I would've noticed."
    voice "MC/line13.mp3"
    you "...yeah?"
    voice "MC/line14.mp3"
    you "Even if she had moved to Canada and-"
    voice "MC/line15.mp3"
    you "and made Canada friends,"
    voice "MC/line16.mp3"
    you "And wore… Canada… clothes??"
    voice "MC/line17.mp3"
    you "I just."
    voice "MC/line18.mp3"
    you "..."
    voice "MC/line19.mp3"
    you "I wish we weren’t strangers when you died, Maddie."
    voice "MC/line20.mp3"
    you "I hope it was snowing when you left."

    show bg bedroom
    with fade

    narrator "After lying on the floor for a while, you finally blink your stinging eyes open."
    narrator "Wiping away tears, you blink once more."
    narrator "Then again."
    narrator "and again."
    show black
    narrator "Then you realize, your room is completely dark."

label move_forward_choice:
    menu:
        "Move Forward":
            jump move_forward

        "Keep lying down":
            voice "MC/line21.mp3"
            you "I'm probably dreaming again..."
            narrator "You lie back down on your back."
            narrator "Nothing happens."
            jump move_forward_choice

label move_forward:

    show black
    voice "MC/line22.mp3"
    you "Guess I’ll try to explore."
    narrator "The room is pitch black. You lift your hands up to your face, but you can’t see them at all."
    voice "MC/line23.mp3"
    you "I better just like, crawl so I don’t bump into anything."
    narrator "You go on all fours and start crawling your way forward, making your way to where you think the wall with the light switch is."
    play sound "audio/sfx_snowing.mp3" volume 0.2
    narrator "However, you never find the wall."
    play sound "audio/sfx_snow_walking.mp3" volume 0.2

    narrator "The path below you grows colder, and colder until…"
    voice "MC/line24.mp3"
    you "Is this... snow?"

    scene bg snow
    with fade

    narrator "The room lights up."
    narrator "All that surrounds you are piles of snow."
    stop sound fadeout 0.5

label build_snowman_choice:
    menu:
        "Look Around":
            narrator "You can’t find an exit. There is only snow."
            jump build_snowman_choice
        "Build A Snowman":
            narrator "Bored, you decide to build a snowman."
            voice "MC/line25.mp3"
            you "I should make..."
            jump build_snowman

label build_snowman:
    menu:
        "My Dog":
            jump build_snowman_dog
        "Handsum Madong":
            jump build_snowman_handsum_madong

label build_snowman_dog:
    #line26
    you "Aaaand there!"
    scene bg snow2
    show dog
    narrator "You look at your creation."
    narrator "Sure, he looks a bit silly but. That’s your dog right there."
    #line27
    you "Man, I really miss you boy."
    #line28
    you "Greatest boy that ever lived."

    menu:
        "Pat the dog's head":
            narrator "You pat the snowdog’s head."
            #line29
            you "Good boy!"
            narrator "In a few seconds, your crusty white dog is alive again,"
            narrator "jumping up and down, and looking at you with those adorable beady eyes."

            play sound "audio/sfx_bark.mp3" volume 0.7
            dog "Arf!"
            narrator "After playing with your dog for a while, you notice him start to melt."
            narrator "He’s melting very fast."
            #line30
            you "Oh, my sweet boy..."
            #line31
            you "I think it's time to say goodbye."
            narrator "In his last moments, you press your temple to his. You tell him how much he is loved and how much you miss him."
            narrator "He knows and he loves you more. More than you’ll ever know."
            #line32
            you "There’s still snow…"
            jump build_another_snowman

label build_another_snowman:
    menu:
        "Build Handsum Madong":
            jump build_snowman_handsum_madong
        "Build Maddie":
            jump build_snowman_maddie
        
label build_snowman_maddie:
    scene bg snow2
    narrator "After hesitating for a moment, you begin to build a snowman of Maddie."
    narrator "Your freezing hands gently press the cold snow into an odd shape."
    narrator "And slowly"
    narrator "The form feels more and more familiar"

    show maddie normal
    narrator "before you know it– you’re holding her again."

    play sound "maddie/maddie_snow1.mp3"
    maddie "I can’t stay long"
    play sound "maddie/maddie_snow2.mp3"
    maddie "I just wanted to tell you that..."
    play sound "maddie/maddie_snow3.mp3"
    maddie "I missed you."

    menu:
        "Tell her you missed her too":
            narrator "snowmen don't have ears"
        
    play sound "maddie/maddie_snow4.mp3"
    maddie "I missed you, so bad."
    play sound "maddie/maddie_snow5.mp3"
    maddie "Did you ever think of me?"

    menu:
        "I miss you Maddie":
            narrator "snowmen don't have ears"

    show maddie crying
    play sound "maddie/maddie_snow6.mp3"
    maddie "I thought of you a lot."
    play sound "maddie/maddie_snow7.mp3"
    maddie "You couldn't have known, but"
    play sound "maddie/maddie_snow8.mp3"
    maddie "When I was sad, you’d make me giggle"
    play sound "maddie/maddie_snow9.mp3"
    maddie "When I was laughing, you’d slip into my mind and my mood would dampen."
    play sound "maddie/maddie_snow10.mp3"
    maddie "just a bit."

    menu:
        "I miss you":
            narrator "snowmen don't have ears"

    play sound "maddie/maddie_snow11.mp3"
    maddie "Are you doing well?"

    menu:
        "I miss you":
            narrator "snowmen don't have ears"
        "Come back":
            narrator "snowmen don't have ears"

    play sound "maddie/maddie_snow12.mp3"
    maddie "Live well, y/n"

    menu:
        "I love you":
            narrator "snowmen don't have ears"
            narrator "..."
            narrator "but they knew what you meant."
            jump ending_scene
        "I love you":
            narrator "snowmen don't have ears"
            narrator "..."
            narrator "but they knew what you meant."
            jump ending_scene
        "I love you":
            narrator "snowmen don't have ears"
            narrator "..."
            narrator "but they knew what you meant."
            jump ending_scene

label build_snowman_handsum_madong:
    scene bg madong
    show madong
    madong "Hey there, buddy."
    madong "Stay in school."

    jump ending_sceness