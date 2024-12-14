from GUICZINHO import banco_dados

<<<<<<< HEAD
class Usuario(banco_dados.Model):
    __tablename__ = 'USUARIO'

    Matricula = banco_dados.column(banco_dados.Integer, primary_key=True, autoincrement=True, nullable=False)
    Nome = banco_dados.column(banco_dados.String(50), nullable=False )
    Tipo = banco_dados.column(banco_dados.Enum('admin', 'usuario'), nullable=False)
    Senha = banco_dados.column(banco_dados.String(50), nullable=False)
=======


class Usuario(banco_dados.Model):
    __tablename__ = 'USUARIO'

    Matricula = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True, nullable=False)
    Nome = banco_dados.Column(banco_dados.String(50), nullable=False )
    Tipo = banco_dados.Column(banco_dados.Enum('admin', 'usuario'), nullable=False)
    Senha = banco_dados.Column(banco_dados.String(50), nullable=False)
>>>>>>> 6077cfe (quinto commit)


class Setores(banco_dados.Model):
    __tablename__ = 'SETORES'
    
<<<<<<< HEAD
    ID_setor = banco_dados.column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_setor = banco_dados.column(banco_dados.String(255))
    Responsavel_setor = banco_dados.column(banco_dados.String(255))
    Descricao_setor = banco_dados.column(banco_dados.String(3000))
    Contato_email = banco_dados.column(banco_dados.String(255))
    Contato_numero = banco_dados.column(banco_dados.Interger)
    Imagens_setor = banco_dados.column(banco_dados.LargeBinary)
=======
    ID_setor = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_setor = banco_dados.Column(banco_dados.String(255))
    Responsavel_setor = banco_dados.Column(banco_dados.String(255))
    Descricao_setor = banco_dados.Column(banco_dados.String(3000))
    Contato_email = banco_dados.Column(banco_dados.String(255))
    Contato_numero = banco_dados.Column(banco_dados.Integer)
    Imagens_setor = banco_dados.Column(banco_dados.LargeBinary)
>>>>>>> 6077cfe (quinto commit)

class Eventos(banco_dados.Model):
    __tablename__ = 'EVENTOS'

<<<<<<< HEAD
    ID_evento = banco_dados.column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_evento = banco_dados.column(banco_dados.String(255))
    Data_evento = banco_dados.column(banco_dados.Date)
    Descricao_evento = banco_dados.column(banco_dados.String(3000))
    Responsaveis_evento = banco_dados.column(banco_dados.String(255))
    local = banco_dados.column(banco_dados.String(255))
    Imagens_evento = banco_dados.column(banco_dados.LargeBinary)
=======
    ID_evento = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_evento = banco_dados.Column(banco_dados.String(255))
    Data_evento = banco_dados.Column(banco_dados.Date)
    Descricao_evento = banco_dados.Column(banco_dados.String(3000))
    Responsaveis_evento = banco_dados.Column(banco_dados.String(255))
    local = banco_dados.Column(banco_dados.String(255))
    Imagens_evento = banco_dados.Column(banco_dados.LargeBinary)
>>>>>>> 6077cfe (quinto commit)

class MaterialApoio(banco_dados.Model):
    __tablename__ = 'MATERIAL_APOIO'

<<<<<<< HEAD
    ID_arquivo = banco_dados.column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_arquivo = banco_dados.column(banco_dados.String(255))
    Quantidade_download = banco_dados.column(banco_dados.Integer)
    Data_download = banco_dados.column(banco_dados.Date)
    Arquivo_pdf = banco_dados.column(banco_dados.LargeBinary)
    Usuario_mat_download = banco_dados.column(banco_dados.Integer, banco_dados.ForeignKey('Usuario.Matricula'))
=======
    ID_arquivo = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Nome_arquivo = banco_dados.Column(banco_dados.String(255))
    Quantidade_download = banco_dados.Column(banco_dados.Integer)
    Data_download = banco_dados.Column(banco_dados.Date)
    Arquivo_pdf = banco_dados.Column(banco_dados.LargeBinary)
    Usuario_mat_download = banco_dados.Column(banco_dados.Integer, banco_dados.ForeignKey('USUARIO.Matricula'))
>>>>>>> 6077cfe (quinto commit)

class Avaliacao(banco_dados.Model):
    __tablename__ = 'AVALIACAO'

<<<<<<< HEAD
    ID_feedback = banco_dados.column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Sugestao = banco_dados.column(banco_dados.String(1000))
    Estrelas = banco_dados.column(banco_dados.Integer, unique=True)
    Data_feedback = banco_dados.column(banco_dados.Date)
    Usuario_mat_avaliacao = banco_dados.column(banco_dados.Integer, banco_dados.ForeignKey('Usuario.Matricula'))
=======
    ID_feedback = banco_dados.Column(banco_dados.Integer, primary_key=True, autoincrement=True)
    Sugestao = banco_dados.Column(banco_dados.String(1000))
    Estrelas = banco_dados.Column(banco_dados.Integer, unique=True)
    Data_feedback = banco_dados.Column(banco_dados.Date)
    Usuario_mat_avaliacao = banco_dados.Column(banco_dados.Integer, banco_dados.ForeignKey('USUARIO.Matricula'))
>>>>>>> 6077cfe (quinto commit)


