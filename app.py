import tkinter as tk
from login import Login
from pagina_aulas import PaginaAulas
from menu_hamburguer import MenuHamburguer
from pagina_inicial import PaginaInicial
from calendario import ListaAulas
from notificacoes import PaginaNotificacoes

class AppGinásio:
    def __init__(self, root):
        self.janela = root
        self.janela.title("Ginásio")
        self.janela.geometry("450x667")

        self.frame_principal = tk.Frame(self.janela)
        self.frame_principal.pack(fill="both", expand=True)

        # Dados de exemplo para as aulas semanais
        self.aulas_semanais = {
            "Pilates": {
                "dias": ["Segunda-feira", "Terça-feira", "Quarta-feira"],
                "horarios": ["08:00", "16:00"],
                "professor": "Prof. Ana"
            },
            "Zumba": {
                "dias": ["Terça-feira", "Quarta-feira", "Quinta-feira"],
                "horarios": ["10:00", "18:00"],
                "professor": "Prof. João"
            },
            "Yoga": {
                "dias": ["Sexta-feira", "Sábado", "Domingo"],
                "horarios": ["09:00", "15:00"],
                "professor": "Prof. Carla"
            },
        }

        # Instâncias das páginas
        self.login = Login(self.frame_principal, self.mostrar_pagina_inicial)
        self.pagina_inicial = PaginaInicial(self.frame_principal)
        self.pagina_aulas = PaginaAulas(self.frame_principal)
        self.lista_aulas = ListaAulas(self.frame_principal, self.aulas_semanais)
        self.pagina_notificacoes = PaginaNotificacoes(self.frame_principal)

        # Instância do menu hambúrguer
        self.menu_hamburguer = MenuHamburguer(
            root=self.janela,
            frame_principal=self.frame_principal,
            mostrar_aulas_callback=self.mostrar_aulas,
            voltar_pagina_inicial_callback=self.mostrar_pagina_inicial,
            mostrar_calendario_callback=self.mostrar_lista_aulas,
            mostrar_notificacoes_callback=self.mostrar_notificacoes,
            logout_callback=self.logout,
        )

        # Inicia na página de login
        self.login.pagina_login()

    def ocultar_frames(self):
        """Esconde todos os frames antes de exibir uma nova página."""
        for widget in self.frame_principal.winfo_children():
            widget.pack_forget()

    def mostrar_pagina_inicial(self):
        """Mostra a página inicial após o login."""
        self.ocultar_frames()
        self.menu_hamburguer.mostrar_menu_hamburguer()
        self.pagina_inicial.mostrar_pagina_inicial()

    def mostrar_aulas(self):
        """Mostra a página de aulas e adiciona o menu hambúrguer."""
        self.ocultar_frames()
        self.menu_hamburguer.mostrar_menu_hamburguer()
        self.pagina_aulas.pagina_aulas()

    def mostrar_lista_aulas(self):
        """Mostra a lista de aulas para os próximos 7 dias."""
        self.ocultar_frames()
        self.menu_hamburguer.mostrar_menu_hamburguer()
        self.lista_aulas.mostrar_lista()

    def mostrar_notificacoes(self):
        """Mostra a página de notificações."""
        self.ocultar_frames()
        self.menu_hamburguer.mostrar_menu_hamburguer()
        self.pagina_notificacoes.mostrar_pagina_notificacoes()

    def logout(self):
        """Realiza o logout e volta para a página de login."""
        self.ocultar_frames()
        self.menu_hamburguer.remover_menu_hamburguer()
        self.login.pagina_login()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppGinásio(root)
    root.mainloop()
