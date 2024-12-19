image flag:
    "flag.png"

image bg1:
    "bg 1.jpg"
image revolution:
    "revolution.jpg"

image monumenttondo:
    "monumenttondo.jpg"
image writingrizal:
    "writingrizal.jpg"


label scenario_7:
    # Background and music for Scenario 7
    play music "bgm_scenario7.mp3" loop
    scene flag with fade

    # Question for Scenario 7
    narrator "Do you want Rizal to write the Constitución de La Liga Filipina?"

    menu:
        "Yes":
            jump write_constitution
        "No":
            jump no_constitution

label write_constitution:
    # Background and music transition
    scene bg1 with dissolve
    play music "bgm_success.mp3" loop

    # Frame 1 Storyline
    show rizal at left
    narrator "La Liga Filipina, founded by José Rizal, aimed to unite Filipinos and improve society. Its rules, secretly printed in Hong Kong, required members to be loyal, honest, and committed to helping the group’s goals."

    hide rizal

    scene revolution with dissolve
    

    narrator "The Liga inspired leaders like Andres Bonifacio and Apolinario Mabini, leading to the Philippine revolution."


    scene monumenttondo with dissolve
    narrator "In 1903, a monument in Tondo was built to honor its role in the fight for freedom."

    # Frame 2 Storyline
    
    scene writingrizal with dissolve
    narrator "José Rizal drafted La Liga Filipina's constitution, aiming for mutual protection, justice, education, economic progress, and meaningful reforms—key steps toward a united Filipino nation."    

    # Transition to Scenario 8
    stop music fadeout 3.0
    return

label no_constitution:
    # Background and music for "No" choice
    scene bg_dark with fade
    play music "bgm_game_over.mp3" loop

    # Short cutscene for the consequences of saying "No"
    scene rizal_portrait with dissolve
    narrator "José Rizal declined to involve himself in any groups or movements."
    narrator "Without Rizal's leadership and ideas, the formation of La Liga Filipina was never realized."
    play music "bgm_sad_violin.mp3" loop
    show rizal_sitting at center with fade
    narrator "Rizal did not give us any plans to work for the welfare of the Philippines."
    narrator "Without his ideas, the Philippines struggled in its quest for unity and freedom."

    # Adding symbolic imagery
    show rizal_in_exile at left
    narrator "He remained in exile, unable to guide the nation toward a brighter future."
    show bg_empty_field at right with fade
    narrator "The Philippines remained fragmented, with no unified cause."

    # Final message
    narrator "Rizal's vision of a united, empowered Philippines was lost."

    # Transition to Game Over
    stop music fadeout 3.0
    scene bg_dark with fade
    narrator "Game Over."

    # Restart Option
    menu:
        "Restart":
            jump scenario_7

        "Exit":
            return

label start:
    # Entry point to the game
    jump scenario_7
