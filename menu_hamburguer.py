import tkinter as tk
from tkinter import messagebox

import tkinter as tk

class MenuHamburguer:
    def __init__(self, root, frame_principal, mostrar_aulas_callback, voltar_pagina_inicial_callback, mostrar_calendario_callback, mostrar_planos_mensais_callback, logout_callback):
        self.root = root
        self.frame_principal = frame_principal
        self.mostrar_aulas_callback = mostrar_aulas_callback
        self.voltar_pagina_inicial_callback = voltar_pagina_inicial_callback
        self.mostrar_calendario_callback = mostrar_calendario_callback
        self.mostrar_planos_mensais_callback = mostrar_planos_mensais_callback
        self.logout_callback = logout_callback

        self.menu_aberto = False
        self.frame_menu = None
        self.botao_menu = None

    def limpar_frame(self, frame):
        """Remove todos os widgets de um frame."""
        for widget in frame.winfo_children():
            widget.destroy()

    def criar_botao(self, parent, texto, comando, bg="white", fg="#333", font=("Arial", 12), activebackground="#e0e0e0"):
        """Cria e retorna um botão estilizado."""
        return tk.Button(
            parent,
            text=texto,
            command=comando,
            bg=bg,
            fg=fg,
            font=font,
            bd=0,
            activebackground=activebackground,
        )

    def mostrar_menu_hamburguer(self):
        """Adiciona o botão de menu hambúrguer apenas em páginas principais."""
        if self.botao_menu and self.botao_menu.winfo_exists():
            return

        self.botao_menu = self.criar_botao(
            self.root,
            texto="☰",
            comando=self.toggle_menu,
            bg="#4682b4",
            fg="white",
            font=("Arial", 18),
            activebackground="#315f82",
        )
        self.botao_menu.place(x=10, y=10)

    def remover_menu_hamburguer(self):
        """Remove o botão de menu hambúrguer."""
        if self.botao_menu:
            self.botao_menu.destroy()

    def toggle_menu(self):
        """Mostra ou oculta o menu hambúrguer."""
        if self.menu_aberto:
            self.fechar_menu()
        else:
            self.abrir_menu()

    def abrir_menu(self):
        """Exibe o menu hambúrguer com estilo lateral."""
        menu_largura = 200
        menu_altura = self.root.winfo_height()

        self.frame_menu = tk.Frame(self.root, bg="#f8f9fa", width=menu_largura, height=menu_altura)
        self.frame_menu.place(x=0, y=0)

        tk.Label(
            self.frame_menu,
            text="Menu",
            bg="#4682b4",
            fg="white",
            font=("Arial", 14, "bold"),
            height=2,
        ).pack(fill="x")

        botoes = [
            ("Página Inicial", self._pagina_inicial),
            ("Página Aulas", self._pagina_aulas),
            ("Calendário", self._mostrar_calendario),
            ("Planos Mensais", self._mostrar_planos_mensais),
            ("Logout", self._logout, "#b22222", "white", "#8b0000"),
        ]

        for texto, comando, *cores in botoes:
            bg, fg, activebg = cores if cores else ("white", "#333", "#e0e0e0")
            self.criar_botao(self.frame_menu, texto, comando, bg, fg, activebg).pack(fill="x", pady=5, padx=10)

        self.menu_aberto = True

    def fechar_menu(self):
        """Esconde o menu hambúrguer."""
        if self.frame_menu:
            self.frame_menu.destroy()
        self.menu_aberto = False

    def _pagina_inicial(self):
        self.fechar_menu()
        self.voltar_pagina_inicial_callback()

    def _pagina_aulas(self):
        self.fechar_menu()
        self.mostrar_aulas_callback()

    def _mostrar_calendario(self):
        self.fechar_menu()
        self.mostrar_calendario_callback()

    def _mostrar_planos_mensais(self):
        self.fechar_menu()
        self.mostrar_planos_mensais_callback()

    def _logout(self):
        self.fechar_menu()
        self.logout_callback()
