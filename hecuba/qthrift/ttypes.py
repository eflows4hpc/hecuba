#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class BasicTypes:
  BIGINT = 0
  BLOB = 1
  BOOLEAN = 2
  DOUBLE = 3
  FLOAT = 4
  INET = 5
  INT = 6
  LIST = 7
  MAP = 8
  SET = 9
  TEXT = 10
  TIMESTAMP = 11
  TIMEUUID = 12
  UUID = 13
  DATE = 14
  TIME = 15
  DECIMAL = 16

  _VALUES_TO_NAMES = {
    0: "BIGINT",
    1: "BLOB",
    2: "BOOLEAN",
    3: "DOUBLE",
    4: "FLOAT",
    5: "INET",
    6: "INT",
    7: "LIST",
    8: "MAP",
    9: "SET",
    10: "TEXT",
    11: "TIMESTAMP",
    12: "TIMEUUID",
    13: "UUID",
    14: "DATE",
    15: "TIME",
    16: "DECIMAL",
  }

  _NAMES_TO_VALUES = {
    "BIGINT": 0,
    "BLOB": 1,
    "BOOLEAN": 2,
    "DOUBLE": 3,
    "FLOAT": 4,
    "INET": 5,
    "INT": 6,
    "LIST": 7,
    "MAP": 8,
    "SET": 9,
    "TEXT": 10,
    "TIMESTAMP": 11,
    "TIMEUUID": 12,
    "UUID": 13,
    "DATE": 14,
    "TIME": 15,
    "DECIMAL": 16,
  }


class FilteringArea:
  """
  Attributes:
   - fromPoint
   - toPoint
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'fromPoint', (TType.DOUBLE,None), None, ), # 1
    (2, TType.LIST, 'toPoint', (TType.DOUBLE,None), None, ), # 2
  )

  def __init__(self, fromPoint=None, toPoint=None,):
    self.fromPoint = fromPoint
    self.toPoint = toPoint

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.fromPoint = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readDouble()
            self.fromPoint.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.toPoint = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readDouble()
            self.toPoint.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FilteringArea')
    if self.fromPoint is not None:
      oprot.writeFieldBegin('fromPoint', TType.LIST, 1)
      oprot.writeListBegin(TType.DOUBLE, len(self.fromPoint))
      for iter12 in self.fromPoint:
        oprot.writeDouble(iter12)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.toPoint is not None:
      oprot.writeFieldBegin('toPoint', TType.LIST, 2)
      oprot.writeListBegin(TType.DOUBLE, len(self.toPoint))
      for iter13 in self.toPoint:
        oprot.writeDouble(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.fromPoint)
    value = (value * 31) ^ hash(self.toPoint)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class entryPoint:
  """
  Attributes:
   - blockid
   - hostname
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'blockid', None, None, ), # 1
    (2, TType.STRING, 'hostname', None, None, ), # 2
    (3, TType.I32, 'port', None, None, ), # 3
  )

  def __init__(self, blockid=None, hostname=None, port=None,):
    self.blockid = blockid
    self.hostname = hostname
    self.port = port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.blockid = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.hostname = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.port = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('entryPoint')
    if self.blockid is not None:
      oprot.writeFieldBegin('blockid', TType.STRING, 1)
      oprot.writeString(self.blockid)
      oprot.writeFieldEnd()
    if self.hostname is not None:
      oprot.writeFieldBegin('hostname', TType.STRING, 2)
      oprot.writeString(self.hostname)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 3)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.blockid)
    value = (value * 31) ^ hash(self.hostname)
    value = (value * 31) ^ hash(self.port)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ColumnMeta:
  """
  Attributes:
   - columnName
   - type
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'columnName', None, None, ), # 1
    (2, TType.I32, 'type', None, None, ), # 2
  )

  def __init__(self, columnName=None, type=None,):
    self.columnName = columnName
    self.type = type

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.columnName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.type = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ColumnMeta')
    if self.columnName is not None:
      oprot.writeFieldBegin('columnName', TType.STRING, 1)
      oprot.writeString(self.columnName)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 2)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.columnName)
    value = (value * 31) ^ hash(self.type)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Result:
  """
  Attributes:
   - hasMore
   - count
   - metadata
   - data
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'hasMore', None, None, ), # 1
    (2, TType.I32, 'count', None, None, ), # 2
    (3, TType.MAP, 'metadata', (TType.BYTE,None,TType.STRUCT,(ColumnMeta, ColumnMeta.thrift_spec)), None, ), # 3
    (4, TType.LIST, 'data', (TType.MAP,(TType.BYTE,None,TType.STRING,None)), None, ), # 4
  )

  def __init__(self, hasMore=None, count=None, metadata=None, data=None,):
    self.hasMore = hasMore
    self.count = count
    self.metadata = metadata
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.hasMore = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.count = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.metadata = {}
          (_ktype15, _vtype16, _size14 ) = iprot.readMapBegin()
          for _i18 in xrange(_size14):
            _key19 = iprot.readByte()
            _val20 = ColumnMeta()
            _val20.read(iprot)
            self.metadata[_key19] = _val20
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.data = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in xrange(_size21):
            _elem26 = {}
            (_ktype28, _vtype29, _size27 ) = iprot.readMapBegin()
            for _i31 in xrange(_size27):
              _key32 = iprot.readByte()
              _val33 = iprot.readString()
              _elem26[_key32] = _val33
            iprot.readMapEnd()
            self.data.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Result')
    if self.hasMore is not None:
      oprot.writeFieldBegin('hasMore', TType.BOOL, 1)
      oprot.writeBool(self.hasMore)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 2)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    if self.metadata is not None:
      oprot.writeFieldBegin('metadata', TType.MAP, 3)
      oprot.writeMapBegin(TType.BYTE, TType.STRUCT, len(self.metadata))
      for kiter34,viter35 in self.metadata.items():
        oprot.writeByte(kiter34)
        viter35.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.LIST, 4)
      oprot.writeListBegin(TType.MAP, len(self.data))
      for iter36 in self.data:
        oprot.writeMapBegin(TType.BYTE, TType.STRING, len(iter36))
        for kiter37,viter38 in iter36.items():
          oprot.writeByte(kiter37)
          oprot.writeString(viter38)
        oprot.writeMapEnd()
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.hasMore)
    value = (value * 31) ^ hash(self.count)
    value = (value * 31) ^ hash(self.metadata)
    value = (value * 31) ^ hash(self.data)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BlockNotFound(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BlockNotFound')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)