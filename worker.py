import zmq

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

def main():
    startWorker()
    global listIds

    listIds = []

    while True:
        id_request = socket.recv()
        if id_request:
            listIds.append(str(id_request))
            print(id_request)

if __name__ == "__main__":
    main()
