resultado = {
    "id_request": "teste",
	"timestamp": "",
	"moagem de calcario": "",
	"moagem de silica": "",
	"temperatura de clinquerizacao": "",
	"grau de homogeneizacao": "",
	"tempo de clinquerizacao": "",
	"1° Resfriamento": "",
	"2° Resfriamento": "",
	"fsc farinha alimentada": "",
	"peso do litro": "",
	"chama": "",
	"forno": "",
    "imgs": []
    }
img = {
        "img_path": "teste01",
	    "img_result": "string",
	    "alita C3S": {
		    "forma": "string",
		    "grau de decomposicao": "string",
		    "inclusao cristalina": "string",
		    "diametro medio": "string"
	    }
    }

def get_database():
    """Faz a conexão com o banco de dados e retorna o mesmo"""
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://Gabrock:a4I9wHatYrMnl36U@cluster0.15rde.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    cliente = MongoClient(CONNECTION_STRING)

    return cliente["myFirstDatabase"]

def getAnalise(id_request: str):
    """
        Recebe o id e Retorna dados importantes do registro a ser analisado
        e altera o status para "Análise em andamento"
    """   
    db = get_database() 
    collection = db["registros"]

    registro = collection.find_one_and_update({'id_request': id_request}, {'$set': {'status': "Análise em andamento"}})

    return registro['img_list'], registro['id_request']

def writeResults(result: dict):
    """
        Recebe e Insere um dict no bd, o objetivo é incluir apenas o 
        resultado, mas também adiciona o dict contendo as imagens.
    """
    db = get_database()
    collection = db['resultados']

    collection.insert_one(result)

def writeImgsInResults(imgs: list, id_request: str):
    """Recebe uma lista e um id, Insere essa lista no documento que vai ser buscado pelo id."""
    db = get_database()
    collection = db['resultados']

    collection.find_one_and_update({'id_request': id_request}, {'$set': {'imgs': imgs}})
