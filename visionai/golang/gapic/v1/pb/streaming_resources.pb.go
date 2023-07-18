// Copyright 2023 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.30.0
// 	protoc        v3.21.12
// source: google/cloud/visionai/v1/streaming_resources.proto

package visionaipb

import (
	_ "google3/google/api/annotations_go_proto"
	protoreflect "google3/third_party/golang/protobuf/v2/reflect/protoreflect/protoreflect"
	protoimpl "google3/third_party/golang/protobuf/v2/runtime/protoimpl/protoimpl"
	durationpb "google3/google/protobuf/duration_go_proto"
	structpb "google3/google/protobuf/struct_go_proto"
	timestamppb "google3/google/protobuf/timestamp_go_proto"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// The descriptor for a gstreamer buffer payload.
type GstreamerBufferDescriptor struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The caps string of the payload.
	CapsString string `protobuf:"bytes,1,opt,name=caps_string,json=capsString,proto3" json:"caps_string,omitempty"`
	// Whether the buffer is a key frame.
	IsKeyFrame bool `protobuf:"varint,2,opt,name=is_key_frame,json=isKeyFrame,proto3" json:"is_key_frame,omitempty"`
	// PTS of the frame.
	PtsTime *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=pts_time,json=ptsTime,proto3" json:"pts_time,omitempty"`
	// DTS of the frame.
	DtsTime *timestamppb.Timestamp `protobuf:"bytes,4,opt,name=dts_time,json=dtsTime,proto3" json:"dts_time,omitempty"`
	// Duration of the frame.
	Duration *durationpb.Duration `protobuf:"bytes,5,opt,name=duration,proto3" json:"duration,omitempty"`
}

func (x *GstreamerBufferDescriptor) Reset() {
	*x = GstreamerBufferDescriptor{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GstreamerBufferDescriptor) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GstreamerBufferDescriptor) ProtoMessage() {}

func (x *GstreamerBufferDescriptor) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GstreamerBufferDescriptor.ProtoReflect.Descriptor instead.
func (*GstreamerBufferDescriptor) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{0}
}

func (x *GstreamerBufferDescriptor) GetCapsString() string {
	if x != nil {
		return x.CapsString
	}
	return ""
}

func (x *GstreamerBufferDescriptor) GetIsKeyFrame() bool {
	if x != nil {
		return x.IsKeyFrame
	}
	return false
}

func (x *GstreamerBufferDescriptor) GetPtsTime() *timestamppb.Timestamp {
	if x != nil {
		return x.PtsTime
	}
	return nil
}

func (x *GstreamerBufferDescriptor) GetDtsTime() *timestamppb.Timestamp {
	if x != nil {
		return x.DtsTime
	}
	return nil
}

func (x *GstreamerBufferDescriptor) GetDuration() *durationpb.Duration {
	if x != nil {
		return x.Duration
	}
	return nil
}

// The descriptor for a raw image.
type RawImageDescriptor struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Raw image format. Its possible values are: "srgb".
	Format string `protobuf:"bytes,1,opt,name=format,proto3" json:"format,omitempty"`
	// The height of the image.
	Height int32 `protobuf:"varint,2,opt,name=height,proto3" json:"height,omitempty"`
	// The width of the image.
	Width int32 `protobuf:"varint,3,opt,name=width,proto3" json:"width,omitempty"`
}

func (x *RawImageDescriptor) Reset() {
	*x = RawImageDescriptor{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RawImageDescriptor) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RawImageDescriptor) ProtoMessage() {}

func (x *RawImageDescriptor) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RawImageDescriptor.ProtoReflect.Descriptor instead.
func (*RawImageDescriptor) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{1}
}

func (x *RawImageDescriptor) GetFormat() string {
	if x != nil {
		return x.Format
	}
	return ""
}

func (x *RawImageDescriptor) GetHeight() int32 {
	if x != nil {
		return x.Height
	}
	return 0
}

func (x *RawImageDescriptor) GetWidth() int32 {
	if x != nil {
		return x.Width
	}
	return 0
}

// The message that represents the data type of a packet.
type PacketType struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The type class of the packet. Its possible values are:
	// "gst", "protobuf", and "string".
	TypeClass string `protobuf:"bytes,1,opt,name=type_class,json=typeClass,proto3" json:"type_class,omitempty"`
	// The type descriptor.
	TypeDescriptor *PacketType_TypeDescriptor `protobuf:"bytes,2,opt,name=type_descriptor,json=typeDescriptor,proto3" json:"type_descriptor,omitempty"`
}

func (x *PacketType) Reset() {
	*x = PacketType{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PacketType) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PacketType) ProtoMessage() {}

func (x *PacketType) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PacketType.ProtoReflect.Descriptor instead.
func (*PacketType) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{2}
}

func (x *PacketType) GetTypeClass() string {
	if x != nil {
		return x.TypeClass
	}
	return ""
}

func (x *PacketType) GetTypeDescriptor() *PacketType_TypeDescriptor {
	if x != nil {
		return x.TypeDescriptor
	}
	return nil
}

// The message that represents server metadata.
type ServerMetadata struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The offset position for the packet in its stream.
	Offset int64 `protobuf:"varint,1,opt,name=offset,proto3" json:"offset,omitempty"`
	// The timestamp at which the stream server receives this packet. This is
	// based on the local clock of on the server side. It is guaranteed to be
	// monotonically increasing for the packets within each session; however
	// this timestamp is not comparable across packets sent to the same stream
	// different sessions. Session here refers to one individual gRPC streaming
	// request to the stream server.
	IngestTime *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=ingest_time,json=ingestTime,proto3" json:"ingest_time,omitempty"`
}

func (x *ServerMetadata) Reset() {
	*x = ServerMetadata{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ServerMetadata) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ServerMetadata) ProtoMessage() {}

func (x *ServerMetadata) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ServerMetadata.ProtoReflect.Descriptor instead.
func (*ServerMetadata) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{3}
}

func (x *ServerMetadata) GetOffset() int64 {
	if x != nil {
		return x.Offset
	}
	return 0
}

func (x *ServerMetadata) GetIngestTime() *timestamppb.Timestamp {
	if x != nil {
		return x.IngestTime
	}
	return nil
}

// The message that represents series metadata.
type SeriesMetadata struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Series name. It's in the format of
	// "projects/{project}/locations/{location}/clusters/{cluster}/series/{stream}".
	Series string `protobuf:"bytes,1,opt,name=series,proto3" json:"series,omitempty"`
}

func (x *SeriesMetadata) Reset() {
	*x = SeriesMetadata{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SeriesMetadata) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SeriesMetadata) ProtoMessage() {}

func (x *SeriesMetadata) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SeriesMetadata.ProtoReflect.Descriptor instead.
func (*SeriesMetadata) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{4}
}

func (x *SeriesMetadata) GetSeries() string {
	if x != nil {
		return x.Series
	}
	return ""
}

// The message that represents packet header.
type PacketHeader struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Input only. The capture time of the packet.
	CaptureTime *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=capture_time,json=captureTime,proto3" json:"capture_time,omitempty"`
	// Input only. Immutable. The type of the payload.
	Type *PacketType `protobuf:"bytes,2,opt,name=type,proto3" json:"type,omitempty"`
	// Input only. This field is for users to attach user managed metadata.
	Metadata *structpb.Struct `protobuf:"bytes,3,opt,name=metadata,proto3" json:"metadata,omitempty"`
	// Output only. Metadata that the server appends to each packet before sending
	// it to receivers. You don't need to set a value for this field when sending
	// packets.
	ServerMetadata *ServerMetadata `protobuf:"bytes,4,opt,name=server_metadata,json=serverMetadata,proto3" json:"server_metadata,omitempty"`
	// Input only. Immutable. Metadata that the server needs to know where to
	// write the packets to. It's only required for the first packet.
	SeriesMetadata *SeriesMetadata `protobuf:"bytes,5,opt,name=series_metadata,json=seriesMetadata,proto3" json:"series_metadata,omitempty"`
	// Immutable. Packet flag set. SDK will set the flag automatically.
	Flags int32 `protobuf:"varint,6,opt,name=flags,proto3" json:"flags,omitempty"`
	// Immutable. Header string for tracing across services. It should be set when
	// the packet is first arrived in the stream server.
	//
	// The input format is a lowercase hex string:
	//   - version_id: 1 byte, currently must be zero - hex encoded (2 characters)
	//   - trace_id: 16 bytes (opaque blob) - hex encoded (32 characters)
	//   - span_id: 8 bytes (opaque blob) - hex encoded (16 characters)
	//   - trace_options: 1 byte (LSB means tracing enabled) - hex encoded (2
	//   characters)
	// Example: "00-404142434445464748494a4b4c4d4e4f-6162636465666768-01"
	//           v  trace_id                         span_id          options
	TraceContext string `protobuf:"bytes,7,opt,name=trace_context,json=traceContext,proto3" json:"trace_context,omitempty"`
}

func (x *PacketHeader) Reset() {
	*x = PacketHeader{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PacketHeader) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PacketHeader) ProtoMessage() {}

func (x *PacketHeader) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PacketHeader.ProtoReflect.Descriptor instead.
func (*PacketHeader) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{5}
}

func (x *PacketHeader) GetCaptureTime() *timestamppb.Timestamp {
	if x != nil {
		return x.CaptureTime
	}
	return nil
}

func (x *PacketHeader) GetType() *PacketType {
	if x != nil {
		return x.Type
	}
	return nil
}

func (x *PacketHeader) GetMetadata() *structpb.Struct {
	if x != nil {
		return x.Metadata
	}
	return nil
}

func (x *PacketHeader) GetServerMetadata() *ServerMetadata {
	if x != nil {
		return x.ServerMetadata
	}
	return nil
}

func (x *PacketHeader) GetSeriesMetadata() *SeriesMetadata {
	if x != nil {
		return x.SeriesMetadata
	}
	return nil
}

func (x *PacketHeader) GetFlags() int32 {
	if x != nil {
		return x.Flags
	}
	return 0
}

func (x *PacketHeader) GetTraceContext() string {
	if x != nil {
		return x.TraceContext
	}
	return ""
}

// The quanta of datum that the series accepts.
type Packet struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The packet header.
	Header *PacketHeader `protobuf:"bytes,1,opt,name=header,proto3" json:"header,omitempty"`
	// The payload of the packet.
	Payload []byte `protobuf:"bytes,2,opt,name=payload,proto3" json:"payload,omitempty"`
}

func (x *Packet) Reset() {
	*x = Packet{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Packet) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Packet) ProtoMessage() {}

func (x *Packet) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Packet.ProtoReflect.Descriptor instead.
func (*Packet) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{6}
}

func (x *Packet) GetHeader() *PacketHeader {
	if x != nil {
		return x.Header
	}
	return nil
}

func (x *Packet) GetPayload() []byte {
	if x != nil {
		return x.Payload
	}
	return nil
}

// The message that fully specifies the type of the packet.
type PacketType_TypeDescriptor struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Detailed information about the type.
	//
	// It is non-empty only for specific type class codecs. Needed only when the
	// type string alone is not enough to disambiguate the specific type.
	//
	// Types that are assignable to TypeDetails:
	//	*PacketType_TypeDescriptor_GstreamerBufferDescriptor
	//	*PacketType_TypeDescriptor_RawImageDescriptor
	TypeDetails isPacketType_TypeDescriptor_TypeDetails `protobuf_oneof:"type_details"`
	// The type of the packet. Its possible values is codec dependent.
	//
	// The fully qualified type name is always the concatenation of the
	// value in `type_class` together with the value in `type`, separated by a
	// '/'.
	//
	// Note that specific codecs can define their own type hierarchy, and so the
	// type string here can in fact be separated by multiple '/'s of its own.
	//
	// Please see the open source SDK for specific codec documentation.
	Type string `protobuf:"bytes,1,opt,name=type,proto3" json:"type,omitempty"`
}

func (x *PacketType_TypeDescriptor) Reset() {
	*x = PacketType_TypeDescriptor{}
	if protoimpl.UnsafeEnabled {
		mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PacketType_TypeDescriptor) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PacketType_TypeDescriptor) ProtoMessage() {}

func (x *PacketType_TypeDescriptor) ProtoReflect() protoreflect.Message {
	mi := &file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PacketType_TypeDescriptor.ProtoReflect.Descriptor instead.
func (*PacketType_TypeDescriptor) Descriptor() ([]byte, []int) {
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP(), []int{2, 0}
}

func (m *PacketType_TypeDescriptor) GetTypeDetails() isPacketType_TypeDescriptor_TypeDetails {
	if m != nil {
		return m.TypeDetails
	}
	return nil
}

func (x *PacketType_TypeDescriptor) GetGstreamerBufferDescriptor() *GstreamerBufferDescriptor {
	if x, ok := x.GetTypeDetails().(*PacketType_TypeDescriptor_GstreamerBufferDescriptor); ok {
		return x.GstreamerBufferDescriptor
	}
	return nil
}

func (x *PacketType_TypeDescriptor) GetRawImageDescriptor() *RawImageDescriptor {
	if x, ok := x.GetTypeDetails().(*PacketType_TypeDescriptor_RawImageDescriptor); ok {
		return x.RawImageDescriptor
	}
	return nil
}

func (x *PacketType_TypeDescriptor) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

type isPacketType_TypeDescriptor_TypeDetails interface {
	isPacketType_TypeDescriptor_TypeDetails()
}

type PacketType_TypeDescriptor_GstreamerBufferDescriptor struct {
	// GstreamerBufferDescriptor is the descriptor for gstreamer buffer type.
	GstreamerBufferDescriptor *GstreamerBufferDescriptor `protobuf:"bytes,2,opt,name=gstreamer_buffer_descriptor,json=gstreamerBufferDescriptor,proto3,oneof"`
}

type PacketType_TypeDescriptor_RawImageDescriptor struct {
	// RawImageDescriptor is the descriptor for the raw image type.
	RawImageDescriptor *RawImageDescriptor `protobuf:"bytes,3,opt,name=raw_image_descriptor,json=rawImageDescriptor,proto3,oneof"`
}

func (*PacketType_TypeDescriptor_GstreamerBufferDescriptor) isPacketType_TypeDescriptor_TypeDetails() {
}

func (*PacketType_TypeDescriptor_RawImageDescriptor) isPacketType_TypeDescriptor_TypeDetails() {}

var File_google_cloud_visionai_v1_streaming_resources_proto protoreflect.FileDescriptor

var file_google_cloud_visionai_v1_streaming_resources_proto_rawDesc = []byte{
	0x0a, 0x32, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2f, 0x76,
	0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x73, 0x74, 0x72, 0x65, 0x61,
	0x6d, 0x69, 0x6e, 0x67, 0x5f, 0x72, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x73, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x18, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f,
	0x75, 0x64, 0x2e, 0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x1a, 0x1f,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x66, 0x69, 0x65, 0x6c, 0x64,
	0x5f, 0x62, 0x65, 0x68, 0x61, 0x76, 0x69, 0x6f, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x19, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x72, 0x65, 0x73, 0x6f,
	0x75, 0x72, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x64, 0x75, 0x72, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x72, 0x75,
	0x63, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74,
	0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x83, 0x02, 0x0a, 0x19, 0x47, 0x73,
	0x74, 0x72, 0x65, 0x61, 0x6d, 0x65, 0x72, 0x42, 0x75, 0x66, 0x66, 0x65, 0x72, 0x44, 0x65, 0x73,
	0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x12, 0x1f, 0x0a, 0x0b, 0x63, 0x61, 0x70, 0x73, 0x5f,
	0x73, 0x74, 0x72, 0x69, 0x6e, 0x67, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x63, 0x61,
	0x70, 0x73, 0x53, 0x74, 0x72, 0x69, 0x6e, 0x67, 0x12, 0x20, 0x0a, 0x0c, 0x69, 0x73, 0x5f, 0x6b,
	0x65, 0x79, 0x5f, 0x66, 0x72, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x08, 0x52, 0x0a,
	0x69, 0x73, 0x4b, 0x65, 0x79, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x12, 0x35, 0x0a, 0x08, 0x70, 0x74,
	0x73, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67,
	0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54,
	0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x07, 0x70, 0x74, 0x73, 0x54, 0x69, 0x6d,
	0x65, 0x12, 0x35, 0x0a, 0x08, 0x64, 0x74, 0x73, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52,
	0x07, 0x64, 0x74, 0x73, 0x54, 0x69, 0x6d, 0x65, 0x12, 0x35, 0x0a, 0x08, 0x64, 0x75, 0x72, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x19, 0x2e, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x44, 0x75, 0x72,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x08, 0x64, 0x75, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x22,
	0x5a, 0x0a, 0x12, 0x52, 0x61, 0x77, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x44, 0x65, 0x73, 0x63, 0x72,
	0x69, 0x70, 0x74, 0x6f, 0x72, 0x12, 0x16, 0x0a, 0x06, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x12, 0x16, 0x0a,
	0x06, 0x68, 0x65, 0x69, 0x67, 0x68, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x06, 0x68,
	0x65, 0x69, 0x67, 0x68, 0x74, 0x12, 0x14, 0x0a, 0x05, 0x77, 0x69, 0x64, 0x74, 0x68, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x05, 0x77, 0x69, 0x64, 0x74, 0x68, 0x22, 0x99, 0x03, 0x0a, 0x0a,
	0x50, 0x61, 0x63, 0x6b, 0x65, 0x74, 0x54, 0x79, 0x70, 0x65, 0x12, 0x1d, 0x0a, 0x0a, 0x74, 0x79,
	0x70, 0x65, 0x5f, 0x63, 0x6c, 0x61, 0x73, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09,
	0x74, 0x79, 0x70, 0x65, 0x43, 0x6c, 0x61, 0x73, 0x73, 0x12, 0x5c, 0x0a, 0x0f, 0x74, 0x79, 0x70,
	0x65, 0x5f, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x33, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f, 0x75,
	0x64, 0x2e, 0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x50, 0x61,
	0x63, 0x6b, 0x65, 0x74, 0x54, 0x79, 0x70, 0x65, 0x2e, 0x54, 0x79, 0x70, 0x65, 0x44, 0x65, 0x73,
	0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x52, 0x0e, 0x74, 0x79, 0x70, 0x65, 0x44, 0x65, 0x73,
	0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x1a, 0x8d, 0x02, 0x0a, 0x0e, 0x54, 0x79, 0x70, 0x65,
	0x44, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x12, 0x75, 0x0a, 0x1b, 0x67, 0x73,
	0x74, 0x72, 0x65, 0x61, 0x6d, 0x65, 0x72, 0x5f, 0x62, 0x75, 0x66, 0x66, 0x65, 0x72, 0x5f, 0x64,
	0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x33, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x76,
	0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x73, 0x74, 0x72, 0x65,
	0x61, 0x6d, 0x65, 0x72, 0x42, 0x75, 0x66, 0x66, 0x65, 0x72, 0x44, 0x65, 0x73, 0x63, 0x72, 0x69,
	0x70, 0x74, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x19, 0x67, 0x73, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x65,
	0x72, 0x42, 0x75, 0x66, 0x66, 0x65, 0x72, 0x44, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f,
	0x72, 0x12, 0x60, 0x0a, 0x14, 0x72, 0x61, 0x77, 0x5f, 0x69, 0x6d, 0x61, 0x67, 0x65, 0x5f, 0x64,
	0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x2c, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x76,
	0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x61, 0x77, 0x49, 0x6d,
	0x61, 0x67, 0x65, 0x44, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x48, 0x00, 0x52,
	0x12, 0x72, 0x61, 0x77, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x44, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70,
	0x74, 0x6f, 0x72, 0x12, 0x12, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x04, 0x74, 0x79, 0x70, 0x65, 0x42, 0x0e, 0x0a, 0x0c, 0x74, 0x79, 0x70, 0x65, 0x5f,
	0x64, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x22, 0x65, 0x0a, 0x0e, 0x53, 0x65, 0x72, 0x76, 0x65,
	0x72, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x16, 0x0a, 0x06, 0x6f, 0x66, 0x66,
	0x73, 0x65, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x06, 0x6f, 0x66, 0x66, 0x73, 0x65,
	0x74, 0x12, 0x3b, 0x0a, 0x0b, 0x69, 0x6e, 0x67, 0x65, 0x73, 0x74, 0x5f, 0x74, 0x69, 0x6d, 0x65,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61,
	0x6d, 0x70, 0x52, 0x0a, 0x69, 0x6e, 0x67, 0x65, 0x73, 0x74, 0x54, 0x69, 0x6d, 0x65, 0x22, 0x4d,
	0x0a, 0x0e, 0x53, 0x65, 0x72, 0x69, 0x65, 0x73, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61,
	0x12, 0x3b, 0x0a, 0x06, 0x73, 0x65, 0x72, 0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x42, 0x23, 0xfa, 0x41, 0x20, 0x0a, 0x1e, 0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x61, 0x70, 0x69, 0x73, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x53,
	0x65, 0x72, 0x69, 0x65, 0x73, 0x52, 0x06, 0x73, 0x65, 0x72, 0x69, 0x65, 0x73, 0x22, 0xc6, 0x03,
	0x0a, 0x0c, 0x50, 0x61, 0x63, 0x6b, 0x65, 0x74, 0x48, 0x65, 0x61, 0x64, 0x65, 0x72, 0x12, 0x42,
	0x0a, 0x0c, 0x63, 0x61, 0x70, 0x74, 0x75, 0x72, 0x65, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70,
	0x42, 0x03, 0xe0, 0x41, 0x04, 0x52, 0x0b, 0x63, 0x61, 0x70, 0x74, 0x75, 0x72, 0x65, 0x54, 0x69,
	0x6d, 0x65, 0x12, 0x40, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x24, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e,
	0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x50, 0x61, 0x63, 0x6b,
	0x65, 0x74, 0x54, 0x79, 0x70, 0x65, 0x42, 0x06, 0xe0, 0x41, 0x04, 0xe0, 0x41, 0x05, 0x52, 0x04,
	0x74, 0x79, 0x70, 0x65, 0x12, 0x38, 0x0a, 0x08, 0x6d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61,
	0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x42,
	0x03, 0xe0, 0x41, 0x04, 0x52, 0x08, 0x6d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x56,
	0x0a, 0x0f, 0x73, 0x65, 0x72, 0x76, 0x65, 0x72, 0x5f, 0x6d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74,
	0x61, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x28, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e,
	0x76, 0x31, 0x2e, 0x53, 0x65, 0x72, 0x76, 0x65, 0x72, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74,
	0x61, 0x42, 0x03, 0xe0, 0x41, 0x03, 0x52, 0x0e, 0x73, 0x65, 0x72, 0x76, 0x65, 0x72, 0x4d, 0x65,
	0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x12, 0x59, 0x0a, 0x0f, 0x73, 0x65, 0x72, 0x69, 0x65, 0x73,
	0x5f, 0x6d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x28, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x76,
	0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x65, 0x72, 0x69, 0x65,
	0x73, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x42, 0x06, 0xe0, 0x41, 0x04, 0xe0, 0x41,
	0x05, 0x52, 0x0e, 0x73, 0x65, 0x72, 0x69, 0x65, 0x73, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74,
	0x61, 0x12, 0x19, 0x0a, 0x05, 0x66, 0x6c, 0x61, 0x67, 0x73, 0x18, 0x06, 0x20, 0x01, 0x28, 0x05,
	0x42, 0x03, 0xe0, 0x41, 0x05, 0x52, 0x05, 0x66, 0x6c, 0x61, 0x67, 0x73, 0x12, 0x28, 0x0a, 0x0d,
	0x74, 0x72, 0x61, 0x63, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x18, 0x07, 0x20,
	0x01, 0x28, 0x09, 0x42, 0x03, 0xe0, 0x41, 0x05, 0x52, 0x0c, 0x74, 0x72, 0x61, 0x63, 0x65, 0x43,
	0x6f, 0x6e, 0x74, 0x65, 0x78, 0x74, 0x22, 0x62, 0x0a, 0x06, 0x50, 0x61, 0x63, 0x6b, 0x65, 0x74,
	0x12, 0x3e, 0x0a, 0x06, 0x68, 0x65, 0x61, 0x64, 0x65, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x26, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e,
	0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x50, 0x61, 0x63, 0x6b,
	0x65, 0x74, 0x48, 0x65, 0x61, 0x64, 0x65, 0x72, 0x52, 0x06, 0x68, 0x65, 0x61, 0x64, 0x65, 0x72,
	0x12, 0x18, 0x0a, 0x07, 0x70, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x0c, 0x52, 0x07, 0x70, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x42, 0xc7, 0x01, 0x0a, 0x1c, 0x63,
	0x6f, 0x6d, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e,
	0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x2e, 0x76, 0x31, 0x42, 0x17, 0x53, 0x74, 0x72,
	0x65, 0x61, 0x6d, 0x69, 0x6e, 0x67, 0x52, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x73, 0x50,
	0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x38, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x2e, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x67, 0x6f, 0x2f, 0x76, 0x69, 0x73, 0x69,
	0x6f, 0x6e, 0x61, 0x69, 0x2f, 0x61, 0x70, 0x69, 0x76, 0x31, 0x2f, 0x76, 0x69, 0x73, 0x69, 0x6f,
	0x6e, 0x61, 0x69, 0x70, 0x62, 0x3b, 0x76, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x61, 0x69, 0x70, 0x62,
	0xaa, 0x02, 0x18, 0x47, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x2e,
	0x56, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x41, 0x49, 0x2e, 0x56, 0x31, 0xca, 0x02, 0x18, 0x47, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x5c, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x5c, 0x56, 0x69, 0x73, 0x69, 0x6f,
	0x6e, 0x41, 0x49, 0x5c, 0x56, 0x31, 0xea, 0x02, 0x1b, 0x47, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x3a,
	0x3a, 0x43, 0x6c, 0x6f, 0x75, 0x64, 0x3a, 0x3a, 0x56, 0x69, 0x73, 0x69, 0x6f, 0x6e, 0x41, 0x49,
	0x3a, 0x3a, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_google_cloud_visionai_v1_streaming_resources_proto_rawDescOnce sync.Once
	file_google_cloud_visionai_v1_streaming_resources_proto_rawDescData = file_google_cloud_visionai_v1_streaming_resources_proto_rawDesc
)

func file_google_cloud_visionai_v1_streaming_resources_proto_rawDescGZIP() []byte {
	file_google_cloud_visionai_v1_streaming_resources_proto_rawDescOnce.Do(func() {
		file_google_cloud_visionai_v1_streaming_resources_proto_rawDescData = protoimpl.X.CompressGZIP(file_google_cloud_visionai_v1_streaming_resources_proto_rawDescData)
	})
	return file_google_cloud_visionai_v1_streaming_resources_proto_rawDescData
}

var file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_google_cloud_visionai_v1_streaming_resources_proto_goTypes = []interface{}{
	(*GstreamerBufferDescriptor)(nil), // 0: google.cloud.visionai.v1.GstreamerBufferDescriptor
	(*RawImageDescriptor)(nil),        // 1: google.cloud.visionai.v1.RawImageDescriptor
	(*PacketType)(nil),                // 2: google.cloud.visionai.v1.PacketType
	(*ServerMetadata)(nil),            // 3: google.cloud.visionai.v1.ServerMetadata
	(*SeriesMetadata)(nil),            // 4: google.cloud.visionai.v1.SeriesMetadata
	(*PacketHeader)(nil),              // 5: google.cloud.visionai.v1.PacketHeader
	(*Packet)(nil),                    // 6: google.cloud.visionai.v1.Packet
	(*PacketType_TypeDescriptor)(nil), // 7: google.cloud.visionai.v1.PacketType.TypeDescriptor
	(*timestamppb.Timestamp)(nil),     // 8: google.protobuf.Timestamp
	(*durationpb.Duration)(nil),       // 9: google.protobuf.Duration
	(*structpb.Struct)(nil),           // 10: google.protobuf.Struct
}
var file_google_cloud_visionai_v1_streaming_resources_proto_depIdxs = []int32{
	8,  // 0: google.cloud.visionai.v1.GstreamerBufferDescriptor.pts_time:type_name -> google.protobuf.Timestamp
	8,  // 1: google.cloud.visionai.v1.GstreamerBufferDescriptor.dts_time:type_name -> google.protobuf.Timestamp
	9,  // 2: google.cloud.visionai.v1.GstreamerBufferDescriptor.duration:type_name -> google.protobuf.Duration
	7,  // 3: google.cloud.visionai.v1.PacketType.type_descriptor:type_name -> google.cloud.visionai.v1.PacketType.TypeDescriptor
	8,  // 4: google.cloud.visionai.v1.ServerMetadata.ingest_time:type_name -> google.protobuf.Timestamp
	8,  // 5: google.cloud.visionai.v1.PacketHeader.capture_time:type_name -> google.protobuf.Timestamp
	2,  // 6: google.cloud.visionai.v1.PacketHeader.type:type_name -> google.cloud.visionai.v1.PacketType
	10, // 7: google.cloud.visionai.v1.PacketHeader.metadata:type_name -> google.protobuf.Struct
	3,  // 8: google.cloud.visionai.v1.PacketHeader.server_metadata:type_name -> google.cloud.visionai.v1.ServerMetadata
	4,  // 9: google.cloud.visionai.v1.PacketHeader.series_metadata:type_name -> google.cloud.visionai.v1.SeriesMetadata
	5,  // 10: google.cloud.visionai.v1.Packet.header:type_name -> google.cloud.visionai.v1.PacketHeader
	0,  // 11: google.cloud.visionai.v1.PacketType.TypeDescriptor.gstreamer_buffer_descriptor:type_name -> google.cloud.visionai.v1.GstreamerBufferDescriptor
	1,  // 12: google.cloud.visionai.v1.PacketType.TypeDescriptor.raw_image_descriptor:type_name -> google.cloud.visionai.v1.RawImageDescriptor
	13, // [13:13] is the sub-list for method output_type
	13, // [13:13] is the sub-list for method input_type
	13, // [13:13] is the sub-list for extension type_name
	13, // [13:13] is the sub-list for extension extendee
	0,  // [0:13] is the sub-list for field type_name
}

func init() { file_google_cloud_visionai_v1_streaming_resources_proto_init() }
func file_google_cloud_visionai_v1_streaming_resources_proto_init() {
	if File_google_cloud_visionai_v1_streaming_resources_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GstreamerBufferDescriptor); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RawImageDescriptor); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PacketType); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ServerMetadata); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SeriesMetadata); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PacketHeader); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Packet); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PacketType_TypeDescriptor); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes[7].OneofWrappers = []interface{}{
		(*PacketType_TypeDescriptor_GstreamerBufferDescriptor)(nil),
		(*PacketType_TypeDescriptor_RawImageDescriptor)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_google_cloud_visionai_v1_streaming_resources_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_google_cloud_visionai_v1_streaming_resources_proto_goTypes,
		DependencyIndexes: file_google_cloud_visionai_v1_streaming_resources_proto_depIdxs,
		MessageInfos:      file_google_cloud_visionai_v1_streaming_resources_proto_msgTypes,
	}.Build()
	File_google_cloud_visionai_v1_streaming_resources_proto = out.File
	file_google_cloud_visionai_v1_streaming_resources_proto_rawDesc = nil
	file_google_cloud_visionai_v1_streaming_resources_proto_goTypes = nil
	file_google_cloud_visionai_v1_streaming_resources_proto_depIdxs = nil
}
