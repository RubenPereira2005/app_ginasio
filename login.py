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

    def guardar_utilizador(self, utilizador, senha, email, telefone, morada):
        utilizadores = self.carregar_utilizadores()  # Carregar os usuários existentes
        if utilizador in utilizadores:
            return False  # Nome de utilizador já existe
        # Adicionar o novo utilizador
        utilizadores[utilizador] = {
            "senha": senha,
            "email": email,
            "telefone": telefone,
            "morada": morada
        }
        try:
            # Salvar no JSON
            with open(self.ARQUIVO_utilizadores, "w") as f:
                json.dump(utilizadores, f, indent=4)
            return True
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")
            return False

    def validar_login(self, identificador, senha):
        """
        Valida o login pelo nome de utilizador ou e-mail e pela senha.
        """
        utilizadores = self.carregar_utilizadores()
        for user, info in utilizadores.items():
            if (user == identificador or info.get("email") == identificador) and info.get("senha") == senha:
                return True
        return False


    def pagina_login(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text="Login", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.frame_principal, text="Utilizador ou E-mail:").pack()
        entrada_identificador = tk.Entry(self.frame_principal)
        entrada_identificador.pack()

        tk.Label(self.frame_principal, text="Senha:").pack()
        entrada_senha = tk.Entry(self.frame_principal, show="*")
        entrada_senha.pack()

        def fazer_login():
            identificador = entrada_identificador.get()
            senha = entrada_senha.get()
            if self.validar_login(identificador, senha):
                self.pagina_aulas_callback()
            else:
                print("Erro: Utilizador ou senha inválidos.")

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

        tk.Label(self.frame_principal, text="E-mail:").pack()
        entrada_email = tk.Entry(self.frame_principal)
        entrada_email.pack()

        tk.Label(self.frame_principal, text="Número de Telefone:").pack()
        entrada_telefone = tk.Entry(self.frame_principal)
        entrada_telefone.pack()

        tk.Label(self.frame_principal, text="Morada:").pack()
        entrada_morada = tk.Entry(self.frame_principal)
        entrada_morada.pack()

        def fazer_registo():
            utilizador = entrada_utilizador.get().strip()
            senha = entrada_senha.get().strip()
            email = entrada_email.get().strip()
            telefone = entrada_telefone.get().strip()
            morada = entrada_morada.get().strip()

            # Verificação simples dos campos
            if not (utilizador and senha and email and telefone and morada):
                print("Todos os campos são obrigatórios!")
                return

            if self.guardar_utilizador(utilizador, senha, email, telefone, morada):
                print("Registro realizado com sucesso!")
                self.pagina_login()
            else:
                print("Erro: Nome de utilizador já existe ou falha ao salvar os dados.")

        tk.Button(self.frame_principal, text="Registar", command=fazer_registo).pack(pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.pagina_login).pack()