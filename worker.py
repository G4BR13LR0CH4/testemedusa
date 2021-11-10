import zmq
from bdcomunication import getAnalise

def startWorker():
    """Cria a conexão e abre a rota para ler as mensagens"""
    global socket

    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://127.0.0.1:3001")

def formatId(id_request):
    """Formata o id, deixando ele pronto para ser usado na consulta do bd"""
    id_request = str(id_request).replace("'", "")
    id_request = id_request[1:]
    return id_request

def main():
    print("\n Leitor iniciado na porta 3001 \n")
    startWorker()

    while True:
        id_request = socket.recv()
        if id_request:
            list_img, id_req = getAnalise(formatId(id_request))
            #Colocar a função que inicia o algoritmo
            print("\nid request = \n" + id_req)
            for x in list_img:
                print(x)

if __name__ == "__main__":
    main()
