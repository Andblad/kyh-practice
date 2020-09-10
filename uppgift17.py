from pathlib import Path

p = Path('text_up_17.txt')
content = p.read_text(encoding='utf8')
tasks = content.splitlines()


def options():
    print('1. Visa lista')
    print('2. Lägg till')
    print('3. Ta bort')
    print('4. Stäng')

    q = input('Vad vill du göra? ')
    if q == '1':
        read()
    if q == '2':
        add()
    if q == '3':
        erase()
    if q == '4':
        return
    else:
        options()


def read():
    nl = '\n'
    content.splitlines()
    content.strip()
    print(nl.join(tasks))
    return


def add():
    task = input("Vad vill du lägga till? ").strip()
    tasks.append(task)
    n = '\n'
    p.write_text(f"{n.join(tasks)}", encoding='utf8')
    return


def erase():
    print(', '.join(tasks))
    delete = input('Vad vill du ta bort?')
    if delete in tasks:
        tasks.remove(delete)
        return
    else:
        erase()


if __name__ == '__main__':
    options()