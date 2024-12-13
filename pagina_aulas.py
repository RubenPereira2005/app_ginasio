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

        for root, dirs, files in os.walk(diretorio):
            for file in files:
                if file.lower().endswith(tipos_imagem):
                    caminho_imagem = os.path.join(root, file)
                    nome_aula = os.path.splitext(file)[0]
                    imagens_encontradas.append({"nome": nome_aula, "imagem": caminho_imagem, "professor": "Prof. Silva", "participantes": 10})

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
        detalhes_janela = tk.Toplevel(self.frame_principal)
        detalhes_janela.title("Detalhes da Aula")

        tk.Label(detalhes_janela, text=f"Aula: {aula['nome']}", font=("Arial", 18)).pack(pady=10)
        tk.Label(detalhes_janela, text=f"Professor: {aula['professor']}", font=("Arial", 14)).pack(pady=5)
        tk.Label(detalhes_janela, text=f"Número de Participantes: {aula['participantes']}", font=("Arial", 14)).pack(pady=5)

        reservar_btn = tk.Button(detalhes_janela, text="Reservar Aula", command=lambda: self.reservar_aula(aula))
        reservar_btn.pack(pady=20)

    def reservar_aula(self, aula):
        messagebox.showinfo("Reservar Aula", f"Você reservou a aula '{aula['nome']}' com sucesso!")

    def pagina_aulas(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text="Aulas Disponíveis", font=("Arial", 20)).pack(pady=10)

        canvas = tk.Canvas(self.frame_principal)
        scrollbar = tk.Scrollbar(self.frame_principal, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        frame_aulas = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_aulas, anchor="nw")
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

            label_aula = tk.Label(frame_aula, image=img_tk)
            label_aula.image = img_tk
            label_aula.pack()

            detalhes_btn = tk.Button(frame_aula, text="Detalhes", command=lambda aula=aula: self.mostrar_detalhes(aula))
            detalhes_btn.pack(pady=5)

        frame_aulas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
