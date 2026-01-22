# if-elif-else statement
from pyscript import display, document


def students_classification(e):
    document.getElementById('result').innerHTML =  '    '

    classification = float(document.getElementById('number1').value)

    if classification >= 95:
        display(f'Bergamo 1', target='result')

    elif classification >= 94:
        display(f'Bergamo 2', target='result')

    elif classification >= 90:
        display(f'Bergamo 3', target='result')

    elif classification >= 85:
        display(f'Perugia 1', target='result')

    elif classification <= 74:
        display(f'Perugia 2', target='result')
    
    else:
        display(f'Invalid input', target='result')