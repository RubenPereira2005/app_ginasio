import tkinter as tk
from login import Login
from pagina_aulas import PaginaAulas


class AppGinásio:
    def __init__(self, root):
        self.janela = root
        self.janela.title("Ginásio")
        self.janela.geometry("450x667")
        
        self.frame_principal = tk.Frame(self.janela)
        self.frame_principal.pack(fill="both", expand=True)

        self.login = Login(self.frame_principal, self.mostrar_aulas)
        self.pagina_aulas = PaginaAulas(self.frame_principal)

        self.login.pagina_login()

    def mostrar_aulas(self):
        self.pagina_aulas.pagina_aulas()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGinásio(root)
    root.mainloop()