screen img_btn(img_idle, posXY, jump_place):
    imagebutton:
        pos (posXY)
        focus_mask True
        idle img_idle
        hover If(action_area_lighting,true=(im.MatrixColor(img_idle,im.matrix.brightness(0.15))),false=img_idle)
        action [Hide("img_btn",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]

screen img_btn1(img_idle, posXY, jump_place):
    imagebutton:
        pos (posXY)
        focus_mask True
        idle img_idle
        hover If(action_area_lighting,true=(im.MatrixColor(img_idle,im.matrix.brightness(0.15))),false=img_idle)
        action [Hide("img_btn1",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]

screen img_btn2(img_idle, posXY, jump_place):
    imagebutton:
        pos (posXY)
        focus_mask True
        idle img_idle
        hover If(action_area_lighting,true=(im.MatrixColor(img_idle,im.matrix.brightness(0.15))),false=img_idle)
        action [Hide("img_btn1",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]
screen img_btn3(img_idle, posXY, jump_place):
    imagebutton:
        pos (posXY)
        focus_mask True
        idle img_idle
        hover If(action_area_lighting,true=(im.MatrixColor(img_idle,im.matrix.brightness(0.15))),false=img_idle)
        action [Hide("img_btn1",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]
screen img_btn4(img_idle, posXY, jump_place):
    imagebutton:
        pos (posXY)
        focus_mask True
        idle img_idle
        hover If(action_area_lighting,true=(im.MatrixColor(img_idle,im.matrix.brightness(0.15))),false=img_idle)
        action [Hide("img_btn1",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]


screen img_btn_hiden(img_idle, posXY, jump_place):
    imagebutton:
        pos (posXY)
        idle img_idle
        action [Hide("img_btn_hiden",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]

screen img_btn_txt(img_idle, posXY, jump_place, txt):
    vbox pos (posXY):
        imagebutton xalign 0.5:
            idle img_idle
            hover (im.MatrixColor(img_idle,im.matrix.brightness(0.10)))
            action [Hide("img_btn_txt",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]
        text (txt) xalign 0.5

screen call_remember(posXY, jump_hardoff, jump_hardon):
    vbox pos (posXY):
        imagebutton xalign 0.5:
            idle "images/Buttons/button_jerk_fantasy.jpg"
            hover (im.MatrixColor("images/Buttons/button_jerk_fantasy.jpg",im.matrix.brightness(0.10)))
            action [Hide("call_remember",transition=dissolve), SetVariable("jump_peremen1",jump_hardoff ), SetVariable("jump_peremen2",jump_hardon), Jump("not_hard_on")]
        text (_("Think about something sexy")) xalign 0.5

screen img_btn_txt1(img_idle, posXY, jump_place, txt):
    vbox pos (posXY):
        imagebutton xalign 0.5:
            idle img_idle
            hover (im.MatrixColor(img_idle,im.matrix.brightness(0.10)))
            action [Hide("img_btn_txt1",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]
        text (txt) xalign 0.5
screen img_btn_txt2(img_idle, posXY, jump_place, txt):
    vbox pos (posXY):
        imagebutton xalign 0.5:
            idle img_idle
            hover (im.MatrixColor(img_idle,im.matrix.brightness(0.10)))
            action [Hide("img_btn_txt1",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]
        text (txt) xalign 0.5
screen img_exit(jump_place=None, nf=False, y=0.98, x=0.99):
    imagebutton xalign x yalign y:
        idle "images/Buttons/arrow_exit.png"
        hover (im.MatrixColor("images/Buttons/arrow_exit.png",im.matrix.brightness(0.10)))
        action [Hide("img_exit"), SetVariable("nofade", nf), If(jump_place == None, Return(1), Jump(jump_place))]

screen img_map(jump_place):
    imagebutton:
        pos (1750,80)
        idle If(block_map, (im.MatrixColor("images/Buttons/maps_icon.png",im.matrix.opacity(0.20))),"images/Buttons/maps_icon.png")
        hover (im.MatrixColor("images/Buttons/maps_icon.png",im.matrix.brightness(0.10)))
        action If(block_map, None,[Hide("img_map",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))])

screen img_custom(pic, x, y, jump_place=None):
    imagebutton:
        align (x,y)
        idle pic
        hover (im.MatrixColor(pic,im.matrix.brightness(0.10)))
        action [Hide("img_custom",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]

screen img_custom_call(pic, x, y, jump_place=None, var):
    imagebutton:
        align (x,y)
        idle pic
        hover (im.MatrixColor(pic,im.matrix.brightness(0.10)))
        action [Hide("img_custom",transition=dissolve), If(jump_place == None, Return(1), Call(jump_place,var = var))]



screen img_custom1(pic, x, y, jump_place=None):
    imagebutton:
        align (x,y)
        idle pic
        hover (im.MatrixColor(pic,im.matrix.brightness(0.10)))
        action [Hide("img_custom1",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]

screen img_custom_plus(pic, pic1, x, y, jump_place=None):
    imagebutton:
        align (x,y)
        idle pic
        hover pic1
        action [Hide("img_custom_plus",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]

screen change_view(jump_place=None, x=.98, y=.9):
    imagebutton:
        align (x,y)
        idle "images/Buttons/button_change_view.png"
        hover (im.MatrixColor("images/Buttons/button_change_view.png",im.matrix.brightness(0.10)))
        action [Hide("img_custom",transition=dissolve), If(jump_place == None, Return(1), Jump(jump_place))]

screen hide_but(x, y, d):
    imagebutton xpos x ypos y:
        idle ("images/Buttons/hide_but.png")
        action [Hide("hide_but"), Jump(d)]

screen hide_butm(x, y, d):
    imagebutton xpos x ypos y:
        idle ("images/Buttons/hide_butm.png")
        action [Hide("hide_but"), Jump(d)]

screen say_2:
    drag:
        drag_name "say"
        yalign 1.0
        drag_handle (0, 0, 1.0, 30)

        xalign 0.5

        window id "window":
            # 确保窗口尺寸小于整个界面。
            xmaximum 600

            has vbox

            if who:
                text who id "who"

            text what id "what"



