# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clientes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='clientes.proto',
  package='clientes',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x63lientes.proto\x12\x08\x63lientes\"$\n\x0f\x43lientesRequest\x12\x11\n\tidCliente\x18\x01 \x01(\x05\"2\n\x0f\x43lienteResponse\x12\x11\n\tidCliente\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\":\n\x0c\x43lientesList\x12*\n\x07\x63liente\x18\x01 \x03(\x0b\x32\x19.clientes.ClienteResponse\"\x07\n\x05\x45mpty2\x8e\x01\n\x08\x43lientes\x12\x46\n\x0c\x42uscaCliente\x12\x19.clientes.ClientesRequest\x1a\x19.clientes.ClienteResponse\"\x00\x12:\n\rTodosClientes\x12\x0f.clientes.Empty\x1a\x16.clientes.ClientesList\"\x00\x62\x06proto3'
)




_CLIENTESREQUEST = _descriptor.Descriptor(
  name='ClientesRequest',
  full_name='clientes.ClientesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idCliente', full_name='clientes.ClientesRequest.idCliente', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=64,
)


_CLIENTERESPONSE = _descriptor.Descriptor(
  name='ClienteResponse',
  full_name='clientes.ClienteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idCliente', full_name='clientes.ClienteResponse.idCliente', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nome', full_name='clientes.ClienteResponse.nome', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=116,
)


_CLIENTESLIST = _descriptor.Descriptor(
  name='ClientesList',
  full_name='clientes.ClientesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cliente', full_name='clientes.ClientesList.cliente', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=176,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='clientes.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=185,
)

_CLIENTESLIST.fields_by_name['cliente'].message_type = _CLIENTERESPONSE
DESCRIPTOR.message_types_by_name['ClientesRequest'] = _CLIENTESREQUEST
DESCRIPTOR.message_types_by_name['ClienteResponse'] = _CLIENTERESPONSE
DESCRIPTOR.message_types_by_name['ClientesList'] = _CLIENTESLIST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientesRequest = _reflection.GeneratedProtocolMessageType('ClientesRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTESREQUEST,
  '__module__' : 'clientes_pb2'
  # @@protoc_insertion_point(class_scope:clientes.ClientesRequest)
  })
_sym_db.RegisterMessage(ClientesRequest)

ClienteResponse = _reflection.GeneratedProtocolMessageType('ClienteResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTERESPONSE,
  '__module__' : 'clientes_pb2'
  # @@protoc_insertion_point(class_scope:clientes.ClienteResponse)
  })
_sym_db.RegisterMessage(ClienteResponse)

ClientesList = _reflection.GeneratedProtocolMessageType('ClientesList', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTESLIST,
  '__module__' : 'clientes_pb2'
  # @@protoc_insertion_point(class_scope:clientes.ClientesList)
  })
_sym_db.RegisterMessage(ClientesList)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'clientes_pb2'
  # @@protoc_insertion_point(class_scope:clientes.Empty)
  })
_sym_db.RegisterMessage(Empty)



_CLIENTES = _descriptor.ServiceDescriptor(
  name='Clientes',
  full_name='clientes.Clientes',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=188,
  serialized_end=330,
  methods=[
  _descriptor.MethodDescriptor(
    name='BuscaCliente',
    full_name='clientes.Clientes.BuscaCliente',
    index=0,
    containing_service=None,
    input_type=_CLIENTESREQUEST,
    output_type=_CLIENTERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TodosClientes',
    full_name='clientes.Clientes.TodosClientes',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CLIENTESLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENTES)

DESCRIPTOR.services_by_name['Clientes'] = _CLIENTES

# @@protoc_insertion_point(module_scope)