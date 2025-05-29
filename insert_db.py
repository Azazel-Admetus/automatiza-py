import mysql.connector
def inserir_db (nome, turno, turma, email):
    # nome = print('Nome: ')
    # turno = print('Turno: ')
    # turma = print('Turma: ')
    # email = print('Email: ')
    conexao = mysql.connector.connect(
        host = 'srv1893.hstgr.io',
        user= 'u169415369_azazeladmetus',
        password =  '314159265358979Ovatsug?',
        db = 'u169415369_ordemdafisica'
    )
    cursor = conexao.cursor()
    comando = '''
        INSERT INTO inscritos (nome, turno, turma, email)
        VALUES (%s, %s, %s, %s)
    '''
    valores = (nome, turno, turma, email)
    cursor.execute(comando, valores)
    cursor.commit()
    print('Registrado!')
    

    
    cursor.close()
    conexao.close()

nome = input('Nome: ')
turno = input('Turno: ')
turma = input('Turma: ')
email = input('Email: ')
inserir_db(nome, turno, turma, email)

