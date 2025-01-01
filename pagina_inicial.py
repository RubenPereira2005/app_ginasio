import tkinter as tk
from datetime import datetime
from calendario import ListaAulas
from pagina_aulas import PaginaAulas

class PaginaBase:
    def __init__(self, frame_principal):
        self.frame_principal = frame_principal

    def mostrar_pagina(self):
        """Exibe a página associada ao frame."""
        self.limpar_frame()

    def limpar_frame(self):
        """Remove todos os widgets do frame principal."""
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

class PaginaInicial(PaginaBase):
    def __init__(self, frame_principal):
        super().__init__(frame_principal)
        self.user_data = {
            "weekly_progress": 3,  
            "total_workouts": 12
        }

    def atualizar_utilizador(self, nome):
        """Atualiza o nome do Utilizador  exibido na interface."""
        self.user_data["name"] = nome
        self.mostrar_pagina()

    def mostrar_pagina(self):
        """Exibe a página inicial."""
        super().mostrar_pagina()

        upcoming_classes = [
            {"name": "Spinning", "time": "18:00", "date": "07/01/2025"},
            {"name": "Yoga", "time": "20:00", "date": "12/01/2025"}
        ]

        class_recommendations = [
            {"name": "Zumba", "time": "19:00"},
            {"name": "Pilates", "time": "08:00"}
        ]

        notifications = [
            "Aula de Spinning às 19h está quase lotada!",
            "Promoção: 10% de desconto no Personal Trainer."
        ]

        # Interface gráfica
        tk.Label(self.frame_principal, text="Bem-vindo ao Ginásio!", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.frame_principal, text=f"Olá", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame_principal, text=f"Progresso semanal: {self.user_data['weekly_progress']} treinos realizados", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.frame_principal, text=f"Total de treinos: {self.user_data['total_workouts']}", font=("Arial", 12)).pack(pady=5)

        self.mostrar_lista("Próximas aulas reservadas", upcoming_classes, "name", "time", "date")
        self.mostrar_lista("Recomendações de aulas", class_recommendations, "name", "time")
        self.mostrar_lista("Notificações", notifications)

        
        tk.Button(self.frame_principal, text="Acessar Calendário", font=("Arial", 12), command=self.ir_para_calendario).pack(pady=10)
        tk.Button(self.frame_principal, text="Acessar Página de Aulas", font=("Arial", 12), command=self.ir_para_aulas).pack(pady=10)

    def mostrar_lista(self, titulo, itens, *keys):
        """Exibe uma lista de itens na interface."""
        tk.Label(self.frame_principal, text=f"\n{titulo}:", font=("Arial", 14, "bold")).pack(pady=10)
        for item in itens:
            if isinstance(item, dict):
                texto = " - ".join([f"{item[key]}" for key in keys])
            else:
                texto = f"- {item}"
            tk.Label(self.frame_principal, text=texto, font=("Arial", 12)).pack()

    def ir_para_calendario(self):
        """Navega para a página de calendário."""
        aulas_semanais = {
            "Bodypump": {
                "dias": ["Segunda-feira", "Quinta-feira", "Sábado"],
                "horarios": ["07:00", "12:00", "19:00"],
                "professor": "Prof. Beatriz"
            },
            "Crossfit": {
                "dias": ["Segunda-feira", "Terça-feira", "Sexta-feira"],
                "horarios": ["06:30", "14:00", "18:30"],
                "professor": "Prof. Ricardo"
            },
            "Hidroginástica": {
                "dias": ["Terça-feira", "Quarta-feira", "Sábado"],
                "horarios": ["09:30", "13:30", "17:00"],
                "professor": "Prof. Sofia"
            },
            "HIIT": {
                "dias": ["Quarta-feira", "Sexta-feira", "Domingo"],
                "horarios": ["07:00", "11:00", "20:00"],
                "professor": "Prof. Paulo"
            },
            "Personal Trainer": {
                "dias": ["Segunda-feira", "Quarta-feira", "Sexta-feira"],
                "horarios": ["08:00", "15:00", "19:00"],
                "professor": "Prof. Mariana"
            },
            "Pilates": {
                "dias": ["Segunda-feira", "Terça-feira", "Quarta-feira"],
                "horarios": ["08:00", "16:00", "18:00"],
                "professor": "Prof. Ana"
            },
            "Spinning": {
                "dias": ["Terça-feira", "Quinta-feira", "Sábado"],
                "horarios": ["06:00", "10:00", "18:00"],
                "professor": "Prof. André"
            },
            "Step Aeróbico": {
                "dias": ["Quinta-feira", "Sexta-feira", "Domingo"],
                "horarios": ["08:30", "13:00", "16:30"],
                "professor": "Prof. Clara"
            },
            "Yoga": {
                "dias": ["Sexta-feira", "Sábado", "Domingo"],
                "horarios": ["09:00", "15:00", "17:00"],
                "professor": "Prof. Carla"
            },
            "Zumba": {
                "dias": ["Terça-feira", "Quarta-feira", "Quinta-feira"],
                "horarios": ["10:00", "18:00", "20:00"],
                "professor": "Prof. João"
            },
        }

        calendario = ListaAulas(self.frame_principal, aulas_semanais)
        calendario.mostrar_lista()

    def ir_para_aulas(self):
        """Navega para a página de aulas."""
        aulas = PaginaAulas(self.frame_principal)
        aulas.pagina_aulas()
