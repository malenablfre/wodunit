
class Role:
    def __init__(self, role_name, description):
        self.role_name = role_name
        self.description = description

    

class Player(Role):
    def __init__(self, name: str, role: Role):
        super().__init__()
        self.name = name
        self.role = role
        self.dead = False

    def die(self):
        self.dead = True

