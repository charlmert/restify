import restify.introspection as introspection
from restify.services import RestInterface
# not all objects have a name but those that do store it in the __name__ attribute.
def main():
    introspection.get_callables('RestInterface','^_.*')

if __name__ == '__main__':
    main()


