import os
import inspect

import nose
import unittest
from .. import ihex

FILENAME = inspect.getfile(inspect.currentframe())
SCRIPT_PATH = os.path.dirname(os.path.abspath(FILENAME))


class testiHex(unittest.TestCase):

    def test_low_offset(self):
        starting_offset = 0x08004000
        working_offset = starting_offset

        ih = ihex.iHex()
        ih.load_bin(os.path.join(SCRIPT_PATH, 'test_collateral/main.bin'), starting_offset)

        wl = ih.get_u32_list()

        for w in wl:
            self.assertEqual(w[0], working_offset)
            working_offset += 4

    def test_hi_offset(self):
        starting_offset = 0x08020000
        working_offset = starting_offset

        ih = ihex.iHex()
        ih.load_bin(os.path.join(SCRIPT_PATH, 'test_collateral/main.bin'), starting_offset)

        wl = ih.get_u32_list()

        for w in wl:
            self.assertEqual(w[0], working_offset)
            working_offset += 4

    def test_arm_gcc_output(self):
        starting_offset = 0x08004000
        working_offset = starting_offset

        ih = ihex.iHex()
        gih = ihex.iHex()
        
        ih.load_bin(os.path.join(SCRIPT_PATH, 'test_collateral/main.bin'),
                    starting_offset)

        gih.load_ihex(os.path.join(SCRIPT_PATH, 'test_collateral/main.hex'))

        wl = ih.get_u32_list()
        wl2 = gih.get_u32_list()

        for idx in range(len(wl)):
            self.assertEqual(wl[idx][0], wl2[idx][0])

    def test_avr_gcc_output(self):
        starting_offset = 0
        working_offset = starting_offset

        ih = ihex.iHex()
        gih = ihex.iHex()
        
        ih.load_bin(os.path.join(SCRIPT_PATH, 'test_collateral/grbl.bin'),
                    starting_offset)

        gih.load_ihex(os.path.join(SCRIPT_PATH, 'test_collateral/grbl.hex'))

        wl = ih.get_u32_list()
        wl2 = gih.get_u32_list()

        for idx in range(len(wl)):
            self.assertEqual(wl[idx][0], wl2[idx][0])
