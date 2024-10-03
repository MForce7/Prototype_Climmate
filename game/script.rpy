# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
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

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"
    call cut_scene
    

    # This ends the game.

    return
label cut_scene:
    play movie "Scene-kawai-elaina.webm"
    $ renpy.pause(14, hard=True)
    pause 14
    stop movie
    return