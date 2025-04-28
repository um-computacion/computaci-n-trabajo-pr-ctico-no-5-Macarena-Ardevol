# src/alumno.py

from src.persona import Persona
from src.materia import Materia

class Alumno(Persona):  # Heredamos de la clase Persona
    def __init__(self, nombre, apellido, dni, materias=None):
        super().__init__(nombre, apellido, dni)  # Inicializamos atributos de Persona
        self.materias = materias if materias else []  # Lista de materias inscritas
        self.notas = {}  # Diccionario de notas por materia
    
    def agregar_materia(self, materia):
        if isinstance(materia, Materia):
            self.materias.append(materia)
        else:
            print("La materia debe ser un objeto de la clase Materia.")
    
    def agregar_nota(self, materia, nota):
        if materia in self.materias:
            self.notas[materia] = nota
        else:
            print("El alumno no está inscrito en esta materia.")
    
    def obtener_promedio(self):
        if self.notas:
            return sum(self.notas.values()) / len(self.notas)
        else:
            return 0  # Si no tiene notas, el promedio es 0
