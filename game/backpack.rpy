transform button_menu_s:
    xanchor 0.5
    yanchor 0.5
    on hover:
        zoom 2.0
        ease 0.15 zoom 2.2
    on idle:
        ease 0.15 zoom 2.0
transform button_menu_s_:
    xalign 0.95
    yalign 0.9
    xanchor 0.5
    yanchor 0.5
    zoom 2.0
    ease 0.25 zoom 0.0
    
transform button_menu:
    xanchor 0.5
    yanchor 0.5
    zoom 0.0 
    pause 0.25
    ease 0.25 zoom 1.0 
    on hover:
        ease 0.25 zoom 1.2
    on idle:
        ease 0.25 zoom 1.0

transform bigging:
    xanchor 0.5
    yanchor 0.5
    zoom 0.0
    ease 0.25 zoom 1.0
transform smalling:
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    ease 0.25 zoom 0.0
transform dissapaer:
    zoom 0.0
default state_= True
default sate = True

screen backpack:
    if state_ == True:
        imagebutton:
            xalign 0.95
            yalign 0.9
            
            idle  "backpack/backpack.png"
            hover "backpack/backpack.png"at button_menu_s
            action [ToggleVariable("state_"), ToggleVariable("sate")]
    else:
        add "backpack/backpack.png" at button_menu_s_
        

image content_icon:
    "backpack/icon_item.png"
    xanchor 0
    yanchor 0
    zoom 1.5
    


screen backpack_item:
    style_prefix "itemUi"
    if state_ == False:
        add "backpack/plate.png" xalign 0.5 yalign 0.5 at bigging
        # conten isi back pack

        # imagebutton:
        #     xalign 0.1
        #     yalign 0.1
        #     idle  "backpack/icon.png"
        #     hover "backpack/icon.png" at button_menu
        #     action NullAction()  
        frame :
            background None
            xalign 0.5
            yalign 0.5
            xoffset 100
            yoffset 120
            vbox spacing 70:
                hbox spacing 70:
                    vbox:

                        imagebutton:
                            # xalign 0.1
                            # yalign 0.1
                            idle  "content_icon"
                            hover "content_icon" at button_menu
                            action NullAction()
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                hbox spacing 70:
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                hbox spacing 70:
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
                    imagebutton:
                        # xalign 0.1
                        # yalign 0.1
                        idle  "content_icon"
                        hover "content_icon" at button_menu
                        action NullAction()  
        
        
        
        
        
    
        imagebutton:
            xalign 0.073
            yalign 0.89
            
            idle  "backpack/back_icon.png"
            hover "backpack/back_icon.png" at button_menu 
            action [ToggleVariable("state_"), ToggleVariable("sate")]
    if sate == True and state_ == False  or sate == False and state_ == True:
        add "backpack/plate.png" xalign 0.5 yalign 0.5 at smalling
        add "backpack/back_icon.png" xalign 0.073 yalign 0.89 at dissapaer

        


    
style itemUi_vbox:
    yalign 0.5
style itemUi_hbox:
    xalign 0.5


    
