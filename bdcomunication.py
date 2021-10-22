def get_database():
    """Faz a conexão com o banco de dados e retorna o mesmo"""
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://Gabrock:a4I9wHatYrMnl36U@cluster0.15rde.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    cliente = MongoClient(CONNECTION_STRING)

    return cliente["myFirstDatabase"]

def get_idRequest():
    """Busca o id na lista e retorna para a consulta"""
    id_request = "dfe0cd85-8e62-4287-96a5-3f5d1490d926"

    return id_request

def getAllanalises():
    """Retorna todos as analises registradas"""
    db = get_database() 
    collection = db["registros"]
    
    return collection.find()

def getAnalise():
    """
        Retorna dados importantes da registro a ser analisado
        e alterado o status para "Análise em andamento"
    """   
    db = get_database() 
    collection = db["registros"]

    objeto = collection.find_one_and_update({'id_request': get_idRequest()}, {'$set': {'status': "Análise em andamento"}})

    return objeto['img_list'], objeto['id_request']
