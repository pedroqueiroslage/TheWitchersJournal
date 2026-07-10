from rich import print
from rich.panel import Panel


def menu(op):
    print('=' * 30)
    print('The Witcher\'s Journal'.center(30))
    print('=' * 30)
    print('[green]1 - View Active Quests\n'
          '2 - Register New Quest\n'
          '3 - Complete a Contract\n4 - Close the Journal')
    print('=' * 30)
    try:
        z = str(input(op)).strip()
        while z not in ['1', '2', '3', '4']:
            print('[red]Invalid Answer![/]')
            z = str(input(op)).strip()
        return z
    except Exception as e:
        print(f'[red]UNEXPECTED ERROR: {e}[/]')
        return '4'


class Interface:
    def __init__(self):
        self.nome = 'Journal'
        self.status = 'Pending'
        try:
            with open(self.nome, 'a'):
                pass
        except Exception as e:
            print(f'[red]UNEXPECTED ERROR: {e}[/]')

    def cad_mission(self):
        try:
            with open(self.nome, 'r') as arq:
                copy = arq.read().splitlines()
            mission = input("What's the contract's name? ")
            if mission in copy:
                while True:
                    val = str(input('This contract is already registered! '
                                    'Register anyway? [Y/N] ').strip().upper()[0])
                    if val == 'Y':
                        value = input("What's the reward? $")
                        mv = f'{mission}\nR${value}\n{self.status}\n'
                        print('[blue]Contract successfully registered in the Journal![/]')
                        with open(self.nome, 'a') as arq:
                            arq.write(mv)
                        break
                    if val == 'N':
                        print('[blue]Returning to the menu...[/]')
                        break
                    else:
                        print('[red]Invalid input![/]')
            else:
                value = input("What's the reward? $")
                mv = f'{mission}\nR${value}\n{self.status}\n'
                print('[blue]Contract successfully registered in the Journal![/]')
                with open(self.nome, 'a') as arq:
                    arq.write(mv)
        except Exception as e:
            print(f'[red]UNEXPECTED ERROR: {e}[/]')

    def conclude_mission(self):
        try:
            con = input('Which contract did you complete? ')
            with open(self.nome, 'r') as arq:
                copy = arq.readlines()
            validation = False
            for line, mission in enumerate(copy):
                if con in copy[line].strip():
                    copy[line + 2] = copy[line + 2].replace('Pending', 'Completed')
                    print('[blue]Contract successfully completed![/]')
                    validation = True
                    break
                else:
                    continue
            if validation:
                with open(self.nome, 'w') as arq:
                    arq.writelines(copy)
            else:
                print('[blue]Quest not found in the system![/]')
        except Exception as e:
            print(f'[red]UNEXPECTED ERROR: {e}[/]')

    def show_missions(self):
        try:
            with open(self.nome, 'r') as arq:
                copy = arq.readlines()
            if len(copy) <= 1:
                print('[blue]No contracts registered in the system...[/]')
            else:
                pass
            for cont in range(0, len(copy), 3):
                print(Panel(f'Reward: [yellow]{copy[1+cont].strip()}[/]\nStatus: [green]{copy[2+cont].strip()}[/]',
                            title=f'[purple]{copy[0+cont].strip()}[/]', width=35))
        except Exception as e:
            print(f'[red]UNEXPECTED ERROR: {e}[/]')


journal_sistema = Interface()
while True:
    per = menu('Qual opcão: ')
    if per in '1234':
        if per == '1':
            journal_sistema.show_missions()
        if per == '2':
            journal_sistema.cad_mission()
        if per == '3':
            journal_sistema.conclude_mission()
        if per == '4':
            print('[blue]Fechando sistema...[/]')
            break
    else:
        print('[red]Digite um valor válido![/]')
