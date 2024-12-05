import tkinter as tk
import json
import os


class Login:
    ARQUIVO_utilizadores = "utilizadores.json"

    def __init__(self, frame_principal, pagina_aulas_callback):
        self.frame_principal = frame_principal
        self.pagina_aulas_callback = pagina_aulas_callback

    def carregar_utilizadores(self):
        if not os.path.exists(self.ARQUIVO_utilizadores):
            with open(self.ARQUIVO_utilizadores, "w") as f:
                json.dump({}, f)
        with open(self.ARQUIVO_utilizadores, "r") as f:
            return json.load(f)

    def guardar_utilizador(self, utilizador, senha):
        utilizadores = self.carregar_utilizadores()
        if utilizador in utilizadores:
            return False
        utilizadores[utilizador] = senha
        with open(self.ARQUIVO_utilizadores, "w") as f:
            json.dump(utilizadores, f)
        return True

    def validar_login(self, utilizador, senha):
        utilizadores = self.carregar_utilizadores()
        return utilizadores.get(utilizador) == senha

    def pagina_login(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text="Login", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.frame_principal, text="Utilizador:").pack()
        entrada_utilizador = tk.Entry(self.frame_principal)
        entrada_utilizador.pack()

        tk.Label(self.frame_principal, text="Senha:").pack()
        entrada_senha = tk.Entry(self.frame_principal, show="*")
        entrada_senha.pack()

        def fazer_login():
            utilizador = entrada_utilizador.get()
            senha = entrada_senha.get()
            if self.validar_login(utilizador, senha):
                self.pagina_aulas_callback()

        tk.Button(self.frame_principal, text="Entrar", command=fazer_login).pack(pady=10)
        tk.Button(self.frame_principal, text="Registe-se", command=self.pagina_registo).pack()

    def pagina_registo(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text="Registo", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.frame_principal, text="Utilizador:").pack()
        entrada_utilizador = tk.Entry(self.frame_principal)
        entrada_utilizador.pack()

        tk.Label(self.frame_principal, text="Senha:").pack()
        entrada_senha = tk.Entry(self.frame_principal, show="*")
        entrada_senha.pack()

        def fazer_registo():
            utilizador = entrada_utilizador.get()
            senha = entrada_senha.get()
            if self.guardar_utilizador(utilizador, senha):
                self.pagina_login()

        tk.Button(self.frame_principal, text="Registar", command=fazer_registo).pack(pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.pagina_login).pack()