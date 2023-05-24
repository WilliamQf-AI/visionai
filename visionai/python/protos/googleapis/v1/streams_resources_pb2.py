# Copyright (c) 2023 Google LLC All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visionai/python/protos/googleapis/v1/streams_resources.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<visionai/python/protos/googleapis/v1/streams_resources.proto\x12\x18google.cloud.visionai.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xaf\x04\n\x06Stream\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x34\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12<\n\x06labels\x18\x04 \x03(\x0b\x32,.google.cloud.visionai.v1.Stream.LabelsEntry\x12\x46\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32\x31.google.cloud.visionai.v1.Stream.AnnotationsEntry\x12\x14\n\x0c\x64isplay_name\x18\x06 \x01(\t\x12\x1b\n\x13\x65nable_hls_playback\x18\x07 \x01(\x08\x12\x1d\n\x15media_warehouse_asset\x18\x08 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:p\xea\x41m\n\x1evisionai.googleapis.com/Stream\x12Kprojects/{project}/locations/{location}/clusters/{cluster}/streams/{stream}\"\x81\x05\n\x05\x45vent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x34\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12;\n\x06labels\x18\x04 \x03(\x0b\x32+.google.cloud.visionai.v1.Event.LabelsEntry\x12\x45\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32\x30.google.cloud.visionai.v1.Event.AnnotationsEntry\x12>\n\x0f\x61lignment_clock\x18\x06 \x01(\x0e\x32%.google.cloud.visionai.v1.Event.Clock\x12/\n\x0cgrace_period\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n\x05\x43lock\x12\x15\n\x11\x43LOCK_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x43\x41PTURE\x10\x01\x12\n\n\x06INGEST\x10\x02:m\xea\x41j\n\x1dvisionai.googleapis.com/Event\x12Iprojects/{project}/locations/{location}/clusters/{cluster}/events/{event}\"\xca\x04\n\x06Series\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x34\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12<\n\x06labels\x18\x04 \x03(\x0b\x32,.google.cloud.visionai.v1.Series.LabelsEntry\x12\x46\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32\x31.google.cloud.visionai.v1.Series.AnnotationsEntry\x12\x36\n\x06stream\x18\x06 \x01(\tB&\xe0\x41\x02\xfa\x41 \n\x1evisionai.googleapis.com/Stream\x12\x34\n\x05\x65vent\x18\x07 \x01(\tB%\xe0\x41\x02\xfa\x41\x1f\n\x1dvisionai.googleapis.com/Event\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:o\xea\x41l\n\x1evisionai.googleapis.com/Series\x12Jprojects/{project}/locations/{location}/clusters/{cluster}/series/{series}\"\xd1\x04\n\x07\x43hannel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12\x34\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03\x12=\n\x06labels\x18\x04 \x03(\x0b\x32-.google.cloud.visionai.v1.Channel.LabelsEntry\x12G\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32\x32.google.cloud.visionai.v1.Channel.AnnotationsEntry\x12\x36\n\x06stream\x18\x06 \x01(\tB&\xe0\x41\x02\xfa\x41 \n\x1evisionai.googleapis.com/Stream\x12\x34\n\x05\x65vent\x18\x07 \x01(\tB%\xe0\x41\x02\xfa\x41\x1f\n\x1dvisionai.googleapis.com/Event\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:s\xea\x41p\n\x1fvisionai.googleapis.com/Channel\x12Mprojects/{project}/locations/{location}/clusters/{cluster}/channels/{channel}B\xc5\x01\n\x1c\x63om.google.cloud.visionai.v1B\x15StreamsResourcesProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visionai.python.protos.googleapis.v1.streams_resources_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.google.cloud.visionai.v1B\025StreamsResourcesProtoP\001Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\252\002\030Google.Cloud.VisionAI.V1\312\002\030Google\\Cloud\\VisionAI\\V1\352\002\033Google::Cloud::VisionAI::V1'
  _STREAM_LABELSENTRY._options = None
  _STREAM_LABELSENTRY._serialized_options = b'8\001'
  _STREAM_ANNOTATIONSENTRY._options = None
  _STREAM_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _STREAM.fields_by_name['create_time']._options = None
  _STREAM.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _STREAM.fields_by_name['update_time']._options = None
  _STREAM.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _STREAM._options = None
  _STREAM._serialized_options = b'\352Am\n\036visionai.googleapis.com/Stream\022Kprojects/{project}/locations/{location}/clusters/{cluster}/streams/{stream}'
  _EVENT_LABELSENTRY._options = None
  _EVENT_LABELSENTRY._serialized_options = b'8\001'
  _EVENT_ANNOTATIONSENTRY._options = None
  _EVENT_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _EVENT.fields_by_name['create_time']._options = None
  _EVENT.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _EVENT.fields_by_name['update_time']._options = None
  _EVENT.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _EVENT._options = None
  _EVENT._serialized_options = b'\352Aj\n\035visionai.googleapis.com/Event\022Iprojects/{project}/locations/{location}/clusters/{cluster}/events/{event}'
  _SERIES_LABELSENTRY._options = None
  _SERIES_LABELSENTRY._serialized_options = b'8\001'
  _SERIES_ANNOTATIONSENTRY._options = None
  _SERIES_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _SERIES.fields_by_name['create_time']._options = None
  _SERIES.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _SERIES.fields_by_name['update_time']._options = None
  _SERIES.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _SERIES.fields_by_name['stream']._options = None
  _SERIES.fields_by_name['stream']._serialized_options = b'\340A\002\372A \n\036visionai.googleapis.com/Stream'
  _SERIES.fields_by_name['event']._options = None
  _SERIES.fields_by_name['event']._serialized_options = b'\340A\002\372A\037\n\035visionai.googleapis.com/Event'
  _SERIES._options = None
  _SERIES._serialized_options = b'\352Al\n\036visionai.googleapis.com/Series\022Jprojects/{project}/locations/{location}/clusters/{cluster}/series/{series}'
  _CHANNEL_LABELSENTRY._options = None
  _CHANNEL_LABELSENTRY._serialized_options = b'8\001'
  _CHANNEL_ANNOTATIONSENTRY._options = None
  _CHANNEL_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _CHANNEL.fields_by_name['create_time']._options = None
  _CHANNEL.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _CHANNEL.fields_by_name['update_time']._options = None
  _CHANNEL.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _CHANNEL.fields_by_name['stream']._options = None
  _CHANNEL.fields_by_name['stream']._serialized_options = b'\340A\002\372A \n\036visionai.googleapis.com/Stream'
  _CHANNEL.fields_by_name['event']._options = None
  _CHANNEL.fields_by_name['event']._serialized_options = b'\340A\002\372A\037\n\035visionai.googleapis.com/Event'
  _CHANNEL._options = None
  _CHANNEL._serialized_options = b'\352Ap\n\037visionai.googleapis.com/Channel\022Mprojects/{project}/locations/{location}/clusters/{cluster}/channels/{channel}'
  _STREAM._serialized_start=216
  _STREAM._serialized_end=775
  _STREAM_LABELSENTRY._serialized_start=564
  _STREAM_LABELSENTRY._serialized_end=609
  _STREAM_ANNOTATIONSENTRY._serialized_start=611
  _STREAM_ANNOTATIONSENTRY._serialized_end=661
  _EVENT._serialized_start=778
  _EVENT._serialized_end=1419
  _EVENT_LABELSENTRY._serialized_start=564
  _EVENT_LABELSENTRY._serialized_end=609
  _EVENT_ANNOTATIONSENTRY._serialized_start=611
  _EVENT_ANNOTATIONSENTRY._serialized_end=661
  _EVENT_CLOCK._serialized_start=1253
  _EVENT_CLOCK._serialized_end=1308
  _SERIES._serialized_start=1422
  _SERIES._serialized_end=2008
  _SERIES_LABELSENTRY._serialized_start=564
  _SERIES_LABELSENTRY._serialized_end=609
  _SERIES_ANNOTATIONSENTRY._serialized_start=611
  _SERIES_ANNOTATIONSENTRY._serialized_end=661
  _CHANNEL._serialized_start=2011
  _CHANNEL._serialized_end=2604
  _CHANNEL_LABELSENTRY._serialized_start=564
  _CHANNEL_LABELSENTRY._serialized_end=609
  _CHANNEL_ANNOTATIONSENTRY._serialized_start=611
  _CHANNEL_ANNOTATIONSENTRY._serialized_end=661
# @@protoc_insertion_point(module_scope)
