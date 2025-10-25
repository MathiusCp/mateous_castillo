import pytest
from app import sumar, restar, dividir

def test_sumar_correcto():
    assert sumar(2, 3) == 5   # ✅ correcta

def test_restar_error():
    assert restar(5, 2) == 3  # ❌ error intencional

def test_dividir_todos_errores():
    assert dividir(10, 2) == 5  # 💥 error intencional
    assert dividir(5, 5) == 1   # 💥 otro error por dividir entre cero
