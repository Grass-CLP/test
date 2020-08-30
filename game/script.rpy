# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")


# 游戏在此开始。

init python:

    def detective_dragged(drags, drop):

        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        return True

screen send_detective_screen:

    # 作为背景的地图。
    # add "europe.jpg"

    # DragGroup确保每个侦探可以拖拽到每个城市。
    draggroup:

        # 侦探们
        drag:
            drag_name "Ivy"
            child "b1.png"
            droppable False
            dragged detective_dragged
            xpos 100 ypos 100
        drag:
            drag_name "Zack"
            child "b12.png"
            droppable False
            dragged detective_dragged
            xpos 150 ypos 100

        # 可选的城市。
        drag:
            drag_name "London"
            child "q11.png"
            draggable False
            xpos 450 ypos 140
        drag:
            drag_name "Paris"
            draggable False
            child "t10.png"
            xpos 500 ypos 280

default canned_food = Item(__("罐装食物"), "images/t10.png")
default canned_food1 = Item(__("罐装食物1"), "images/b1.png")
default canned_food2 = Item(__("罐装食物2"), "images/b12.png")
default canned_food3 = Item(__("罐装食物3"), "images/q11.png")
default canned_food4 = Item(__("罐装食物4"), "images/b1.png")

default items = [canned_food, canned_food1, canned_food2, canned_food3]
default tb = ToolBar("images/bg/1.png", None, rect=(0, 0, 160, 1080), direction=1, items=items)


init python:
    def items_init():
        mar = 300
        for i in range(max(len(items), 8)):
            item = items[i]
            Drag(None, drag_name=item.name, dchild=item.img_idle)
    

label start:
    scene 2
    with fade

    # show screen input(_("xxxx"), "xxx")
    "fuck u asshole!!!!"

    $ print(canned_food)
    $ tb.show()
    $ tb.sensitive = True

    "dfsdf"

    python:
        # items = [canned_food, canned_food1, canned_food2, canned_food3]

        # print(store.items)
        # print(len(items))
        # items = [canned_food, canned_food1, canned_food2, canned_food3]
        # tb = ToolBar("images/bg/1.png", None, rect=(0, 0, 160, 1080), direction=1, items=items)
        # tb.show()
        # print(canned_food)
        pass

    # call screen send_detective_screen

    "好的，我们派 [detective] 去 [city]。"

    # call screen say("xxx", "yyy")

    call screen img_btn("images/b1.png",(200,100),None)

    call screen say_2("xxx", "yyy")


    "fuck!!!!!!!!"

    show eileen happy
    show 3 at right

    e "您已创建一个新的 Ren'Py 游戏。"

    call screen drag_img("test")

    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    show screen go(_("xxxx"), "xxx")

label test:
    scene 3 with dissolve

    "fuck2"

    jump testx