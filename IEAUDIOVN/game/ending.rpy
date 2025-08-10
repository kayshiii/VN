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
    you "I said goodbye to you again last night."
    you "Sometimes,"
    you "I try to trick my brain into thinking I'm still asleep"
    you "But even when I hold my breath low, refusing to move an inch"
    you "I still wake up"
    you "And when I do,"
    you "I don't see you."

    you "But I know you're never really gone."
    you "I find traces of you in the jokes I tell, the food I eat, and in the box you left behind."
    you "Now, even if that tears my chest apart"
    you "I'll move forward."
    you "I'll keep tidying my room, hoping I'll meet you again."