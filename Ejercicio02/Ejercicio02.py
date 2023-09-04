from hypothesis import given
import hypothesis.strategies as st

# Supongamos que tenemos una función simple que suma dos números
def suma(a, b):
    return a + b

# Definimos una estrategia de entrada que genera pares de números enteros.
@given(st.integers(), st.integers())
def test_suma(a, b):
    resultado = suma(a, b)
    
    # Verificamos que la suma es igual a la suma esperada.
    assert resultado == a + b

# Ejecutamos las pruebas generadas por Hypothesis.
test_suma()