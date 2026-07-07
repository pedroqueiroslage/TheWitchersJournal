from rich import print
from rich.panel import Panel


def menu(op):
    print('=' * 30)
    print('The Witcher\'s Journal'.center(30))
    print('=' * 30)
    print('[green]1 - Ver missões cadastradas\n'
          '2 - Cadastrar nova missão\n'
          '3 - Concluir missão existente\n4 - Sair do Sistema')
    print('=' * 30)
    try:
        z = str(input(op)).strip()
        while z not in ['1', '2', '3', '4']:
            print('[red]Resposta Inválida![/]')
            z = str(input(op)).strip()
        return z
    except Exception as e:
        print(f'[red]ERRO INESPERADO: {e}[/]')
        return '4'


class Interface:
    def __init__(self):
        self.nome = 'Journal'
        self.status = 'Pendente'
        try:
            with open(self.nome, 'a'):
                pass
        except Exception as e:
            print(f'[red]ERRO INESPERADO: {e}[/]')

    def cad_mission(self):
        try:
            with open(self.nome, 'r') as arq:
                copy = arq.read().splitlines()
            mission = input('Qual o nome da missão? ')
            if mission in copy:
                while True:
                    val = str(input('Missão com nome já cadastrado, deseja fazer novo '
                                    'cadastro mesmo assim? [S/N] ').strip().upper()[0])
                    if val == 'S':
                        value = input('Qual sua recompensa? R$')
                        mv = f'{mission}\nR${value}\n{self.status}\n'
                        print('[blue]Missão cadastrada com sucesso![/]')
                        with open(self.nome, 'a') as arq:
                            arq.write(mv)
                        break
                    if val == 'N':
                        print('[blue]Retornando ao menu...[/]')
                        break
                    else:
                        print('[red]Resposta Inválida![/]')
            else:
                value = input('Qual sua recompensa? R$')
                mv = f'{mission}\nR${value}\n{self.status}\n'
                print('[blue]Missão cadastrada com sucesso![/]')
                with open(self.nome, 'a') as arq:
                    arq.write(mv)
        except Exception as e:
            print(f'[red]ERRO INESPERADO: {e}[/]')

    def conclude_mission(self):
        try:
            con = input('Qual o nome da missão concluida? ')
            with open(self.nome, 'r') as arq:
                copy = arq.readlines()
            validation = False
            for line, mission in enumerate(copy):
                if con in copy[line].strip():
                    copy[line + 2] = copy[line + 2].replace('Pendente', 'Concluida')
                    print('[blue]Missão concluida com sucesso![/]')
                    validation = True
                    break
                else:
                    continue
            if validation:
                with open(self.nome, 'w') as arq:
                    arq.writelines(copy)
            else:
                print('[blue]Missão não encontrada no sistema![/]')
        except Exception as e:
            print(f'[red]ERRO INESPERADO: {e}[/]')

    def show_missions(self):
        try:
            with open(self.nome, 'r') as arq:
                copy = arq.readlines()
            if len(copy) <= 1:
                print('[blue]Nenhuma missão cadastrada no sistema...[/]')
            else:
                pass
            for cont in range(0, len(copy), 3):
                print(Panel(f'Reward: [yellow]{copy[1+cont].strip()}[/]\nStatus: [green]{copy[2+cont].strip()}[/]',
                            title=f'[purple]{copy[0+cont].strip()}[/]', width=35))
        except Exception as e:
            print(f'[red]ERRO INESPERADO: {e}[/]')
