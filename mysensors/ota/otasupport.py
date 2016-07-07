#!/usr/bin/python

import struct
import binascii

FIRMWARE_BLOCK_SIZE = 16

class OtaBase:
	type		= 0	# u16
	version		= 0	# u16

class OtaCfgBase(OtaBase):
	blocks		= 0 	# u16
	crc		= 0 	# u16


# FW config structure, stored in eeprom
class NodeFirmwareConfig(OtaCfgBase):
	def serialize(self):
		return struct.pack('<HHHH', self.type, self.version, self.blocks, self.crc)
	def parse(self, ba):
		(self.type, self.version, self.blocks, self.crc) = struct.unpack('<HHHH', ba)

class RequestFirmwareConfig(OtaCfgBase):
	BLVersion	= 0	# u16
	def serialize(self):
		return struct.pack('<HHHHH', self.type, self.version, self.blocks, self.crc, self.BLVersion)
	def parse(self, ba):
		(self.type, self.version, self.blocks, self.crc, self.BLVersion) = struct.unpack('<HHHHH', ba)

class RequestFWBlock(OtaBase):
	block		= 0	# u16
	def serialize(self):
		return struct.pack('<HHH', self.type, self.version, self.block)
	def parse(self, ba):
		(self.type, self.version, self.block) = struct.unpack('<HHH', ba)

class ReplyFWBlock(OtaBase):
	block		= 0 	# u16
	data		= '' 	# u8[FIRMWARE_BLOCK_SIZE]
	def serialize(self):
		datlen = FIRMWARE_BLOCK_SIZE if len(self.data) > FIRMWARE_BLOCK_SIZE else len(self.data)
		ba = struct.pack('<3H' , self.type, self.version, self.block)
		for b in self.data:
			ba += b
		return ba

	def parse(self, ba):
		fmt = "<3H"
		sz = struct.calcsize(fmt)
		(self.type, self.version, self.block) = struct.unpack(fmt, ba[0:sz])
		i=sz
		while i < len(ba):
			self.data += ba[i]
			i += 1


if "__main__" == __name__:
	x = NodeFirwwareConfig()
	ba = '\x03\x00\x04\x00\x01\x02\xad\xde'
	x.parse(ba)
#	x.type = 3
#	x.version = 4
#	x.blocks = 513
#	x.crc = 0xdead
	print x.version
	print x.blocks
	print binascii.hexlify(x.serialize())
