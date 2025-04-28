import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_creacion_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")

if __name__ == "__main__":
    unittest.main()
