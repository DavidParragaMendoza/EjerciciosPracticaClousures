from typing import Callable


def crear_conversor(tasa: float, margen_lambda: Callable[[float], float]) -> Callable[[float], float]:
    def convertir_monto(monto_base: float) -> float:
        monto_convertido = monto_base * tasa
        return monto_convertido + margen_lambda(monto_convertido)

    return convertir_monto


conversor_euros = crear_conversor(0.92, lambda monto: monto * 0.05)
print(f"100 USD a euros (incluyendo comisión): €{conversor_euros(100.0)}")
