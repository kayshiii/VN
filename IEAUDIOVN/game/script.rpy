# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define zeil = Character('Zeil', color = "#E03B8B")


# The game starts here.

label start:
    "*knocking*"
    "Nak, I left your dinner outside the door."
    "..."
    "Eat it while it’s warm."
    "..."
    "Thanks mom"
    "Oh, it smells like pares."
    "I don’t think she’s made that since Maddie stopped coming over…"
    "Man."
    "You look over to the box of stuff Maddie left behind. Two things catch your attention"

label sprites:
    "Zeil"  "But wait, where are you?"
    show zeil delighted
    "Zeil"  "Oh!"
    show zeil angry
    "Zeil" "It's not like I was looking for you or anything."
    show extra normal at right
    "Random Girl" "Tsundere..."
    hide extra
    "Zeil" "..."