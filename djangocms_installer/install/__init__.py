# -*- coding: utf-8 -*-
from __future__ import print_function
import os.path
import subprocess


def check_install(config_data):
    """
    Here we do some **really** basic environment sanity checks.

    Basically we test for the more delicate and failing-prone dependencies:
     * database driver
     * Pillow image format support

    Many other errors will go undetected
    """
    errors = []
    size = 128, 128

    # PIL tests
    try:
        from PIL import Image

        try:
            im = Image.open(os.path.join(os.path.dirname(__file__), "../share/test_image.png"))
            im.thumbnail(size)
        except IOError:  # pragma: no cover
            errors.append("Pillow is not compiled with PNG support, see 'Libraries installation issues' documentation section: http://djangocms-installer.readthedocs.org/en/latest/libraries.html.")
        try:
            im = Image.open(os.path.join(os.path.dirname(__file__), "../share/test_image.jpg"))
            im.thumbnail(size)
        except IOError:  # pragma: no cover
            errors.append("Pillow is not compiled with JPEG support, see 'Libraries installation issues' documentation section: http://djangocms-installer.readthedocs.org/en/latest/libraries.html")
    except ImportError:  # pragma: no cover
        errors.append("Pillow is not installed check for installation errors and see 'Libraries installation issues' documentation section: http://djangocms-installer.readthedocs.org/en/latest/libraries.html")

    # PostgreSQL test
    if config_data.db_driver == 'psycopg2' and not config_data.no_db_driver:  # pragma: no cover
        try:
            import psycopg2  # NOQA
        except ImportError:
            errors.append("PostgreSQL driver is not installed, but you configured a PostgreSQL database, please check your installation and see 'Libraries installation issues' documentation section: http://djangocms-installer.readthedocs.org/en/latest/libraries.html")

    # MySQL test
    if config_data.db_driver == 'MySQL-python' and not config_data.no_db_driver:  # pragma: no cover
        try:
            import MySQLdb  # NOQA
        except ImportError:
            errors.append("MySQL driver is not installed, but you configured a MySQL database, please check your installation and see 'Libraries installation issues' documentation section: http://djangocms-installer.readthedocs.org/en/latest/libraries.html")
    if errors:  # pragma: no cover
        raise EnvironmentError("\n".join(errors))


def requirements(requirements, is_file=False):

    if is_file:  # pragma: no cover
        args = ['install', '-q', '-r', requirements]
    else:
        args = ['install', '-q']
        args.extend(['%s' % package for package in requirements.split()])
    subprocess.check_call(['pip'] + args)
    return True


def cleanup(requirements):  # pragma: no cover
    import pip

    args = ['uninstall', '-q', '-y']
    args.extend(requirements.split())
    exit_status = pip.main(args)
    return True
