import grpc
import clientes_pb2 as message
import clientes_pb2_grpc as service
from configdb import conn
from concurrent import futures
import time
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Clientes(service.ClientesServicer):
    def BuscaCliente(self, request, context):
        with conn.cursor() as cur:
            sql = 'select nome from dbclientes.clientes where idCliente = %s'
            cur.execute(sql, (request.idCliente))
            res = cur.fetchone()
        result = message.ClienteResponse(idCliente=request.idCliente, nome=res['nome'])
        return result

    def TodosClientes(self, request, context):
        with conn.cursor() as cur:
            sql = 'select * from dbclientes.clientes;'
            cur.execute(sql)
            res = cur.fetchall()
        result = message.ClientesList(cliente=res)
        return result

def Serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.add_ClientesServicer_to_server(Clientes(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print('Server Stop')
        server.stop(0)

if __name__ == '__main__':
    print('Server Start')
    Serve()
    conn.close()

