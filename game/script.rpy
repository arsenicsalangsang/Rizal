default Narrator = Character('Narrator', color="#E03B8B")
default Pepe = Character('Jose Rizal (Pepe)', color="#4c4fff")

# Declared Images:
image pepe:
    "Scene 6/pepe.png"
    zoom 1.5

image pepe open mouth:
    "Scene 6/pepe open mouth.png"
    zoom 1.5

image pepe smile:
    "Scene 6/pepe smile.png"
    zoom 1.5

image pepe schoked:
    "Scene 6/pepe shock.png"
    zoom 1.5

image pepe sad:
    "Scene 6/pepe sad.png"
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

transform resize_to_1080p:
    xsize 1920
    ysize 1080

# Scene5
label start:
    Narrator "After studying in UST, Rizal decided to study abroad to fulfill the 
    mission given by the comite de propaganda, to collect templates for nation 
    building."

    scene salvadore bg at resize_to_1080p
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

    menu:
        "Move to Madrid":
            jump scene6

        "Stay in Barcelona":    
            jump scene5_choice2

# Scene 5 Wrong Choice
label scene5_choice2:
    scene barcelona bg at resize_to_1080p
    Narrator "You decided to stay in Barcelona, Spain, choosing to focus on exploring 
    the city rather than broadening your horizons."

    Narrator "Although the information you collected was valuable, it lacked the diversity and 
    depth needed for effective nation-building."

    show pepe sad at left
    Narrator "Limited exposure to different templates for reform and the inhospitable 
    environment of Barcelona hindered your progress."

    Narrator "Without the crucial insights from other nations and their movements, your 
    aspirations for meaningful change remained unfulfilled."

    menu:
        "Restart the game.":
            return


# Scene 6
label scene6:
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
        scene comite de propaganda bg at resize_to_1080p
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
    label scene6_choice1_frame_4_wrong:
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
            
            "Continue advocating internationally, pushing for more widespread recognition.":
                jump scene7

            "Focus on more local reforms, connecting with other Filipino reformists.":
                jump scene6_choice1_frame5_wrong
    
    # Scene 6 Frame 5 Wrong Choice
    label scene6_choice1_frame5_wrong:
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

        menu:
            "Restart the game.":
                return

# Scene 6 Wrong Choice
label scene6_choice2:
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
    
    menu:
        "Restart the game":
            return