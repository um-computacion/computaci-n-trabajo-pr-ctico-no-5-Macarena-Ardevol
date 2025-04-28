class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<no pensó en nada>"

    def __repr__(self):
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"

    def pensar(self, idea):
        """Incrementa el contador de pensamientos y actualiza la última idea."""
        self.pensamientos += 1
        self.ultima_idea = idea
