from conexao import conectar

class Produto:
    def __init__(self, nome, preco, categoria, ativo = True, criado_em = None, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.ativo = ativo
        self.criado_em = criado_em

    def mostrar(self):
        print (f"""
        Código: {self.id}
        Nome: {self.nome}
        Preço: {self.preco}
        Categoria: {self.categoria}
        Ativo: {self.ativo}
        Criado_em: {self.criado_em}
        """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO produto (nome, preco, categoria, ativo) VALEUS (%s, %s, %s, %s)"
        cursor.execute(sql, (self.nome, self.preco, self.categoria, self.ativo))

        conexao.commit()
        conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM produto"
    cursor.execute(sql)

    produtos = []
    for id, nome, preco, categoria, ativo, criado_em in cursor.fetchall():
        produto = Produto(nome, preco, categoria, ativo, criado_em, id)
        produtos.append(produto)

    conexao.close()
    return produtos