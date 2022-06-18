# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: safeentry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsafeentry.proto\"O\n\x0e\x43heckInRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0f\n\x07\x63heckin\x18\x04 \x01(\t\"\"\n\x0f\x43heckInOutReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"1\n\x0f\x43heckOutRequest\x12\x0c\n\x04nric\x18\x01 \x01(\t\x12\x10\n\x08\x63heckout\x18\x02 \x01(\t\"O\n\x0eGroupInRequest\x12\x0c\n\x04name\x18\x01 \x03(\t\x12\x0c\n\x04nric\x18\x02 \x03(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x0f\n\x07\x63heckin\x18\x04 \x01(\t\"1\n\x0fGroupOutRequest\x12\x0c\n\x04nric\x18\x01 \x03(\t\x12\x10\n\x08\x63heckout\x18\x02 \x01(\t2\xd9\x01\n\tSafeEntry\x12.\n\x07\x43heckIn\x12\x0f.CheckInRequest\x1a\x10.CheckInOutReply\"\x00\x12\x30\n\x08\x43heckOut\x12\x10.CheckOutRequest\x1a\x10.CheckInOutReply\"\x00\x12\x33\n\x0c\x43heckInGroup\x12\x0f.GroupInRequest\x1a\x10.CheckInOutReply\"\x00\x12\x35\n\rCheckOutGroup\x12\x10.GroupOutRequest\x1a\x10.CheckInOutReply\"\x00\x62\x06proto3')



_CHECKINREQUEST = DESCRIPTOR.message_types_by_name['CheckInRequest']
_CHECKINOUTREPLY = DESCRIPTOR.message_types_by_name['CheckInOutReply']
_CHECKOUTREQUEST = DESCRIPTOR.message_types_by_name['CheckOutRequest']
_GROUPINREQUEST = DESCRIPTOR.message_types_by_name['GroupInRequest']
_GROUPOUTREQUEST = DESCRIPTOR.message_types_by_name['GroupOutRequest']
CheckInRequest = _reflection.GeneratedProtocolMessageType('CheckInRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINREQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:CheckInRequest)
  })
_sym_db.RegisterMessage(CheckInRequest)

CheckInOutReply = _reflection.GeneratedProtocolMessageType('CheckInOutReply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINOUTREPLY,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:CheckInOutReply)
  })
_sym_db.RegisterMessage(CheckInOutReply)

CheckOutRequest = _reflection.GeneratedProtocolMessageType('CheckOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUTREQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:CheckOutRequest)
  })
_sym_db.RegisterMessage(CheckOutRequest)

GroupInRequest = _reflection.GeneratedProtocolMessageType('GroupInRequest', (_message.Message,), {
  'DESCRIPTOR' : _GROUPINREQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:GroupInRequest)
  })
_sym_db.RegisterMessage(GroupInRequest)

GroupOutRequest = _reflection.GeneratedProtocolMessageType('GroupOutRequest', (_message.Message,), {
  'DESCRIPTOR' : _GROUPOUTREQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:GroupOutRequest)
  })
_sym_db.RegisterMessage(GroupOutRequest)

_SAFEENTRY = DESCRIPTOR.services_by_name['SafeEntry']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKINREQUEST._serialized_start=19
  _CHECKINREQUEST._serialized_end=98
  _CHECKINOUTREPLY._serialized_start=100
  _CHECKINOUTREPLY._serialized_end=134
  _CHECKOUTREQUEST._serialized_start=136
  _CHECKOUTREQUEST._serialized_end=185
  _GROUPINREQUEST._serialized_start=187
  _GROUPINREQUEST._serialized_end=266
  _GROUPOUTREQUEST._serialized_start=268
  _GROUPOUTREQUEST._serialized_end=317
  _SAFEENTRY._serialized_start=320
  _SAFEENTRY._serialized_end=537
# @@protoc_insertion_point(module_scope)
