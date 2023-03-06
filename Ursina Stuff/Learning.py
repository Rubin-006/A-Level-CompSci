from ursina import *


app = Ursina(size=(1000,800))

cube = Entity(model="cube",color = color.orange,scale=(2,2,2),texture="brick")


def update():
    if held_keys["w"]: cube.rotation_x += time.dt * 250
    if held_keys["s"]: cube.rotation_x -= time.dt * 250

window.borderless = False
window.exit_button.visible = False
window.borderless = False
EditorCamera()
app.run()