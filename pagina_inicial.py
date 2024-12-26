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
            "Pilates": {"dias": ["Segunda-feira", "Quarta-feira"], "horarios": ["08:00", "16:00"], "professor": "Ana"},
            "Yoga": {"dias": ["Terça-feira", "Quinta-feira"], "horarios": ["09:00", "18:00"], "professor": "Carla"},
        }

        calendario = ListaAulas(self.frame_principal, aulas_semanais)
        calendario.mostrar_lista()

    def ir_para_aulas(self):
        from pagina_aulas import PaginaAulas

        aulas = PaginaAulas(self.frame_principal)
        aulas.pagina_aulas()



