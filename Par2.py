class NodoBST:
    """Representa un nodo dentro del Árbol Binario de Búsqueda."""
    def __init__(self, codigo: int):
        self.codigo = codigo
        self.izquierdo = None
        self.derecho = None


class ArbolBST:
    """Implementación del Árbol Binario de Búsqueda para códigos de productos."""
    def __init__(self):
        self.raiz = None

    def insertar(self, codigo: int):
        if not self.raiz:
            self.raiz = NodoBST(codigo)
        else:
            self._insertar_recursivo(self.raiz, codigo)

    def _insertar_recursivo(self, nodo: NodoBST, codigo: int):
        if codigo < nodo.codigo:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoBST(codigo)
            else:
                self._insertar_recursivo(nodo.izquierdo, codigo)
        elif codigo > nodo.codigo:
            if nodo.derecho is None:
                nodo.derecho = NodoBST(codigo)
            else:
                self._insertar_recursivo(nodo.derecho, codigo)

    def buscar(self, codigo: int) -> bool:
        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, nodo: NodoBST, codigo: int) -> bool:
        if not nodo:
            return False
        if nodo.codigo == codigo:
            return True
        elif codigo < nodo.codigo:
            return self._buscar_recursivo(nodo.izquierdo, codigo)
        else:
            return self._buscar_recursivo(nodo.derecho, codigo)

    def inorden(self) -> list:
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo: NodoBST, resultado: list):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.codigo)
            self._inorden_recursivo(nodo.derecho, resultado)

    def eliminar(self, codigo: int):
        self.raiz = self._eliminar_recursivo(self.raiz, codigo)

    def _eliminar_recursivo(self, nodo, codigo):
        if not nodo:
            return nodo
        if codigo < nodo.codigo:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, codigo)
        elif codigo > nodo.codigo:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, codigo)
        else:
            # Nodo con un solo hijo o sin hijos
            if not nodo.izquierdo:
                return nodo.derecho
            elif not nodo.derecho:
                return nodo.izquierdo
            
            # Nodo con dos hijos: obtener el sucesor inorden (menor del subárbol derecho)
            sucesor = self._minimo_valor(nodo.derecho)
            nodo.codigo = sucesor.codigo
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.codigo)
        return nodo

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual


class SistemaDistribuidora:
    """Sistema integrador para la distribuidora 'Las naranjas'."""
    def __init__(self):
        # Datos iniciales obligatorios
        # Cola FIFO: Solicitudes P001, P002, P003 con datos de estudiantes
        self.cola_solicitudes = [
            {"id": "P001", "cliente": "Anderson Ezequiel Reyes Rivera"},
            {"id": "P002", "cliente": "Estudiante Colaborador 1"},
            {"id": "P003", "cliente": "Estudiante Colaborador 2"}
        ]
        
        # Pila LIFO: Despachos D001, D002, D003 registrados en ese orden
        self.pila_despachos = [
            {"operacion": "D001", "producto": "Prod-100"},
            {"operacion": "D002", "producto": "Prod-200"},
            {"operacion": "D003", "producto": "Prod-300"}
        ]
        
        # Árbol BST: Códigos 50, 30, 70, 20, 40, 60, 80 insertados en ese orden
        self.arbol_productos = ArbolBST()
        for codigo in [50, 30, 70, 20, 40, 60, 80]:
            self.arbol_productos.insertar(codigo)

    # --- A. Gestión de solicitudes (FIFO) ---
    def registrar_solicitud(self):
        codigo = input("Ingrese el código de la solicitud (Ej. P004): ").strip()
        cliente = input("Ingrese el nombre del estudiante/cliente: ").strip()
        if codigo and cliente:
            self.cola_solicitudes.append({"id": codigo, "cliente": cliente})
            print(f"-> Solicitud '{codigo}' registrada exitosamente.")
        else:
            print("Error: Los campos no pueden estar vacíos.")

    def atender_solicitud(self):
        if len(self.cola_solicitudes) > 0:
            atendida = self.cola_solicitudes.pop(0)
            print(f"-> Atendiendo solicitud: ID {atendida['id']} - Cliente: {atendida['cliente']}")
        else:
            print("-> Control: No existen solicitudes pendientes por atender.")

    def mostrar_solicitudes(self):
        print("\n--- SOLICITUDES PENDIENTES (FIFO) ---")
        if not self.cola_solicitudes:
            print("No hay solicitudes en la cola.")
        else:
            for idx, sol in enumerate(self.cola_solicitudes, 1):
                print(f"{idx}. ID: {sol['id']} | Cliente: {sol['cliente']}")

    # --- B. Registro de despachos (LIFO) ---
    def registrar_despacho(self):
        op_codigo = input("Ingrese el código de operación (Ej. D004): ").strip()
        prod_codigo = input("Ingrese el código del producto despachado: ").strip()
        if op_codigo and prod_codigo:
            self.pila_despachos.append({"operacion": op_codigo, "producto": prod_codigo})
            print(f"-> Despacho '{op_codigo}' registrado en la pila.")
        else:
            print("Error: Los campos no pueden estar vacíos.")

    def consultar_despachos(self):
        print("\n--- DESPACHOS REGISTRADOS (Pila - Base a Cima) ---")
        if not self.pila_despachos:
            print("La pila de despachos está vacía.")
        else:
            for idx, desp in enumerate(self.pila_despachos, 1):
                print(f"{idx}. Operación: {desp['operacion']} | Producto: {desp['producto']}")

    def retirar_despacho(self):
        if len(self.pila_despachos) > 0:
            revertido = self.pila_despachos.pop()
            print(f"-> Despacho revertido/retirado de la cima: Operación {revertido['operacion']} (Producto {revertido['producto']})")
        else:
            print("-> Control: Intento fallido. La pila de despachos está vacía.")

    # --- C. Consulta mediante Árbol Binario de Búsqueda ---
    def insertar_producto_arbol(self):
        try:
            codigo = int(input("Ingrese el código numérico del producto a insertar: "))
            if self.arbol_productos.buscar(codigo):
                print(f"-> El código {codigo} ya existe en el árbol.")
            else:
                self.arbol_productos.insertar(codigo)
                print(f"-> Código {codigo} insertado correctamente en el ABB.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    def buscar_producto_arbol(self):
        try:
            codigo = int(input("Ingrese el código numérico a buscar: "))
            existe = self.arbol_productos.buscar(codigo)
            if existe:
                print(f"-> ¡Resultado positivo! El código {codigo} SÍ existe en el sistema.")
            else:
                print(f"-> El código {codigo} NO fue encontrado en el árbol.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    def mostrar_inorden_arbol(self):
        elementos = self.arbol_productos.inorden()
        print("\n--- RECORRIDO INORDEN (Productos ordenados de menor a mayor) ---")
        print(elementos if elementos else "El árbol está vacío.")

    def eliminar_producto_arbol(self):
        try:
            codigo = int(input("Ingrese el código numérico que desea eliminar del árbol: "))
            if self.arbol_productos.buscar(codigo):
                self.arbol_productos.eliminar(codigo)
                print(f"-> El código {codigo} ha sido eliminado conservando las propiedades del ABB.")
            else:
                print(f"-> El código {codigo} no existe en el árbol.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    # --- D. Menú Principal ---
    def ejecutar(self):
        while True:
            print("\n==================================================")
            print("   SISTEMA DE GESTIÓN - DISTRIBUIDORA 'LAS NARANJAS'")
            print("==================================================")
            print("1. Registrar nueva solicitud (Cola FIFO)")
            print("2. Atender solicitud siguiente (Cola FIFO)")
            print("3. Mostrar solicitudes pendientes")
            print("4. Registrar nuevo despacho (Pila LIFO)")
            print("5. Consultar despachos registrados")
            print("6. Retirar último despacho / Revertir (Pila LIFO)")
            print("7. Insertar código de producto en ABB")
            print("8. Buscar código en ABB")
            print("9. Mostrar códigos en orden (Recorrido Inorden)")
            print("10. Eliminar código de producto en ABB")
            print("11. Salir")
            
            opcion = input("Seleccione una opción (1-11): ").strip()
            
            if opcion == '1':
                self.registrar_solicitud()
            elif opcion == '2':
                self.atender_solicitud()
            elif opcion == '3':
                self.mostrar_solicitudes()
            elif opcion == '4':
                self.registrar_despacho()
            elif opcion == '5':
                self.consultar_despachos()
            elif opcion == '6':
                self.retirar_despacho()
            elif opcion == '7':
                self.insertar_producto_arbol()
            elif opcion == '8':
                self.buscar_producto_arbol()
            elif opcion == '9':
                self.mostrar_inorden_arbol()
            elif opcion == '10':
                self.eliminar_producto_arbol()
            elif opcion == '11':
                print("\nSaliendo del sistema de gestión. ¡Éxitos en su defensa!")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 11.")


if __name__ == "__main__":
    app = SistemaDistribuidora()
    app.ejecutar()