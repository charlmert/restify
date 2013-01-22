# dynamic keyword based arguments kwargs
def fn(a_str, *args, **kwargs):
    print 'var1 and 2 : ', kwargs['var1'], ' and ', kwargs['var2']
    if 'var3' in kwargs:
        print 'var3 is :', kwargs['var3']


print "calling: fn('one', var1='1', var2='2')"
fn('one', var1='1', var2='2')
print
print "calling: fn('one', var1='1', var2='2', var3='3')"
fn('one', var1='1', var2='2', var3='3')
