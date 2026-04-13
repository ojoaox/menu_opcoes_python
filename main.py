# BIBLIOTECAS NECESSÁRIAS:
# pip install rich
# pip install pyttsx3

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import print

import math
import datetime
import os
import random
import pyttsx3

console = Console()

def limpar():
    os.system("cls")


# Voz
def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 300)  
    engine.say(texto)
    engine.runAndWait()


# Início
limpar()
nome = Prompt.ask("[bold]Qual o seu nome?[/]")
falar(f"Olá, {nome}! Seja bem-vindo ao programa!")
limpar()

# Menu
def menu():
    console.print(
        f"[bold]Bem-vindo, {nome}![/]\n\n"
        "[yellow][1][/] Calculadora\n"
        "[yellow][2][/] Data / Hora\n"
        "[yellow][3][/] Lista de Animes\n"
        "[yellow][4][/] Mensagem Motivacional\n"
        "[yellow][9][/] Limpar Tela\n"
        "[yellow][0][/] Sair",
    )


# Calculadora
def calculadora():
    while True:
        limpar()
        console.print(Panel("[bold yellow]CALCULADORA[/]", border_style="yellow"))

        try:
            num1 = float(input("Digite o primeiro número: "))
            op = input("Operador [+ - * /]")
            num2 = float(input("Digite o segundo número: "))

            if op == "+":
                resultado = num1 + num2
            elif op == "-":
                resultado = num1 - num2
            elif op == "*":
                resultado = num1 * num2
            elif op == "/":
                resultado = num1 / num2
            else:
                console.print("[red]Operação inválida![/]")
                continue

            console.print(Panel(f"[bold green]Resultado: {resultado}[/]", border_style="green"))

        except ZeroDivisionError:
            console.print("[red]Não é possível dividir por zero![/]")
        except:
            console.print("[red]Entrada inválida![/]")

        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != "s":
            limpar()
            break


# Data e Hora
def data():
    data_atual = datetime.date.today()
    console.print(f"[green]📅 Data:[/] {data_atual.strftime('%d/%m/%Y')}")
    falar(f"A data atual é {data_atual.strftime('%d/%m/%Y')}")


def hora():
    hora_atual = datetime.datetime.now()
    console.print(f"[blue]⏰ Hora:[/] {hora_atual.strftime('%H:%M:%S')}")
    falar(f"A hora atual é {hora_atual.strftime('%H:%M:%S')}")


def data_hora():
    console.print(Panel("[bold yellow]CONSULTAR DATA/HORA[/]", border_style="yellow"))
    while True:
        console.print("[1] Ver Data\n[2] Ver Hora\n[3] Voltar")

        escolha = int(input("Digite: "))

        match escolha:
            case 1:
                limpar()
                data()
            case 2:
                limpar()
                hora()
            case 3:
                break
            case _:
                console.print("[red]Opção inválida![/]")


# Lista de Animes
lista = ["Attack On Titan", "Death Note", "Naruto"]

def mostrar_lista():
    tabela = Table(title="Lista de Animes")
    tabela.add_column("Índice")
    tabela.add_column("Nome")

    for anime in lista:
        tabela.add_row(str(lista.index(anime)), anime)

    console.print(tabela)


def anime():
    console.print(Panel("[bold yellow]LISTA DE ANIMES[/]", border_style="yellow"))
    while True:
        console.print(
            "[1] Adicionar\n[2] Remover\n[3] Ver lista\n[4] Tamanho\n[5] Ordenar\n[6] Voltar",
        )

        escolha = int(input("Digite: "))

        match escolha:
            case 1:
                nome_anime = input("Nome do anime: ")
                lista.append(nome_anime.title())
                falar(f"{nome_anime} adicionado!")

            case 2:
                if not lista:
                    console.print("[red]Lista vazia![/]")
                    continue

                mostrar_lista()

                try:
                    indice = int(input("Índice: "))
                    removido = lista.pop(indice)
                    console.print(f"[red]{removido} removido![/]")
                except:
                    console.print("[red]Índice inválido![/]")

            case 3:
                mostrar_lista()

            case 4:
                console.print(f"[yellow]Total:[/] {len(lista)}")

            case 5:
                console.print(sorted(lista))

            case 6:
                break

            case _:
                console.print("[red]Opção inválida![/]")


# Mensagem Motivacional
mensagens = [
    "Acredite em você. Você é capaz de muito mais do que imagina!",
    "Cada pequeno passo te aproxima do seu objetivo.",
    "Erros são provas de que você está tentando.",
    "Não desista. Grandes coisas levam tempo.",
    "Seu esforço de hoje é o sucesso de amanhã.",
    "Você não precisa ser perfeito, só precisa começar.",
    "Persistência vence talento quando o talento não persiste.",
    "Continue, mesmo quando estiver difícil. É aí que você cresce.",
    "Seu futuro é criado pelo que você faz hoje, não amanhã.",
    "Disciplina é a ponte entre metas e conquistas.",
    "A jornada pode ser longa, mas vale a pena.",
    "Você já superou desafios antes, vai superar esse também.",
    "Grandes resultados exigem grandes atitudes.",
    "Confie no processo.",
    "O sucesso começa com a decisão de tentar.",
    "Seja melhor do que ontem.",
    "Nada muda se você não mudar.",
    "A dor de hoje é a força de amanhã.",
    "Você é mais forte do que pensa.",
    "Foque no progresso, não na perfeição."
]

def mensagem():
    limpar()
    msg = random.choice(mensagens)
    console.print(f"[bold]{msg}[/]")
    falar(msg)


# Main
def main():
    while True:
        menu()
        escolha = int(input("Escolha: "))

        match escolha:
            case 1:
                calculadora()
            case 2:
                data_hora()
            case 3:
                anime()
            case 4:
                mensagem()
            case 9:
                limpar()
            case 0:
                console.print("[bold red]Saindo...[/]")
                falar("Até a próxima!")
                break
            case _:
                console.print("[red]Opção inválida![/]")


main()