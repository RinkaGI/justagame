from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController
import sys

app = Ursina()

# Algunas configuraciones
window.size = (1280, 890)
Entity.default_shader = lit_with_shadows_shader
random.seed(0)
Sky()

# El jugador
player = FirstPersonController()

# Se me olvidó que necesitaba un suelo
class Suelo(Entity):
    def __init__(self, position):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            texture = 'grass',
            origin_y = .5,
            collider = 'box' # Se me olvidó que tenía que ponerle el collider
        )

for z in range(16):
    for x in range(16):
        Suelo(position=(x, -1, z))

# Por ultimo el sol para que se vea mas bonito :D
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))

# Entrada de teclado
def input(key):
    if key == 'escape':
        quit()
        sys.exit(0)
        
app.run()