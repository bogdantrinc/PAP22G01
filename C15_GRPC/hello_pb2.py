# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\x12\x08\x63\x31\x35_grpc\"0\n\x0fGetMeasurements\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06length\x18\x02 \x01(\x05\"\x1e\n\x0cGiveResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1f\n\x0bHelloReplay\x12\x10\n\x08response\x18\x01 \x01(\t2\x86\x01\n\x07Greeter\x12;\n\x08SayHello\x12\x16.c15_grpc.HelloRequest\x1a\x15.c15_grpc.HelloReplay\"\x00\x12>\n\x07GetData\x12\x19.c15_grpc.GetMeasurements\x1a\x16.c15_grpc.GiveResponse\"\x00\x62\x06proto3')



_GETMEASUREMENTS = DESCRIPTOR.message_types_by_name['GetMeasurements']
_GIVERESPONSE = DESCRIPTOR.message_types_by_name['GiveResponse']
_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLOREPLAY = DESCRIPTOR.message_types_by_name['HelloReplay']
GetMeasurements = _reflection.GeneratedProtocolMessageType('GetMeasurements', (_message.Message,), {
  'DESCRIPTOR' : _GETMEASUREMENTS,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:c15_grpc.GetMeasurements)
  })
_sym_db.RegisterMessage(GetMeasurements)

GiveResponse = _reflection.GeneratedProtocolMessageType('GiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _GIVERESPONSE,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:c15_grpc.GiveResponse)
  })
_sym_db.RegisterMessage(GiveResponse)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:c15_grpc.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReplay = _reflection.GeneratedProtocolMessageType('HelloReplay', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLAY,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:c15_grpc.HelloReplay)
  })
_sym_db.RegisterMessage(HelloReplay)

_GREETER = DESCRIPTOR.services_by_name['Greeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETMEASUREMENTS._serialized_start=25
  _GETMEASUREMENTS._serialized_end=73
  _GIVERESPONSE._serialized_start=75
  _GIVERESPONSE._serialized_end=105
  _HELLOREQUEST._serialized_start=107
  _HELLOREQUEST._serialized_end=135
  _HELLOREPLAY._serialized_start=137
  _HELLOREPLAY._serialized_end=168
  _GREETER._serialized_start=171
  _GREETER._serialized_end=305
# @@protoc_insertion_point(module_scope)
