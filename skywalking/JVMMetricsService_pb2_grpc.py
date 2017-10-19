# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Downstream_pb2 as Downstream__pb2
import JVMMetricsService_pb2 as JVMMetricsService__pb2


class JVMMetricsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.collect = channel.unary_unary(
        '/JVMMetricsService/collect',
        request_serializer=JVMMetricsService__pb2.JVMMetrics.SerializeToString,
        response_deserializer=Downstream__pb2.Downstream.FromString,
        )


class JVMMetricsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def collect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JVMMetricsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'collect': grpc.unary_unary_rpc_method_handler(
          servicer.collect,
          request_deserializer=JVMMetricsService__pb2.JVMMetrics.FromString,
          response_serializer=Downstream__pb2.Downstream.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'JVMMetricsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))