import clientes_pb2 as message
import clientes_pb2_grpc as service
import grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service.ClientesStub(channel)

    #Função do .proto de buscar cliente específico no db
    response = stub.BuscaCliente(message.ClientesRequest(idCliente=3))
    print(response)

    #Função do .proto de buscar todos os clientes no db sem parâmetro de chamada
    response = stub.TodosClientes(message.Empty())
    print(response)

    ## É possível pegar as variáveis fácilmente pois o return é uma classe com os atributos de clientes
    for cliente in response.cliente: 
        nome = cliente.nome
        id = cliente.idCliente 
        
        #os nomes das variáveis necessitam ser idênticas ao do banco de dados e do arquivo .proto
        print(f'Cliente {nome}, ID: {id}')
        
run()
    