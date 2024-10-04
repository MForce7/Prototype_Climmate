# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Eileen")
define mari = Character("Mari")
define sensei = Character("Sensei")
image mari_n = "Mari/Mari_Portrait_Expression_1.png"
image mari_s = "Mari/Mari_Portrait_Expression_3.png"
image mari_t  = "Mari/Mari_Portrait_Expression_99.png"
image mari_b = "Mari/Mari_Portrait_Expression_2.png"
image mari_r = "Mari/Mari_Portrait_Expression_7.png"
image mari_sd = "Mari/Mari_Portrait_Expression_6.png"
image background:
    "Mari/trinity_bg1.jpeg"
    zoom 2

image title_logo:
    contains:
        "game_menu.png"
    contains:
        "Title.png" 
        xalign 0.5
        xanchor 0.5
        yanchor 0.5
        ypos 300
        ease 1.0 zoom 1.4
        ease 1.0 zoom 1.3
    
        repeat 
transform tes:
    linear 0.15 
    pos (1318, 900) 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        point_to None 
    mari "Oh, Sensei. Thank you for coming."
    hide mari_n
    show mari_s:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        point_to None 
    mari "I was just saying a prayer for you."
    hide mari_s
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        point_to None
    call cut_scene
    play music "instrumental.mp3" fadein 1.0 fadeout 1.0 loop
    mari "A quiet place like this is great for praying."
    hide mari_n
    show mari_t:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        point_to None
    mari "When I pray, it feels as though my heart is being cleansed."
    hide mari_t
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        point_to None 
    mari "There are paths you've taken so far and paths you must still take."
    hide mari_n
    show mari_t:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "May peace and happiness find you whenever you choose to walk them."
    menu:
        "Have you ever pray for yourself?":
            pass
        "How about you?":
            pass
    hide mari_t
    show mari_b:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0)   
    mari "What have I ever prayed for myself?"

    mari "That's... "
    hide mari_b
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "No, it's okay."
    hide mari_n
    show mari_s:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "I am happy if you are happy, Sensei."
    hide mari_s
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1300, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    show mari_n:
        subpixel True 
        pos (1300, 900) 
        linear 0.15 pos (1325, 900) 
    with Pause(0.4)
    hide mari_n
    show mari_s:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1326, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 

    mari "In other words, this can be a prayer for us."
    hide mari_s
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1326, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "I wanted to offer this prayer much sooner, but I've been kind of busy with my cathedral work lately."
    hide mari_n
    show mari_r:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1326, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "Hmm, I suppose that's just an excuse."
    hide mari_r
    show mari_sd:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1326, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        subpixel True 
        linear 0.15 pos (1318, 900) 
    with Pause(0.4)
    mari "A sister mustn't develop a habit for excuses."
    hide mari_sd
    show mari_r:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1319, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "Please forgive me for only now attending to your needs, Sensei."
    menu:
        "Not at all. You seem like you'll be a model sister.":
            pass
        "I can tell that you are already a superb sister.":
            pass
    hide mari_r
    show mari_b:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1319, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "What is that so?"
    hide mari_b
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1319, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "Anyway..."

    mari "Sensei, if it's alright, can you come a little closer?"
    hide mari_n
    show mari_n:
        subpixel True 
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (1319, 900) 
        zpos 0.0 
        rotate 0.0 
        xzoom 0.7 
        yzoom 0.7 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        parallel:
            alpha 1.0 
            linear 0.30 alpha 1.0 
            linear 0.19 alpha 0.0 
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 0.30 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 
    with Pause(0.59)
    show mari_n:
        alpha 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 
    hide mari_n
    with Pause(0.4)
    show mari_n:
        subpixel True 
        parallel:
            pos (800, 1300) anchor (0.5, 0.5) xzoom 1.0 yzoom 1.0 zoom 1.0 alpha 0.0 
            linear 0.30 pos (800, 1300) anchor (0.5, 0.5) xzoom 1.0 yzoom 1.0 zoom 1.0 alpha 1.0 
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 
            linear 0.30 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 
            linear 0.20 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(0.60)
    show mari_n:
        pos (800, 1300) anchor (0.5, 0.5) xzoom 1.0 yzoom 1.0 zoom 1.0 alpha 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    mari "There are several different ways to pray."
    hide mari_n
    show mari_t:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "One of them..."
    hide mari_t
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
        subpixel True xpos 800 
        ypos 1300 
        easein_back 0.33 ypos 1350 
        easein_back 0.33 ypos 1300 
    with Pause(0.76)
    show mari_n:
        pos (800, 1300) 
    
    mari "..."
    hide mari_n
    show mari_t:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "is where you hold your hands together and lift them in prayer like this."
    hide mari_t
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "I personally think this is more easily heard."
    hide mari_n
    show mari_s:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "And for people like Sensei, who tend to put others first..."
    hide mari_s
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0) 
    mari "Well, I think you probably pray for students before yourself,"
    mari "which is why I think it's necessary for someone to stay and pray with you like this."
    hide mari_n
    show mari_s:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0)
    mari "I will take on that role because I want to be a great sister one day."
    hide mari_s
    show mari_n:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0)
    mari "Now then, if you would please close your eyes, Sensei,"
    hide mari_n
    show mari_s:
        offset (0.0, 0.0) 
        anchor (0.5, 0.5) 
        pos (800, 1300) 
        xzoom 1.0 
        yzoom 1.0 
        xrotate 0.0 
        yrotate 0.0 
        zrotate 0.0 
        orientation (0.0, 0.0, 0.0)
    mari "let's pray together for your happiness once more."

    return
label cut_scene:
    play movie "Scene-kawai-elaina.webm"
    $ renpy.pause(14, hard=True)
    pause 14
    stop movie
    return
label coba_coba:
    return
