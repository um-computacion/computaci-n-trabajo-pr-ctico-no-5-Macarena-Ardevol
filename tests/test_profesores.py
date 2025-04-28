import unittest
from src.profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_creacion_profesor(self):
        profesor = Profesor("Ana", "García", "87654321", "Matemática")
        self.assertEqual(profesor.nombre, "Ana")
        self.assertEqual(profesor.apellido, "García")
        self.assertEqual(profesor.dni, "87654321")
        self.assertEqual(profesor.materia, "Matemática")
        self.assertEqual(profesor.ultima_idea, "Educar es mi vocación")

    def test_repr_profesor(self):
        profesor = Profesor("Ana", "García", "87654321", "Matemática")
        expected = ("Profesor: DNI: 87654321 Nombre: Ana Apellido: García "
                    "Materia: Matemática Ultima Idea: Educar es mi vocación")
        self.assertEqual(str(profesor), expected)

if __name__ == "__main__":
    unittest.main()
