from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()

sword_texture = load_texture("sword.png")
Sky()

sword = Entity(
    parent=camera.ui,
    model="cube",
    texture=sword_texture,
    position=(0.6, -0.4),
    scale=(1, 1, 1),
    enabled=False,
    rotation=(0, 0, -90)
)


attack_in_progress = False


def attack():
    global attack_in_progress
    if attack_in_progress:
        return
    attack_in_progress = True
    sword.enabled = True
    sword.animate_rotation_z(45, duration=0.1)
    sword.animate_rotation_z(-90, duration=0.1, delay=0.1)
    invoke(finish_attack, delay=0.2)


def finish_attack():
    global attack_in_progress
    sword.enabled = False
    attack_in_progress = False


sword.on_click = attack


def update():
    if held_keys["left mouse"] or held_keys["right mouse"]:
        attack()


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
