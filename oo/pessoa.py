class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} = olhos {cls.olhos}'


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
    fabio.sobrenome = 'Martins'
    del fabio.filhos
    fabio.olhos = 1
    del fabio.olhos
    print(fabio.__dict__)
    print(felipe.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(fabio.olhos)
    print(felipe.olhos)
    print(id(Pessoa.olhos), id(fabio.olhos), id(felipe.olhos))
    print(Pessoa.metodo_estatico(), fabio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), fabio.nome_e_atributos_de_classe())