class Programa:  # Classe Pai - Super Classe
    # Ler sobre o "dunder methods" __init__
    def __init__(self, nome, ano):
        self._nome = nome.title()
        # _Programa__nome / Problema de deixar o nome privado com __
        # Por convenção usamos so um _
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # Sobrescrevendo o metodo mãe com dunder methods __str__
    # Sempre usar o returnx
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


class Filme(Programa):  # Classe Filho pegando a informação da classe mãe
    def __init__(self, nome, ano, duracao):  # to sobrescrevendo a classe init
        super().__init__(nome, ano)
        # Estou chamando o inicializador da classe mae,
        # passando o parametro nome e ano
        self.duracao = duracao

    # Sobrescrevendo o metodo mãe com dunder methods __str__
    # Sempre usar o return
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao}min - {self._likes}'


class Serie(Programa):  # Classe Filho
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # Sobrescrevendo o metodo mãe com dunder methods __str__
    # Sempre usar o return
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas}temporadas - {self._likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

# Herdando o comportamento do list (iteracão da lista)
# Essa herança tras beneficios e problemas
# class Playlist(list):
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)

    # def tamanho(self):
    #     return len(self.programas)


vingadores = Filme('Vingadores-guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()


# Polimorfismo (vingadores e atlanta são um programa)
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

    # 1) Primeira vez
    # hasattr em tempo de execucao verifica qual
    # objeto está sendo passado
    # if ternario
    # detalhes = programa.duracao if hasattr(
    #     programa, 'duracao') else programa.temporadas

    # print(
    #     f'{programa.nome} - {detalhes} - {programa.likes}')
