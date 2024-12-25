import tkinter as tk

class PaginaNotificacoes:
    def __init__(self, root):
        self.root = root
        self.frame_notificacoes = tk.Frame(self.root)

    def mostrar_pagina_notificacoes(self):
        """Exibe a página de notificações."""
        # Limpa ou recria o frame
        if not self.frame_notificacoes.winfo_exists():
            self.frame_notificacoes = tk.Frame(self.root, bg="white")

        self.limpar_frame()
        self.frame_notificacoes.pack(fill="both", expand=True)

        # Título da página
        tk.Label(
            self.frame_notificacoes,
            text="Notificações",
            font=("Arial", 16, "bold"),
            bg="#4682b4",
            fg="white",
            height=2,
            anchor="center",
        ).pack(fill="x")

        # Área de notificações
        container = tk.Frame(self.frame_notificacoes, bg="white")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        notificacoes = self.obter_notificacoes()
        for notificacao in notificacoes:
            tk.Label(
                container,
                text=notificacao,
                font=("Arial", 12),
                bg="#f5f5f5",
                fg="#333",
                anchor="w",
                pady=10,
                padx=10,
                relief="groove",
                borderwidth=1,
            ).pack(fill="x", pady=5)


    def obter_notificacoes(self):
        """Retorna uma lista de notificações genéricas do ginásio."""
        return [
            "Aula de Zumba das 10:00 foi cancelada.",
            "Novo horário para Yoga: Sábado às 18:00.",
            "Pilates terá um novo professor a partir da próxima semana.",
            "O ginásio estará fechado no feriado de 25 de dezembro.",
            "Promoção: Traga um amigo e ganhe 1 mês grátis!",
        ]
    
    def limpar_frame(self):
        """Remove todos os widgets do frame principal."""
        if self.frame_notificacoes.winfo_exists():
            for widget in self.frame_notificacoes.winfo_children():
                widget.destroy()
