import tkinter as tk
from tkinter import Toplevel, messagebox
import calendar
from datetime import datetime

class Calendario:
    def __init__(self, frame_principal, aulas_por_dia):
        """
        Inicializa o calendário.
        :param frame_principal: Frame onde o calendário será exibido.
        :param aulas_por_dia: Dicionário com (ano, mes, dia) como chaves e lista de aulas como valores.
        """
        self.frame_principal = frame_principal
        self.aulas_por_dia = aulas_por_dia  # Exemplo: {(2024, 1, 1): ["Aula 1 - 10:00", "Aula 2 - 14:00"]}
        self.ano_atual = datetime.now().year
        self.mes_atual = datetime.now().month

    def mostrar_calendario(self):
        """Exibe o calendário do mês atual."""
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        # Cabeçalho com botões de navegação do mês
        frame_cabecalho = tk.Frame(self.frame_principal)
        frame_cabecalho.pack(pady=10)

        btn_mes_anterior = tk.Button(
            frame_cabecalho, text="◀", command=self.mes_anterior, font=("Arial", 14)
        )
        btn_mes_anterior.pack(side="left", padx=10)

        lbl_mes = tk.Label(
            frame_cabecalho,
            text=f"{calendar.month_name[self.mes_atual]} {self.ano_atual}",
            font=("Arial", 16, "bold"),
        )
        lbl_mes.pack(side="left")

        btn_mes_posterior = tk.Button(
            frame_cabecalho, text="▶", command=self.mes_posterior, font=("Arial", 14)
        )
        btn_mes_posterior.pack(side="left", padx=10)

        # Criar o calendário do mês
        frame_calendario = tk.Frame(self.frame_principal)
        frame_calendario.pack(pady=10)

        # Dias da semana
        dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        for dia in dias_semana:
            tk.Label(frame_calendario, text=dia, font=("Arial", 12, "bold"), width=5).grid(row=0, column=dias_semana.index(dia))

        # Dias do mês
        cal = calendar.Calendar(firstweekday=0)  # Começa na segunda-feira
        dias_mes = cal.itermonthdays2(self.ano_atual, self.mes_atual)  # Retorna (dia, dia_da_semana)

        linha = 1
        for dia, dia_semana in dias_mes:
            if dia == 0:  # Dias fora do mês
                tk.Label(frame_calendario, text="", width=5).grid(row=linha, column=dia_semana)
            else:
                btn_dia = tk.Button(
                    frame_calendario,
                    text=str(dia),
                    width=5,
                    command=lambda d=dia: self.mostrar_aulas(d)
                )
                btn_dia.grid(row=linha, column=dia_semana)
            if dia_semana == 6:  # Domingo, nova linha
                linha += 1

    def mes_anterior(self):
        """Navega para o mês anterior."""
        if self.mes_atual == 1:
            self.mes_atual = 12
            self.ano_atual -= 1
        else:
            self.mes_atual -= 1
        self.mostrar_calendario()

    def mes_posterior(self):
        """Navega para o mês seguinte."""
        if self.mes_atual == 12:
            self.mes_atual = 1
            self.ano_atual += 1
        else:
            self.mes_atual += 1
        self.mostrar_calendario()

    def mostrar_aulas(self, dia):
        """Exibe as aulas disponíveis para o dia selecionado."""
        aulas = self.aulas_por_dia.get((self.ano_atual, self.mes_atual, dia), [])

        if not aulas:
            messagebox.showinfo("Sem Aulas", f"Não há aulas disponíveis para o dia {dia}.")
            return

        # Janela popup para mostrar as aulas
        janela_aulas = Toplevel(self.frame_principal)
        janela_aulas.title(f"Aulas do Dia {dia} - {calendar.month_name[self.mes_atual]} {self.ano_atual}")

        tk.Label(janela_aulas, text=f"Aulas do Dia {dia}", font=("Arial", 16)).pack(pady=10)

        for aula in aulas:
            tk.Label(janela_aulas, text=aula, font=("Arial", 12)).pack(pady=5)
