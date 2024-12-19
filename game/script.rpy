# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# $ Zeil = Character('Zeil', color="#E03B8B")
default Zeil = Character('Zeil', color="#E03B8B")       
default Narrator = Character('Narrator', color="#E03B8B")
default Pepe = Character('Pepe')
default Paciano = Character('Paciano')
# The game starts here.



#Character Images:
image pepe:
    "pepe.png"
    zoom 1.5

image pepe smile:
    "pepe smile.png"
    zoom 1.5

image pepe open mouth:
    "pepe open mouth.png"
    zoom 1.5

image paciano:
    "paciano calm.png"
    zoom 1.5

image paciano smile: 
    "paciano smile.png"
    zoom 1.5

image paciano talking 2:
    "paciano talking 2.png"
    zoom 1.5

image paciano talking: 
    "paciano talking.png"
    zoom 1.5

image pepe_student:
    "pepe_student.png"
    zoom 1.5

transform resize_to_1080p:
    xsize 1920
    ysize 1080

label start:
    play music "audio/birds.mp3" fadein 1.0 volume 1.5
    scene bg 1 at resize_to_1080p
    "A peaceful rural setting in the Philippines. We hear birds chirping, and the wind rustling through the trees. The year is 1872, and the world of Jose Rizal is about to change."

label Gomburza:
    scene gomburza at resize_to_1080p
    hide pepe
    "Narrator" "The scene shifts to the somber execution of Gomburza in 1872, their bodies hanging in public as a symbol of Spanish oppression. The sound of the crowd murmuring in fear and sorrow echoes in the background."
   
    
label Jose_Rizal:
    scene bg 3 at resize_to_1080p
    show pepe   
    "Narrator" "Jose Protacio Rizal Mercado y Alonzo Realonda, a young man from Calamba, Laguna, had dreams far beyond the borders of his hometown. But the winds of change were beginning to stir, with tensions rising against the Spanish colonial rule."
    
    show pepe
    "Narrator" "Jose was not just an aspiring scholar; he was a visionary who would one day ignite the flame of reform for the Philippines. But first, he needed to make a decision that would alter the course of his life and the nation’s future."

    stop music


    scene bg 2 at resize_to_1080p
    hide pepe
    "Rizal and his brother Paciano are seated by the window, gazing out into the distance."

    scene bg 2 at resize_to_1080p
    show paciano talking at right
    "Paciano" "We should change the surname you're using, Pepe! We need to avoid suspicion, and it's the only way for you to enter formal schooling. We need to lessen the obstacles to our goals."

    show pepe open mouth at left
    "Pepe" "I know, brother, but let's decide carefully."


# label decision_of_pepe:
#     default learned = False

#     menu:
#         "Change the surname":
#             jump choices1_a_1
#         "Don't Change":
#             jump choices1_b_2


label choices:
    default learned = False

menu:
    "Change the surname":
        jump choices1_a
    "Don't Change":
        jump choices1_b

label choices1_a:
    Zeil "Jose decided to keep the original surname of his family, Mercado, but things did not go as planned."
    jump choices1_common

label choices1_b:
    Zeil "The original surname, Mercado, brought challenges that altered his course in history."
    jump choices2_common

label choices1_common:
    Zeil "Pepe decided to changes his surname"
    jump School

label choices2_common:
    scene pepe house soldier at resize_to_1080p
    Narrator "He was unable to accomplish his goals, and since the Mercado family was under suspicion, his entire family was arrested."
    return


label School:
    scene bg classroom at resize_to_1080p 
    show pepe_student
    "Narrator" "Jose Rizal began his higher education at the prestigious Ateneo Municipal de Manila. In this esteemed institution, he thrived, excelling in his studies and earning accolades for his intellectual brilliance. His professors quickly recognized his potential, and Rizal’s reputation as a gifted scholar began to grow."
    

    
return





# label choices1_a_1:
#     Zeil "Good choice! Jose decides to change the surname."
#     $ learned = True
#     jump choices1_common

# label choices1_b_2:
#     Zeil "Jose decided to keep the original surname of his family, Mercado, but things did not go as planned."
#     jump choices1_common_2

# label choices1_common:
#     "Narrator" "Jose's decision to change the surname set him on a path to shape his destiny in unexpected ways."
#     jump "Scenario_2"

# label choices1_common_2:
#     "Narrator" "The original surname, Mercado, brought challenges that altered his course in history."
#     return



# label Scenario_2:

#     Narrator " Scenario 2: School involvement. "
#     return


# label flags:
#     if learned:
#         Zeil "If you learned a thing or two, please like the video!"
#     else:
#         Zeil "You can check out my other videos to learn more about game development!"



# label Scenario1GomBurza:
#     scene gomburza at resize_to_1080p
#     hide pepe
#     "Narrator" "The scene shifts to the somber execution of Gomburza in 1872, their bodies hanging in public as a symbol of Spanish oppression. The sound of the crowd murmuring in fear and sorrow echoes in the background."

    

# label sprites:
#     "Zeil"  "But wait, where are you?"
#     show epep
#     "Zeil"  "Oh!"
#     show zeil angry
#     "Zeil" "It's not like I was looking for you or anything."
#     show extra normal at right
#     "Random Girl" "Tsundere..."
#     hide extra
#     "Zeil" "..."
# label character:
#     show zeil bored
#     "Zeil" "Wow... this is too plain."
#     show zeil smile2 with dissolve
#     "Zeil" "I want my color to be bright pink!"
#     Zeil "Wonderful!"    
# label background:
#     Zeil "Come on! Let's go the gym."
#     scene bg gym at resize_to_1080p
#     with fade
    
#     show zeil smile2 at left
#     Zeil "You got here faster than I did!"  
# label bgm:
#     play music "audio/bgm_basketball.mp3" fadein 1.0 volume 1.5
#     Zeil "Oh, the basketball team is playing?"
#     Zeil "It's too loud. I'll meet you in the classroom."
    
#     stop music fadeout 1.0
#     scene bg classroom
#     with fade
    
# label sfx:
#     play sound "audio/sfx_bell.mp3"
#     Zeil "Oh no. It's already time."

# label choices:
#     default learned = False
#     Zeil "Did you learn a thing or two?"
# menu:
#     "Yes":
#         jump choices1_a
#     "...":
#         jump choices1_b
# label choices1_a:
#     Zeil "Good!"
#     $ learned = True
#     jump choices1_common

# label choices1_b:
#     Zeil "..."
#     jump choices1_common

# label choices1_common:
#     Zeil "For more effects, you can check out Ren'Py's guides."
#     Zeil "The link can be found in the description."

# label flags:
#     if learned:
#         Zeil "If you learned a thing or two, please like the video!"
#     else:
#         Zeil "You can check out my other videos to learn more about game development!"

#     return





















