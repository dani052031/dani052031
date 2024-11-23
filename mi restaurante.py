class Restaurante:
    def __init__(self):
        self.menu = {
            "Tacos": 60,
            "Burrito": 80,
            "Ensalada": 50,
            "Sopa": 40,
            "Postre": 30,
            "Menú Infantil": 35
        }
        self.reservas = []
        self.pedidos = []
        self.comentarios = []
        self.promociones = []
        self.clientes_diarios = {}
        self.mantenimiento_fisico = []

    def mostrar_menu(self):
        print("Menú del Restaurante:")
        for platillo, precio in self.menu.items():
            print(f"{platillo}: ${precio}")

    def hacer_reserva(self, nombre, fecha, hora):
        self.reservas.append({"nombre": nombre, "fecha": fecha, "hora": hora})
        print(f"Reserva hecha para {nombre} el {fecha} a las {hora}.")

    def tomar_pedido(self):
        print("¿Qué te gustaría pedir? (Escribe 'fin' para terminar)")
        while True:
            platillo = input("Ingrese el nombre del platillo: ")
            if platillo.lower() == 'fin':
                break
            elif platillo in self.menu:
                self.pedidos.append(platillo)
                print(f"{platillo} agregado a tu pedido.")
            else:
                print("Platillo no encontrado en el menú.")

    def mostrar_pedido(self):
        if not self.pedidos:
            print("No has realizado ningún pedido.")
        else:
            total = sum(self.menu[platillo] for platillo in self.pedidos)
            print("Tu pedido:")
            for platillo in self.pedidos:
                print(f"- {platillo}: ${self.menu[platillo]}")
            print(f"Total: ${total}")

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)
        print("Comentario agregado.")

    def agregar_promocion(self, promocion):
        self.promociones.append(promocion)
        print("Promoción agregada.")

    def registrar_cliente_diario(self, fecha, num_clientes):
        if fecha in self.clientes_diarios:
            self.clientes_diarios[fecha] += num_clientes
        else:
            self.clientes_diarios[fecha] = num_clientes
        print(f"Clientes registrados para el {fecha}: {num_clientes}")

    def mostrar_clientes_semanales(self):
        total_semanal = sum(self.clientes_diarios.values())
        print(f"Número total de clientes esta semana: {total_semanal}")

    def registrar_mantenimiento(self, tarea):
        self.mantenimiento_fisico.append(tarea)
        print("Tarea de mantenimiento registrada.")

    def mostrar_mantenimiento(self):
        if not self.mantenimiento_fisico:
            print("No hay tareas de mantenimiento registradas.")
        else:
            print("Tareas de mantenimiento:")
            for tarea in self.mantenimiento_fisico:
                print(f"- {tarea}")

# Ejemplo de uso de la aplicación
restaurante = Restaurante()
restaurante.mostrar_menu()
restaurante.hacer_reserva("Juan Perez", "2024-11-20", "19:00")
restaurante.tomar_pedido()
restaurante.mostrar_pedido()
restaurante.agregar_comentario("Excelente servicio.")
restaurante.agregar_promocion("10% de descuento en la compra de un menú infantil.")
restaurante.registrar_cliente_diario("2024-11-16", 50)
restaurante.mostrar_clientes_semanales()
restaurante.registrar_mantenimiento("Revisar aire acondicionado.")
restaurante.mostrar_mantenimiento()
