class TestClass():
  def __init__(self):
    print "created instance of Test"

  def __call__(self):
    print "called Test"

  VERSION = 1.0
  __doc__ = 'this is a Test Class' # docstrings (inline documentation)


if __name__ == '__main__':
    tc = TestClass()

    # don't know when this is called (probably a callback)
    # the script is executed on import
    tc.__call__()
