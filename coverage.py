import coverage

cov = coverage.Coverage()
cov.start()

coverage run manage.py test user
coverage run manage.py test trip
coverage run manage.py test place

cov.stop()
cov.save()

cov.html_report()