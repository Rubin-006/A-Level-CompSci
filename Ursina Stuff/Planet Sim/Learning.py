from classes import *
from ursina import *






if __name__ == "__main__":
    app = Ursina(size=(1000,800))

    sun = Entity(model="sphere",texture="sun.jpg",scale=1)
    earth = Entity(model="sphere",scale=.5,texture="earth.jpg")

    t = -pi
    def update():
        global t
        t += 0.01
        angle = pi*2

        radius = 5
        pd = 4
        earth.x = -cos(pd*t + angle) * radius
        earth.y = sin(pi/2-(pd*t + angle))* radius
        earth.z = sin(pi-(pd*t + angle)) * radius
        sun.rotation_y += 20*time.dt
        earth.rotation_y += 20*time.dt

    window.borderless = False
    window.exit_button.visible = False
    window.borderless = False
    EditorCamera()
    app.run()