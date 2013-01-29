class BaseInterface(object):
    my_int = 32
    my_string = 'a string'

    def do_int(self, number):
        self.my_int += number
        return self.my_int

    def do_string(self, text):
        self.my_string = text
        return self.my_string

class RestInterface(BaseInterface):
    def do_kwargs(self, var1=1, *args, **kwargs):
        self.my_int += 3

        if (kwargs['content']):
            return ''.join([kwargs['content'], ' : ', str(self.my_int)])

        # return standard json error object
        return 'error'
