this is a django project

install django 1.6 (previous versions seem to all have the TEMPLATE NOT FOUND error)
git checkout or download zip: ??
sudo python setup.py install

change settings nltkws/nltkws/settings.py
 - configure DATABASES for your database (nltkws uses postgres by default)
 - change TEMPLATE_DIRS to point to your rest app's templates
   e.g. '/home/charl/open/nltkws/rest/templates'

run sql (sync/init database)
- cd nltkws
- python manage.py syncdb

when creating a superuser use
username: admin
password: admin

use developer server
- python manage.py runserver
server started at http://localhost:8000

OR

setup wsgi server in apache or your prefered wsgi server
for apache wsgi:
??

test your installation by navigating to
http://localhost:8000/admin
use your superuser credentials to log in.

similarily you can navigate to
http://localhost:8000/home

and
http://localhost:8000/raw
