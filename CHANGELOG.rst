django-encrypted-model-field Changelog
---------------------------------------
- 0.5.7 - rearrange requirements and update dependencies
  * fix issue with output of generate_encryption_key command
  * define default value for FIELD_ENCRYPTION_KEY

- 0.5.6 - Fixed issue with generating encryption keys (thanks Dave Alan)
  * dropped support for Django 1.8, 1.9 and 1.10
  * fix classifier to include Django 2.0

- 0.5.5 - Fixed README

- 0.5.4 - drop python 3.4 support
  * add django 2.0 support
  * expand testing to cover python 2.7, 3.5 and 3.6 for django 1.9, 1.10, 1.11 and 2.0
  * fix broken test

- 0.5.3 - Fork from foundertherapy/django-cryptographic-fields
  * update dependencies
  * convert to run under python 3.x
  * rename package so it can be uploaded to pypi
  * add support for tox/travis-ci testing
