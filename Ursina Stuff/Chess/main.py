from ursina import *


class Square(Entity):

    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)






class Chess:


    def __init__(self,w,h):
        self.game = Ursina(size=(w,h))
        window.borderless = False
        window.exit_button.visible = False
        window.borderless = False
        EditorCamera()

    def build_board(self):
      col = color.black
      for i in range(8):
          col = color.black if col != color.black else color.yellow
          for j in range(8):
              col = color.black if col != color.black else color.yellow
              s = Square(model="cube",color=col,position=(i,j))
    def run(self):
        self.game.run()




g = Chess(1000,800)
    



def update():
    if held_keys["q"]:quit()



g.build_board()
g.run()