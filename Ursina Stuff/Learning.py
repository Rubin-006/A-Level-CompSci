from classes import *
from ursina import *






if __name__ == "__main__":
    app = Ursina(size=(1000,800))

    sun = Entity(model="sphere",texture="sun.jpg")
    earth = Entity(model="sphere",position = (10,0,0),texture="earth.jpg")

    def update():
        velocity = Vec3(-earth.x,-earth.y,-earth.z)
        earth.x += (velocity.x)*0.01
        earth.y += (velocity.y)*0.01+time.dt *10
        earth.z += (velocity.z)*0.01+time.dt *10
        earth.look_at(sun)
        if held_keys["d"]: sun.x += time.dt * 5
        if held_keys["a"]: sun.x -= time.dt * 5
        if held_keys["w"]: sun.y += time.dt * 5
        if held_keys["s"]: sun.y -= time.dt * 5









    window.borderless = False
    window.exit_button.visible = False
    window.borderless = False
    EditorCamera()
    app.run()