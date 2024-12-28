import tkinter as tk

class PaginaGestaoPlanos:
    def __init__(self, root):
        self.root = root
        self.frame_planos = tk.Frame(self.root)

    def mostrar_pagina_planos(self):
        """Exibe a página de gestão de planos de assinatura."""
        # Limpa ou recria o frame
        if not self.frame_planos.winfo_exists():
            self.frame_planos = tk.Frame(self.root, bg="white")

        self.limpar_frame()
        self.frame_planos.pack(fill="both", expand=True)

        # Título da página
        tk.Label(
            self.frame_planos,
            text="Gestão de Planos de Assinatura",
            font=("Arial", 16, "bold"),
            bg="#4682b4",
            fg="white",
            height=2,
            anchor="center",
        ).pack(fill="x")

        # Container para scroll
        canvas = tk.Canvas(self.frame_planos)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.frame_planos, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        container = tk.Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=container, anchor="nw")

        # Atualiza a região visível do canvas quando o conteúdo mudar
        container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        planos = self.obter_planos()
        for plano in planos:
            frame_item = tk.Frame(container, bg="#f5f5f5", relief="groove", borderwidth=1)
            frame_item.pack(fill="x", pady=10, padx=5)

            # Nome do plano
            tk.Label(
                frame_item,
                text=plano['nome'],
                font=("Arial", 14, "bold"),
                bg="#f5f5f5",
                fg="#333",
                anchor="w",
                padx=10,
            ).pack(fill="x", pady=5)

            # Detalhes do plano
            detalhes = (
                f"Aulas: {plano['aulas_por_semana']} vezes/semana | "
                f"Máximo: {plano['max_aulas_por_mes']} aulas/mês"
            )
            tk.Label(
                frame_item,
                text=detalhes,
                font=("Arial", 12),
                bg="#f5f5f5",
                fg="#555",
                anchor="w",
                padx=10,
            ).pack(fill="x", pady=5)

            # Valor do plano
            tk.Label(
                frame_item,
                text=f"€ {plano['valor']:.2f}/mês",
                font=("Arial", 12, "bold"),
                bg="#f5f5f5",
                fg="#228B22",
                anchor="w",
                padx=10,
            ).pack(fill="x", pady=5)

            # Botão para mais detalhes
            btn_detalhes = tk.Button(
                frame_item,
                text="Ver Detalhes",
                bg="#1E90FF",
                fg="white",
                font=("Arial", 12),
                command=lambda p=plano: self.mostrar_detalhes_plano(p)
            )
            btn_detalhes.pack(fill="x", pady=5, padx=10)

    def obter_planos(self):
        """Retorna uma lista de planos fictícios."""
        return [
            {'id': 1, 'nome': 'Plano Fitness Básico', 'aulas_por_semana': 2, 'max_aulas_por_mes': 8, 'valor': 40.00},
            {'id': 2, 'nome': 'Plano Fitness Premium', 'aulas_por_semana': 4, 'max_aulas_por_mes': 16, 'valor': 70.00},
            {'id': 3, 'nome': 'Plano Fitness Ilimitado', 'aulas_por_semana': 7, 'max_aulas_por_mes': 28, 'valor': 100.00},
            {'id': 4, 'nome': 'Plano Fitness Diário', 'aulas_por_semana': 1, 'max_aulas_por_mes': 1, 'valor': 10.0},
        ]

    def mostrar_detalhes_plano(self, plano):
        """Exibe os detalhes de um plano selecionado."""
        detalhe_janela = tk.Toplevel(self.root)
        detalhe_janela.title(f"Detalhes do {plano['nome']}")

        tk.Label(
            detalhe_janela,
            text=f"Plano: {plano['nome']}",
            font=("Arial", 16, "bold"),
            pady=10,
        ).pack()

        detalhes = (
            f"Aulas por semana: {plano['aulas_por_semana']}\n"
            f"Máximo de aulas por mês: {plano['max_aulas_por_mes']}\n"
            f"Valor mensal: € {plano['valor']:.2f}"
        )
        tk.Label(
            detalhe_janela,
            text=detalhes,
            font=("Arial", 12),
            justify="left",
            padx=10,
            pady=10,
        ).pack()

        tk.Button(
            detalhe_janela,
            text="Fechar",
            command=detalhe_janela.destroy,
            bg="#4682b4",
            fg="white",
            padx=10,
            pady=5,
        ).pack(pady=10)

    def limpar_frame(self):
        """Remove todos os widgets do frame principal."""
        if self.frame_planos.winfo_exists():
            for widget in self.frame_planos.winfo_children():
                widget.destroy()

