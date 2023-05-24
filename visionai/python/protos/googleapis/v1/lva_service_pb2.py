# Copyright (c) 2023 Google LLC All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visionai/python/protos/googleapis/v1/lva_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from visionai.python.protos.googleapis.v1 import common_pb2 as visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_common__pb2
from visionai.python.protos.googleapis.v1 import lva_resources_pb2 as visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_lva__resources__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6visionai/python/protos/googleapis/v1/lva_service.proto\x12\x18google.cloud.visionai.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x31visionai/python/protos/googleapis/v1/common.proto\x1a\x38visionai/python/protos/googleapis/v1/lva_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\"\x97\x01\n\x13ListAnalysesRequest\x12\x37\n\x06parent\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"z\n\x14ListAnalysesResponse\x12\x34\n\x08\x61nalyses\x18\x01 \x03(\x0b\x32\".google.cloud.visionai.v1.Analysis\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t\"L\n\x12GetAnalysisRequest\x12\x36\n\x04name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n visionai.googleapis.com/Analysis\"\xbe\x01\n\x15\x43reateAnalysisRequest\x12\x37\n\x06parent\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fvisionai.googleapis.com/Cluster\x12\x18\n\x0b\x61nalysis_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x39\n\x08\x61nalysis\x18\x03 \x01(\x0b\x32\".google.cloud.visionai.v1.AnalysisB\x03\xe0\x41\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0\x41\x01\"\xa1\x01\n\x15UpdateAnalysisRequest\x12\x34\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02\x12\x39\n\x08\x61nalysis\x18\x02 \x01(\x0b\x32\".google.cloud.visionai.v1.AnalysisB\x03\xe0\x41\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0\x41\x01\"h\n\x15\x44\x65leteAnalysisRequest\x12\x36\n\x04name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n visionai.googleapis.com/Analysis\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0\x41\x01\"\x98\x01\n\x14ListProcessesRequest\x12\x37\n\x06parent\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fvisionai.googleapis.com/Cluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\"{\n\x15ListProcessesResponse\x12\x34\n\tprocesses\x18\x01 \x03(\x0b\x32!.google.cloud.visionai.v1.Process\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t\"J\n\x11GetProcessRequest\x12\x35\n\x04name\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fvisionai.googleapis.com/Process\"\xba\x01\n\x14\x43reateProcessRequest\x12\x37\n\x06parent\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fvisionai.googleapis.com/Cluster\x12\x17\n\nprocess_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x37\n\x07process\x18\x03 \x01(\x0b\x32!.google.cloud.visionai.v1.ProcessB\x03\xe0\x41\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0\x41\x01\"\x9e\x01\n\x14UpdateProcessRequest\x12\x34\n\x0bupdate_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02\x12\x37\n\x07process\x18\x02 \x01(\x0b\x32!.google.cloud.visionai.v1.ProcessB\x03\xe0\x41\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0\x41\x01\"f\n\x14\x44\x65leteProcessRequest\x12\x35\n\x04name\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fvisionai.googleapis.com/Process\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0\x41\x01\"\xd1\x02\n\x16\x42\x61tchRunProcessRequest\x12\x37\n\x06parent\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fvisionai.googleapis.com/Cluster\x12\x45\n\x08requests\x18\x02 \x03(\x0b\x32..google.cloud.visionai.v1.CreateProcessRequestB\x03\xe0\x41\x02\x12]\n\x07options\x18\x03 \x01(\x0b\x32G.google.cloud.visionai.v1.BatchRunProcessRequest.BatchRunProcessOptionsB\x03\xe0\x41\x01\x12\x15\n\x08\x62\x61tch_id\x18\x04 \x01(\tB\x03\xe0\x41\x03\x1a\x41\n\x16\x42\x61tchRunProcessOptions\x12\x13\n\x0bretry_count\x18\x01 \x01(\x05\x12\x12\n\nbatch_size\x18\x02 \x01(\x05\"a\n\x17\x42\x61tchRunProcessResponse\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\x12\x34\n\tprocesses\x18\x02 \x03(\x0b\x32!.google.cloud.visionai.v1.Process2\xfd\x12\n\x12LiveVideoAnalytics\x12\xb7\x01\n\x0cListAnalyses\x12-.google.cloud.visionai.v1.ListAnalysesRequest\x1a..google.cloud.visionai.v1.ListAnalysesResponse\"H\x82\xd3\xe4\x93\x02\x39\x12\x37/v1/{parent=projects/*/locations/*/clusters/*}/analyses\xda\x41\x06parent\x12\xa7\x01\n\x0bGetAnalysis\x12,.google.cloud.visionai.v1.GetAnalysisRequest\x1a\".google.cloud.visionai.v1.Analysis\"F\x82\xd3\xe4\x93\x02\x39\x12\x37/v1/{name=projects/*/locations/*/clusters/*/analyses/*}\xda\x41\x04name\x12\xea\x01\n\x0e\x43reateAnalysis\x12/.google.cloud.visionai.v1.CreateAnalysisRequest\x1a\x1d.google.longrunning.Operation\"\x87\x01\x82\xd3\xe4\x93\x02\x43\"7/v1/{parent=projects/*/locations/*/clusters/*}/analyses:\x08\x61nalysis\xda\x41\x1bparent,analysis,analysis_id\xca\x41\x1d\n\x08\x41nalysis\x12\x11OperationMetadata\x12\xec\x01\n\x0eUpdateAnalysis\x12/.google.cloud.visionai.v1.UpdateAnalysisRequest\x1a\x1d.google.longrunning.Operation\"\x89\x01\x82\xd3\xe4\x93\x02L2@/v1/{analysis.name=projects/*/locations/*/clusters/*/analyses/*}:\x08\x61nalysis\xda\x41\x14\x61nalysis,update_mask\xca\x41\x1d\n\x08\x41nalysis\x12\x11OperationMetadata\x12\xd5\x01\n\x0e\x44\x65leteAnalysis\x12/.google.cloud.visionai.v1.DeleteAnalysisRequest\x1a\x1d.google.longrunning.Operation\"s\x82\xd3\xe4\x93\x02\x39*7/v1/{name=projects/*/locations/*/clusters/*/analyses/*}\xda\x41\x04name\xca\x41*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x12\xbb\x01\n\rListProcesses\x12..google.cloud.visionai.v1.ListProcessesRequest\x1a/.google.cloud.visionai.v1.ListProcessesResponse\"I\x82\xd3\xe4\x93\x02:\x12\x38/v1/{parent=projects/*/locations/*/clusters/*}/processes\xda\x41\x06parent\x12\xa5\x01\n\nGetProcess\x12+.google.cloud.visionai.v1.GetProcessRequest\x1a!.google.cloud.visionai.v1.Process\"G\x82\xd3\xe4\x93\x02:\x12\x38/v1/{name=projects/*/locations/*/clusters/*/processes/*}\xda\x41\x04name\x12\xe5\x01\n\rCreateProcess\x12..google.cloud.visionai.v1.CreateProcessRequest\x1a\x1d.google.longrunning.Operation\"\x84\x01\x82\xd3\xe4\x93\x02\x43\"8/v1/{parent=projects/*/locations/*/clusters/*}/processes:\x07process\xda\x41\x19parent,process,process_id\xca\x41\x1c\n\x07Process\x12\x11OperationMetadata\x12\xe7\x01\n\rUpdateProcess\x12..google.cloud.visionai.v1.UpdateProcessRequest\x1a\x1d.google.longrunning.Operation\"\x86\x01\x82\xd3\xe4\x93\x02K2@/v1/{process.name=projects/*/locations/*/clusters/*/processes/*}:\x07process\xda\x41\x13process,update_mask\xca\x41\x1c\n\x07Process\x12\x11OperationMetadata\x12\xd4\x01\n\rDeleteProcess\x12..google.cloud.visionai.v1.DeleteProcessRequest\x1a\x1d.google.longrunning.Operation\"t\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/clusters/*/processes/*}\xda\x41\x04name\xca\x41*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x12\xf2\x01\n\x0f\x42\x61tchRunProcess\x12\x30.google.cloud.visionai.v1.BatchRunProcessRequest\x1a\x1d.google.longrunning.Operation\"\x8d\x01\x82\xd3\xe4\x93\x02\x46\"A/v1/{parent=projects/*/locations/*/clusters/*}/processes:batchRun:\x01*\xda\x41\x0fparent,requests\xca\x41,\n\x17\x42\x61tchRunProcessResponse\x12\x11OperationMetadata\x1aK\xca\x41\x17visionai.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xbf\x01\n\x1c\x63om.google.cloud.visionai.v1B\x0fLvaServiceProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visionai.python.protos.googleapis.v1.lva_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.google.cloud.visionai.v1B\017LvaServiceProtoP\001Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\252\002\030Google.Cloud.VisionAI.V1\312\002\030Google\\Cloud\\VisionAI\\V1\352\002\033Google::Cloud::VisionAI::V1'
  _LISTANALYSESREQUEST.fields_by_name['parent']._options = None
  _LISTANALYSESREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A!\n\037visionai.googleapis.com/Cluster'
  _GETANALYSISREQUEST.fields_by_name['name']._options = None
  _GETANALYSISREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\"\n visionai.googleapis.com/Analysis'
  _CREATEANALYSISREQUEST.fields_by_name['parent']._options = None
  _CREATEANALYSISREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A!\n\037visionai.googleapis.com/Cluster'
  _CREATEANALYSISREQUEST.fields_by_name['analysis_id']._options = None
  _CREATEANALYSISREQUEST.fields_by_name['analysis_id']._serialized_options = b'\340A\002'
  _CREATEANALYSISREQUEST.fields_by_name['analysis']._options = None
  _CREATEANALYSISREQUEST.fields_by_name['analysis']._serialized_options = b'\340A\002'
  _CREATEANALYSISREQUEST.fields_by_name['request_id']._options = None
  _CREATEANALYSISREQUEST.fields_by_name['request_id']._serialized_options = b'\340A\001'
  _UPDATEANALYSISREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEANALYSISREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\002'
  _UPDATEANALYSISREQUEST.fields_by_name['analysis']._options = None
  _UPDATEANALYSISREQUEST.fields_by_name['analysis']._serialized_options = b'\340A\002'
  _UPDATEANALYSISREQUEST.fields_by_name['request_id']._options = None
  _UPDATEANALYSISREQUEST.fields_by_name['request_id']._serialized_options = b'\340A\001'
  _DELETEANALYSISREQUEST.fields_by_name['name']._options = None
  _DELETEANALYSISREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\"\n visionai.googleapis.com/Analysis'
  _DELETEANALYSISREQUEST.fields_by_name['request_id']._options = None
  _DELETEANALYSISREQUEST.fields_by_name['request_id']._serialized_options = b'\340A\001'
  _LISTPROCESSESREQUEST.fields_by_name['parent']._options = None
  _LISTPROCESSESREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A!\n\037visionai.googleapis.com/Cluster'
  _GETPROCESSREQUEST.fields_by_name['name']._options = None
  _GETPROCESSREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A!\n\037visionai.googleapis.com/Process'
  _CREATEPROCESSREQUEST.fields_by_name['parent']._options = None
  _CREATEPROCESSREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A!\n\037visionai.googleapis.com/Cluster'
  _CREATEPROCESSREQUEST.fields_by_name['process_id']._options = None
  _CREATEPROCESSREQUEST.fields_by_name['process_id']._serialized_options = b'\340A\002'
  _CREATEPROCESSREQUEST.fields_by_name['process']._options = None
  _CREATEPROCESSREQUEST.fields_by_name['process']._serialized_options = b'\340A\002'
  _CREATEPROCESSREQUEST.fields_by_name['request_id']._options = None
  _CREATEPROCESSREQUEST.fields_by_name['request_id']._serialized_options = b'\340A\001'
  _UPDATEPROCESSREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEPROCESSREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\002'
  _UPDATEPROCESSREQUEST.fields_by_name['process']._options = None
  _UPDATEPROCESSREQUEST.fields_by_name['process']._serialized_options = b'\340A\002'
  _UPDATEPROCESSREQUEST.fields_by_name['request_id']._options = None
  _UPDATEPROCESSREQUEST.fields_by_name['request_id']._serialized_options = b'\340A\001'
  _DELETEPROCESSREQUEST.fields_by_name['name']._options = None
  _DELETEPROCESSREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A!\n\037visionai.googleapis.com/Process'
  _DELETEPROCESSREQUEST.fields_by_name['request_id']._options = None
  _DELETEPROCESSREQUEST.fields_by_name['request_id']._serialized_options = b'\340A\001'
  _BATCHRUNPROCESSREQUEST.fields_by_name['parent']._options = None
  _BATCHRUNPROCESSREQUEST.fields_by_name['parent']._serialized_options = b'\340A\002\372A!\n\037visionai.googleapis.com/Cluster'
  _BATCHRUNPROCESSREQUEST.fields_by_name['requests']._options = None
  _BATCHRUNPROCESSREQUEST.fields_by_name['requests']._serialized_options = b'\340A\002'
  _BATCHRUNPROCESSREQUEST.fields_by_name['options']._options = None
  _BATCHRUNPROCESSREQUEST.fields_by_name['options']._serialized_options = b'\340A\001'
  _BATCHRUNPROCESSREQUEST.fields_by_name['batch_id']._options = None
  _BATCHRUNPROCESSREQUEST.fields_by_name['batch_id']._serialized_options = b'\340A\003'
  _LIVEVIDEOANALYTICS._options = None
  _LIVEVIDEOANALYTICS._serialized_options = b'\312A\027visionai.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _LIVEVIDEOANALYTICS.methods_by_name['ListAnalyses']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['ListAnalyses']._serialized_options = b'\202\323\344\223\0029\0227/v1/{parent=projects/*/locations/*/clusters/*}/analyses\332A\006parent'
  _LIVEVIDEOANALYTICS.methods_by_name['GetAnalysis']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['GetAnalysis']._serialized_options = b'\202\323\344\223\0029\0227/v1/{name=projects/*/locations/*/clusters/*/analyses/*}\332A\004name'
  _LIVEVIDEOANALYTICS.methods_by_name['CreateAnalysis']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['CreateAnalysis']._serialized_options = b'\202\323\344\223\002C\"7/v1/{parent=projects/*/locations/*/clusters/*}/analyses:\010analysis\332A\033parent,analysis,analysis_id\312A\035\n\010Analysis\022\021OperationMetadata'
  _LIVEVIDEOANALYTICS.methods_by_name['UpdateAnalysis']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['UpdateAnalysis']._serialized_options = b'\202\323\344\223\002L2@/v1/{analysis.name=projects/*/locations/*/clusters/*/analyses/*}:\010analysis\332A\024analysis,update_mask\312A\035\n\010Analysis\022\021OperationMetadata'
  _LIVEVIDEOANALYTICS.methods_by_name['DeleteAnalysis']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['DeleteAnalysis']._serialized_options = b'\202\323\344\223\0029*7/v1/{name=projects/*/locations/*/clusters/*/analyses/*}\332A\004name\312A*\n\025google.protobuf.Empty\022\021OperationMetadata'
  _LIVEVIDEOANALYTICS.methods_by_name['ListProcesses']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['ListProcesses']._serialized_options = b'\202\323\344\223\002:\0228/v1/{parent=projects/*/locations/*/clusters/*}/processes\332A\006parent'
  _LIVEVIDEOANALYTICS.methods_by_name['GetProcess']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['GetProcess']._serialized_options = b'\202\323\344\223\002:\0228/v1/{name=projects/*/locations/*/clusters/*/processes/*}\332A\004name'
  _LIVEVIDEOANALYTICS.methods_by_name['CreateProcess']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['CreateProcess']._serialized_options = b'\202\323\344\223\002C\"8/v1/{parent=projects/*/locations/*/clusters/*}/processes:\007process\332A\031parent,process,process_id\312A\034\n\007Process\022\021OperationMetadata'
  _LIVEVIDEOANALYTICS.methods_by_name['UpdateProcess']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['UpdateProcess']._serialized_options = b'\202\323\344\223\002K2@/v1/{process.name=projects/*/locations/*/clusters/*/processes/*}:\007process\332A\023process,update_mask\312A\034\n\007Process\022\021OperationMetadata'
  _LIVEVIDEOANALYTICS.methods_by_name['DeleteProcess']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['DeleteProcess']._serialized_options = b'\202\323\344\223\002:*8/v1/{name=projects/*/locations/*/clusters/*/processes/*}\332A\004name\312A*\n\025google.protobuf.Empty\022\021OperationMetadata'
  _LIVEVIDEOANALYTICS.methods_by_name['BatchRunProcess']._options = None
  _LIVEVIDEOANALYTICS.methods_by_name['BatchRunProcess']._serialized_options = b'\202\323\344\223\002F\"A/v1/{parent=projects/*/locations/*/clusters/*}/processes:batchRun:\001*\332A\017parent,requests\312A,\n\027BatchRunProcessResponse\022\021OperationMetadata'
  _LISTANALYSESREQUEST._serialized_start=409
  _LISTANALYSESREQUEST._serialized_end=560
  _LISTANALYSESRESPONSE._serialized_start=562
  _LISTANALYSESRESPONSE._serialized_end=684
  _GETANALYSISREQUEST._serialized_start=686
  _GETANALYSISREQUEST._serialized_end=762
  _CREATEANALYSISREQUEST._serialized_start=765
  _CREATEANALYSISREQUEST._serialized_end=955
  _UPDATEANALYSISREQUEST._serialized_start=958
  _UPDATEANALYSISREQUEST._serialized_end=1119
  _DELETEANALYSISREQUEST._serialized_start=1121
  _DELETEANALYSISREQUEST._serialized_end=1225
  _LISTPROCESSESREQUEST._serialized_start=1228
  _LISTPROCESSESREQUEST._serialized_end=1380
  _LISTPROCESSESRESPONSE._serialized_start=1382
  _LISTPROCESSESRESPONSE._serialized_end=1505
  _GETPROCESSREQUEST._serialized_start=1507
  _GETPROCESSREQUEST._serialized_end=1581
  _CREATEPROCESSREQUEST._serialized_start=1584
  _CREATEPROCESSREQUEST._serialized_end=1770
  _UPDATEPROCESSREQUEST._serialized_start=1773
  _UPDATEPROCESSREQUEST._serialized_end=1931
  _DELETEPROCESSREQUEST._serialized_start=1933
  _DELETEPROCESSREQUEST._serialized_end=2035
  _BATCHRUNPROCESSREQUEST._serialized_start=2038
  _BATCHRUNPROCESSREQUEST._serialized_end=2375
  _BATCHRUNPROCESSREQUEST_BATCHRUNPROCESSOPTIONS._serialized_start=2310
  _BATCHRUNPROCESSREQUEST_BATCHRUNPROCESSOPTIONS._serialized_end=2375
  _BATCHRUNPROCESSRESPONSE._serialized_start=2377
  _BATCHRUNPROCESSRESPONSE._serialized_end=2474
  _LIVEVIDEOANALYTICS._serialized_start=2477
  _LIVEVIDEOANALYTICS._serialized_end=4906
# @@protoc_insertion_point(module_scope)
