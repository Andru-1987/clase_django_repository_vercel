import pytest
from django.core.exceptions import ValidationError
from entidades.models import Estudiante

# @pytest.mark.django_db  # le indica que puede acceder a la base de datos
def test_estudiante_create_to_fail_long_name():

    # esto no guarda en la base de datos
    estudiante = Estudiante(
            nombre="Supercalifragilisticoespialidosamenteultracomplejo Megahipertransdisciplinariamentedesproporcionado",
            apellido="Pirulo",
            email="maria@example.com"
        )

    # Lo que esté dentro de este bloque debe lanzar una excepción ValidationError
    with pytest.raises(ValidationError):
        estudiante.full_clean()
    