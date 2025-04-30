import os
import sys
import unittest

from tests import TestCustom

try:
    from selenium.webdriver.common.by import By
except ImportError as err:
    print('[Error]',
          err, '\n\n'
          'Please refer to the Selenium documentation on installing the '
          'webdriver:\n'
          'https://www.selenium.dev/documentation/webdriver/'
          'getting_started/',
          file=sys.stderr)
    sys.exit(1)

if not os.path.isfile('package.json'):
    print('Invalid directory: cannot find \'package.json\'',
          file=sys.stderr)
    sys.exit(1)

tests = unittest.defaultTestLoader.loadTestsFromTestCase(TestCustom)

unittest.TextTestRunner().run(tests)
