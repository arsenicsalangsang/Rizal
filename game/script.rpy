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


# Scene 6
label Scene6:
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
        scene 
        show pepe shock at left 

        Narrator "You chose not to join the Comité de Propaganda, thinking their methods 
        didn't align with your ideals."
    
        Narrator "But without the group's collective efforts, your ambitions for Filipino 
        independence and social reform struggle to gain traction."
        
        Narrator "Rizal's nationalistic vision needed the influence and collaboration of this 
        intellectual circle, and by stepping back, you miss out on shaping history alongside 
        other revolutionary figures."

        show pepe sad at right
        
        menu:
            "Restart the game.":
                return

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
    
    label scene6_choice1_frame3_wrong:
        "Game Over"
        return

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

        label scene6_choice1_frame5:
            Narrator "You joined the Asociacion Internacional de Filipinistas, dedicating 
            efforts to elevating the Philippines' global presence and fostering a deeper 
            understanding of its plight."

            jump scene7
        
        label scene6_choice1_frame5_wrong:
            "Game Over"
            return

# Scene 6 Wrong Choice
label scene6_choice2:
    "Game Over"
    return