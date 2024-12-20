default Narrator = Character('Narrator', color="#E03B8B")
default Pepe = Character('Pepe', color="#4e6eff")
default Paciano = Character('Paciano', color="#fcff41")
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

image pepe student:
    "pepe student.png"
    zoom 1.5

image pepe house solider:
    "pepe house soldier.PNG"

image pepe shock:
    "Scene 6/pepe shock.png"
    zoom 1.5

image pepe sad:
    "Scene 6/pepe sad.png"
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

image writing bg:
    "Scene 5/writing bg.jpg"

image barcelona bg:
    "Scene 5/barcelona bg.jpg"

image madrid bg:
    "Scene 6/madrid bg.jpg"

image madrid wrong bg:
    "Scene 6/madrid wrong bg.png"

image comite de reformadores bg:
    "Scene 6/comite de reformadores bg.jpg"

image comite de reformadores wrong bg:
    "Scene 6/comite de reformadores wrong bg.png"

image comite de propaganda bg:
    "Scene 6/comite de propaganda bg.jpg"

image comite de propaganda wrong bg:
    "Scene 6/comite de propaganda wrong bg.png"

image circulo hispano filipino bg:
    "Scene 6/circulo hispano filipino bg.jpg"

image circulo hispano filipino wrong bg:
    "Scene 6/circulo hispano filipino wrong bg.png"

image asociacion hispano filipina bg:
    "Scene 6/asociacion hispano filipina bg.jpg"

image asociacion hispano filipina wrong bg:
    "Scene 6/asociacion hispano filipina wrong bg.png"

image asociacion internacional de filipinistas bg:
    "Scene 6/asociacion internacional de filipinistas bg.jpg"

image asociacion internacional de filipinistas wrong bg:
    "Scene 6/asociacion internacional de filipinistas wrong bg.png"

image flag:
    "Scene 7/tondo bg.jpg"

image la liga filipina:
    "Scene 7/la liga filipina bg.jpg"

image revolution bg:
    "Scene 7/revolution bg.jpg"

image monumenttondo bg:
    "Scene 7/monumenttondo bg.jpg"

image writingrizal bg:
    "Scene 7/writingrizal bg.jpg"

image struggles bg:
    "Scene 7/struggles bg.jpg"

image scene8 bg:
    "Scene 8/scene8 bg.jpg"

image firstwrite bg:
    "Scene 8/firstwrite bg.jpg"

image nolime bg:
    "Scene 8/nolime bg.jpg"

image madrid noli bg:
    "Scene 8/madrid noli bg.jpg"

image deskrizal bg:
    "Scene 8/deskrizal bg.jpg"

image elfili bg:
    "Scene 8/elfili bg.webp"

image rizaldecline bg:
    "Scene 8/rizaldecline bg.jpg"

image rizal:
    "Scene 9/rizal.png"
    zoom 1.5

image rizal smiling:
    "Scene 9/rizal_smiling.png"
    zoom 1.5

image rizal thinking:
    "Scene 9/rizal_thinking.png"
    zoom 1.5

image bg 4:
    "Scene 9/bg 4.jpg"

image bg 5:
    "Scene 9/bg 5.jpg"

image bg 6:
    "Scene 9/bg 6.jpg"

image bg philippine:
    "Scene 9/bg philippine.jpg"

image bg singapore:
    "Scene 9/bg singapore.jpg"

image bg spain:
    "Scene 9/bg spain.jpg"

image bg barcelona:
    "Scene 9/bg barcelona.jpg"

image bg madrid:
    "Scene 9/bg madrid.jpg"

image bg japan:
    "Scene 9/bg japan.jpg"

image bg america:
    "Scene 9/bg america.jpg"

image ending bg:
    "Scene 9/ending bg.jpg"


transform resize_to_1080p:
    xsize 1920
    ysize 1080

# Start FLASHBACKS
label start:
    play music "audio/birds.mp3" fadein 1.0 volume 1.5
    scene bg 1 at resize_to_1080p

    Narrator "A peaceful rural setting in the Philippines. We hear birds chirping, and 
    the wind rustling through the trees. The year is 1872, and the world of Jose Rizal 
    is about to change."

label Gomburza:
    scene gomburza at resize_to_1080p
    hide pepe

    Narrator "The scene shifts to the somber execution of Gomburza in 1872, their bodies
    hanging in public as a symbol of Spanish oppression. The sound of the crowd murmuring 
    in fear and sorrow echoes in the background."
   
# Scene 1
label scene1:
    scene bg 3 at resize_to_1080p
    show pepe   

    Narrator "Jose Protacio Rizal Mercado y Alonzo Realonda, a young man from Calamba, 
    Laguna, had dreams far beyond the borders of his hometown. But the winds of change 
    were beginning to stir, with tensions rising against the Spanish colonial rule."
    
    show pepe

    Narrator "Jose was not just an aspiring scholar; he was a visionary who would one day 
    ignite the flame of reform for the Philippines. But first, he needed to make a decision 
    that would alter the course of his life and the nation's future."

    scene bg 2 at resize_to_1080p
    hide pepe

    Narrator "Rizal and his brother Paciano are seated by the window, gazing out into the 
    distance."

    scene bg 2 at resize_to_1080p
    show paciano talking at right

    Paciano "We should change the surname you're using, Pepe! We need to avoid suspicion, 
    and it's the only way for you to enter formal schooling. We need to lessen the obstacles 
    to our goals."

    show pepe open mouth at left

    Pepe "I know, brother, but let's decide carefully."

    menu:
        "Change the surname":
            jump scene1_choice1

        "Don't Change":
            jump scene1_choice2

label scene1_choice1:
    Narrator "Jose decided to use 'Rizal' as his surname."
    
    stop music
    jump scene2
    

label scene1_choice2:
    stop music
    play music "audio/violin.mp3" fadein 1.0 loop
    
    Narrator "Jose decided to use their family's surname 'Mercado'. This brought challenges to him 
    and his family."

    scene pepe house soldier at resize_to_1080p

    Narrator "Eventually, He was unable to accomplish his goals and since the Mercado family 
    was under suspicion, his entire family was arrested."

    stop music
    menu: 
        "Restart the game.":    
            return    


# Scene 2
label scene2:
    play music "audio/classroom noise.mp3" fadein 1.0 volume 0.5
    scene bg classroom at resize_to_1080p 
    show pepe student
    Pepe "Should I study in Ateneo and move to UST? or should I just study in UST?"
    
    scene ateneo vs ust at resize_to_1080p
    stop music

    menu:
        "Study in Ateneo and move to UST":
            jump scene2_choice1

        "Study in UST only":
            jump scene2_choice2

label scene2_choice1:
    play music "audio/normal day.mp3" fadein 1.0 volume 1 loop
    scene 1_ateneo at resize_to_1080p

    Narrator "Jose Rizal began his higher education at the prestigious Ateneo Municipal de 
    Manila, where he thrived in an environment of intellectual rigor, discipline, and 
    advanced studies."
    
    Narrator "He quickly earned high grades, medals, and respect from his professors."
    
    scene fr paula de sanchez ust drawing classroom at resize_to_1080p

    Narrator "At Ateneo, Rizal was inspired by his professors, especially Fr. Francisco de 
    Paula Sanchez, who encouraged his love for poetry and intellectual growth." 
    
    Narrator "His extracurricular activities in literature and physical training further 
    shaped his character."
    
    scene 1_graduation at resize_to_1080p

    Narrator "However, after completing his degree in Bachelor of Arts, Rizal's family faced financial 
    strain," 
    
    Narrator "and Rizal decided to continue his studies at the Universidad de Santo Tomas, despite 
    his growing dissatisfaction with Spanish colonial rule and the oppressive educational system."
    
    scene eah at resize_to_1080p

    Narrator "At UST, Rizal enrolled in Philosophy and Letters, but he quickly grew disillusioned."
    
    Narrator "The harsh, repressive teaching methods of the Dominican professors and racial discrimination 
    against Filipino students made it difficult for him to focus on his studies."
    
    scene eah2 at resize_to_1080p

    Narrator "Despite the struggles, Rizal pursued a medical course and won literary awards for works that 
    expressed his growing nationalist sentiments." 
    
    Narrator "His time at UST further fueled his desire for reform, and he eventually decided to continue 
    his education abroad, where he could work towards his vision of change for the Philippines."

    jump scene3

label scene2_choice2:
    stop music
    play music "audio/violin.mp3" fadein 1.0 loop
    scene eah2 at resize_to_1080p

    Narrator "Jose Rizal entered the Universidad de Santo Tomas in 1877, pursuing Philosophy 
    and Letters, but quickly became disheartened by the oppressive atmosphere, outdated teaching 
    methods, and racial discrimination from Dominican professors."

    Narrator "Struggling without the intellectual stimulation he had at Ateneo, his academic 
    performance declined, and his passion for reform faded. His disillusionment led him to 
    abandon his original mission, and his time at UST became a period of stagnation, ultimately 
    thwarting his dreams of improving his country."
    
    stop music

    menu:
        "Restart the game.":
            return


# Scene 3
label scene3:
    scene eah

    Narrator "Jose Rizal has excelled in his studies at the Ateneo de Manila, displaying a keen 
    intellect and a thirst for knowledge. However, the educational system in the Philippines under 
    Spanish colonial rule feels stifling to his curious mind."

    stop music
    
    menu:
        "Go to Abroad":
            jump scene3_choice1

        "Jose Rizal remains in the Philippines":
            jump scene3_choice2 

label scene3_choice1:
    play music "audio/normal day2.mp3" fadein 1.0 volume 1 loop
    scene 1_scenario4 frames 1-3

    Narrator "In the heart of colonial Manila, a young mind yearns for freedom. Jose Rizal, a 
    brilliant student at the Ateneo de Manila, feels the weight of the Spanish colonial yoke. 
    The implacable curriculum and oppressive atmosphere suppress his intellectual curiosity."

    Narrator "A spark ignites within Rizal's soul. He dreams for a Philippines liberated from 
    the chains of colonialism. But to realize this dream, he must seek knowledge beyond the 
    confines of his homeland."

    scene 2_scenario4 choice 2

    Narrator "A crucial decision looms large. Should Rizal remain in the Philippines? Where 
    his potential may be limited? Or should he embark on a risky journey to Europe, seeking 
    higher education and enlightenment?"
    
    scene 4_bids farewell scene4

    Narrator "Rizal chooses the path less traveled. He bids farewell to his family and friends, 
    his heart filled with hope and determination. As the ship sets sail, a new chapter in his 
    life begins, a chapter that will shape the destiny of a nation."

    jump scene4

label scene3_choice2:
    stop music
    play music "audio/violin.mp3" fadein 1.0 loop
    scene eah

    Narrator "Jose Rizal, denied the opportunity to broaden his horizons, became increasingly 
    disillusioned with the limitations of the colonial system."

    Narrator "Jose Rizal may find himself confined to a conventional career within the colonial 
    bureaucracy, gradually losing his idealism and becoming unconcerned or not interested with 
    the existing order."

    stop music

    menu:
        "Restart the game.":
            return

# Scene 4
label scene4:
    scene medfield

    Narrator "Choosing a degree of Medicine. Do you want to study in the Medical Field?"

    stop music

    menu:
        "Yes":
            jump scene4_choice1
        "No":
            jump scene4_choice2 

label scene4_choice1:
    play music "audio/normal day3.mp3" fadein 1.0 volume 1 loop
    Narrator "When Rizal's transferred and took up the Medical course."

    scene wpac

    Narrator "His brother Paciano reminded him to focus on his true purpose."

    scene wpac2
    show paciano talking at right

    Paciano "While you may finish your medical studies in Barcelona, go to Madrid instead. 
    Your journey is about more than just medicine, it's about pursuing what truly matters 
    to you."
    
    jump scene5

label scene4_choice2:
    stop music
    play music "audio/violin.mp3" fadein 1.0 loop
    scene medfield2
    Narrator "Rizal failed to earn the Licentiate in Medicine from Universidad 
    Central de Madrid"    
    
    stop music

    menu:
        "Restart the game.":
            return


# Scene5
label scene5:
    Narrator "After studying in UST, Rizal decided to study abroad to fulfill the 
    mission given by the comite de propaganda, to collect templates for nation 
    building."

    scene salvadore bg at resize_to_1080p
    show pepe sad

    Narrator "Rizal boarded the Salvadora and was disheartened to realize how his 
    country is not recognized by the masses. This made Rizal establish another mission, 
    to place the Philippines on the map of the sovereign world."

    scene writing bg at resize_to_1080p
    Narrator "Once having arrived in Barcelona and collected a nation building template, 
    In order to cope with the feeling of missing his home country, Rizal wrote his first 
    essay “El Amor Patrio”."

    scene barcelona bg at resize_to_1080p
    Narrator "After collecting the nation building template in Barcelona, Rizal is faced 
    with a decision to stay in Barcelona or move to Madrid."

    Narrator "After studying in Barcelona..."
    
    show pepe at right 
    Pepe "Hmmm.... Should I stay in Barcelona or move to Madrid"

    stop music

    menu:
        "Move to Madrid":
            jump scene6

        "Stay in Barcelona":    
            jump scene5_choice2

# Scene 5 Wrong Choice
label scene5_choice2:
    stop music
    play music "audio/violin.mp3" fadein 1.0 loop
    scene barcelona bg at resize_to_1080p

    Narrator "You decided to stay in Barcelona, Spain, choosing to focus on exploring 
    the city rather than broadening your horizons."

    Narrator "Although the information collected was valuable, it lacked the diversity and 
    depth needed for effective nation-building."

    show pepe sad at left
    Narrator "Limited exposure to different templates for reform and the inhospitable 
    environment of Barcelona hindered your progress."

    Narrator "Without the crucial insights from other nations and their movements, your 
    aspirations for meaningful change remained unfulfilled."

    stop music

    menu:
        "Restart the game.":
            return


# Scene 6
label scene6:
    play music "audio/normal day4.mp3" fadein 1.0 loop
    scene madrid bg at resize_to_1080p
    Narrator "After arriving to Madrid, Spain..."

    show pepe at left
    Pepe "Hmm... Should I join some groups and movements?"
    
    menu:
        "Yes, I'll consider joining them.":
            jump scene6_choice1
        
        "No, I prefer to focus on my work.":
            jump scene6_choice2


# Scene 6 Correct Choice 
label scene6_choice1:
    Narrator "As you progress in your journey, you realize that Rizal's story was 
    not just about individual endeavors."
    
    Narrator "Let's take a closer look at the different paths Rizal took as he 
    navigated this world of activism and reform."

    scene comite de reformadores bg at resize_to_1080p

    Narrator "The Comité de Reformadores is a coalition of visionary minds, united 
    to ignite a movement for social justice and transformative reforms in the 
    Philippines under Spanish colonial rule."

    show pepe at left

    menu:
        Pepe "Should I join the Comité de Reformadores?"

        "Yes, I'll join them. Their goals align with my vision for reform.":
            jump scene6_choice1_frame1

        "No, I believe their focus might be too narrow to create lasting reform.":
            jump scene6_choice1_frame1_wrong
    
    # Scene 6 Frame 1 Correct Choice
    label scene6_choice1_frame1:
        Narrator "By joining the Comité de Reformadores, you became part of a 
        pioneering group of Filipinos advocating for justice and equality."
        
        Narrator "The Comité de Reformadores was one of the earliest proto-nationalist 
        groups in Philippine history."

        Narrator "Focused on reform, not independence, it sought equality and fair 
        treatment under Spanish rule, advocating for representation, freedom, and 
        secularization."

        Narrator "Its ties to Paciano Mercado connect it to José Rizal, whose 
        nationalist efforts were shaped by these early ideals, laying the groundwork 
        for future revolutionary movements."

        scene comite de propaganda bg at resize_to_1080p

        Narrator "The Comité de Propaganda emerged as a beacon of reform, uniting 
        Filipino intellectuals in Spain to advocate for equality, justice, and the 
        recognition of Filipino rights under Spanish rule."

        show pepe at right

        menu:
            Pepe "Should I join Comité de Propaganda?"

            "Sure, I'll join this group and explore its direction.":
                jump scene6_choice1_frame2

            "No, I believe their methods may not align with my aspirations.":
                jump scene6_choice1_frame2_wrong
    
    # Scene 6 Frame 1 Wrong Choice
    label scene6_choice1_frame1_wrong:
        stop music
        play music "audio/violin.mp3" fadein 1.0 loop
        scene comite de reformadores wrong bg at resize_to_1080p
        show pepe shock at left

        Narrator "You decided against joining the Comité de Reformadores."
    
        Narrator "However, without the support of like-minded reformers, your efforts to 
        promote social justice and change in the Philippines fall short."
        
        Narrator "While Rizal's actions remained noble, his potential was diminished by 
        choosing isolation over collaboration with other activists."

        show pepe sad at left

        Narrator "You find yourself overwhelmed by obstacles, struggling to make a 
        significant impact on your own."
    
        Narrator "The reform movement needed unity, and without it, your journey fades into 
        the background of history."
    
        stop music

        menu:
            "Restart the game.":
                return


    # Scene 6 Frame 2 Correct Choice
    label scene6_choice1_frame2:
        Narrator "You joined the Comité de Propaganda, immersing yourself in the 
        exchange of ideas and plans that would shape the future of the Philippine 
        reform movement."

        Narrator "The Comité de Reformadores evolved into the Comité de Propaganda, 
        shifting from modest reforms to a broader push for Filipino unity and independence."
        
        Narrator "The group focused on fundraising, strategic planning, and expanding 
        membership, including figures like Paciano Mercado and Andres Bonifacio, signaling a 
        shift toward revolution."
        
        Narrator "José Rizal played a key role, using his education and writings as part of a 
        (secret) mission to advance reform and inspire nationalism."

        scene circulo hispano filipino bg at resize_to_1080p

        Narrator "The Círculo Hispano-Filipino fostered dialogue and camaraderie 
        between Filipinos and Spaniards, advocating for cultural exchange, mutual 
        understanding, and peaceful reforms for the Philippines."
        
        show pepe at left

        menu:
            Pepe "Should I be involved in Círculo Hispano-Filipino?"

            "Yes, I'll join this group and connect with fellow Filipinos.":
                jump scene6_choice1_frame3

            "No, I think my efforts are better directed elsewhere.":
                jump scene6_choice1_frame3_wrong

    # Scene 6 Frame 2 Wrong Choice
    label scene6_choice1_frame2_wrong:
        stop music
        play music "audio/violin.mp3" fadein 1.0 loop
        scene comite de propaganda wrong bg at resize_to_1080p
        show pepe shock at right 

        Narrator "You chose not to join the Comité de Propaganda, thinking their methods 
        didn't align with your ideals."
    
        Narrator "But without the group's collective efforts, your ambitions for Filipino 
        independence and social reform struggle to gain traction."
        
        Narrator "Rizal's nationalistic vision needed the influence and collaboration of this 
        intellectual circle, and by stepping back, you miss out on shaping history alongside 
        other revolutionary figures."

        show pepe sad at right

        Narrator "Your efforts, while well-intentioned, become fragmented and ultimately 
        insufficient to spark the change you hoped for."
    
        Narrator "The fight for equality and justice under Spanish rule continues, but you 
        are left behind."
        
        stop music

        menu:
            "Restart the game.":
                return


    # Scene 6 Frame 3 Correct Choice
    label scene6_choice1_frame3:
        Narrator "You joined the Circulo Hispano-Filipino, engaging in rich discussions 
        that broadened your perspectives and strengthened bonds within the Filipino 
        community abroad."

        Narrator "In 1882, a group of Filipino students in Madrid, led by Juan Atayde, 
        established an organization with headquarters at Don Pablo Ortiga y Rey's residence, 
        a hub for political discussions."
        
        Narrator "The group included political, literary, and sports sections and published 
        Revista del Circulo Hispano Filipino. Notably, Rizal engaged in discussions with the 
        Paternos about Gregorio Sanciangco's El Progreso de Filipinas."

        scene asociacion hispano filipina bg at resize_to_1080p

        Narrator "The Asociación Hispano-Filipina was formed to promote Filipino interests 
        in Spain, serving as a platform for intellectuals and reformists to push for 
        political and social changes in the Philippines."

        show pepe at right

        menu:
            Pepe "Is it worth joining this group?"

            "Yes, I'll join to this group.":
                jump scene6_choice1_frame4

            "No, I prefer to stop.":
                jump scene6_choice1_frame4_wrong
    
    # Scene 6 Frame 3 Wrong Choice
    label scene6_choice1_frame3_wrong:
        stop music
        play music "audio/violin.mp3" fadein 1.0 loop
        scene circulo hispano filipino wrong bg at resize_to_1080p
        show pepe at left
        Narrator "You turned down the opportunity to join the Círculo Hispano-Filipino, 
        thinking your efforts would be better spent elsewhere."
    
        Narrator "Without participating in their dialogues and cultural exchanges, you 
        miss out on gaining crucial support from Filipinos and Spaniards who were working 
        for peaceful reforms."
        
        Narrator "Your isolation and reluctance to engage with others who shared your 
        goals create a widening gap in your mission."
        
        show pepe at left

        Narrator "The road to reform requires unity, and by distancing yourself, you only 
        push further away from the chance to shape history."
        
        stop music

        menu:
            "Restart the game":
                return

     
    # Scene 6 Frame 4 Correct Choice
    label scene6_choice1_frame4:
        Narrator "You joined the Asociacion Hispano-Filipina, contributing to its mission 
        of advocating for Philippine welfare and reforms."

        Narrator "The Asociación Hispano-Filipina was established in 1889 in Madrid with 
        the primary goal of advocating for reforms that would improve the welfare of the 
        Philippines."
        
        Narrator "The organization aimed to bridge ties between the Philippines and Spain, 
        pushing for changes that would benefit Filipinos under Spanish rule."

        scene asociacion internacional de filipinistas bg at resize_to_1080p

        Narrator "The Asociación Internacional de Filipinistas brought together scholars and 
        advocates from around the world to study, promote, and support Filipino culture, 
        history, and the rights of the Filipino people under Spanish rule."

        show pepe at left

        menu:
            Pepe "Should I join the Asociacion Internacional de Filipinistas?"

            "Yes, I'll join this group and advocate for international recognition.":
                jump scene6_choice1_frame5

            "No, I think my priorities lie elsewhere.":
                jump scene6_choice1_frame5_wrong

    # Scene 6 Frame 4 Wrong Choice
    label scene6_choice1_frame4_wrong:
        stop music
        play music "audio/violin.mp3" fadein 1.0 loop
        scene asociacion hispano filipina wrong bg at resize_to_1080p
        show pepe shock at right

        Narrator "You opted not to join the Asociación Hispano-Filipina, thinking it 
        wouldn't offer the political leverage you sought."
        
        Narrator "However, without the group's platform to advocate for Filipino rights, 
        your influence remains limited, and your vision for the Philippines' future falters."
        
        Narrator "Rizal's journey would have been much harder without this network of 
        reformists advocating for the Philippines in Spain."
        
        show pepe at right

        Narrator "The movement loses momentum, and your efforts fall short, unable to reach 
        the ears of those who could truly make a difference."
        
        stop music

        menu:
            "Restart the game":
                return

    # Scene 6 Frame 5 Correct Choice
    label scene6_choice1_frame5:
        Narrator "You joined the Asociacion Internacional de Filipinistas, dedicating 
        efforts to elevating the Philippines' global presence and fostering a deeper 
        understanding of its plight."

        scene asociacion internacional de filipinistas bg at resize_to_1080p

        Narrator "This organization was pivotal in promoting Filipino culture and advocating 
        for the rights and welfare of the Filipino people on an international platform."

        Narrator "Through your involvement, you helped raise global awareness about the 
        injustices faced by Filipinos under Spanish rule, creating valuable diplomatic ties."

        Narrator "Your engagement with international scholars and activists laid the groundwork 
        for a broader movement that reached beyond the shores of the Philippines, encouraging 
        solidarity from around the world."

        scene madrid bg at resize_to_1080p

        Narrator "As a result of your efforts, the global community began to take notice of the 
        Philippines' struggle for reform, laying the foundations for the eventual recognition 
        of Filipino rights."

        show pepe smile at left

        Narrator "The seeds of change were planted, and with the support of international allies, 
        you now see the potential for true transformation in the Philippines."

        menu:
            Pepe "What should I do next in my mission for reform?"

            "Focus on more local reforms, connecting with other Filipino reformists.":
                jump scene7
    
    # Scene 6 Frame 5 Wrong Choice
    label scene6_choice1_frame5_wrong:
        stop music
        play music "audio/violin.mp3" fadein 1.0 loop
        scene asociacion internacional de filipinistas wrong bg at resize_to_1080p
        show pepe shock at right

        Narrator "You decided not to join the Asociación Internacional de Filipinistas, 
        thinking international advocacy wasn't a priority for you."
    
        Narrator "But without this global network of scholars and reformists, your efforts 
        to gain international attention for the Philippines' plight fall flat."
        
        Narrator "Rizal's work could have benefited from international recognition, but by 
        rejecting this opportunity, you hinder the movement's chances for global support."

        show pepe sad at right

        Narrator "Your mission goes unnoticed, and the global support that could have 
        changed the course of history never materializes."

        stop music

        menu:
            "Restart the game.":
                return

# Scene 6 Wrong Choice
label scene6_choice2:
    stop music
    play music "audio/violin.mp3" fadein 1.0 loop
    scene madrid wrong bg at resize_to_1080p
    show pepe shock at left

    Narrator "You chose to focus solely on your work, avoiding involvement in groups and movements."

    Narrator "While your dedication is admirable, the fight for reform was never a solo journey."

    show pepe sad at left
    
    Narrator "Rizal's legacy was built not just on individual brilliance but also on collaboration 
    with others who shared his vision for change."
    
    Narrator "Without the support of these movements, your impact is limited, and the momentum for 
    reform stalls."
    
    Narrator "In the end, the collective strength of the reformists was what moved mountains—and by 
    opting out, you step away from the stage of history."
    
    stop music

    menu:
        "Restart the game":
            return


# Scene 7
label scene7:
    play music "audio/suspense.mp3" loop
    scene tondo bg at resize_to_1080p

    Narrator "Rizal arrived in Tondo, Manila..."

    show pepe

    menu:
        Pepe "Will it be a good idea to write the Constitución de La Liga Filipina?"

        "Yes":
            jump scene7_choice1

        "No":
            jump scene7_choice2

label scene7_choice1:
    scene la liga filipina bg at resize_to_1080p
    play music "audio/success.mp3" loop

    show pepe at left

    Narrator "La Liga Filipina, founded by José Rizal, aimed to unite Filipinos and improve society. 
    Its rules, secretly printed in Hong Kong, required members to be loyal, honest, and committed to 
    helping the group's goals."

    scene revolution bg at resize_to_1080p

    Narrator "The Liga inspired leaders like Andres Bonifacio and Apolinario Mabini, leading to the 
    Philippine revolution."

    scene monumenttondo bg at resize_to_1080p

    Narrator "In 1903, a monument in Tondo was built to honor its role in the fight for freedom."

    scene writingrizal bg at resize_to_1080p

    Narrator "José Rizal drafted La Liga Filipina's constitution, aiming for mutual protection, justice, 
    education, economic progress, and meaningful reforms—key steps toward a united Filipino nation."

    stop music fadeout 3.0
    jump scene8

label scene7_choice2:
    stop music
    play music "audio/violin.mp3" volume 0.3 loop

    scene struggles bg at resize_to_1080p

    Narrator "Without the Constitución de La Liga Filipina, the unity and organization needed to guide 
    the people were lost. As a result, Filipinos struggled in their daily lives, without a clear 
    direction or the reforms that could have improved their society."

    scene nounity bg at resize_to_1080p

    Narrator "Without Rizal's vision, the hopes for a unified, independent Philippines remained unmet. 
    This lack of leadership led to confusion and division, making the struggle for freedom and identity 
    harder, especially during American colonization."

    stop music

    menu:
        "Restart the game":
            return


# Scene 8
label scene8:
    play music "cinematic.mp3" loop
    scene scene8 bg at resize_to_1080p
    
    Narrator "continue..."
    
    scene firstwrite bg at resize_to_1080p

    menu:
        Narrator "Rizal is filled with determination, but he knows the risks of challenging Spanish authorities. 
        Should he commit to writing his first novel?"

        "Yes. Rizal should write a novel.":
            jump scene8_choice1

        "No. Rizal should note write or he will be endangered.":
            jump scene8_choice2

label scene8_choice1:
    scene nolime bg at resize_to_1080p

    Narrator "Rizal wrote Noli Me Tangere, pouring his heart into the story of Filipino suffering under 
    Spanish rule. His journey of reform begins."
    
    scene madrid noli bg at resize_to_1080p
    
    Narrator "In 1884, while studying in Madrid, Rizal begins writing Noli Me Tangere, a novel that 
    depicts the social and political issues in the Philippines under Spanish rule."

    scene deskrizal bg at resize_to_1080p
    show pepe at left 

    Pepe "This story will reveal the truth about the plight of my people. It is my duty to tell it."

    scene elfili bg at resize_to_1080p

    Narrator "After the success of Noli Me Tangere, Rizal starts writing El Filibusterismo, continuing 
    his mission to expose societal issues and inspire change."

    stop music fadeout 3.0

    jump scene9

label scene8_choice2:
    play music "audio/sad.mp3" volume 0.2 loop
    scene rizaldecline bg at resize_to_1080p

    Narrator "Riza's hesitation stifles his resolve. Without his voice, the call for reform fades 
    into silence."

    stop music fadeout 3.0

    menu:
        "Restart the game":
            return


# Scene 9
label scene9:
    play music "audio/intro.mp3" fadein 1.0 volume 1.5
    scene bg 4 at resize_to_1080p

    Narrator "The year is 1872, and the world of Jose Rizal is about to change."
 
    scene bg 5 at resize_to_1080p
    show rizal at left

    Narrator "After witnessing the execution of Gomburza, Jose Rizal embarks on a journey to 
    different countries, determined to gather knowledge and ideas to bring reform to the 
    Philippines."

    stop music

    play music "audio/travel.mp3" fadein 1.0 volume 1.5 loop
    scene bg 6 at resize_to_1080p
    hide rizal

    Narrator "Rizal travels across continents, observing governance, culture, and societal 
    systems that could inspire his vision of a better nation."

    menu:
        "Apply the lessons Rizal learns":
            jump Lessons_Applied
            
        "Dismiss the lessons Rizal learns":
            jump Lessons_Dismissed

label Lessons_Applied:
    Narrator "Rizal returns home with a clear vision: honest leadership from Singapore, 
    the courage for freedom from Spain, discipline from Japan, progress from America, 
    education from France, and rigor from Germany. He commits to using these ideals to 
    inspire reforms for his country."

    jump Scene_Selection

label Lessons_Dismissed:
    stop music 
    play music "audio/sad.mp3" volume 0.2 loop

    Narrator "Rizal becomes cynical and disheartened. He focuses only on the flaws he 
    saw in the countries he visited and fails to see the value of the positive lessons 
    they offered."

    scene bg philippine at resize_to_1080p

    Narrator "Back in the Philippines, Rizal's disillusionment with his journey 
    spreads. The reform movement lacks vision and unity. His failure to integrate the 
    lessons of progress, freedom, and resilience leaves the people without the 
    inspiration they desperately need."

    Narrator "As tensions rise, a revolution breaks out. However, it lacks strong 
    leadership and a clear purpose. The movement falters and collapses, crushed by 
    the Spanish authorities."
    
    show pepe sad at center

    Pepe "I could have been the change... but my doubts and failure to see the bigger 
    picture have cost my people their chance at freedom."

    Narrator "The Philippines remains in the grip of colonial rule, its people 
    disheartened and without the leadership needed to break free."
    
    stop music

    menu:
        "Restart the game.":
            return

label Scene_Selection:
    # Scene 1: Singapore
    scene bg singapore at resize_to_1080p

    Narrator "In the English colony of Singapore, Rizal is impressed by its progress 
    and the confidence of its people."
    
    show rizal smiling at right

    Pepe "A nation led with dignity and honesty can achieve so much. Our leaders must 
    aspire to govern like this."

    # Scene 2: Spain
    scene bg spain at resize_to_1080p

    Narrator "In Spain, Rizal experiences contrasting emotions."

    menu:
        "Visit Barcelona":
            jump Barcelona_Scene

        "Visit Madrid":
            jump Madrid_Scene

label Barcelona_Scene:
    scene bg barcelona at resize_to_1080p
    show rizal thinking at right

    Narrator "Barcelona's dirt and unwelcoming attitude disappoint him, but he 
    realizes there is something to learn from the resilience of the people here."
    
    show rizal smiling at center
    
    Pepe "Although this city feels gritty, there is strength in its struggle for 
    freedom. We must embrace this resilience in our fight for independence."
    
    jump Conclude_in_Madrid

label Madrid_Scene:
    scene bg madrid at resize_to_1080p
    show rizal thinking at left

    Narrator "Madrid gives Rizal hope. It's vibrant, full of intellectual energy. 
    There's a sense of freedom that stirs something in his heart."
    
    show rizal smiling at left
    
    Pepe "The ideals of freedom and courage here must be embraced by every Filipino. 
    This city embodies the spirit of what we should strive for."
    
    jump Conclude_in_Madrid

label Conclude_in_Madrid:
    scene bg madrid at resize_to_1080p
    show rizal thinking at center

    Narrator "Regardless of his earlier observations, Rizal finds himself deeply 
    inspired by Madrid. The intellectual atmosphere and the ideals of freedom solidify 
    his resolve to bring change to the Philippines."

    Narrator "As Rizal continues his journey, his vision for reform becomes clearer. 
    He is ready to take the next steps in his mission to awaken the Filipino spirit."

    jump Japan_Scene
   
label Japan_Scene:
    scene bg japan at resize_to_1080p
    show rizal smiling at center

    Narrator "Rizal sees Japan's unique blend of discipline and cultural pride."

    show rizal smiling at left

    Pepe "Their cleanliness, order, and respect for tradition allow Japan to progress 
    without losing its identity. The Philippines must learn this balance."

    jump America_Scene

label America_Scene:
    scene bg america at resize_to_1080p
    show rizal thinking at center

    Narrator "America's advancements and industries inspire Rizal, but he cannot ignore 
    its racial inequalities."

    show rizal thinking at right

    Pepe "Progress means nothing without equality. True freedom must lift all people, 
    not just a privileged few."

    jump France_Scene

label France_Scene:
    scene bg madrid at resize_to_1080p
    show rizal smiling at right

    Narrator "Immersed in France's intellectual atmosphere, Rizal realizes the power 
    of education."

    show rizal smiling at center

    Pepe "Through education, we can empower Filipinos to lead their country to 
    greatness."

    jump Germany_Scene

label Germany_Scene:
    scene bg madrid at resize_to_1080p
    show rizal smiling at center

    Narrator "In Germany, Rizal finds his ideal nation, admiring its academic 
    excellence and discipline."

    show rizal smiling at left

    Pepe "The discipline and knowledge here are the foundations of progress. 
    If our people adopt these values, we can transform the Philippines."
   
    jump Ending

label Ending:
    stop music
    play music "audio/Ending.mp3" fadein 1.0 loop
    scene ending bg at resize_to_1080p
    show pepe smile at center

    Narrator "After years of unwavering dedication, sacrifice, and tireless 
    efforts, Rizal's name echoed not only throughout the Philippines but across 
    the world."
    
    Narrator "His writings, fueled by his vision of equality and freedom, 
    ignited a spark in the hearts of his fellow Filipinos."
    
    show pepe smile at center

    Narrator "Rizal's bravery in exposing injustice and advocating for reform 
    laid the foundation for a united movement, inspiring generations to fight 
    for independence."
    
    Narrator "Though his life was tragically cut short, his legacy became 
    eternal, as the seeds of his vision grew into a nation proud of its heritage 
    and its heroes."

    Narrator "Rizal's story is a testament to the power of resilience, education, 
    and the courage to stand against oppression."
    
    Narrator "As history remembers him, Rizal became not just a figure of the past, 
    but a symbol of hope, justice, and unwavering love for one's country."
    
    show pepe at center with dissolve

    Pepe "Thank you for accompanying me on this journey. Together, we have witnessed 
    the struggles and triumphs that led to the awakening of a nation."
    
    Narrator "Congratulations! You have completed the story of Rizal's extraordinary 
    life and legacy."
    
    menu:
        "The End.":
            return
