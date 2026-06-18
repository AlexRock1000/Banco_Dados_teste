from conexao import conectar

class Produto:
    def __init__(self, nome, preco, categoria, ativo = True, criado_em = None, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.ativo = ativo
        self.criado_em = criado_em

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO produto (nome, preco, categoria, ativo) VALEUS (%s, %s, %s, %s)"
        cursor.execute(sql, (self.nome, self.preco, self.categoria, self.ativo))