# django-encrypted-model-field Changelog

-   0.6.5 - RE-Correct links to repository and homepage
-   0.6.4 - Correct links to repository and homepage
-   0.6.3 - Converted to poetry for build system
-   0.6.2 - Bump support to any python \< 4
    -   Make Generating an Encryption Key more prominent
-   0.6.1 - Add Support for Python up to 3.11
-   0.6.0 - Major Update
    -   Drop Python 2 Support
    -   Drop support for Django \< 2.2
    -   Add support for Django 2.2, 3.0, 3.1, and 3.2
    -   Drop support for Python \< 3.6
    -   Add Support for Python 3.6, 3.7, 3.8, and 3.9
    -   Move travis-ci testing to gitlab
    -   Remove Support for EncryptedNullBooleanField (deprecated by
        Django 4.0)
    -   Update Test App to Django 2.2 standard
    -   Include 2 of Oleg Pesok's fixes: for Timezone-aware datetimes,
        and the cached validator crash
-   0.5.8 - Move to GITLAB repository
-   0.5.7 - rearrange requirements and update dependencies
    -   fix issue with output of generate_encryption_key command
    -   define default value for FIELD_ENCRYPTION_KEY
    -   restore support for Django 1.9, 1.10, and 1.11
-   0.5.6 - Fixed issue with generating encryption keys (thanks Dave
    Alan)
    -   dropped support for Django 1.8, 1.9 and 1.10
    -   fix classifier to include Django 2.0
-   0.5.5 - Fixed README
-   0.5.4 - drop python 3.4 support
    -   add django 2.0 support
    -   expand testing to cover python 2.7, 3.5 and 3.6 for django 1.9,
        1.10, 1.11 and 2.0
    -   fix broken test
-   0.5.3 - Fork from foundertherapy/django-cryptographic-fields
    -   update dependencies
    -   convert to run under python 3.x
    -   rename package so it can be uploaded to pypi
    -   add support for tox/travis-ci testing
