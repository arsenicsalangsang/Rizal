# Define the Narrator character
define Narrator = Character('Narrator', color="#007BFF")
define Rizal = Character('Rizal', color="#FF5733")

# Image definitions
image flag = "flag.jpg"
image bg1 = "bg1.jpg"
image revolution = "revolution.jpg"
image monumenttondo = "monumenttondo.jpg"
image writingrizal = "writingrizal.jpg"
image rizaldecline = "rizaldecline.png"
image rizalleader = "rizalleader.webp"
image welfare2 = "welfare2.jpg"
image struggles = "struggles.jpg"
image exile = "exile.jpg"
image PhWar = "PhWar.png"
image nounity = "nounity.png"
image restartexit = "restartexit.jpg"
image gameover = "gameover.jpg"
image scene8 = "scene8.png" 
image firstwrite = "firstwrite.jpg"
image nolime = "nolime.jpg"
image madrid = "madrid.jpg"
image deskrizal = "deskrizal.jpg"
image rizalnarrate = "rizalnarrate.png"
image elfili = "elfili.webp"

label start:
    jump scenario_7

label scenario_7:
    # Background and music for Scenario 7
    play music "audio/suspense.mp3" loop
    scene flag with fade

    # Question for Scenario 7
    Narrator "Do you want Rizal to write the Constitución de La Liga Filipina?"

    menu:
        "Yes":
            jump write_constitution
        "No":
            jump no_constitution

label write_constitution:
    # Background and music transition
    scene bg1 with dissolve
    play music "audio/success.mp3" loop

    # Frame 1 Storyline
    show rizal at left
    Narrator "La Liga Filipina, founded by José Rizal, aimed to unite Filipinos and improve society. Its rules, secretly printed in Hong Kong, required members to be loyal, honest, and committed to helping the group’s goals."

    hide rizal

    scene revolution with dissolve
    Narrator "The Liga inspired leaders like Andres Bonifacio and Apolinario Mabini, leading to the Philippine revolution."

    scene monumenttondo with dissolve
    Narrator "In 1903, a monument in Tondo was built to honor its role in the fight for freedom."

    scene writingrizal with dissolve
    Narrator "José Rizal drafted La Liga Filipina's constitution, aiming for mutual protection, justice, education, economic progress, and meaningful reforms—key steps toward a united Filipino nation."

    # Transition to Scenario 8
    stop music fadeout 3.0
    jump scenario_8

label no_constitution:
    # Background and music for "No" choice
    play music "audio/violin.mp3" volume 0.3 loop

    # Short cutscene for the consequences of saying "No"
    scene struggles with dissolve
    Narrator "Without the Constitución de La Liga Filipina, the unity and organization needed to guide the people were lost. As a result, Filipinos struggled in their daily lives, without a clear direction or the reforms that could have improved their society."

    scene nounity with dissolve
    Narrator "Without Rizal's vision, the hopes for a unified, independent Philippines remained unmet. This lack of leadership led to confusion and division, making the struggle for freedom and identity harder, especially during American colonization."



    # Transition to Game Over
    stop music fadeout 3.0
    scene gameover with fade
    Narrator "Game Over."

    # Restart Option
    scene restartexit with dissolve
    menu:
        "Restart":
            jump scenario_7

        "Exit":
            return

label scenario_8:
    # Frame 2: Writing Noli Me Tangere and El Filibusterismo
   
    play music "cinematic.mp3" loop
    scene scene8 with fade
    
    Narrator "continue..."
    
    scene firstwrite with fade
   
    Narrator "Rizal is filled with determination, but he knows the risks of challenging Spanish authorities. Will he commit to writing his first novel?"

    menu:
        "Rizal begins writing Noli Me Tangere.":
            jump write_noli
        "Rizal hesitates, fearing the consequences.":
            jump hesitate_noli

label write_noli:
    # Successful writing scene
    scene nolime with dissolve
    Narrator "Rizal starts Noli Me Tangere, pouring his heart into the story of Filipino suffering under Spanish rule. His journey of reform begins."
    
    scene madrid with dissolve
    Narrator "In 1884, while studying in Madrid, Rizal begins writing Noli Me Tangere, a novel that depicts the social and political issues in the Philippines under Spanish rule."


    scene deskrizal with dissolve
    # Frame 1 Storyline
    show rizal at left 
    Rizal "This story will reveal the truth about the plight of my people. It is my duty to tell it."

    # Proceed to writing El Filibusterismo
    scene elfili with dissolve
    Narrator "After the success of Noli Me Tangere, Rizal starts writing El Filibusterismo, continuing his mission to expose societal issues and inspire change."

    # Transition to next part of the game
    stop music fadeout 3.0
    return

label hesitate_noli:
    # Hesitation leading to Game Over
    play music "audio/sad.mp3" volume 0.2 loop
    scene rizaldecline with dissolve
    Narrator "Rizal’s hesitation stifles his resolve. Without his voice, the call for reform fades into silence."

    # Transition to Game Over
    stop music fadeout 3.0
    scene gameover with fade
    Narrator "Game Over."

    # Restart Option
    scene restartexit with dissolve
    menu:
        "Restart":
            jump scenario_7

        "Exit":
            return
