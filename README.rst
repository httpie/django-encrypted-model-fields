Django Encrypted Model Fields
=============================

.. image:: https://travis-ci.org/lanshark/django-encrypted-model-fields.png
   :target: https://travis-ci.org/lanshark/django-encrypted-model-fields

About
-----

This is a fork of https://github.com/foundertherapy/django-cryptographic-fields.
It has been renamed, and updated to properly support Python3 and latest versions
of Django.

``django-encrypted-model-fields`` is set of fields that wrap standard Django
fields with encryption provided by the python cryptography library. These
fields are much more compatible with a 12-factor design since they take their
encryption key from the settings file instead of a file on disk used by
``keyczar``.

While keyczar is an excellent tool to use for encryption, it's not compatible
with Python 3, and it requires, for hosts like Heroku, that you either check
your key file into your git repository for deployment, or implement manual
post-deployment processing to write the key stored in an environment variable
into a file that keyczar can read.

Getting Started
---------------

    $ pip install django-encrypted-model-fields

Add "encrypted_model_fields" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'encrypted_model_fields',
    )

``django-encrypted-model-fields`` expects the encryption key to be specified
using ``FIELD_ENCRYPTION_KEY`` in your project's ``settings.py`` file. For
example, to load it from the local environment:

    import os

    FIELD_ENCRYPTION_KEY = os.environ.get('FIELD_ENCRYPTION_KEY', '')

To use an encrypted field in a Django model, use one of the fields from the
``encrypted_model_fields`` module:

    from encrypted_model_fields.fields import EncryptedCharField

    class EncryptedFieldModel(models.Model):
        encrypted_char_field = EncryptedCharField(max_length=100)

For fields that require ``max_length`` to be specified, the ``Encrypted``
variants of those fields will automatically increase the size of the database
field to hold the encrypted form of the content. For example, a 3 character
CharField will automatically specify a database field size of 100 characters
when ``EncryptedCharField(max_length=3)`` is specified.

Due to the nature of the encrypted data, filtering by values contained in
encrypted fields won't work properly. Sorting is also not supported.

Generating an Encryption Key
----------------------------

There is a Django management command ``generate_encryption_key`` provided
with the ``encrypted_model_fields`` library. Use this command to generate a new
encryption key to set as ``settings.FIELD_ENCRYPTION_KEY``.

    ./manage.py generate_encryption_key

Running this command will print an encryption key to the terminal, which can
be configured in your environment or settings file.

NOTE: This command will ONLY work in a CLEAN, NEW django project that does NOT
import encrypted_model_fields in any of it's apps.  IF you are already importing
encrypted_model_fields, try running this in a python shell instead::

   import os
   import base64

   new_key = base64.urlsafe_b64encode(os.urandom(32))
   print(new_key)

Development Environment
-----------------------

Added Tox for testing with different versions of Django and Python.  To get started:
    pip install -r requirements/dev.txt

using ``pyenv`` add the requisite python interpreters:
    pyenv install 3.6.14
    pyenv install 3.7.11
    pyenv install 3.8.11
    pyenv install 3.9.6

Add the requisite versions to the local version:
    pyenv local 3.6.14 3.7.11 3.8.11 3.9.6

Run ``tox``
    tox
