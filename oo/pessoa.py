class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    fabio = Pessoa(felipe, nome='Fabio')
    print(Pessoa.cumprimentar(fabio))
    print(id(fabio))
    print(fabio.cumprimentar())
    print(fabio.nome)
    print(fabio.idade)
    for filho in fabio.filhos:
        print(filho.nome)
