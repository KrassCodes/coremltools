# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FeatureTypes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='FeatureTypes.proto',
  package='CoreML.Specification',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x46\x65\x61tureTypes.proto\x12\x14\x43oreML.Specification\"\x12\n\x10Int64FeatureType\"\x13\n\x11\x44oubleFeatureType\"\x13\n\x11StringFeatureType\"3\n\tSizeRange\x12\x12\n\nlowerBound\x18\x01 \x01(\x04\x12\x12\n\nupperBound\x18\x02 \x01(\x03\"\x95\x05\n\x10ImageFeatureType\x12\r\n\x05width\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12V\n\x0f\x65numeratedSizes\x18\x15 \x01(\x0b\x32;.CoreML.Specification.ImageFeatureType.EnumeratedImageSizesH\x00\x12O\n\x0eimageSizeRange\x18\x1f \x01(\x0b\x32\x35.CoreML.Specification.ImageFeatureType.ImageSizeRangeH\x00\x12\x45\n\ncolorSpace\x18\x03 \x01(\x0e\x32\x31.CoreML.Specification.ImageFeatureType.ColorSpace\x1a*\n\tImageSize\x12\r\n\x05width\x18\x01 \x01(\x04\x12\x0e\n\x06height\x18\x02 \x01(\x04\x1aW\n\x14\x45numeratedImageSizes\x12?\n\x05sizes\x18\x01 \x03(\x0b\x32\x30.CoreML.Specification.ImageFeatureType.ImageSize\x1a{\n\x0eImageSizeRange\x12\x33\n\nwidthRange\x18\x01 \x01(\x0b\x32\x1f.CoreML.Specification.SizeRange\x12\x34\n\x0bheightRange\x18\x02 \x01(\x0b\x32\x1f.CoreML.Specification.SizeRange\"]\n\nColorSpace\x12\x17\n\x13INVALID_COLOR_SPACE\x10\x00\x12\r\n\tGRAYSCALE\x10\n\x12\x07\n\x03RGB\x10\x14\x12\x07\n\x03\x42GR\x10\x1e\x12\x15\n\x11GRAYSCALE_FLOAT16\x10(B\x11\n\x0fSizeFlexibility\"\x9d\x05\n\x10\x41rrayFeatureType\x12\r\n\x05shape\x18\x01 \x03(\x03\x12\x46\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\x34.CoreML.Specification.ArrayFeatureType.ArrayDataType\x12S\n\x10\x65numeratedShapes\x18\x15 \x01(\x0b\x32\x37.CoreML.Specification.ArrayFeatureType.EnumeratedShapesH\x00\x12G\n\nshapeRange\x18\x1f \x01(\x0b\x32\x31.CoreML.Specification.ArrayFeatureType.ShapeRangeH\x00\x12\x19\n\x0fintDefaultValue\x18) \x01(\x05H\x01\x12\x1b\n\x11\x66loatDefaultValue\x18\x33 \x01(\x02H\x01\x12\x1c\n\x12\x64oubleDefaultValue\x18= \x01(\x01H\x01\x1a\x16\n\x05Shape\x12\r\n\x05shape\x18\x01 \x03(\x03\x1aP\n\x10\x45numeratedShapes\x12<\n\x06shapes\x18\x01 \x03(\x0b\x32,.CoreML.Specification.ArrayFeatureType.Shape\x1a\x41\n\nShapeRange\x12\x33\n\nsizeRanges\x18\x01 \x03(\x0b\x32\x1f.CoreML.Specification.SizeRange\"e\n\rArrayDataType\x12\x1b\n\x17INVALID_ARRAY_DATA_TYPE\x10\x00\x12\r\n\x07\x46LOAT32\x10\xa0\x80\x04\x12\x0c\n\x06\x44OUBLE\x10\xc0\x80\x04\x12\x0b\n\x05INT32\x10\xa0\x80\x08\x12\r\n\x07\x46LOAT16\x10\x90\x80\x04\x42\x12\n\x10ShapeFlexibilityB\x16\n\x14\x64\x65\x66\x61ultOptionalValue\"\xa4\x01\n\x15\x44ictionaryFeatureType\x12>\n\x0cint64KeyType\x18\x01 \x01(\x0b\x32&.CoreML.Specification.Int64FeatureTypeH\x00\x12@\n\rstringKeyType\x18\x02 \x01(\x0b\x32\'.CoreML.Specification.StringFeatureTypeH\x00\x42\t\n\x07KeyType\"\xcd\x01\n\x13SequenceFeatureType\x12;\n\tint64Type\x18\x01 \x01(\x0b\x32&.CoreML.Specification.Int64FeatureTypeH\x00\x12=\n\nstringType\x18\x03 \x01(\x0b\x32\'.CoreML.Specification.StringFeatureTypeH\x00\x12\x32\n\tsizeRange\x18\x65 \x01(\x0b\x32\x1f.CoreML.Specification.SizeRangeB\x06\n\x04Type\"\xee\x03\n\x0b\x46\x65\x61tureType\x12;\n\tint64Type\x18\x01 \x01(\x0b\x32&.CoreML.Specification.Int64FeatureTypeH\x00\x12=\n\ndoubleType\x18\x02 \x01(\x0b\x32\'.CoreML.Specification.DoubleFeatureTypeH\x00\x12=\n\nstringType\x18\x03 \x01(\x0b\x32\'.CoreML.Specification.StringFeatureTypeH\x00\x12;\n\timageType\x18\x04 \x01(\x0b\x32&.CoreML.Specification.ImageFeatureTypeH\x00\x12@\n\x0emultiArrayType\x18\x05 \x01(\x0b\x32&.CoreML.Specification.ArrayFeatureTypeH\x00\x12\x45\n\x0e\x64ictionaryType\x18\x06 \x01(\x0b\x32+.CoreML.Specification.DictionaryFeatureTypeH\x00\x12\x41\n\x0csequenceType\x18\x07 \x01(\x0b\x32).CoreML.Specification.SequenceFeatureTypeH\x00\x12\x13\n\nisOptional\x18\xe8\x07 \x01(\x08\x42\x06\n\x04TypeB\x02H\x03\x62\x06proto3')
)



_IMAGEFEATURETYPE_COLORSPACE = _descriptor.EnumDescriptor(
  name='ColorSpace',
  full_name='CoreML.Specification.ImageFeatureType.ColorSpace',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_COLOR_SPACE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAYSCALE', index=1, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGB', index=2, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGR', index=3, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAYSCALE_FLOAT16', index=4, number=40,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=709,
  serialized_end=802,
)
_sym_db.RegisterEnumDescriptor(_IMAGEFEATURETYPE_COLORSPACE)

_ARRAYFEATURETYPE_ARRAYDATATYPE = _descriptor.EnumDescriptor(
  name='ArrayDataType',
  full_name='CoreML.Specification.ArrayFeatureType.ArrayDataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_ARRAY_DATA_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT32', index=1, number=65568,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=65600,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=3, number=131104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT16', index=4, number=65552,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1348,
  serialized_end=1449,
)
_sym_db.RegisterEnumDescriptor(_ARRAYFEATURETYPE_ARRAYDATATYPE)


_INT64FEATURETYPE = _descriptor.Descriptor(
  name='Int64FeatureType',
  full_name='CoreML.Specification.Int64FeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=62,
)


_DOUBLEFEATURETYPE = _descriptor.Descriptor(
  name='DoubleFeatureType',
  full_name='CoreML.Specification.DoubleFeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=83,
)


_STRINGFEATURETYPE = _descriptor.Descriptor(
  name='StringFeatureType',
  full_name='CoreML.Specification.StringFeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=104,
)


_SIZERANGE = _descriptor.Descriptor(
  name='SizeRange',
  full_name='CoreML.Specification.SizeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lowerBound', full_name='CoreML.Specification.SizeRange.lowerBound', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upperBound', full_name='CoreML.Specification.SizeRange.upperBound', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=157,
)


_IMAGEFEATURETYPE_IMAGESIZE = _descriptor.Descriptor(
  name='ImageSize',
  full_name='CoreML.Specification.ImageFeatureType.ImageSize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='CoreML.Specification.ImageFeatureType.ImageSize.width', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='CoreML.Specification.ImageFeatureType.ImageSize.height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=493,
)

_IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES = _descriptor.Descriptor(
  name='EnumeratedImageSizes',
  full_name='CoreML.Specification.ImageFeatureType.EnumeratedImageSizes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sizes', full_name='CoreML.Specification.ImageFeatureType.EnumeratedImageSizes.sizes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=582,
)

_IMAGEFEATURETYPE_IMAGESIZERANGE = _descriptor.Descriptor(
  name='ImageSizeRange',
  full_name='CoreML.Specification.ImageFeatureType.ImageSizeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='widthRange', full_name='CoreML.Specification.ImageFeatureType.ImageSizeRange.widthRange', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heightRange', full_name='CoreML.Specification.ImageFeatureType.ImageSizeRange.heightRange', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=584,
  serialized_end=707,
)

_IMAGEFEATURETYPE = _descriptor.Descriptor(
  name='ImageFeatureType',
  full_name='CoreML.Specification.ImageFeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='CoreML.Specification.ImageFeatureType.width', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='CoreML.Specification.ImageFeatureType.height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enumeratedSizes', full_name='CoreML.Specification.ImageFeatureType.enumeratedSizes', index=2,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageSizeRange', full_name='CoreML.Specification.ImageFeatureType.imageSizeRange', index=3,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='colorSpace', full_name='CoreML.Specification.ImageFeatureType.colorSpace', index=4,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_IMAGEFEATURETYPE_IMAGESIZE, _IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES, _IMAGEFEATURETYPE_IMAGESIZERANGE, ],
  enum_types=[
    _IMAGEFEATURETYPE_COLORSPACE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='SizeFlexibility', full_name='CoreML.Specification.ImageFeatureType.SizeFlexibility',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=160,
  serialized_end=821,
)


_ARRAYFEATURETYPE_SHAPE = _descriptor.Descriptor(
  name='Shape',
  full_name='CoreML.Specification.ArrayFeatureType.Shape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='CoreML.Specification.ArrayFeatureType.Shape.shape', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1175,
  serialized_end=1197,
)

_ARRAYFEATURETYPE_ENUMERATEDSHAPES = _descriptor.Descriptor(
  name='EnumeratedShapes',
  full_name='CoreML.Specification.ArrayFeatureType.EnumeratedShapes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shapes', full_name='CoreML.Specification.ArrayFeatureType.EnumeratedShapes.shapes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1199,
  serialized_end=1279,
)

_ARRAYFEATURETYPE_SHAPERANGE = _descriptor.Descriptor(
  name='ShapeRange',
  full_name='CoreML.Specification.ArrayFeatureType.ShapeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sizeRanges', full_name='CoreML.Specification.ArrayFeatureType.ShapeRange.sizeRanges', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1281,
  serialized_end=1346,
)

_ARRAYFEATURETYPE = _descriptor.Descriptor(
  name='ArrayFeatureType',
  full_name='CoreML.Specification.ArrayFeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='CoreML.Specification.ArrayFeatureType.shape', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='CoreML.Specification.ArrayFeatureType.dataType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enumeratedShapes', full_name='CoreML.Specification.ArrayFeatureType.enumeratedShapes', index=2,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shapeRange', full_name='CoreML.Specification.ArrayFeatureType.shapeRange', index=3,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intDefaultValue', full_name='CoreML.Specification.ArrayFeatureType.intDefaultValue', index=4,
      number=41, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='floatDefaultValue', full_name='CoreML.Specification.ArrayFeatureType.floatDefaultValue', index=5,
      number=51, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doubleDefaultValue', full_name='CoreML.Specification.ArrayFeatureType.doubleDefaultValue', index=6,
      number=61, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ARRAYFEATURETYPE_SHAPE, _ARRAYFEATURETYPE_ENUMERATEDSHAPES, _ARRAYFEATURETYPE_SHAPERANGE, ],
  enum_types=[
    _ARRAYFEATURETYPE_ARRAYDATATYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ShapeFlexibility', full_name='CoreML.Specification.ArrayFeatureType.ShapeFlexibility',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='defaultOptionalValue', full_name='CoreML.Specification.ArrayFeatureType.defaultOptionalValue',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=824,
  serialized_end=1493,
)


_DICTIONARYFEATURETYPE = _descriptor.Descriptor(
  name='DictionaryFeatureType',
  full_name='CoreML.Specification.DictionaryFeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int64KeyType', full_name='CoreML.Specification.DictionaryFeatureType.int64KeyType', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stringKeyType', full_name='CoreML.Specification.DictionaryFeatureType.stringKeyType', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='KeyType', full_name='CoreML.Specification.DictionaryFeatureType.KeyType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1496,
  serialized_end=1660,
)


_SEQUENCEFEATURETYPE = _descriptor.Descriptor(
  name='SequenceFeatureType',
  full_name='CoreML.Specification.SequenceFeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int64Type', full_name='CoreML.Specification.SequenceFeatureType.int64Type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stringType', full_name='CoreML.Specification.SequenceFeatureType.stringType', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sizeRange', full_name='CoreML.Specification.SequenceFeatureType.sizeRange', index=2,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='CoreML.Specification.SequenceFeatureType.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1663,
  serialized_end=1868,
)


_FEATURETYPE = _descriptor.Descriptor(
  name='FeatureType',
  full_name='CoreML.Specification.FeatureType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int64Type', full_name='CoreML.Specification.FeatureType.int64Type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doubleType', full_name='CoreML.Specification.FeatureType.doubleType', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stringType', full_name='CoreML.Specification.FeatureType.stringType', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageType', full_name='CoreML.Specification.FeatureType.imageType', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiArrayType', full_name='CoreML.Specification.FeatureType.multiArrayType', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dictionaryType', full_name='CoreML.Specification.FeatureType.dictionaryType', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequenceType', full_name='CoreML.Specification.FeatureType.sequenceType', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isOptional', full_name='CoreML.Specification.FeatureType.isOptional', index=7,
      number=1000, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='CoreML.Specification.FeatureType.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1871,
  serialized_end=2365,
)

_IMAGEFEATURETYPE_IMAGESIZE.containing_type = _IMAGEFEATURETYPE
_IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES.fields_by_name['sizes'].message_type = _IMAGEFEATURETYPE_IMAGESIZE
_IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES.containing_type = _IMAGEFEATURETYPE
_IMAGEFEATURETYPE_IMAGESIZERANGE.fields_by_name['widthRange'].message_type = _SIZERANGE
_IMAGEFEATURETYPE_IMAGESIZERANGE.fields_by_name['heightRange'].message_type = _SIZERANGE
_IMAGEFEATURETYPE_IMAGESIZERANGE.containing_type = _IMAGEFEATURETYPE
_IMAGEFEATURETYPE.fields_by_name['enumeratedSizes'].message_type = _IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES
_IMAGEFEATURETYPE.fields_by_name['imageSizeRange'].message_type = _IMAGEFEATURETYPE_IMAGESIZERANGE
_IMAGEFEATURETYPE.fields_by_name['colorSpace'].enum_type = _IMAGEFEATURETYPE_COLORSPACE
_IMAGEFEATURETYPE_COLORSPACE.containing_type = _IMAGEFEATURETYPE
_IMAGEFEATURETYPE.oneofs_by_name['SizeFlexibility'].fields.append(
  _IMAGEFEATURETYPE.fields_by_name['enumeratedSizes'])
_IMAGEFEATURETYPE.fields_by_name['enumeratedSizes'].containing_oneof = _IMAGEFEATURETYPE.oneofs_by_name['SizeFlexibility']
_IMAGEFEATURETYPE.oneofs_by_name['SizeFlexibility'].fields.append(
  _IMAGEFEATURETYPE.fields_by_name['imageSizeRange'])
_IMAGEFEATURETYPE.fields_by_name['imageSizeRange'].containing_oneof = _IMAGEFEATURETYPE.oneofs_by_name['SizeFlexibility']
_ARRAYFEATURETYPE_SHAPE.containing_type = _ARRAYFEATURETYPE
_ARRAYFEATURETYPE_ENUMERATEDSHAPES.fields_by_name['shapes'].message_type = _ARRAYFEATURETYPE_SHAPE
_ARRAYFEATURETYPE_ENUMERATEDSHAPES.containing_type = _ARRAYFEATURETYPE
_ARRAYFEATURETYPE_SHAPERANGE.fields_by_name['sizeRanges'].message_type = _SIZERANGE
_ARRAYFEATURETYPE_SHAPERANGE.containing_type = _ARRAYFEATURETYPE
_ARRAYFEATURETYPE.fields_by_name['dataType'].enum_type = _ARRAYFEATURETYPE_ARRAYDATATYPE
_ARRAYFEATURETYPE.fields_by_name['enumeratedShapes'].message_type = _ARRAYFEATURETYPE_ENUMERATEDSHAPES
_ARRAYFEATURETYPE.fields_by_name['shapeRange'].message_type = _ARRAYFEATURETYPE_SHAPERANGE
_ARRAYFEATURETYPE_ARRAYDATATYPE.containing_type = _ARRAYFEATURETYPE
_ARRAYFEATURETYPE.oneofs_by_name['ShapeFlexibility'].fields.append(
  _ARRAYFEATURETYPE.fields_by_name['enumeratedShapes'])
_ARRAYFEATURETYPE.fields_by_name['enumeratedShapes'].containing_oneof = _ARRAYFEATURETYPE.oneofs_by_name['ShapeFlexibility']
_ARRAYFEATURETYPE.oneofs_by_name['ShapeFlexibility'].fields.append(
  _ARRAYFEATURETYPE.fields_by_name['shapeRange'])
_ARRAYFEATURETYPE.fields_by_name['shapeRange'].containing_oneof = _ARRAYFEATURETYPE.oneofs_by_name['ShapeFlexibility']
_ARRAYFEATURETYPE.oneofs_by_name['defaultOptionalValue'].fields.append(
  _ARRAYFEATURETYPE.fields_by_name['intDefaultValue'])
_ARRAYFEATURETYPE.fields_by_name['intDefaultValue'].containing_oneof = _ARRAYFEATURETYPE.oneofs_by_name['defaultOptionalValue']
_ARRAYFEATURETYPE.oneofs_by_name['defaultOptionalValue'].fields.append(
  _ARRAYFEATURETYPE.fields_by_name['floatDefaultValue'])
_ARRAYFEATURETYPE.fields_by_name['floatDefaultValue'].containing_oneof = _ARRAYFEATURETYPE.oneofs_by_name['defaultOptionalValue']
_ARRAYFEATURETYPE.oneofs_by_name['defaultOptionalValue'].fields.append(
  _ARRAYFEATURETYPE.fields_by_name['doubleDefaultValue'])
_ARRAYFEATURETYPE.fields_by_name['doubleDefaultValue'].containing_oneof = _ARRAYFEATURETYPE.oneofs_by_name['defaultOptionalValue']
_DICTIONARYFEATURETYPE.fields_by_name['int64KeyType'].message_type = _INT64FEATURETYPE
_DICTIONARYFEATURETYPE.fields_by_name['stringKeyType'].message_type = _STRINGFEATURETYPE
_DICTIONARYFEATURETYPE.oneofs_by_name['KeyType'].fields.append(
  _DICTIONARYFEATURETYPE.fields_by_name['int64KeyType'])
_DICTIONARYFEATURETYPE.fields_by_name['int64KeyType'].containing_oneof = _DICTIONARYFEATURETYPE.oneofs_by_name['KeyType']
_DICTIONARYFEATURETYPE.oneofs_by_name['KeyType'].fields.append(
  _DICTIONARYFEATURETYPE.fields_by_name['stringKeyType'])
_DICTIONARYFEATURETYPE.fields_by_name['stringKeyType'].containing_oneof = _DICTIONARYFEATURETYPE.oneofs_by_name['KeyType']
_SEQUENCEFEATURETYPE.fields_by_name['int64Type'].message_type = _INT64FEATURETYPE
_SEQUENCEFEATURETYPE.fields_by_name['stringType'].message_type = _STRINGFEATURETYPE
_SEQUENCEFEATURETYPE.fields_by_name['sizeRange'].message_type = _SIZERANGE
_SEQUENCEFEATURETYPE.oneofs_by_name['Type'].fields.append(
  _SEQUENCEFEATURETYPE.fields_by_name['int64Type'])
_SEQUENCEFEATURETYPE.fields_by_name['int64Type'].containing_oneof = _SEQUENCEFEATURETYPE.oneofs_by_name['Type']
_SEQUENCEFEATURETYPE.oneofs_by_name['Type'].fields.append(
  _SEQUENCEFEATURETYPE.fields_by_name['stringType'])
_SEQUENCEFEATURETYPE.fields_by_name['stringType'].containing_oneof = _SEQUENCEFEATURETYPE.oneofs_by_name['Type']
_FEATURETYPE.fields_by_name['int64Type'].message_type = _INT64FEATURETYPE
_FEATURETYPE.fields_by_name['doubleType'].message_type = _DOUBLEFEATURETYPE
_FEATURETYPE.fields_by_name['stringType'].message_type = _STRINGFEATURETYPE
_FEATURETYPE.fields_by_name['imageType'].message_type = _IMAGEFEATURETYPE
_FEATURETYPE.fields_by_name['multiArrayType'].message_type = _ARRAYFEATURETYPE
_FEATURETYPE.fields_by_name['dictionaryType'].message_type = _DICTIONARYFEATURETYPE
_FEATURETYPE.fields_by_name['sequenceType'].message_type = _SEQUENCEFEATURETYPE
_FEATURETYPE.oneofs_by_name['Type'].fields.append(
  _FEATURETYPE.fields_by_name['int64Type'])
_FEATURETYPE.fields_by_name['int64Type'].containing_oneof = _FEATURETYPE.oneofs_by_name['Type']
_FEATURETYPE.oneofs_by_name['Type'].fields.append(
  _FEATURETYPE.fields_by_name['doubleType'])
_FEATURETYPE.fields_by_name['doubleType'].containing_oneof = _FEATURETYPE.oneofs_by_name['Type']
_FEATURETYPE.oneofs_by_name['Type'].fields.append(
  _FEATURETYPE.fields_by_name['stringType'])
_FEATURETYPE.fields_by_name['stringType'].containing_oneof = _FEATURETYPE.oneofs_by_name['Type']
_FEATURETYPE.oneofs_by_name['Type'].fields.append(
  _FEATURETYPE.fields_by_name['imageType'])
_FEATURETYPE.fields_by_name['imageType'].containing_oneof = _FEATURETYPE.oneofs_by_name['Type']
_FEATURETYPE.oneofs_by_name['Type'].fields.append(
  _FEATURETYPE.fields_by_name['multiArrayType'])
_FEATURETYPE.fields_by_name['multiArrayType'].containing_oneof = _FEATURETYPE.oneofs_by_name['Type']
_FEATURETYPE.oneofs_by_name['Type'].fields.append(
  _FEATURETYPE.fields_by_name['dictionaryType'])
_FEATURETYPE.fields_by_name['dictionaryType'].containing_oneof = _FEATURETYPE.oneofs_by_name['Type']
_FEATURETYPE.oneofs_by_name['Type'].fields.append(
  _FEATURETYPE.fields_by_name['sequenceType'])
_FEATURETYPE.fields_by_name['sequenceType'].containing_oneof = _FEATURETYPE.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['Int64FeatureType'] = _INT64FEATURETYPE
DESCRIPTOR.message_types_by_name['DoubleFeatureType'] = _DOUBLEFEATURETYPE
DESCRIPTOR.message_types_by_name['StringFeatureType'] = _STRINGFEATURETYPE
DESCRIPTOR.message_types_by_name['SizeRange'] = _SIZERANGE
DESCRIPTOR.message_types_by_name['ImageFeatureType'] = _IMAGEFEATURETYPE
DESCRIPTOR.message_types_by_name['ArrayFeatureType'] = _ARRAYFEATURETYPE
DESCRIPTOR.message_types_by_name['DictionaryFeatureType'] = _DICTIONARYFEATURETYPE
DESCRIPTOR.message_types_by_name['SequenceFeatureType'] = _SEQUENCEFEATURETYPE
DESCRIPTOR.message_types_by_name['FeatureType'] = _FEATURETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Int64FeatureType = _reflection.GeneratedProtocolMessageType('Int64FeatureType', (_message.Message,), dict(
  DESCRIPTOR = _INT64FEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.Int64FeatureType)
  ))
_sym_db.RegisterMessage(Int64FeatureType)

DoubleFeatureType = _reflection.GeneratedProtocolMessageType('DoubleFeatureType', (_message.Message,), dict(
  DESCRIPTOR = _DOUBLEFEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.DoubleFeatureType)
  ))
_sym_db.RegisterMessage(DoubleFeatureType)

StringFeatureType = _reflection.GeneratedProtocolMessageType('StringFeatureType', (_message.Message,), dict(
  DESCRIPTOR = _STRINGFEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.StringFeatureType)
  ))
_sym_db.RegisterMessage(StringFeatureType)

SizeRange = _reflection.GeneratedProtocolMessageType('SizeRange', (_message.Message,), dict(
  DESCRIPTOR = _SIZERANGE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.SizeRange)
  ))
_sym_db.RegisterMessage(SizeRange)

ImageFeatureType = _reflection.GeneratedProtocolMessageType('ImageFeatureType', (_message.Message,), dict(

  ImageSize = _reflection.GeneratedProtocolMessageType('ImageSize', (_message.Message,), dict(
    DESCRIPTOR = _IMAGEFEATURETYPE_IMAGESIZE,
    __module__ = 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType.ImageSize)
    ))
  ,

  EnumeratedImageSizes = _reflection.GeneratedProtocolMessageType('EnumeratedImageSizes', (_message.Message,), dict(
    DESCRIPTOR = _IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES,
    __module__ = 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType.EnumeratedImageSizes)
    ))
  ,

  ImageSizeRange = _reflection.GeneratedProtocolMessageType('ImageSizeRange', (_message.Message,), dict(
    DESCRIPTOR = _IMAGEFEATURETYPE_IMAGESIZERANGE,
    __module__ = 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType.ImageSizeRange)
    ))
  ,
  DESCRIPTOR = _IMAGEFEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType)
  ))
_sym_db.RegisterMessage(ImageFeatureType)
_sym_db.RegisterMessage(ImageFeatureType.ImageSize)
_sym_db.RegisterMessage(ImageFeatureType.EnumeratedImageSizes)
_sym_db.RegisterMessage(ImageFeatureType.ImageSizeRange)

ArrayFeatureType = _reflection.GeneratedProtocolMessageType('ArrayFeatureType', (_message.Message,), dict(

  Shape = _reflection.GeneratedProtocolMessageType('Shape', (_message.Message,), dict(
    DESCRIPTOR = _ARRAYFEATURETYPE_SHAPE,
    __module__ = 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType.Shape)
    ))
  ,

  EnumeratedShapes = _reflection.GeneratedProtocolMessageType('EnumeratedShapes', (_message.Message,), dict(
    DESCRIPTOR = _ARRAYFEATURETYPE_ENUMERATEDSHAPES,
    __module__ = 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType.EnumeratedShapes)
    ))
  ,

  ShapeRange = _reflection.GeneratedProtocolMessageType('ShapeRange', (_message.Message,), dict(
    DESCRIPTOR = _ARRAYFEATURETYPE_SHAPERANGE,
    __module__ = 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType.ShapeRange)
    ))
  ,
  DESCRIPTOR = _ARRAYFEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType)
  ))
_sym_db.RegisterMessage(ArrayFeatureType)
_sym_db.RegisterMessage(ArrayFeatureType.Shape)
_sym_db.RegisterMessage(ArrayFeatureType.EnumeratedShapes)
_sym_db.RegisterMessage(ArrayFeatureType.ShapeRange)

DictionaryFeatureType = _reflection.GeneratedProtocolMessageType('DictionaryFeatureType', (_message.Message,), dict(
  DESCRIPTOR = _DICTIONARYFEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.DictionaryFeatureType)
  ))
_sym_db.RegisterMessage(DictionaryFeatureType)

SequenceFeatureType = _reflection.GeneratedProtocolMessageType('SequenceFeatureType', (_message.Message,), dict(
  DESCRIPTOR = _SEQUENCEFEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.SequenceFeatureType)
  ))
_sym_db.RegisterMessage(SequenceFeatureType)

FeatureType = _reflection.GeneratedProtocolMessageType('FeatureType', (_message.Message,), dict(
  DESCRIPTOR = _FEATURETYPE,
  __module__ = 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.FeatureType)
  ))
_sym_db.RegisterMessage(FeatureType)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
