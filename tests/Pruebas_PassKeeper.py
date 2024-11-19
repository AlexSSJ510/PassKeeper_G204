import unittest
from unittest.mock import patch, mock_open

from PassKeeper.src.logica.Contraseñas import Contrasena
from PassKeeper.src.logica.Contraseñas import GestorContraseñas


class TestContrasena(unittest.TestCase):

    def test_contrasena_segura(self):
        contrasena = Contrasena("Passw0rd!")
        self.assertTrue(contrasena.es_segura())

if __name__ == '__main__':
    unittest.main()
