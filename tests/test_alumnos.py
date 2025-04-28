# tests/test_alumno.py

import unittest
from src.alumno import Alumno
from src.materia import Materia

class TestAlumno(unittest.TestCase):
    
    def setUp(self):
        # Creamos un objeto Alumno y una materia para probar
        self.alumno = Alumno("Juan", "Pérez", "12345678")
        self.materia_matematica = Materia("Matemáticas", "MAT101", 3)
    
    def test_agregar_materia(self):
        self.alumno.agregar_materia(self.materia_matematica)
        self.assertIn(self.materia_matematica, self.alumno.materias)
    
    def test_agregar_nota(self):
        self.alumno.agregar_materia(self.materia_matematica)
        self.alumno.agregar_nota(self.materia_matematica, 8)
        self.assertEqual(self.alumno.notas[self.materia_matematica], 8)
    
    def test_obtener_promedio(self):
        self.alumno.agregar_materia(self.materia_matematica)
        self.alumno.agregar_nota(self.materia_matematica, 8)
        self.assertEqual(self.alumno.obtener_promedio(), 8)

if __name__ == "__main__":
    unittest.main()
