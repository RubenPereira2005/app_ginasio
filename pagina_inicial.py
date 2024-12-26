import tkinter as tk
import datetime

class PaginaInicial:
    def __init__(self, frame_principal):
        self.frame_principal = frame_principal
        self.user_data = {
            "weekly_progress": 3,  # Treinos realizados na semana
            "total_workouts": 12
        }

    def atualizar_usuario(self, nome):
        """Atualiza o nome do usuário exibido na interface."""
        self.user_data["name"] = nome
        self.mostrar_pagina_inicial()

    def mostrar_pagina_inicial(self):
        """Exibe a página inicial."""
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        upcoming_classes = [
            {"name": "Spinning", "time": "18:00", "date": "07/01/2025"},
            {"name": "Yoga", "time": "20:00", "date": "12/01/2025"}
        ]

        class_recommendations = [
            {"name": "Zumba", "time": "19:00"},
            {"name": "Pilates", "time": "08:00"}
        ]

        notifications = [
            "Aula de Spinning às 19h está quase !",
            "Promoção: 10% de desconto no Personal Trainer."
        ]

        # Interface gráfica
        tk.Label(self.frame_principal, text="Bem-vindo ao Ginásio!", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.frame_principal, text=f"Olá", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame_principal, text=f"Progresso semanal: {self.user_data['weekly_progress']} treinos realizados", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.frame_principal, text=f"Total de treinos: {self.user_data['total_workouts']}", font=("Arial", 12)).pack(pady=5)

        # Próximas aulas reservadas
        tk.Label(self.frame_principal, text="Próximas aulas reservadas:", font=("Arial", 14, "bold")).pack(pady=10)
        for cls in upcoming_classes:
            tk.Label(self.frame_principal, text=f"- {cls['name']} às {cls['time']} em {cls['date']}", font=("Arial", 12)).pack()

        # Recomendações de aulas
        tk.Label(self.frame_principal, text="\nRecomendações de aulas:", font=("Arial", 14, "bold")).pack(pady=10)
        for rec in class_recommendations:
            tk.Label(self.frame_principal, text=f"- {rec['name']} às {rec['time']}", font=("Arial", 12)).pack()

        # Notificações
        tk.Label(self.frame_principal, text="\nNotificações:", font=("Arial", 14, "bold")).pack(pady=10)
        for note in notifications:
            tk.Label(self.frame_principal, text=f"- {note}", font=("Arial", 12)).pack()

        # Botões para páginas adicionais
        tk.Button(self.frame_principal, text="Acessar Calendário", font=("Arial", 12), command=self.ir_para_calendario).pack(pady=10)
        tk.Button(self.frame_principal, text="Acessar Página de Aulas", font=("Arial", 12), command=self.ir_para_aulas).pack(pady=10)

    def ir_para_calendario(self):
        from calendario import ListaAulas

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
        from pagina_aulas import PaginaAulas

        aulas = PaginaAulas(self.frame_principal)
        aulas.pagina_aulas()



