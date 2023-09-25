class Noticia:
    def __init__(self, titulo, conteudo, data_publicacao):
        self.titulo = titulo
        self.conteudo = conteudo
        self.data_publicacao = data_publicacao
    def validate(self):
        if not self.titulo:
            return False
        if not self.conteudo:
            return False
        if not self.data_publicacao:
            return False
        return True