import coverage

cov = coverage.Coverage()
cov.start()

coverage run manage.py test

cov.stop()
cov.save()

cov.html_report()
