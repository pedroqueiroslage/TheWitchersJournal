from interface import Interface, menu
from rich import print


journal_sistema = Interface()
while True:
    per = menu('Choose an option: ')
    if per in '1234':
        if per == '1':
            journal_sistema.show_missions()
        if per == '2':
            journal_sistema.cad_mission()
        if per == '3':
            journal_sistema.conclude_mission()
        if per == '4':
            print('[blue]Closing the Journal...[/]')
            break
    else:
        print('[red]Please enter a valid value![/]')

comitt isso aq no teste