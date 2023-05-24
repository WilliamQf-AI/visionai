# Copyright (c) 2023 Google LLC All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from visionai.python.protos.googleapis.v1 import streaming_service_pb2 as visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2


class StreamingServiceStub(object):
    """Streaming service for receiving and sending packets.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendPackets = channel.stream_stream(
                '/google.cloud.visionai.v1.StreamingService/SendPackets',
                request_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.SendPacketsRequest.SerializeToString,
                response_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.SendPacketsResponse.FromString,
                )
        self.ReceivePackets = channel.stream_stream(
                '/google.cloud.visionai.v1.StreamingService/ReceivePackets',
                request_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceivePacketsRequest.SerializeToString,
                response_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceivePacketsResponse.FromString,
                )
        self.ReceiveEvents = channel.stream_stream(
                '/google.cloud.visionai.v1.StreamingService/ReceiveEvents',
                request_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceiveEventsRequest.SerializeToString,
                response_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceiveEventsResponse.FromString,
                )
        self.AcquireLease = channel.unary_unary(
                '/google.cloud.visionai.v1.StreamingService/AcquireLease',
                request_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.AcquireLeaseRequest.SerializeToString,
                response_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.Lease.FromString,
                )
        self.RenewLease = channel.unary_unary(
                '/google.cloud.visionai.v1.StreamingService/RenewLease',
                request_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.RenewLeaseRequest.SerializeToString,
                response_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.Lease.FromString,
                )
        self.ReleaseLease = channel.unary_unary(
                '/google.cloud.visionai.v1.StreamingService/ReleaseLease',
                request_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReleaseLeaseRequest.SerializeToString,
                response_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReleaseLeaseResponse.FromString,
                )


class StreamingServiceServicer(object):
    """Streaming service for receiving and sending packets.
    """

    def SendPackets(self, request_iterator, context):
        """Send packets to the series.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceivePackets(self, request_iterator, context):
        """Receive packets from the series.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveEvents(self, request_iterator, context):
        """Receive events given the stream name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcquireLease(self, request, context):
        """AcquireLease acquires a lease.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenewLease(self, request, context):
        """RenewLease renews a lease.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseLease(self, request, context):
        """RleaseLease releases a lease.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendPackets': grpc.stream_stream_rpc_method_handler(
                    servicer.SendPackets,
                    request_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.SendPacketsRequest.FromString,
                    response_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.SendPacketsResponse.SerializeToString,
            ),
            'ReceivePackets': grpc.stream_stream_rpc_method_handler(
                    servicer.ReceivePackets,
                    request_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceivePacketsRequest.FromString,
                    response_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceivePacketsResponse.SerializeToString,
            ),
            'ReceiveEvents': grpc.stream_stream_rpc_method_handler(
                    servicer.ReceiveEvents,
                    request_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceiveEventsRequest.FromString,
                    response_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceiveEventsResponse.SerializeToString,
            ),
            'AcquireLease': grpc.unary_unary_rpc_method_handler(
                    servicer.AcquireLease,
                    request_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.AcquireLeaseRequest.FromString,
                    response_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.Lease.SerializeToString,
            ),
            'RenewLease': grpc.unary_unary_rpc_method_handler(
                    servicer.RenewLease,
                    request_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.RenewLeaseRequest.FromString,
                    response_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.Lease.SerializeToString,
            ),
            'ReleaseLease': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseLease,
                    request_deserializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReleaseLeaseRequest.FromString,
                    response_serializer=visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReleaseLeaseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.cloud.visionai.v1.StreamingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamingService(object):
    """Streaming service for receiving and sending packets.
    """

    @staticmethod
    def SendPackets(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.cloud.visionai.v1.StreamingService/SendPackets',
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.SendPacketsRequest.SerializeToString,
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.SendPacketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceivePackets(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.cloud.visionai.v1.StreamingService/ReceivePackets',
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceivePacketsRequest.SerializeToString,
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceivePacketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveEvents(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.cloud.visionai.v1.StreamingService/ReceiveEvents',
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceiveEventsRequest.SerializeToString,
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReceiveEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcquireLease(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.StreamingService/AcquireLease',
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.AcquireLeaseRequest.SerializeToString,
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.Lease.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RenewLease(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.StreamingService/RenewLease',
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.RenewLeaseRequest.SerializeToString,
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.Lease.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReleaseLease(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.StreamingService/ReleaseLease',
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReleaseLeaseRequest.SerializeToString,
            visionai_dot_python_dot_protos_dot_googleapis_dot_v1_dot_streaming__service__pb2.ReleaseLeaseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
