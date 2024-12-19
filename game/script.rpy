label scenario_7:
    # Background and music for Scenario 7
    play music "bgm_scenario7.mp3" loop
    scene bg_philippine_flag with fade

    # Question for Scenario 7
    narrator "Do you want Rizal to write the Constitución de La Liga Filipina?"

    menu:
        "Yes":
            jump write_constitution
        "No":
            jump no_constitution

label write_constitution:
    # Background and music transition
    scene bg_meeting_room with dissolve
    play music "bgm_success.mp3" loop

    # Frame 1 Storyline
    show rizal_portrait at left
    narrator "La Liga Filipina, founded by José Rizal, aimed to unite Filipinos and improve society. Its rules, secretly printed in Hong Kong, required members to be loyal, honest, and committed to helping the group’s goals."
    hide rizal_portrait

    show bg_tondo_monument at right
    narrator "The Liga inspired leaders like Andres Bonifacio and Apolinario Mabini, leading to the Philippine revolution. In 1903, a monument in Tondo was built to honor its role in the fight for freedom."
    hide bg_tondo_monument

    # Frame 2 Storyline
    show rizal_writing at center
    narrator "José Rizal authored the constitution of La Liga Filipina, outlining 'end goals', which hold significant importance:\n- Mutual protection in all want and necessity\n- Defense against all violence and injustice\n- Encourage education, agriculture, industry, and commerce\n- Study and application of reforms\nThese goals reflect Rizal's vision for a united and empowered Filipino nation."
    hide rizal_writing

    # Transition to Scenario 8
    stop music fadeout 3.0
    return

label no_constitution:
    # Background and music for "No" choice
    scene bg_dark with fade
    play music "bgm_game_over.mp3"

    # Game Over Text
    narrator "The Constitución de La Liga Filipina will not exist.\nThe objectives of Rizal in the 'End Goals' will not happen."
    narrator "Game Over"

    # Restart Option
    menu:
        "Restart":
            jump scenario_7

        "Exit":
            return

label start:
    # Entry point to the game
    jump scenario_7
