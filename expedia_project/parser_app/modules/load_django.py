import sys
import os
import django

sys.path.append(os.path.abspath("expedia_project"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'expedia_project.settings'
django.setup()
