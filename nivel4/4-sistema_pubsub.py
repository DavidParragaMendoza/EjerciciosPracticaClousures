from typing import Any, Callable, Dict, List


def crear_sistema_eventos() -> Dict[str, Callable[..., Any]]:
    suscriptores: List[Callable[[Any], None]] = []

    def registrar(fn_suscriptor: Callable[[Any], None]) -> None:
        suscriptores.append(fn_suscriptor)

    def emitir(datos_evento: Any) -> int:
        for suscriptor in suscriptores:
            suscriptor(datos_evento)
        return len(suscriptores)

    return {"registrar": registrar, "emitir": emitir}


gestor = crear_sistema_eventos()
gestor["registrar"](lambda mensaje: print(f"Email recibió: {mensaje}"))
gestor["registrar"](lambda mensaje: print(f"Logger recibió: {mensaje}"))
print(f"Total notificados: {gestor['emitir']({'tipo': 'ALERTA', 'codigo': 404})}")
