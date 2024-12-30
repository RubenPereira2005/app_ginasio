import tkinter as tk
from tkinter import messagebox

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

    def mostrar_menu_hamburguer(self):
        """Adiciona o botão de menu hambúrguer apenas em páginas principais."""
        if self.botao_menu and self.botao_menu.winfo_exists():
            return  # Se o botão já existe, não faz nada

        self.botao_menu = tk.Button(
            self.root,
            text="☰",
            font=("Arial", 18),
            command=self.toggle_menu,
            bg="#4682b4",
            fg="white",
            bd=0,
            activebackground="#315f82",
            activeforeground="white",
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
        self.frame_menu = tk.Frame(self.root, bg="#f8f9fa", width=200, height=667)
        self.frame_menu.place(x=0, y=0)

        # Título no menu
        tk.Label(
            self.frame_menu,
            text="Menu",
            bg="#4682b4",
            fg="white",
            font=("Arial", 14, "bold"),
            height=2,
        ).pack(fill="x")

        # Botão Página Inicial
        tk.Button(
            self.frame_menu,
            text="Página Inicial",
            command=self._pagina_inicial,
            bg="white",
            fg="#333",
            font=("Arial", 12),
            bd=0,
            activebackground="#e0e0e0",
        ).pack(fill="x", pady=5, padx=10)

        # Botão Página Aulas
        tk.Button(
            self.frame_menu,
            text="Página Aulas",
            command=self._pagina_aulas,
            bg="white",
            fg="#333",
            font=("Arial", 12),
            bd=0,
            activebackground="#e0e0e0",
        ).pack(fill="x", pady=5, padx=10)

        # Botão Calendário
        tk.Button(
            self.frame_menu,
            text="Calendário",
            command=self._mostrar_calendario,
            bg="white",
            fg="#333",
            font=("Arial", 12),
            bd=0,
            activebackground="#e0e0e0",
        ).pack(fill="x", pady=5, padx=10)

        # Botão Planos Mensais
        tk.Button(
            self.frame_menu,
            text="Planos Mensais",
            command=self._mostrar_planos_mensais,
            bg="white",
            fg="#333",
            font=("Arial", 12),
            bd=0,
            activebackground="#e0e0e0",
        ).pack(fill="x", pady=5, padx=10)

        # Botão Logout
        tk.Button(
            self.frame_menu,
            text="Logout",
            command=self._logout,
            bg="#b22222",
            fg="white",
            font=("Arial", 12),
            bd=0,
            activebackground="#8b0000",
        ).pack(fill="x", pady=10, padx=10)

        self.menu_aberto = True

    def fechar_menu(self):
        """Esconde o menu hambúrguer."""
        if self.frame_menu:
            self.frame_menu.destroy()
        self.menu_aberto = False

    def _pagina_inicial(self):
        """Callback para a página inicial que também fecha o menu."""
        self.fechar_menu()
        self.voltar_pagina_inicial_callback()

    def _pagina_aulas(self):
        """Callback para a página de aulas que também fecha o menu."""
        self.fechar_menu()
        self.mostrar_aulas_callback()

    def _mostrar_calendario(self):
        """Callback para exibir o calendário que também fecha o menu."""
        self.fechar_menu()
        self.mostrar_calendario_callback()

    def _mostrar_planos_mensais(self):
        """Callback para exibir as Planos Mensais que também fecha o menu."""
        self.fechar_menu()
        self.mostrar_planos_mensais_callback()

    def _logout(self):
        """Callback para logout que também fecha o menu."""
        self.fechar_menu()
        self.logout_callback()
