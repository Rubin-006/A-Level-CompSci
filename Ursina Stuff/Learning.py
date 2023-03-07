from ursina import *


app = Ursina(size=(1000,800))

cube = Entity(model="cube",color = color.orange,scale=(2,2,2),texture="brick")


def update():
    if held_keys["d"]: cube.x += time.dt * 5
    if held_keys["a"]: cube.x -= time.dt * 5
    if held_keys["w"]: cube.y += time.dt * 5
    if held_keys["s"]: cube.y -= time.dt * 5

window.borderless = False
window.exit_button.visible = False
window.borderless = False
EditorCamera()
app.run()