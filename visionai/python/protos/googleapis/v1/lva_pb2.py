# Copyright (c) 2023 Google LLC All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visionai/python/protos/googleapis/v1/lva.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.visionai/python/protos/googleapis/v1/lva.proto\x12\x18google.cloud.visionai.v1\"M\n\x0e\x41ttributeValue\x12\x0b\n\x01i\x18\x01 \x01(\x03H\x00\x12\x0b\n\x01\x66\x18\x02 \x01(\x02H\x00\x12\x0b\n\x01\x62\x18\x03 \x01(\x08H\x00\x12\x0b\n\x01s\x18\x04 \x01(\x0cH\x00\x42\x07\n\x05value\"\xd4\x04\n\x12\x41nalyzerDefinition\x12\x10\n\x08\x61nalyzer\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12H\n\x06inputs\x18\x03 \x03(\x0b\x32\x38.google.cloud.visionai.v1.AnalyzerDefinition.StreamInput\x12\x46\n\x05\x61ttrs\x18\x04 \x03(\x0b\x32\x37.google.cloud.visionai.v1.AnalyzerDefinition.AttrsEntry\x12P\n\rdebug_options\x18\x05 \x01(\x0b\x32\x39.google.cloud.visionai.v1.AnalyzerDefinition.DebugOptions\x1a\x1c\n\x0bStreamInput\x12\r\n\x05input\x18\x01 \x01(\t\x1a\xbf\x01\n\x0c\x44\x65\x62ugOptions\x12r\n\x15\x65nvironment_variables\x18\x01 \x03(\x0b\x32S.google.cloud.visionai.v1.AnalyzerDefinition.DebugOptions.EnvironmentVariablesEntry\x1a;\n\x19\x45nvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aV\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.google.cloud.visionai.v1.AttributeValue:\x02\x38\x01\"U\n\x12\x41nalysisDefinition\x12?\n\tanalyzers\x18\x01 \x03(\x0b\x32,.google.cloud.visionai.v1.AnalyzerDefinition\"\xbc\x01\n\tRunStatus\x12\x38\n\x05state\x18\x01 \x01(\x0e\x32).google.cloud.visionai.v1.RunStatus.State\x12\x0e\n\x06reason\x18\x02 \x01(\t\"e\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07PENDING\x10\x05*=\n\x07RunMode\x12\x18\n\x14RUN_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04LIVE\x10\x01\x12\x0e\n\nSUBMISSION\x10\x02\x42\xb8\x01\n\x1c\x63om.google.cloud.visionai.v1B\x08LvaProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visionai.python.protos.googleapis.v1.lva_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.google.cloud.visionai.v1B\010LvaProtoP\001Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\252\002\030Google.Cloud.VisionAI.V1\312\002\030Google\\Cloud\\VisionAI\\V1\352\002\033Google::Cloud::VisionAI::V1'
  _ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY._options = None
  _ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY._serialized_options = b'8\001'
  _ANALYZERDEFINITION_ATTRSENTRY._options = None
  _ANALYZERDEFINITION_ATTRSENTRY._serialized_options = b'8\001'
  _RUNMODE._serialized_start=1032
  _RUNMODE._serialized_end=1093
  _ATTRIBUTEVALUE._serialized_start=76
  _ATTRIBUTEVALUE._serialized_end=153
  _ANALYZERDEFINITION._serialized_start=156
  _ANALYZERDEFINITION._serialized_end=752
  _ANALYZERDEFINITION_STREAMINPUT._serialized_start=442
  _ANALYZERDEFINITION_STREAMINPUT._serialized_end=470
  _ANALYZERDEFINITION_DEBUGOPTIONS._serialized_start=473
  _ANALYZERDEFINITION_DEBUGOPTIONS._serialized_end=664
  _ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY._serialized_start=605
  _ANALYZERDEFINITION_DEBUGOPTIONS_ENVIRONMENTVARIABLESENTRY._serialized_end=664
  _ANALYZERDEFINITION_ATTRSENTRY._serialized_start=666
  _ANALYZERDEFINITION_ATTRSENTRY._serialized_end=752
  _ANALYSISDEFINITION._serialized_start=754
  _ANALYSISDEFINITION._serialized_end=839
  _RUNSTATUS._serialized_start=842
  _RUNSTATUS._serialized_end=1030
  _RUNSTATUS_STATE._serialized_start=929
  _RUNSTATUS_STATE._serialized_end=1030
# @@protoc_insertion_point(module_scope)
