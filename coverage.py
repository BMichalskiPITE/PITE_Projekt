import coverage

cov = coverage.Coverage()
cov.start()

coverage run manage.py test user
coverage run manage.py test place
coverage run manage.py test trip 

cov.stop()
cov.save()

cov.html_report()