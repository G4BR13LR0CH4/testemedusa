import zmq
from bdcomunication import getAnalise

def startWorker():
    """Cria a conexão e abre a rota para ler as mensagens"""
    global socket

    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://127.0.0.1:3001")

def readList():
    """Lê a lista e retorna o último id adicionado, necessário alteração para LIFO"""
    id_request = listIds.pop()
    return id_request

def writeList():
    """Escreve em um arquivo de texto o id"""
    print("")

def formatId(id_request):
    """Formata o id, deixando ele pronto para ser usado na consulta do bd"""
    id_request = str(id_request).replace("'", "")
    id_request = id_request[1:]
    return id_request

def main():
    startWorker()
    global listIds

    listIds = []

    while True:
        id_request = socket.recv()
        if id_request:
            

            #função que inicia o algoritmo passando o id_requesr por parâmetro
            #Essa função pode retornar o json que vai ser cadastrado no bd para logo depois o algoritmo que lida com o bd cadastrar
            list_img, id_req = getAnalise(formatId(id_request))
            print("\n" + id_req + "\n")
            for x in list_img:
                print(x)

if __name__ == "__main__":
    main()
