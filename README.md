# 🏋️‍♂️ App de Gestão de Ginásio

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge"/>
</p>

## 📌 Sobre o Projeto
Esta aplicação foi desenvolvida no âmbito da unidade curricular de **Linguagens de Programação** da Licenciatura em Engenharia Informática na Universidade Lusófona do Porto. 

O objetivo do projeto foi criar um sistema desktop intuitivo para a gestão integral de um ginásio. A aplicação permite gerir a interação dos clientes com o ginásio, incluindo a escolha de planos, agendamento de aulas e visualização de horários, tudo através de uma interface gráfica amigável desenvolvida em Python.

## ✨ Funcionalidades Principais
* **🔐 Autenticação de Utilizadores:** Sistema de login seguro com persistência de dados utilizando ficheiros locais (JSON).
* **📝 Cadastro de Clientes:** Registo de informações pessoais como nome, idade, data de nascimento e contactos.
* **💳 Gestão de Planos de Assinatura:** Consulta e seleção de planos mensais adequados a cada cliente.
* **📅 Calendário Interativo:** Visualização de um calendário dinâmico para consulta de dias e horários das aulas.
* **🏋️ Marcação de Aulas:** Sistema de agendamento com limitação de participantes por aula.
* **📊 Relatórios e Inventário:** Consulta da frequência de clientes (dia/semana/mês) e gestão da lista de equipamentos disponíveis.
* **🍔 Navegação Intuitiva:** Implementação de um menu hambúrguer para facilitar a navegação entre as várias páginas (Aulas, Planos, Página Inicial, etc.).

## 🚀 Tecnologias Utilizadas
* **Linguagem Principal:** Python 3.12.0
* **Interface Gráfica (GUI):** Tkinter
* **Manipulação de Imagens:** Pillow (PIL)
* **Persistência de Dados:** JSON

## 📂 Estrutura do Projeto
* `app.py` - Ficheiro principal de execução da aplicação.
* `login.py` - Lógica de autenticação e registo.
* `pagina_inicial.py` - Dashboard/página inicial pós-login.
* `pagina_aulas.py` - Módulo de gestão e marcação de aulas.
* `calendario.py` - Implementação do calendário interativo.
* `planos_mensais.py` - Apresentação e gestão de subscrições.
* `menu_hamburguer.py` - Componente de navegação da interface.
* `/imagens/` - Diretório de recursos visuais e ícones da aplicação.



## ⚙️ Como Instalar e Executar

**Clonar o repositório:**
git clone https://github.com/RubenPereira2005/app_ginasio.git

cd app_ginasio

python app.py

## Projeto desenvolvido colaborativamente por:

Francisco Estrela (a22405810) 

Tomás Nogueira (a22304893)

Rúben Pereira (a22303926) 



   
