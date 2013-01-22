# new style inheritance must specify an inheritable as inheriting
# from wait for it ... object.
# python 2.2 was when the new style classes was introduced.
# was declared default behavior in python 3
class A():
    def init(self):
        print 'A.init(self)'

class B(A):
    def init(self):
        print 'B.init(self)'
        #super(B, self).init() # requires A(object):
        A.init(self) # doesn't require parent to explicitly inherit from object

if __name__ == '__main__':
    print 'exec: '
    b = B()
    b.init()
