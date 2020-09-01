default items = [eggplant, sleepface, laughface, handsup]
default tb = ToolBar(rect=(0, 0, 160, 1080), direction=1, items=items)


init:
    image dim = "#0008"

label start:
    "大家好，我是废话，介绍游戏背景"

    scene 2
    with fade

    # show screen input(_("xxxx"), "xxx")
    "这里是个美女，请把茄子放到她胸前，可以解密"

    default ev = AreaEvent(rect=(550, 250, 200, 200), item=eggplant, label='puzzle')

    python:
        _window_hide()
        tb.set_evens(ev)
        tb.show()
        tb.sensitive = True
        tb.interact()
        tb.hide()

label test:
    scene 3 with dissolve

    "你可能要进入死循环了"

    jump start

label puzzle:

    scene 1 with dissolve

    "恭喜你操作正确，进入房间,这里的茄子是个按钮"

    call screen img_btn("t10.png",(800,500),None)

    "好累我想睡屁股"

    "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"
    $ renpy.scene()

    jump test