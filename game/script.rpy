default Narrator = Character('Narrator', color="#E03B8B")
default Rizal = Character('Rizal')

# Character Images
image rizal:
    "rizal.png"
    zoom 1.5

image rizal smiling:
    "rizal_smiling.png"
    zoom 1.5

image rizal thinking:
    "rizal_thinking.png"
    zoom 1.5

transform resize_to_1080p:
    xsize 1920
    ysize 1080

label start:
    play music "audio/intro.mp3" fadein 1.0 volume 1.5
    scene bg 4 at resize_to_1080p
    "The year is 1872, and the world of Jose Rizal is about to change."

label Scenario_9: 
    scene bg 5 at resize_to_1080p
    show rizal at left
    "Narrator" "After witnessing the execution of Gomburza, Jose Rizal embarks on a journey to different countries, determined to gather knowledge and ideas to bring reform to the Philippines."

    play music "audio/travel.mp3" fadein 1.0 volume 1.5
    scene bg 6 at resize_to_1080p
    hide rizal
    "Narrator" "Rizal travels across continents, observing governance, culture, and societal systems that could inspire his vision of a better nation."

    menu:
        "Apply the lessons Rizal learns":
            jump Lessons_Applied
        "Dismiss the lessons Rizal learns":
            jump Lessons_Dismissed

label Lessons_Applied:
    "Narrator" "Rizal returns home with a clear vision: honest leadership from Singapore, the courage for freedom from Spain, discipline from Japan, progress from America, education from France, and rigor from Germany. He commits to using these ideals to inspire reforms for his country."
    jump Scene_Selection

label Lessons_Dismissed:
    "Narrator" "Rizal becomes cynical and disheartened. He focuses only on the flaws he saw in the countries he visited and fails to see the value of the positive lessons they offered."
    scene bg philippine at resize_to_1080p
    "Narrator" "Back in the Philippines, Rizal’s disillusionment with his journey spreads. The reform movement lacks vision and unity. His failure to integrate the lessons of progress, freedom, and resilience leaves the people without the inspiration they desperately need."
    
    scene bg philippine at resize_to_1080p
    "Narrator" "As tensions rise, a revolution breaks out. However, it lacks strong leadership and a clear purpose. The movement falters and collapses, crushed by the Spanish authorities."
    
    show rizal smiling at center
    "Rizal" "I could have been the change... but my doubts and failure to see the bigger picture have cost my people their chance at freedom."
    show rizal thinking at center
    "Narrator" "The Philippines remains in the grip of colonial rule, its people disheartened and without the leadership needed to break free."
    
    menu
        "Restart the game"
        return

label Scene_Selection:
    # Scene 1: Singapore
    scene bg singapore at resize_to_1080p
    "Narrator" "In the English colony of Singapore, Rizal is impressed by its progress and the confidence of its people."
    show rizal smiling at right
    "Rizal" "A nation led with dignity and honesty can achieve so much. Our leaders must aspire to govern like this."

    # Scene 2: Spain
    scene bg spain at resize_to_1080p
    "Narrator" "In Spain, Rizal experiences contrasting emotions."

    menu:
        "Visit Barcelona":
            jump Barcelona_Scene
        "Visit Madrid":
            jump Madrid_Scene

label Barcelona_Scene:
    scene bg barcelona at resize_to_1080p
    show rizal thinking at right
    "Narrator" "Barcelona’s dirt and unwelcoming attitude disappoint him, but he realizes there is something to learn from the resilience of the people here."
    show rizal smiling at center
    "Rizal" "Although this city feels gritty, there is strength in its struggle for freedom. We must embrace this resilience in our fight for independence."
    jump Conclude_in_Madrid

label Madrid_Scene:
    scene bg madrid at resize_to_1080p
    show rizal thinking at left
    "Narrator" "Madrid gives Rizal hope. It's vibrant, full of intellectual energy. There's a sense of freedom that stirs something in his heart."
    show rizal smiling at left
    "Rizal" "The ideals of freedom and courage here must be embraced by every Filipino. This city embodies the spirit of what we should strive for."
    jump Conclude_in_Madrid

label Conclude_in_Madrid:
    scene bg madrid at resize_to_1080p
    show rizal thinking at center
    "Narrator" "Regardless of his earlier observations, Rizal finds himself deeply inspired by Madrid. The intellectual atmosphere and the ideals of freedom solidify his resolve to bring change to the Philippines."
    "Narrator" "As Rizal continues his journey, his vision for reform becomes clearer. He is ready to take the next steps in his mission to awaken the Filipino spirit."
   
label Japan_Scene
    scene bg madrid at resize_to_1080p
    show rizal smiling at center
    "Narrator" "Rizal sees Japan’s unique blend of discipline and cultural pride."
    show rizal smiling at left
    "Rizal" "Their cleanliness, order, and respect for tradition allow Japan to progress without losing its identity. The Philippines must learn this balance."

label America_Scene
    scene bg madrid at resize_to_1080p
    show rizal thinking at center
    "Narrator" "America’s advancements and industries inspire Rizal, but he cannot ignore its racial inequalities."
    show rizal thinking at right
    "Rizal"  'Progress means nothing without equality. True freedom must lift all people, not just a privileged few.'

label France_Scene
    scene bg madrid at resize_to_1080p
    show rizal smiling at right
    "Narrator" "Immersed in France’s intellectual atmosphere, Rizal realizes the power of education."
    show rizal smiling at center
    "Rizal" "Through education, we can empower Filipinos to lead their country to greatness."

label Germany_Scene
    scene bg madrid at resize_to_1080p
    show rizal smiling at center
    "Narrator" "In Germany, Rizal finds his ideal nation, admiring its academic excellence and discipline."
    show rizal smiling at left
    "Rizal" "The discipline and knowledge here are the foundations of progress. If our people adopt these values, we can transform the Philippines."
   
    return
