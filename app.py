import tkinter as tk
from login import Login
from pagina_aulas import PaginaAulas
from menu_hamburguer import MenuHamburguer
from pagina_inicial import PaginaInicial 

class AppGinásio:
    def __init__(self, root):
        self.janela = root
        self.janela.title("Ginásio")
        self.janela.geometry("450x667")
        
        self.frame_principal = tk.Frame(self.janela)
        self.frame_principal.pack(fill="both", expand=True)

        # Instâncias das páginas
        self.login = Login(self.frame_principal, self.mostrar_pagina_inicial)
        self.pagina_inicial = PaginaInicial(self.frame_principal)
        self.pagina_aulas = PaginaAulas(self.frame_principal)

        # Instância do menu hambúrguer
        self.menu_hamburguer = MenuHamburguer(
            root=self.janela,
            frame_principal=self.frame_principal,
            mostrar_aulas_callback=self.mostrar_aulas,
            voltar_pagina_inicial_callback=self.mostrar_pagina_inicial,
            logout_callback=self.logout,  # Callback de logout
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

    def logout(self):
        """Realiza o logout e volta para a página de login."""
        self.menu_hamburguer.remover_menu_hamburguer()
        self.login.pagina_login()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGinásio(root)
    root.mainloop()
