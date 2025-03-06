def todos_params(*args, **kwargs):
    print(f'args {args}') # Posicionais
    print(f'kwargs {kwargs}') # Nomeados


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params('a', 'b', 'c', {"Celular": 1500}, chovendo=True, sol=False)
    todos_params(primeiro='Davi', segundo='Tanaka')
    todos_params('Tanaka' ,primeiro='Davi')
