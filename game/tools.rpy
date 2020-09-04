init -1 python:
    import pygame

    class Item(renpy.store.object):
        def __init__(self, name="", pic="", rect=(0,0,0,0)):
            self.name = name
            self.rect = rect
            self.index = -1
            self.offset = __Fixed(0, 0)

            self.pic = renpy.easy.displayable(pic)

        def place(self):
            return self.rect[0:2]

        def springback(self, tb):
                x, y = self.place()
                ox, oy = self.offset.offset()
                self.offset = __Springback(self, tb, x + ox, y + oy)

        def center_pos(self):
            x, y, w, h = self.rect
            ox, oy = self.offset.offset()
            return x + ox + w / 2, y + oy + h / 2

        def __repr__(self):
            return "Item: {}".format(self.name)

    class AreaEvent():
        def __init__(self, rect=(0,0,100,100), item=None, label=None):
            self.rect = rect
            self.item = item
            self.label = label

        def event(self, item):
            if item is self.item:
                # renpy.checkpoint()
                renpy.jump(self.label)
                return self

            return None
        

    class ToolBar(renpy.Displayable):
        def __init__(self, back=None, base=None, springback=0.1, rect=(0,0,0,0), direction=0, num=8, margin=0.1, items=[], areaevens=[], **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)

            # The back of cards that don't have a more specific back
            # defined.
            self.back = renpy.easy.displayable_or_none(back)

            # The base of stacks that don't have a more specific base
            # defined.
            self.base = renpy.easy.displayable_or_none(base)

            # The amount of time it takes for item to springback
            # into their rightful place.
            self.springback = springback

            # The item that is being dragged.
            self.drag_item = None

            # The amount of time we've been shown for.
            self.st = 0

            self.x, self.y, self.w, self.h = rect

            self.items = items
            self.areaevens = areaevens
            self.item_rects = []
            self.sensitive = False
            self.click_x = 0
            self.click_y = 0
            self.dragging = False


            # for areaeven in self.areaevens:

            # calc item pos
            if direction == 0:
                item_box = min(int(self.w / num), self.h)
                for i in range(num):
                    item_rect = (int(self.x + item_box * (i + margin)), int(self.y + item_box * margin),
                                int(item_box * (1 - 2 * margin)), int(item_box * (1 - 2 * margin)))
                    self.item_rects.append(item_rect)
            else:
                item_box = min(int(self.h / num), self.w)
                for i in range(num):
                    item_rect = (int(self.x + item_box * margin), int(self.y + item_box * (i + margin)),
                                int(item_box * (1 - 2 * margin)), int(item_box * (1 - 2 * margin)))
                    self.item_rects.append(item_rect)
                    
            for i in range(min(len(items), num)):
                items[i].rect = self.item_rects[i]
                items[i].index = i

        def _reset(self):
            for i in range(min(len(items), len(self.item_rects))):
                items[i].rect = self.item_rects[i]
                items[i].offset = __Fixed(0,0)
                items[i].index = i
            self.dragging = False
            self.click_x = 0
            self.click_y = 0
            self.drag_item = None

        def show(self, layer='master'):
            ui.layer(layer)
            ui.add(self)
            ui.close()

        def hide(self, layer='master'):
            ui.layer(layer)
            ui.remove(self)
            ui.close()

        def set_evens(self, areaevens):
            if type(areaevens) is list:
                self.areaevens = areaevens
            else:
                self.areaevens = [areaevens]

            self._reset()

        def set_items(self, items):
            if type(items) is list:
                self.items = items
            else:
                self.items = [items]

            self._reset()

        # Force a redraw on each interaction.
        def per_interact(self):
            renpy.redraw(self, 0)

        def interact(self):
            ui.interact()

        def render(self, width, height, st, at):
            self.st = st

            rv = renpy.Render(width, height)

            for item in self.items:
                x, y, w, h = item.rect
                if w == 0 or h == 0:
                    continue
                ox, oy = item.offset.offset()
                surf = renpy.render(item.pic, width, height, st, at)
                w, h = surf.get_size()
                item.rect = x, y , w, h
                rv.blit(surf, (x + ox, y + oy))
            
            return rv

        def event(self, ev, x, y, st):

            self.st = st

            if not self.sensitive:
                return

            grabbed = renpy.display.focus.get_grab()

            if (grabbed is not None) and (grabbed is not self):
                return
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                item = None
                
                for it in self.items:
                    sx, sy, sw, sh = it.rect
                    if sx <= x and sy <= y and sx + sw > x and sy + sh > y:
                        item = it
                        break
                            
                if item is None:
                    return

                # Grab the display.
                renpy.display.focus.set_grab(self)
                item.offset = __Fixed(0, 0)
                
                self.drag_item = item
                self.click_x = x
                self.click_y = y
                self.dragging = False
                
                renpy.redraw(self, 0)
                
                raise renpy.IgnoreEvent()

            if ev.type == pygame.MOUSEMOTION or (ev.type == pygame.MOUSEBUTTONUP and ev.button == 1):

                if abs(x - self.click_x) > 7 or abs(y - self.click_y) > 7 and self.drag_item is not None:
                    self.dragging = True

                if self.dragging and self.drag_item is not None:
                    dx = x - self.click_x
                    dy = y - self.click_y

                    self.drag_item.offset = __Fixed(dx, dy)
                    renpy.redraw(self, 0)

                    if ev.type == pygame.MOUSEMOTION:
                        raise renpy.IgnoreEvent()

            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:

                # Ungrab the display.
                renpy.display.focus.set_grab(None)

                evt = None

                if self.dragging and self.drag_item is not None:

                    for areaeven in self.areaevens:
                        print("pos: ({}, {})".format(*self.drag_item.center_pos()))
                        print("even rect: ({}, {}, {}, {})".format(*areaeven.rect))
                        if __pos_area_in(self.drag_item.center_pos(), areaeven.rect):
                            evt = areaeven.event(self.drag_item)
                            break;

                    self.dragging = False

                if self.drag_item:
                    self.drag_item.springback(self)
                    
                self.click_card = None
                self.click_stack = None
                self.drag_item = None

                if evt is not None:
                    return evt
                else:
                    raise renpy.IgnoreEvent()


    class __Springback(object):

        def __init__(self, item, toolbar, startx, starty):
            self.item = item
            self.toolbar = toolbar
            
            self.start = toolbar.st

            self.startx = startx
            self.starty = starty

        def offset(self):

            t = (self.toolbar.st - self.start) / self.toolbar.springback
            t = min(t, 1.0)
            
            if t < 1.0:
                renpy.redraw(self.toolbar, 0)

            px, py = self.item.place() 
                
            return int((self.startx - px) * (1.0 - t)), int((self.starty - py) * (1.0 - t))


    class __Fixed(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def offset(self):
            return self.x, self.y


    def __rect_overlap_area(r1, r2):
        if r1 is None or r2 is None:
            return 0
        
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2

        maxleft = max(x1, x2)
        minright = min(x1 + w1, x2 + w2)
        maxtop = max(y1, y2)
        minbottom = min(y1 + h1, y2 + h2)

        if minright < maxleft:
            return 0

        if minbottom < maxtop:
            return 0

        return (minright - maxleft) * (minbottom - maxtop)

    def __rect_area_in(r1, r2):
        if r1 is None or r2 is None:
            return False
        
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2

        cx, cy = x1 + w1/2, y1 + h1/2
        return cx >= x2 and cx <= x2 + w2 and cy >= y2 and cy <= y2 + h2

    def __pos_area_in(pos, r2):
        if pos is None or r2 is None:
            return False
        
        cx, cy = pos
        x2, y2, w2, h2 = r2

        return cx >= x2 and cx <= x2 + w2 and cy >= y2 and cy <= y2 + h2