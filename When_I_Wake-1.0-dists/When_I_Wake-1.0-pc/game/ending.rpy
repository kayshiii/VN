# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character('You', color = "#ffffff")
define mom = Character('Mom', color = "#6999ff")
define dog = Character('Dog', color = "#b700ff")
define madong = Character('Hansum Madong', color = "#22ff04")
define maddie = Character('Maddie', color = "#8c00ff")
define narrator = Character(None, what_color="#979797", what_italic=True)

label ending_scene:
    scene bg bedroom with fade
    play music "audio/bgm_intro_outro.mp3" volume 0.5
    voice "MC/line58.mp3"
    you "I said goodbye to you again last night."
    voice "MC/line59.mp3"
    you "Sometimes,"
    voice "MC/line60.mp3"
    you "I try to trick my brain into thinking I'm still asleep"
    voice "MC/line61.mp3"
    you "But even when I hold my breath low, refusing to move an inch"
    voice "MC/line62.mp3"
    you "I still wake up"
    voice "MC/line63.mp3"
    you "And when I do,"
    voice "MC/line64.mp3"
    you "I don't see you."
    voice "MC/line65.mp3"
    you "But I know you're never really gone."
    voice "MC/line66.mp3"
    you "I find traces of you in the jokes I tell, the food I eat, and in the box you left behind."
    voice "MC/line67.mp3"
    you "Now, even if that tears my chest apart"
    voice "MC/line68.mp3"
    you "I'll move forward."
    voice "MC/line69.mp3"
    you "I'll keep tidying my room, hoping I'll meet you again."