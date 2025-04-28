from src.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, materia):
        super().__init__(nombre, apellido, dni)
        self.materia = materia
        self.ultima_idea = "Educar es mi vocación"

    def __repr__(self):
        return (f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} "
                f"Materia: {self.materia} Ultima Idea: {self.ultima_idea}")
