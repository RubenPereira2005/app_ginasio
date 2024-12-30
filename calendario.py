import tkinter as tk
from datetime import datetime, timedelta

class GestaoAulas:
    def __init__(self, aulas_semanais):
        self.aulas_semanais = aulas_semanais
        self.dia_atual = datetime.now()  # Dia inicial para exibição
        self.dia_limite = timedelta(days=6)  # Limite de 6 dias

        # Dicionário para traduzir os dias da semana para português de Portugal
        self.dias_da_semana_pt = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }

    def obter_aulas_do_dia(self):
        """Retorna as aulas do dia atual."""
        nome_dia = self.dias_da_semana_pt[self.dia_atual.strftime("%A")]
        aulas_do_dia = []

        for aula, detalhes in self.aulas_semanais.items():
            if nome_dia in detalhes["dias"]:
                for horario in detalhes["horarios"]:
                    aulas_do_dia.append(f"{aula} - {horario} - {detalhes['professor']}")
        return aulas_do_dia

    def dia_anterior(self):
        """Retrocede um dia no período exibido."""
        if self.dia_atual > datetime.now() - self.dia_limite:
            self.dia_atual -= timedelta(days=1)
            return True
        return False

    def dia_proximo(self):
        """Avança um dia no período exibido (máximo de 7 dias a partir de hoje)."""
        if self.dia_atual < datetime.now() + self.dia_limite:
            self.dia_atual += timedelta(days=1)
            return True
        return False

    def atualizar_botoes(self, btn_anterior, btn_proximo):
        """Atualiza a visibilidade dos botões de navegação dependendo dos limites."""
        # Verificar se atingiu o limite para o botão anterior
        if self.dia_atual <= datetime.now() - self.dia_limite:
            btn_anterior.grid_forget()
        else:
            btn_anterior.grid(row=0, column=0, padx=1)

        # Verificar se atingiu o limite para o botão próximo
        if self.dia_atual >= datetime.now() + self.dia_limite:
            btn_proximo.grid_forget()
        else:
            btn_proximo.grid(row=0, column=2, padx=1)


class ListaAulas(GestaoAulas):
    def __init__(self, frame_principal, aulas_semanais):
        super().__init__(aulas_semanais)
        self.frame_principal = frame_principal

    def mostrar_lista(self):
        """Exibe a lista de aulas para o dia atual."""
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        # Cabeçalho com botões de navegação
        frame_cabecalho = tk.Frame(self.frame_principal)
        frame_cabecalho.pack(pady=10, fill="x")

        # Frame para os botões de navegação e texto centralizado com largura fixa
        frame_navegacao = tk.Frame(frame_cabecalho)
        frame_navegacao.pack(side="top", pady=5)

        # Largura fixa baseada no maior texto ("Segunda-feira")
        largura_fixa = 20

        # Botão anterior sem borda e com maior seta
        self.btn_anterior = tk.Button(
            frame_navegacao, text="◀", command=self.dia_anterior, font=("Arial", 18), width=3, bd=0
        )
        self.btn_anterior.grid(row=0, column=0, padx=1)

        # Usar o dicionário para traduzir o nome do dia
        nome_dia = self.dias_da_semana_pt[self.dia_atual.strftime("%A")]

        lbl_dia = tk.Label(
            frame_navegacao,
            text=f"{nome_dia}, {self.dia_atual.strftime('%d/%m/%Y')}",
            font=("Arial", 14, "bold"),
            width=largura_fixa,
            anchor="center"
        )
        lbl_dia.grid(row=0, column=1, padx=10)

        # Botão próximo sem borda e com maior seta
        self.btn_proximo = tk.Button(
            frame_navegacao, text="▶", command=self.dia_proximo, font=("Arial", 18), width=3, bd=0
        )
        self.btn_proximo.grid(row=0, column=2, padx=1)

        # Título centralizado
        tk.Label(self.frame_principal, text="Aulas do Dia", font=("Arial", 16, "bold")).pack(pady=20, anchor="center")

        # Exibir aulas para o dia atual
        aulas_do_dia = self.obter_aulas_do_dia()

        # Frame para o dia
        frame_dia = tk.Frame(self.frame_principal)
        frame_dia.pack(fill="both", pady=10)

        # Listar aulas do dia
        if aulas_do_dia:
            for aula in aulas_do_dia:
                tk.Label(frame_dia, text=aula, font=("Arial", 12)).pack(anchor="center", pady=5)
        else:
            tk.Label(frame_dia, text="Sem aulas", font=("Arial", 12, "italic")).pack(anchor="center", pady=5)

        # Atualizar a visibilidade dos botões
        self.atualizar_botoes(self.btn_anterior, self.btn_proximo)

    def dia_anterior(self):
        """Retrocede um dia no período exibido e atualiza a interface."""
        if super().dia_anterior():  # Chama o método da classe base
            self.mostrar_lista()

    def dia_proximo(self):
        """Avança um dia no período exibido e atualiza a interface."""
        if super().dia_proximo():  # Chama o método da classe base
            self.mostrar_lista()