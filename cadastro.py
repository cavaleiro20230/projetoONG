def cadastrar_usuario():
    """
    Função para cadastrar um novo usuário no sistema.
    """
    nome = input('Nome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    tipo_usuario = input('Tipo de usuário (administrador/comum): ')

    # Verificar se o email já está cadastrado
    consulta_email = """
    SELECT 1 FROM usuarios WHERE email = ?
    """
    cursor.execute(consulta_email, (email,))
    if cursor.fetchone():
        print('Email já cadastrado. Tente outro.')
        return

    # Criptografar a senha
    senha_criptografada = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    # Consulta SQL para cadastrar o usuário
    consulta = """
    INSERT INTO usuarios (nome, email, senha, tipo)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(consulta, (nome, email, senha_criptografada, tipo_usuario))
    db.commit()

    print(f'Usuário {nome} cadastrado com sucesso!')

def cadastrar_pessoa():
    """
    Função para cadastrar um novo doador ou voluntário no sistema.
    """
    nome = input('Nome: ')
    contato = input('Contato (e-mail/telefone): ')
    endereco = input('Endereço: ')
    data_nascimento_str = input('Data de nascimento (DD/MM/AAAA):
