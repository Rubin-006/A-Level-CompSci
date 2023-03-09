from classes import *
from ursina import *

class SolarSystem:

    def __init__(self,star,planet):
        m1 = 2*(10**30)
        self.star = StellarBody(body=star,r=696340,m=m1)
        self.planet = StellarBody(body=planet,r=6371,m=6*(10**24))


    def velcity_calc(self):
        self







if __name__ == "__main__":
    app = Ursina(size=(1000,800))

    sun = Entity(model="sphere",scale=(109,109,109),texture="sun.jpg")
    earth = Entity(model="sphere",position = (0,0,(-500)),scale=(20,20,20),texture="earth.jpg")
    earth.look_at(sun)
    
    SS = SolarSystem(
        sun,
        earth
        )

    def update():
        velocity = Vec3(100,200,-270)
        earth.x += velocity.x
        earth.y += velocity.y
        earth.z += velocity.z
        if held_keys["d"]: sun.x += time.dt * 5
        if held_keys["a"]: sun.x -= time.dt * 5
        if held_keys["w"]: sun.y += time.dt * 5
        if held_keys["s"]: sun.y -= time.dt * 5









    window.borderless = False
    window.exit_button.visible = False
    window.borderless = False
    EditorCamera()
    app.run()