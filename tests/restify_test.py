import unittest
import sys

sys.path.append('../restify')
from test_services import RestInterface
from introspection import *

class IntrospectionTestCase(unittest.TestCase):

  def test_valid(self):
    self.args = get_args(RestInterface.do_int)
    # checking for valid arguments
    self.assertEquals(self.args['args'][0], 'number')

  def test_invalid(self):
    try:
      self.args = get_args(RestInterface.my_int)
    except Exception:
      pass

def suite():
  suite = unittest.TestSuite()
  loader = unittest.TestLoader()

  suite.addTest(loader.loadTestsFromTestCase(IntrospectionTestCase))

  return suite


if __name__ == "__main__":
  unittest.main(defaultTest="suite", testRunner=unittest.TextTestRunner(verbosity=2))
