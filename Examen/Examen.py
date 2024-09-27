import tkinter as tk
import random


class JuegoAventuraEstrategia:
    def __init__(self, root):
        self.root = root
        self.root.title("Caminos Inexplorados")  # Título de la ventana principal
        self.root.geometry("900x700")

        # Variables del juego
        self.vida_jugador = 100
        self.vida_enemigo = 0
        self.puntuacion = 0
        self.escenario_actual = "bosque"
        self.historia = "Te encuentras en un bosque misterioso. ¿Qué deseas hacer?"
        self.nombre_jugador = ""

        # Etiqueta del título dentro del juego
        self.titulo_label = tk.Label(self.root, text="Caminos Inexplorados", font=("Helvetica", 16, "bold"))

        # Etiquetas para mostrar la historia, vida del jugador y puntuación
        self.historia_label = tk.Label(self.root, text=self.historia, wraplength=500)
        self.vida_label = tk.Label(self.root, text=f"Vida del Jugador: {self.vida_jugador}")
        self.vida_enemigo_label = tk.Label(self.root, text="")
        self.puntuacion_label = tk.Label(self.root, text=f"Puntuación: {self.puntuacion}")
        self.mensaje_label = tk.Label(self.root, text="", fg="green")

        # Botones para el menú
        self.boton_empezar = tk.Button(self.root, text="Empezar", command=self.pedir_nombre)
        self.boton_instrucciones = tk.Button(self.root, text="Instrucciones", command=self.mostrar_instrucciones)
        self.boton_puntuaciones = tk.Button(self.root, text="Puntuaciones", command=self.mostrar_puntuaciones)
        self.boton_salir = tk.Button(self.root, text="Salir", command=root.quit)

        # Botones para las acciones del jugador
        self.boton_izquierda = tk.Button(self.root, text="Ir a la Izquierda (Cueva)", command=self.ir_a_cueva)
        self.boton_derecha = tk.Button(self.root, text="Ir a la Derecha (Castillo)", command=self.ir_a_castillo)
        self.boton_arriba = tk.Button(self.root, text="Ir al Norte (Montaña)", command=self.ir_a_montana)
        self.boton_abajo = tk.Button(self.root, text="Ir al Sur (Pantano)", command=self.ir_a_pantano)
        self.boton_atacar = tk.Button(self.root, text="Atacar Enemigo", command=self.atacar, state=tk.DISABLED)
        self.boton_descansar = tk.Button(self.root, text="Descansar", command=self.descansar)
        self.boton_regresar = tk.Button(self.root, text="Regresar a explorar", command=self.regresar_a_explorar,
                                        state=tk.DISABLED)

        # Botón para regresar al menú principal
        self.boton_menu_principal = tk.Button(self.root, text="Menú Principal", command=self.mostrar_menu_principal)

        # Mostrar el menú principal
        self.mostrar_menu_principal()

    def mostrar_menu_principal(self):
        """Muestra el menú principal con opciones de Empezar, Instrucciones, Puntuaciones, y Salir"""
        self.limpiar_pantalla()
        self.titulo_label.pack(pady=20)  # Mostrar el título al principio
        self.boton_empezar.pack(pady=10)
        self.boton_instrucciones.pack(pady=10)
        self.boton_puntuaciones.pack(pady=10)
        self.boton_salir.pack(pady=10)

    def limpiar_pantalla(self):
        """Oculta todos los elementos de la pantalla"""
        widgets = self.root.winfo_children()
        for widget in widgets:
            widget.pack_forget()

    def pedir_nombre(self):
        """Pide el nombre del jugador y comienza el juego"""
        self.limpiar_pantalla()
        self.titulo_label.pack(pady=20)  # Mostrar el título dentro del juego también
        self.nombre_label = tk.Label(self.root, text="Ingresa tu nombre:")
        self.nombre_label.pack(pady=20)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack(pady=20)
        self.boton_confirmar = tk.Button(self.root, text="Confirmar", command=self.empezar_juego)
        self.boton_confirmar.pack(pady=20)

    def empezar_juego(self):
        """Inicia el juego y muestra la interfaz del juego"""
        self.nombre_jugador = self.nombre_entry.get()
        self.limpiar_pantalla()
        self.titulo_label.pack(pady=20)  # Mostrar el título en la interfaz del juego
        self.historia_label.pack(pady=20)
        self.vida_label.pack(pady=20)
        self.vida_enemigo_label.pack(pady=10)
        self.puntuacion_label.pack(pady=10)
        self.mensaje_label.pack(pady=10)
        self.boton_izquierda.pack(pady=10)
        self.boton_derecha.pack(pady=10)
        self.boton_arriba.pack(pady=10)
        self.boton_abajo.pack(pady=10)
        self.boton_atacar.pack(pady=10)
        self.boton_descansar.pack(pady=10)
        self.boton_regresar.pack(pady=10)
        self.boton_menu_principal.pack(side=tk.TOP, anchor='ne')
        self.boton_instrucciones.pack(side=tk.TOP, anchor='ne')  # Muestra el botón de instrucciones

    def mostrar_instrucciones(self):
        """Muestra las instrucciones del juego"""
        self.limpiar_pantalla()
        instrucciones = "Instrucciones:\n1. Explora diferentes escenarios.\n2. Enfréntate a enemigos.\n3. Derrota a los enemigos y explora el mundo."
        self.historia_label.config(text=instrucciones)
        self.historia_label.pack(pady=20)
        self.boton_menu_principal.pack(side=tk.TOP, anchor='ne')

    def mostrar_puntuaciones(self):
        """Muestra las puntuaciones del jugador"""
        self.limpiar_pantalla()
        puntuaciones = f"Tu puntuación actual es: {self.puntuacion}"
        self.historia_label.config(text=puntuaciones)
        self.historia_label.pack(pady=20)
        self.boton_menu_principal.pack(side=tk.TOP, anchor='ne')

    def ir_a_cueva(self):
        """Acción al ir a la cueva"""
        self.historia = "Te diriges a una cueva oscura. Hay un enemigo esperando."
        self.vida_enemigo = random.randint(20, 50)
        self.boton_atacar.config(state=tk.NORMAL)  # Habilitar el botón de atacar
        self.actualizar_interfaz()

    def ir_a_castillo(self):
        """Acción al ir al castillo"""
        self.historia = "Te diriges al castillo abandonado. Es un lugar peligroso."
        self.vida_enemigo = random.randint(30, 60)
        self.boton_atacar.config(state=tk.NORMAL)  # Habilitar el botón de atacar
        self.actualizar_interfaz()

    def ir_a_montana(self):
        """Acción al ir a la montaña"""
        self.historia = "Subes a la montaña y te enfrentas a los vientos helados. Un enemigo aparece."
        self.vida_enemigo = random.randint(40, 70)
        self.boton_atacar.config(state=tk.NORMAL)  # Habilitar el botón de atacar
        self.actualizar_interfaz()

    def ir_a_pantano(self):
        """Acción al ir al pantano"""
        self.historia = "Llegas al pantano. Hay enemigos y el terreno es difícil."
        self.vida_enemigo = random.randint(25, 55)
        self.boton_atacar.config(state=tk.NORMAL)  # Habilitar el botón de atacar
        self.actualizar_interfaz()

    def atacar(self):
        """Acción de atacar al enemigo"""
        if self.vida_enemigo > 0:
            dano_jugador = random.randint(5, 15)
            self.vida_enemigo -= dano_jugador
            self.historia = f"¡Atacas al enemigo y le haces {dano_jugador} de daño!"

            # Asegurarse de que la vida del enemigo no sea negativa
            if self.vida_enemigo < 0:
                self.vida_enemigo = 0
                self.historia += "\n¡Has derrotado al enemigo!"

                self.puntuacion += 10

            # El enemigo ataca al jugador
            if self.vida_enemigo > 0:  # Solo ataca si aún está vivo
                dano_enemigo = random.randint(5, 10)
                self.vida_jugador -= dano_enemigo
                self.historia += f"\nEl enemigo te ataca y te hace {dano_enemigo} de daño."

            if self.vida_jugador <= 0:
                self.historia = "¡Has sido derrotado!"
                self.boton_atacar.config(state=tk.DISABLED)
            else:
                self.boton_atacar.config(state=tk.NORMAL)

        self.actualizar_interfaz()

    def descansar(self):
        """Acción de descansar para recuperar vida"""
        if self.vida_jugador < 100:
            recuperacion = random.randint(10, 30)
            self.vida_jugador += recuperacion
            if self.vida_jugador > 100:
                self.vida_jugador = 100
            self.historia = f"Descansas y recuperas {recuperacion} de vida."
        else:
            self.historia = "Tu vida está completa. No puedes descansar más."

        self.actualizar_interfaz()

    def regresar_a_explorar(self):
        """Regresar a explorar después de una batalla"""
        self.limpiar_pantalla()
        self.historia_label.pack(pady=20)
        self.vida_label.pack(pady=20)
        self.vida_enemigo_label.pack(pady=10)
        self.puntuacion_label.pack(pady=10)
        self.mensaje_label.pack(pady=10)
        self.boton_izquierda.pack(pady=10)
        self.boton_derecha.pack(pady=10)
        self.boton_arriba.pack(pady=10)
        self.boton_abajo.pack(pady=10)
        self.boton_atacar.pack(pady=10)
        self.boton_descansar.pack(pady=10)

    def actualizar_interfaz(self):
        """Actualiza la interfaz con la información actual del juego"""
        self.historia_label.config(text=self.historia)
        self.vida_label.config(text=f"Vida del Jugador: {self.vida_jugador}")
        self.vida_enemigo_label.config(text=f"Vida del Enemigo: {self.vida_enemigo}")
        self.puntuacion_label.config(text=f"Puntuación: {self.puntuacion}")
        self.mensaje_label.config(text="")  # Limpia el mensaje anterior

        # Mostrar el mensaje cuando el jugador es derrotado
        if self.vida_jugador <= 0:
            self.mensaje_label.config(text="¡Has sido derrotado!")

        # Mostrar el mensaje cuando el enemigo es derrotado
        if self.vida_enemigo <= 0:
            self.mensaje_label.config(text="¡Felicidades, has derrotado al enemigo! Puedes seguir explorando.")


# Ejecución del juego
root = tk.Tk()
juego = JuegoAventuraEstrategia(root)
root.mainloop()
