from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

sword_texture = load_texture("sword.png")

sword = Entity(
    parent=camera.ui,
    model="cube",
    texture=sword_texture,
    position=(0.6, -0.4),
    scale=(0.3, 0.5),
)


def update():
    if held_keys["left mouse"] or held_keys["right mouse"]:
        sword.position = (0.5, -0.3)
        sword.scale = (0.6, 0.9)
    else:
        sword.position = (0.6, -0.4)
        sword.scale = (0.5, 0.8)


boxes = []

for i in range(20):
    for j in range(20):
        box = Button(
            color=color.white,
            model="cube",
            position=(j, 0, i),
            texture="grass_3d.png",
            parent=scene,
            origin_y=0.5,
        )
        boxes.append(box)


def input(key):
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                new = Button(
                    color=color.white,
                    model="cube",
                    position=box.position + mouse.normal,
                    texture="grass_3d.png",
                    parent=scene,
                    origin_y=0.5,
                )
                boxes.append(new)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)


app.run()
