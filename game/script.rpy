# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# $ Zeil = Character('Zeil', color="#E03B8B")
default Zeil = Character('Zeil', color="#E03B8B")       
default Narrator = Character('Narrator', color="#E03B8B")
# The game starts here.



#Character Images:
image pepe:
    "pepe.png"
    zoom 1.5

transform resize_to_1080p:
    xsize 1920
    ysize 1080

label start:
    play music "audio/birds.mp3" fadein 1.0 volume 1.5
    scene bg 1 at resize_to_1080p
    "A peaceful rural setting in the Philippines. We hear birds chirping, and the wind rustling through the trees. The year is 1872, and the world of Jose Rizal is about to change."
   
    scene bg 3 at resize_to_1080p
    show pepe 
    "Narrator" "Jose Protacio Rizal Mercado y Alonzo Realonda, a young man from Calamba, Laguna, had dreams far beyond the borders of his hometown. But the winds of change were beginning to stir, with tensions rising against the Spanish colonial rule."
    
    hide pepe
    "Narrator" "Jose was not just an aspiring scholar; he was a visionary who would one day ignite the flame of reform for the Philippines. But first, he needed to make a decision that would alter the course of his life and the nation’s future."

    scene bg 2 at resize_to_1080p
    "Rizal and his brother Paciano are seated by the window, gazing out into the distance."

label Scenario1GomBurza:
    scene gomburza at resize_to_1080p
    show pepe
    "Narrator" "The scene shifts to the somber execution of Gomburza in 1872, their bodies hanging in public as a symbol of Spanish oppression. The sound of the crowd murmuring in fear and sorrow echoes in the background."
    
label sprites:
    "Zeil"  "But wait, where are you?"
    show epep
    "Zeil"  "Oh!"
    show zeil angry
    "Zeil" "It's not like I was looking for you or anything."
    show extra normal at right
    "Random Girl" "Tsundere..."
    hide extra
    "Zeil" "..."
label character:
    show zeil bored
    "Zeil" "Wow... this is too plain."
    show zeil smile2 with dissolve
    "Zeil" "I want my color to be bright pink!"
    Zeil "Wonderful!"    
label background:
    Zeil "Come on! Let's go the gym."
    scene bg gym at resize_to_1080p
    with fade
    
    show zeil smile2 at left
    Zeil "You got here faster than I did!"  
label bgm:
    play music "audio/bgm_basketball.mp3" fadein 1.0 volume 1.5
    Zeil "Oh, the basketball team is playing?"
    Zeil "It's too loud. I'll meet you in the classroom."
    
    stop music fadeout 1.0
    scene bg classroom
    with fade
    
label sfx:
    play sound "audio/sfx_bell.mp3"
    Zeil "Oh no. It's already time."










label choices:
    default learned = False
    Zeil "Did you learn a thing or two?"
menu:
    "Yes":
        jump choices1_a
    "...":
        jump choices1_b
label choices1_a:
    Zeil "Good!"
    $ learned = True
    jump choices1_common

label choices1_b:
    Zeil "..."
    jump choices1_common

label choices1_common:
    Zeil "For more effects, you can check out Ren'Py's guides."
    Zeil "The link can be found in the description."

label flags:
    if learned:
        Zeil "If you learned a thing or two, please like the video!"
    else:
        Zeil "You can check out my other videos to learn more about game development!"

    return





















