def login():
    """
    Função para realizar o login de um usuário no sistema.
    Retorna o ID, nome e tipo do usuário logado ou None em caso de falha.
    """
    email = input('Email: ')
    senha = input('Senha: ')

    # Criptografar a senha digitada
    senha_criptografada = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    # Consulta SQL para verificar login e senha
    consulta = """
    SELECT id, nome, tipo FROM usuarios
    WHERE email = ? AND senha = ?
    """
    cursor.execute(consulta, (email, senha_criptografada))
    resultado = cursor.fetchone()

    if resultado:
        print(f'Login efetuado com sucesso!')
        return resultado[0], resultado[1], resultado[2]  # Retorna ID, nome e tipo do usuário
    else:
        print('Email ou senha inválidos!')
        return None

def get_id_usuario_logado():
    """
    Retorna o ID do usuário logado, se existir.
    """
    # Verificar se existe um usuário logado
    if not hasattr(get_id_usuario_logado, 'id_usuario'):
        get_id_usuario_logado.id_usuario = None

    return get_id_usuario_logado.id_usuario
