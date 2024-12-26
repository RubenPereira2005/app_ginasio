import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class PaginaAulas:
    def __init__(self, frame_principal):
        self.frame_principal = frame_principal
        self.diretorio_base = os.path.dirname(os.path.abspath(__file__))
        self.aulas = self.localizar_imagens(self.diretorio_base)

    def localizar_imagens(self, diretorio):
        tipos_imagem = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
        imagens_encontradas = []

        horarios_por_aula = {
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

        for root, dirs, files in os.walk(diretorio):
            for file in files:
                if file.lower().endswith(tipos_imagem):
                    caminho_imagem = os.path.join(root, file)
                    nome_aula = os.path.splitext(file)[0].capitalize()
                    
                    horarios = horarios_por_aula.get(nome_aula, {
                        "dias": ["Segunda-feira"],
                        "horarios": ["08:00"],
                        "professor": "Prof. Silva"
                    })

                    imagens_encontradas.append({
                        "nome": nome_aula,
                        "imagem": caminho_imagem,
                        "professor": horarios["professor"],
                        "participantes": 0,
                        "dias": horarios["dias"],
                        "horarios": horarios["horarios"]
                    })

        return imagens_encontradas

    def criar_imagem_com_texto(self, imagem, texto, radius=15, border_width=5, border_color="black"):
        largura, altura = imagem.size
        imagem = imagem.convert("RGBA")

        mascara = Image.new("L", (largura, altura), 0)
        draw = ImageDraw.Draw(mascara)
        draw.rounded_rectangle((0, 0, largura, altura), radius, fill=255)
        imagem.putalpha(mascara)

        borda = Image.new("RGBA", (largura + 2 * border_width, altura + 2 * border_width), border_color)
        mascara_borda = Image.new("L", (largura + 2 * border_width, altura + 2 * border_width), 0)
        draw = ImageDraw.Draw(mascara_borda)
        draw.rounded_rectangle((0, 0, largura + 2 * border_width, altura + 2 * border_width), radius + border_width, fill=255)
        borda.paste(imagem, (border_width, border_width), mascara)

        overlay = Image.new("RGBA", (largura + 2 * border_width, altura + 2 * border_width), (0, 0, 0, 128))
        borda.paste(overlay, (0, 0), overlay)

        draw = ImageDraw.Draw(borda)
        try:
            fonte = ImageFont.truetype("arial.ttf", 20)
        except IOError:
            fonte = ImageFont.load_default()

        text_bbox = draw.textbbox((0, 0), texto, font=fonte)
        if text_bbox:
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            text_x = (borda.width - text_width) // 2
            text_y = (borda.height - text_height) // 2
            draw.text((text_x, text_y), texto, font=fonte, fill="white")

        return borda

    def mostrar_detalhes(self, aula):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text=f"Aula: {aula['nome']}", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.frame_principal, text=f"Professor: {aula['professor']}", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.frame_principal, text=f"Número de Participantes: {aula['participantes']}", font=("Arial", 14)).pack(pady=5)

        reservar_btn = tk.Button(self.frame_principal, text="Reservar Aula", command=lambda: self.abrir_menu_reserva(aula))
        reservar_btn.pack(pady=20)

        voltar_btn = tk.Button(self.frame_principal, text="Voltar", command=self.pagina_aulas)
        voltar_btn.pack(pady=20)

    def abrir_menu_reserva(self, aula):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text=f"Reservar: {aula['nome']}", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.frame_principal, text="Escolha o dia:", font=("Arial", 14)).pack(pady=5)
        dia_var = tk.StringVar(value=aula['dias'][0])
        dia_menu = tk.OptionMenu(self.frame_principal, dia_var, *aula['dias'])
        dia_menu.pack(pady=5)

        tk.Label(self.frame_principal, text="Escolha o horário:", font=("Arial", 14)).pack(pady=5)
        horario_var = tk.StringVar(value=aula['horarios'][0])
        horario_menu = tk.OptionMenu(self.frame_principal, horario_var, *aula['horarios'])
        horario_menu.pack(pady=5)

        confirmar_btn = tk.Button(
            self.frame_principal,
            text="Confirmar Reserva",
            command=lambda: self.confirmar_reserva(aula, dia_var.get(), horario_var.get())
        )
        confirmar_btn.pack(pady=20)

        voltar_btn = tk.Button(self.frame_principal, text="Voltar", command=lambda: self.mostrar_detalhes(aula))
        voltar_btn.pack(pady=10)

    def confirmar_reserva(self, aula, dia, horario):
        aula['participantes'] += 1
        messagebox.showinfo(
            "Reserva Confirmada",
            f"Aula '{aula['nome']}' reservada para {dia} às {horario}. Participantes atualizados!"
        )
        self.mostrar_detalhes(aula)

    def pagina_aulas(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text="Aulas Disponíveis", font=("Arial", 20)).pack(pady=10)

        # Canvas para suportar rolagem
        canvas = tk.Canvas(self.frame_principal)
        scrollbar = tk.Scrollbar(self.frame_principal, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame interno para conter as aulas
        frame_aulas = tk.Frame(canvas)
        frame_aulas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame_aulas, anchor="nw")

        # Função para rolar com o mouse
        def _on_mouse_wheel(event):
            canvas.yview_scroll(-1 * int(event.delta / 120), "units")

        canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        for i, aula in enumerate(self.aulas):
            frame_aula = tk.Frame(frame_aulas, bg="#f0f0f0", width=200, height=200, padx=10, pady=10)
            frame_aula.grid(row=i // 2, column=i % 2, padx=10, pady=10)

            try:
                img = Image.open(aula["imagem"])
                img = img.resize((150, 150), Image.Resampling.LANCZOS)
                img = self.criar_imagem_com_texto(img, aula["nome"])
                img_tk = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Erro ao carregar a imagem: {e}")
                continue

            label_aula = tk.Label(frame_aula, image=img_tk, cursor="hand2")
            label_aula.image = img_tk
            label_aula.pack()

            label_aula.bind("<Button-1>", lambda event, aula=aula: self.mostrar_detalhes(aula))