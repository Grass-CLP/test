init -2 python:
    import sys
    sys.path.append(".")
    from tools import tool_bar
    import pygame

    # ToolBar = tool_bar.export("ToolBar", ui, renpy, pygame)
    # AreaEvent = tool_bar.export("AreaEvent", ui, renpy, pygame)
    # Item = tool_bar.export("Item", ui, renpy, pygame)
    Item, AreaEvent, ToolBar = tool_bar.export(ui, renpy, pygame)

    a = AreaEvent()

    eggplant = Item("xx", "images/t10.png")
    print(eggplant)

init:
    define e = Character("艾琳")

    default eggplant = Item(__("茄子"), "images/t10.png")
    default sleepface = Item(__("睡脸"), "images/b1.png")
    default laughface = Item(__("笑脸"), "images/b12.png")
    default handsup = Item(__("举手"), "images/q11.png")
