     
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



label choices:
    default learned = False

menu:
    "Change the surname":
        jump choices1_a
    "Don't Change":
        jump choices1_b

label choices1_a:
    "Jose decided to keep the original surname of his family, Mercado, but things did not go as planned."
    jump choices1_common

label choices1_b:
    "The original surname, Mercado, brought challenges that altered his course in history."
    jump choices2_common

label choices1_common:

    "Pepe decided to changes his surname"

    Zeil "Pepe decided to change his surname"

    jump School

label choices2_common:
    scene pepe house soldier at resize_to_1080p
    Narrator "He was unable to accomplish his goals, and since the Mercado family was under suspicion, his entire family was arrested."
    return


#ATENEO VS UST

label School:
    scene bg classroom at resize_to_1080p 
    show pepe_student
    "If Jose Rizal starts to study at Ateneo Municipal De Manila and later transfers to UST. He will be able to make progress on his mission. This will follow the original historical timeline of Jose Rizal's journey becoming a nationalist."
    
label choiceschool:
    scene ateneo vs ust at resize_to_1080p
menu:
    
    "Ateneo to UST":
        jump choiceschool_a
    "UST only":
        jump choiceschool_b

label choiceschool_a:
    scene 1_ateneo at resize_to_1080p
    "Jose Rizal began his higher education at the prestigious Ateneo Municipal de Manila, where he thrived in an environment of intellectual rigor, discipline, and advanced studies. He quickly earned high grades, medals, and respect from his professors."
    
    scene fr paula de sanchez ust drawing classroom at resize_to_1080p
    "At Ateneo, Rizal was inspired by his professors, especially Fr. Francisco de Paula Sanchez, who encouraged his love for poetry and intellectual growth. His extracurricular activities in literature and physical training further shaped his character."
    
    scene 1_graduation at resize_to_1080p
    "However, after completing his degree in Bachelor of Arts, Rizal's family faced financial strain, and Rizal decided to continue his studies at the Universidad de Santo Tomas, despite his growing dissatisfaction with Spanish colonial rule and the oppressive educational system."
    
    scene eah at resize_to_1080p
    "At UST, Rizal enrolled in Philosophy and Letters, but he quickly grew disillusioned. The harsh, repressive teaching methods of the Dominican professors and racial discrimination against Filipino students made it difficult for him to focus on his studies."
    
    scene eah2 at resize_to_1080p
    "Despite the struggles, Rizal pursued a medical course and won literary awards for works that expressed his growing nationalist sentiments. His time at UST further fueled his desire for reform, and he eventually decided to continue his education abroad, where he could work towards his vision of change for the Philippines."
    jump Scenario_3


label choiceschool_b:
    scene eah2 at resize_to_1080p
    "Jose Rizal entered the Universidad de Santo Tomas in 1877, pursuing Philosophy and Letters, but quickly became disheartened by the oppressive atmosphere, outdated teaching methods, and racial discrimination from Dominican professors."
    "Struggling without the intellectual stimulation he had at Ateneo, his academic performance declined, and his passion for reform faded. His disillusionment led him to abandon his original mission, and his time at UST became a period of stagnation, ultimately thwarting his dreams of improving his country."
    return

label Scenario_3:
    scene eah
    "Jose Rizal has excelled in his studies at the Ateneo de Manila, displaying a keen intellect and a thirst for knowledge. However, the educational system in the Philippines under Spanish colonial rule feels stifling to his curious mind."
    
label choiceabroad:
    scene eah

menu:
    "Go to Abroad":
        jump choiceabroad_a
    "Jose Rizal remains in the Philippines":
        jump choiceabroad_b 

label choiceabroad_a:
    scene 1_scenario4 frames 1-3
    "In the heart of colonial Manila, a young mind yearns for freedom. Jose Rizal, a brilliant student at the Ateneo de Manila, feels the weight of the Spanish colonial yoke. The implacable curriculum and oppressive atmosphere suppress his intellectual curiosity."

    "A spark ignites within Rizal’s soul. He dreams for a Philippines liberated from the chains of colonialism. But to realize this dream, he must seek knowledge beyond the confines of his homeland."
    scene 2_scenario4 choice 2
    "A crucial decision looms large. Should Rizal remain in the Philippines? Where his potential may be limited? Or should he embark on a risky journey to Europe, seeking higher education and enlightenment?"
    
    scene 4_bids farewell scene4
    "Rizal chooses the path less traveled. He bids farewell to his family and friends, his heart filled with hope and determination. As the ship sets sail, a new chapter in his life begins, a chapter that will shape the destiny of a nation."
    jump Scenario_4

label choiceabroad_b:
    scene eah
    "Jose Rizal, denied the opportunity to broaden his horizons, became increasingly disillusioned with the limitations of the colonial system."
    "Jose Rizal may find himself confined to a conventional career within the colonial bureaucracy, gradually losing his idealism and becoming unconcerned or not interested with the existing order."
    return

label Scenario_4:
    scene medfield
    "Choosing a degree of Medicine"
    scene medfield2
    "Do you want to study in the Medical Field?"

label choicemed:
    
menu:
    "Yes":
        jump choicemed_a
    "No":
        jump choicemed_b 

label choicemed_a:
    "When Rizal's transferred and took up the Medical course."
    scene wpac
    "His brother Paciano reminded him to focus on his true purpose:"
    scene wpac2
    "While you may finish your medical studies in Barcelona, go to Madrid instead. Your journey is about more than just medicine—it's about pursuing what truly matters to you."
    scene wpac2
    "Rizals Following his advice, he went to Madrid, a hub of knowledge and opportunity. In 1884, he earned his Licentiate in Medicine from the Universidad Central de Madrid. By 1885, he completed all requirements for a Doctor of Medicine but couldn't afford the diploma. To further his skills, he worked part-time in clinics, specializing in ophthalmology, a field aligned with his passion for helping others."
    jump Scenario_6

label choicemed_b:
    scene medfield2
    "Rizal's wouldn't be earned the Licentiate in Medicine from Universidad Central de Madrid"    
    return

label Scenario_6:
    "Do you want to Involve in Groups and Movement?"














