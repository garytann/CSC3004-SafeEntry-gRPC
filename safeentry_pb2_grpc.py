# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import safeentry_pb2 as safeentry__pb2


class SafeEntryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckIn = channel.unary_unary(
                '/SafeEntry/CheckIn',
                request_serializer=safeentry__pb2.CheckInRequest.SerializeToString,
                response_deserializer=safeentry__pb2.CheckInOutReply.FromString,
                )
        self.CheckOut = channel.unary_unary(
                '/SafeEntry/CheckOut',
                request_serializer=safeentry__pb2.CheckOutRequest.SerializeToString,
                response_deserializer=safeentry__pb2.CheckInOutReply.FromString,
                )
        self.CheckInGroup = channel.unary_unary(
                '/SafeEntry/CheckInGroup',
                request_serializer=safeentry__pb2.GroupInRequest.SerializeToString,
                response_deserializer=safeentry__pb2.CheckInOutReply.FromString,
                )
        self.CheckOutGroup = channel.unary_unary(
                '/SafeEntry/CheckOutGroup',
                request_serializer=safeentry__pb2.GroupOutRequest.SerializeToString,
                response_deserializer=safeentry__pb2.CheckInOutReply.FromString,
                )
        self.LocationHistory = channel.unary_unary(
                '/SafeEntry/LocationHistory',
                request_serializer=safeentry__pb2.HistoryRequest.SerializeToString,
                response_deserializer=safeentry__pb2.HistoryReply.FromString,
                )
        self.CheckCases = channel.unary_unary(
                '/SafeEntry/CheckCases',
                request_serializer=safeentry__pb2.LocationCheck.SerializeToString,
                response_deserializer=safeentry__pb2.LocationReply.FromString,
                )
        self.FlagLocation = channel.unary_unary(
                '/SafeEntry/FlagLocation',
                request_serializer=safeentry__pb2.FlagRequest.SerializeToString,
                response_deserializer=safeentry__pb2.FlagReply.FromString,
                )


class SafeEntryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckInGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckOutGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LocationHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckCases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FlagLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SafeEntryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckIn': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckIn,
                    request_deserializer=safeentry__pb2.CheckInRequest.FromString,
                    response_serializer=safeentry__pb2.CheckInOutReply.SerializeToString,
            ),
            'CheckOut': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckOut,
                    request_deserializer=safeentry__pb2.CheckOutRequest.FromString,
                    response_serializer=safeentry__pb2.CheckInOutReply.SerializeToString,
            ),
            'CheckInGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckInGroup,
                    request_deserializer=safeentry__pb2.GroupInRequest.FromString,
                    response_serializer=safeentry__pb2.CheckInOutReply.SerializeToString,
            ),
            'CheckOutGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckOutGroup,
                    request_deserializer=safeentry__pb2.GroupOutRequest.FromString,
                    response_serializer=safeentry__pb2.CheckInOutReply.SerializeToString,
            ),
            'LocationHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.LocationHistory,
                    request_deserializer=safeentry__pb2.HistoryRequest.FromString,
                    response_serializer=safeentry__pb2.HistoryReply.SerializeToString,
            ),
            'CheckCases': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckCases,
                    request_deserializer=safeentry__pb2.LocationCheck.FromString,
                    response_serializer=safeentry__pb2.LocationReply.SerializeToString,
            ),
            'FlagLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.FlagLocation,
                    request_deserializer=safeentry__pb2.FlagRequest.FromString,
                    response_serializer=safeentry__pb2.FlagReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SafeEntry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SafeEntry(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry/CheckIn',
            safeentry__pb2.CheckInRequest.SerializeToString,
            safeentry__pb2.CheckInOutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry/CheckOut',
            safeentry__pb2.CheckOutRequest.SerializeToString,
            safeentry__pb2.CheckInOutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckInGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry/CheckInGroup',
            safeentry__pb2.GroupInRequest.SerializeToString,
            safeentry__pb2.CheckInOutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckOutGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry/CheckOutGroup',
            safeentry__pb2.GroupOutRequest.SerializeToString,
            safeentry__pb2.CheckInOutReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LocationHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry/LocationHistory',
            safeentry__pb2.HistoryRequest.SerializeToString,
            safeentry__pb2.HistoryReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckCases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry/CheckCases',
            safeentry__pb2.LocationCheck.SerializeToString,
            safeentry__pb2.LocationReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FlagLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry/FlagLocation',
            safeentry__pb2.FlagRequest.SerializeToString,
            safeentry__pb2.FlagReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
