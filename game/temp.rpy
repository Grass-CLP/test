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