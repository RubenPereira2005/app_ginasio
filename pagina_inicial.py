import tkinter as tk

class PaginaInicial:
    def __init__(self, frame_principal):
        self.frame_principal = frame_principal

    def mostrar_pagina_inicial(self):
        """Exibe a página inicial."""
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text="Bem-vindo ao Ginásio!", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.frame_principal, text="Escolha uma opção no menu.", font=("Arial", 14)).pack(pady=10)