#!/usr/bin/python

import ota.otasupport as ota
import unittest
import binascii

# FW config structure, stored in eeprom
class TestOtaClasses(unittest.TestCase):
	def testNodeFirmwareConfig(self):
		nfc = ota.NodeFirmwareConfig()
		nfc.type = 31334
		nfc.version = 31335
		nfc.blocks = 31336
		nfc.crc = 31337
		
		ba = nfc.serialize()
		nfc2 = ota.NodeFirmwareConfig()
		nfc2.parse(ba)
		self.assertEqual(nfc.type, nfc2.type)
		self.assertEqual(nfc.version, nfc2.version)
		self.assertEqual(nfc.blocks, nfc2.blocks)
		self.assertEqual(nfc.crc, nfc2.crc)

	def testRequestFirmwareConfig(self):
		x = ota.RequestFirmwareConfig()
		x.type = 31334
		x.version = 31335
		x.blocks = 31336
		x.crc = 31337
		x.BLVersion = 31338
		
		ba = x.serialize()
		x2 = ota.RequestFirmwareConfig()
		x2.parse(ba)
		self.assertEqual(x.type, x2.type)
		self.assertEqual(x.version, x2.version)
		self.assertEqual(x.blocks, x2.blocks)
		self.assertEqual(x.crc, x2.crc)
		self.assertEqual(x.BLVersion, x2.BLVersion)

	def testRequestFWBlock(self):
		x = ota.RequestFWBlock()
		x.type = 31334
		x.version = 31335
		x.block = 31336
		
		ba = x.serialize()
		x2 = ota.RequestFWBlock()
		x2.parse(ba)
		self.assertEqual(x.type, x2.type)
		self.assertEqual(x.version, x2.version)
		self.assertEqual(x.block, x2.block)

	def testReplyFWBlock(self):
		x = ota.ReplyFWBlock()
		x.type = 31334
		x.version = 31335
		x.block = 31336
		x.data = '0123456789abcdef'

		x2 = ota.ReplyFWBlock()
		ba = x.serialize()
		x2.parse(ba)
		self.assertEqual(x.type, x2.type)
		self.assertEqual(x.version, x2.version)
		self.assertEqual(x.block, x2.block)
		self.assertEqual(x.data, x2.data)

if __name__ == "__main__":
	unittest.main()
