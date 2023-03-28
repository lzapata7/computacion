import unittest

def decimal_to_roman(decimal):
    resultado = ''
    if decimal >= 1000:
        resultado = 'M'
        decimal -= 1000
    if decimal >= 100:
        centenas = decimal // 100 # 108 -> centena 1
        decimal -= centenas * 100 # decimal = 1 * 100 - 108
        if centenas <= 3:
            resultado = 'C' * centenas
        elif centenas == 4:
            resultado += 'CD'
        elif centenas <= 8:
            resultado += 'D' + (centenas - 5) * 'C'
        elif centenas <= 9:
            resultado += 'CM'
    if decimal >= 10:
        decenas = decimal // 10
        if decenas <= 3:
            resultado += 'X' * decenas
        elif decenas == 4:
            resultado += 'XL'
        elif decenas <= 8:
            resultado += 'L' + (decenas - 5) * 'X'
        elif decenas == 9:
            resultado += 'XC'
        decimal = decimal % 10
    if decimal <= 3:
        resultado += 'I' * decimal
    elif decimal == 4:
        resultado += 'IV'
    elif decimal <= 8:
        resultado += 'V' + (decimal - 5) * 'I'
    elif decimal == 9:
        resultado += 'IX'
    return resultado


class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_4(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')

    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')

    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')

    def test_8(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, 'VIII')

    def test_9(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')

    def test_11(self):
        resultado = decimal_to_roman(11)
        self.assertEqual(resultado, 'XI')

    def test_13(self):
        resultado = decimal_to_roman(13)
        self.assertEqual(resultado, 'XIII')

    def test_16(self):
        resultado = decimal_to_roman(16)
        self.assertEqual(resultado, 'XVI')

    def test_24(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado, 'XXIV')

    def test_35(self):
        resultado = decimal_to_roman(35)
        self.assertEqual(resultado, 'XXXV')

    def test_46(self):
        resultado = decimal_to_roman(46)
        self.assertEqual(resultado, 'XLVI')

    def test_57(self):
        resultado = decimal_to_roman(57)
        self.assertEqual(resultado, 'LVII')

    def test_68(self):
        resultado = decimal_to_roman(68)
        self.assertEqual(resultado, 'LXVIII')

    def test_89(self):
        resultado = decimal_to_roman(89)
        self.assertEqual(resultado, 'LXXXIX')

    def test_99(self):
        resultado = decimal_to_roman(99)
        self.assertEqual(resultado, 'XCIX')

    def test_100(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')

    def test_111(self):
        resultado = decimal_to_roman(111)
        self.assertEqual(resultado, 'CXI')

    def test_222(self):
        resultado = decimal_to_roman(222)
        self.assertEqual(resultado, 'CCXXII')

    def test_333(self):
        resultado = decimal_to_roman(333)
        self.assertEqual(resultado, 'CCCXXXIII')

    def test_444(self):
        resultado = decimal_to_roman(444)
        self.assertEqual(resultado, 'CDXLIV')

    def test_555(self):
        resultado = decimal_to_roman(555)
        self.assertEqual(resultado, 'DLV')

    def test_666(self):
        resultado = decimal_to_roman(666)
        self.assertEqual(resultado, 'DCLXVI')

    def test_999(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado, 'CMXCIX')

    def test_1999(self):
        resultado = decimal_to_roman(1999)
        self.assertEqual(resultado, 'MCMXCIX')

if __name__ == '__main__':
    unittest.main()