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

    play music "audio/bgm_winter.mp3" fadein 0.5 volume 0.4
    you "This is… kinda disgusting."

    scene bg snowglobe
    with fade

    narrator "The edges of your lips crease up, and for the first time in a while, you can’t help but crack into a smile."
    you "When we were kids, she kept talking about how much she wanted to play in the snow."

    show bg philippines
    with fade

    you "We waited for it all year but, turns out we don’t have that kind of weather in the Philippines."
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
    you "Oh- oh my god"
    narrator "You scramble to find something to wipe it with, but in your hurry…"
    stop sound fadeout 0.5

    show black
    play sound "audio/sfx_thud.mp3" volume 0.5
    narrator "You slip."


    scene black with fade
    pause 0.5
    show text "{size=30}{color=#ffffff} The Next day...{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    pause 0.5

label next_day:
    scene bg bedroom
    with fade

    you "I know I should’ve just like, called or something."
    you "Maddie wouldn’t have told me she was sick but–"
    you "I know I would've noticed."
    you "...yeah?"
    you "Even if she had moved to Canada and-"
    you "and made Canada friends,"
    you "And wore… Canada… clothes??"
    you "I just."
    you "..."
    you "I wish we weren’t strangers when you died, Maddie."
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
            you "I'm probably dreaming again..."
            narrator "You lie back down on your back."
            narrator "Nothing happens."
            jump move_forward_choice

label move_forward:

    show black

    you "Guess I’ll try to explore."
    narrator "The room is pitch black. You lift your hands up to your face, but you can’t see them at all."
    you "I better just like, crawl so I don’t bump into anything."
    narrator "You go on all fours and start crawling your way forward, making your way to where you think the wall with the light switch is."

    play sound "audio/sfx_snowing.mp3" volume 0.2
    narrator "However, you never find the wall."
    play sound "audio/sfx_snow_walking.mp3" volume 0.2

    narrator "The path below you grows colder, and colder until…"
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
            you "I should make..."
            jump build_snowman

label build_snowman:
    menu:
        "My Dog":
            jump build_snowman_dog
        "Handsum Madong":
            jump build_snowman_handsum_madong

label build_snowman_dog:
    you "Aaaand there!"
    scene bg snow2
    show dog
    narrator "You look at your creation."
    narrator "Sure, he looks a bit silly but. That’s your dog right there."
    you "Man, I really miss you boy."
    you "Greatest boy that ever lived."

    menu:
        "Pat the dog's head":
            narrator "You pat the snowdog’s head."
            you "Good boy!"
            narrator "In a few seconds, your crusty white dog is alive again,"
            narrator "jumping up and down, and looking at you with those adorable beady eyes."

            play sound "audio/sfx_bark.mp3" volume 0.7
            dog "Arf!"
            narrator "After playing with your dog for a while, you notice him start to melt."
            narrator "He’s melting very fast."
            you "Oh, my sweet boy..."
            you "I think it's time to say goodbye."
            narrator "In his last moments, you press your temple to his. You tell him how much he is loved and how much you miss him."
            narrator "He knows and he loves you more. More than you’ll ever know."
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

    maddie "I can’t stay long"
    maddie "I just wanted to tell you that..."
    maddie "I missed you."

    menu:
        "Tell her you missed her too":
            narrator "snowmen don't have ears"
        
    maddie "I missed you, so bad."
    maddie "Did you ever think of me?"

    menu:
        "I miss you Maddie":
            narrator "snowmen don't have ears"

    show maddie crying
    maddie "I thought of you a lot."
    maddie "You couldn't have known, but"
    maddie "When I was sad, you’d make me giggle"
    maddie "When I was laughing, you’d slip into my mind and my mood would dampen."
    maddie "just a bit."

    menu:
        "I miss you":
            narrator "snowmen don't have ears"

    maddie "Are you doing well?"

    menu:
        "I miss you":
            narrator "snowmen don't have ears"
        "Come back":
            narrator "snowmen don't have ears"

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
    show bg snow2
    show madong
    madong "Hey there, buddy."
    madong "Stay  in school."

    jump ending_scene