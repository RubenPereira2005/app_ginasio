import tkinter as tk
from login import Login
from pagina_aulas import PaginaAulas
from menu_hamburguer import MenuHamburguer
from pagina_inicial import PaginaInicial
from calendario import Calendario

class AppGinásio:
    def __init__(self, root):
        self.janela = root
        self.janela.title("Ginásio")
        self.janela.geometry("450x667")
        
        self.frame_principal = tk.Frame(self.janela)
        self.frame_principal.pack(fill="both", expand=True)

        # Dados de exemplo para o calendário
        self.aulas_por_dia = {
            (2024, 1, 1): ["Aula 1 - 10:00", "Aula 2 - 14:00"],
            (2024, 1, 3): ["Aula 3 - 08:00", "Aula 4 - 16:00"],
            (2024, 2, 15): ["Aula 5 - 18:00"],
            (2025, 2, 15): ["Aula 5 - 18:00"]
        }


        # Instâncias das páginas
        self.login = Login(self.frame_principal, self.mostrar_pagina_inicial)
        self.pagina_inicial = PaginaInicial(self.frame_principal)
        self.pagina_aulas = PaginaAulas(self.frame_principal)
        self.calendario = Calendario(self.frame_principal, self.aulas_por_dia)

        # Instância do menu hambúrguer
        self.menu_hamburguer = MenuHamburguer(
            root=self.janela,
            frame_principal=self.frame_principal,
            mostrar_aulas_callback=self.mostrar_aulas,
            voltar_pagina_inicial_callback=self.mostrar_pagina_inicial,
            mostrar_calendario_callback=self.mostrar_calendario,
            logout_callback=self.logout,
        )

        # Inicia na página de login
        self.login.pagina_login()

    def mostrar_pagina_inicial(self):
        """Mostra a página inicial após o login."""
        self.menu_hamburguer.mostrar_menu_hamburguer()
        self.pagina_inicial.mostrar_pagina_inicial()

    def mostrar_aulas(self):
        """Mostra a página de aulas e adiciona o menu hambúrguer."""
        self.menu_hamburguer.mostrar_menu_hamburguer()
        self.pagina_aulas.pagina_aulas()

    def mostrar_calendario(self):
        """Mostra o calendário de aulas."""
        self.menu_hamburguer.mostrar_menu_hamburguer()
        self.calendario.mostrar_calendario()

    def logout(self):
        """Realiza o logout e volta para a página de login."""
        self.menu_hamburguer.remover_menu_hamburguer()
        self.login.pagina_login()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGinásio(root)
    root.mainloop()