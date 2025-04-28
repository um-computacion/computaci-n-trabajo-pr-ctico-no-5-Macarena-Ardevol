import unittest
from src.materia import Materia
from src.profesor import Profesor

class TestMateria(unittest.TestCase):
    def test_creacion_materia(self):
        profesor = Profesor("Ana", "García", "98765432", "Programación")
        materia = Materia("Computación I", "COMP1", profesor)
        
        self.assertEqual(materia.nombre, "Computación I")
        self.assertEqual(materia.codigo, "COMP1")
        self.assertEqual(materia.profesor.nombre, "Ana")
        self.assertEqual(materia.profesor.apellido, "García")
        self.assertEqual(materia.profesor.dni, "98765432")
        self.assertEqual(materia.profesor.materia, "Programación")

if __name__ == "__main__":
    unittest.main()
