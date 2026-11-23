
import tkinter as tk
from tkinter import messagebox

# Cores
AZUL = "#0D47A1"
AZUL_CLARO = "#1565C0"
BRANCO = "#FFFFFF"

# Perguntas do quiz
perguntas = [
    {
        "pergunta": "1. O que significa a sigla CPU?",
        "alternativas": [
            "A) Central Personal Unit",
            "B) Central Processing Unit",
            "C) Computer Program Utility",
            "D) Control Power Unit"
        ],
        "resposta": "B"
    },
    {
        "pergunta": "2. Qual linguagem é conhecida por sua simplicidade?",
        "alternativas": [
            "A) Assembly",
            "B) COBOL",
            "C) Python",
            "D) Fortran"
        ],
        "resposta": "C"
    },
    {
        "pergunta": "3. Qual comando exibe algo na tela em Python?",
        "alternativas": [
            "A) input()",
            "B) write()",
            "C) display()",
            "D) print()"
        ],
        "resposta": "D"
    },
    {
        "pergunta": "4. Qual comando recebe dados do usuário?",
        "alternativas": [
            "A) input()",
            "B) print()",
            "C) return",
            "D) int()"
        ],
        "resposta": "A"
    },
    {
        "pergunta": "5. Qual símbolo é utilizado para realizar uma soma?",
        "alternativas": [
            "A) -",
            "B) /",
            "C) +",
            "D) *"
        ],
        "resposta": "C"
    },
    {
        "pergunta": "6. Qual estrutura verifica uma condição?",
        "alternativas": [
            "A) print",
            "B) if",
            "C) input",
            "D) def"
        ],
        "resposta": "B"
    },
    {
        "pergunta": "7. Qual palavra cria uma função em Python?",
        "alternativas": [
            "A) function",
            "B) func",
            "C) create",
            "D) def"
        ],
        "resposta": "D"
    },
    {
        "pergunta": "8. Qual estrutura de repetição existe em Python?",
        "alternativas": [
            "A) while",
            "B) repeat",
            "C) repetition",
            "D) loop"
        ],
        "resposta": "A"
    },
    {
        "pergunta": "9. Qual tipo de dado representa um número inteiro?",
        "alternativas": [
            "A) str",
            "B) float",
            "C) int",
            "D) bool"
        ],
        "resposta": "C"
    },
    {
        "pergunta": "10. Qual comando retorna um valor de uma função?",
        "alternativas": [
            "A) print",
            "B) return",
            "C) break",
            "D) input"
        ],
        "resposta": "B"
    }
]

# Variáveis
indice = 0
pontuacao = 0
janela_quiz = None
resposta_selecionada = None

lbl_progresso = None
lbl_pergunta = None
frame_alternativas = None
lbl_feedback = None
lbl_pontuacao = None
btn_responder = None


# Iniciar quiz
def iniciar_quiz():
    global indice, pontuacao, janela_quiz
    global resposta_selecionada
    global lbl_progresso, lbl_pergunta
    global frame_alternativas, lbl_feedback
    global lbl_pontuacao, btn_responder

    indice = 0
    pontuacao = 0

    janela_quiz = tk.Toplevel(janela_principal)
    janela_quiz.title("Quiz de Programação")
    janela_quiz.geometry("600x500")
    janela_quiz.configure(bg=AZUL)
    janela_quiz.resizable(False, False)

    resposta_selecionada = tk.StringVar()

    # Número da pergunta
    lbl_progresso = tk.Label(
        janela_quiz,
        text="",
        font=("Arial", 14, "bold"),
        bg=AZUL,
        fg=BRANCO
    )
    lbl_progresso.pack(pady=20)

    # Texto da pergunta
    lbl_pergunta = tk.Label(
        janela_quiz,
        text="",
        font=("Arial", 14),
        bg=AZUL,
        fg=BRANCO,
        wraplength=520
    )
    lbl_pergunta.pack(pady=20)

    # Alternativas
    frame_alternativas = tk.Frame(
        janela_quiz,
        bg=AZUL
    )
    frame_alternativas.pack(pady=10, padx=30, fill="x")

    # Mensagem de acerto ou erro
    lbl_feedback = tk.Label(
        janela_quiz,
        text="",
        font=("Arial", 12, "bold"),
        bg=AZUL,
        fg=BRANCO
    )
    lbl_feedback.pack(pady=10)

    # Pontuação
    lbl_pontuacao = tk.Label(
        janela_quiz,
        text="Pontuação: 0",
        font=("Arial", 12, "bold"),
        bg=AZUL,
        fg=BRANCO
    )
    lbl_pontuacao.pack(pady=10)

    # Botão responder
    btn_responder = tk.Button(
        janela_quiz,
        text="Responder",
        command=verificar_resposta,
        bg=AZUL_CLARO,
        fg=BRANCO,
        font=("Arial", 12, "bold"),
        width=15
    )
    btn_responder.pack(pady=20)

    # Mostrar a primeira pergunta imediatamente
    mostrar_pergunta()


# Mostrar pergunta
def mostrar_pergunta():
    resposta_selecionada.set("")

    pergunta_atual = perguntas[indice]

    lbl_progresso.config(
        text=f"Pergunta {indice + 1} de 10"
    )

    lbl_pergunta.config(
        text=pergunta_atual["pergunta"]
    )

    # Limpar alternativas anteriores
    for widget in frame_alternativas.winfo_children():
        widget.destroy()

    # Criar alternativas
    for alternativa in pergunta_atual["alternativas"]:
        tk.Radiobutton(
            frame_alternativas,
            text=alternativa,
            variable=resposta_selecionada,
            value=alternativa[0],
            bg=AZUL,
            fg=BRANCO,
            selectcolor=AZUL_CLARO,
            activebackground=AZUL,
            activeforeground=BRANCO,
            font=("Arial", 12),
            anchor="w"
        ).pack(fill="x", pady=8)

    lbl_feedback.config(text="")
    lbl_pontuacao.config(text=f"Pontuação: {pontuacao}")

    btn_responder.config(
        text="Responder",
        command=verificar_resposta
    )


# Verificar resposta
def verificar_resposta():
    global pontuacao

    resposta = resposta_selecionada.get()

    if resposta == "":
        messagebox.showwarning(
            "Atenção",
            "Selecione uma alternativa!",
            parent=janela_quiz
        )
        return

    resposta_correta = perguntas[indice]["resposta"]

    if resposta == resposta_correta:
        pontuacao += 1

        lbl_feedback.config(
            text="Resposta correta!",
            fg="#90EE90"
        )
    else:
        lbl_feedback.config(
            text=f"Resposta incorreta! Correta: {resposta_correta}",
            fg="#FFB6B6"
        )

    lbl_pontuacao.config(
        text=f"Pontuação: {pontuacao}"
    )

    btn_responder.config(
        text="Próxima",
        command=proxima_pergunta
    )


# Próxima pergunta
def proxima_pergunta():
    global indice

    indice += 1

    if indice < len(perguntas):
        mostrar_pergunta()
    else:
        finalizar_quiz()


# Resultado final
def finalizar_quiz():
    if pontuacao == 10:
        mensagem = "Excelente! Você acertou todas!"
    elif pontuacao >= 7:
        mensagem = "Muito bom! Você tem ótimo conhecimento!"
    elif pontuacao >= 5:
        mensagem = "Bom trabalho! Continue estudando."
    else:
        mensagem = "Continue estudando e tente novamente!"

    messagebox.showinfo(
        "Resultado Final",
        f"Você acertou {pontuacao} de 10 perguntas.\n\n{mensagem}",
        parent=janela_quiz
    )

    fechar_quiz()


# Fechar janela do quiz
def fechar_quiz():
    global janela_quiz

    if janela_quiz is not None:
        janela_quiz.destroy()
        janela_quiz = None


# Criar botão
def criar_botao(texto, comando):
    return tk.Button(
        janela_principal,
        text=texto,
        command=comando,
        bg=AZUL_CLARO,
        fg=BRANCO,
        activebackground=BRANCO,
        activeforeground=AZUL,
        font=("Arial", 12, "bold"),
        width=25,
        height=2
    )


# Menu principal
janela_principal = tk.Tk()
janela_principal.title("Quiz de Programação")
janela_principal.geometry("500x400")
janela_principal.configure(bg=AZUL)
janela_principal.resizable(False, False)

tk.Label(
    janela_principal,
    text="QUIZ DE PROGRAMAÇÃO",
    font=("Arial", 22, "bold"),
    bg=AZUL,
    fg=BRANCO
).pack(pady=40)

tk.Label(
    janela_principal,
    text="Teste seus conhecimentos!",
    font=("Arial", 14),
    bg=AZUL,
    fg=BRANCO
).pack(pady=10)

criar_botao("Iniciar Quiz", iniciar_quiz).pack(pady=20)
criar_botao("Sair", janela_principal.destroy).pack(pady=10)

# Executar programa
janela_principal.mainloop()
