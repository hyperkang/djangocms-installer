# -*- coding: utf-8 -*-
from __future__ import print_function
import os
from subprocess import CalledProcessError
import sys

from mock import patch

from djangocms_installer import main
from .base import unittest, IsolatedTestClass


class TestMain(IsolatedTestClass):

    def test_requirements_invocation(self):
        with patch('sys.stdout', self.stdout):
            with patch('sys.stderr', self.stderr):
                sys.argv = ['main'] + ['--db=sqlite://localhost/test.db',
                                       '-len', '--cms-version=stable', '-R',
                                       '-q', '-u', '-p'+self.project_dir,
                                       'example_prj']
                main.execute()
        stdout = self.stdout.getvalue()
        self.assertTrue(stdout.find('Django<1.7') > -1)
        self.assertTrue(stdout.find('django-reversion>=1.8') > -1)
        self.assertTrue(stdout.find('djangocms-text-ckeditor') > -1)
        self.assertTrue(stdout.find('djangocms-admin-style') > -1)
        self.assertTrue(stdout.find('djangocms-column') > -1)
        self.assertTrue(stdout.find('djangocms-file') > -1)
        self.assertTrue(stdout.find('djangocms-flash') > -1)
        self.assertTrue(stdout.find('djangocms-googlemap') > -1)
        self.assertTrue(stdout.find('djangocms-inherit') > -1)
        self.assertTrue(stdout.find('djangocms-link') > -1)
        self.assertTrue(stdout.find('djangocms-picture') > -1)
        self.assertTrue(stdout.find('djangocms-style') > -1)
        self.assertTrue(stdout.find('djangocms-teaser') > -1)
        self.assertTrue(stdout.find('djangocms-video') > -1)

    def test_main_invocation(self):
        with patch('sys.stdout', self.stdout):
            with patch('sys.stderr', self.stderr):
                sys.argv = ['main'] + ['--db=sqlite://localhost/test.db',
                                       '-len', '--cms-version=stable',
                                       '-q', '-u', '-p'+self.project_dir,
                                       'example_prj']
                main.execute()
                self.assertTrue(os.path.exists(os.path.join(self.project_dir, 'static')))
                self.assertTrue(os.path.exists(os.path.join(self.project_dir, 'example_prj', 'static')))
                # Checking we successfully completed the whole process
                self.assertTrue(("Get into '%s' directory and type 'python manage.py runserver' to start your project" % self.project_dir) in self.stdout.getvalue())

    def test_two_langs_invocation(self):
        with patch('sys.stdout', self.stdout):
            with patch('sys.stderr', self.stderr):
                sys.argv = ['main'] + ['--db=sqlite://localhost/test.db',
                                       '-len', '-lfr', '--cms-version=stable',
                                       '-q', '-u', '-p'+self.project_dir,
                                       'example_prj']
                main.execute()
                # Checking we successfully completed the whole process
                self.assertTrue(("Get into '%s' directory and type 'python manage.py runserver' to start your project" % self.project_dir) in self.stdout.getvalue())

    def test_develop(self):
        with patch('sys.stdout', self.stdout):
            with patch('sys.stderr', self.stderr):
                sys.argv = ['main'] + ['--db=sqlite://localhost/test.db',
                                       '-len', '--cms-version=develop',
                                       '-q', '-u', '-p'+self.project_dir,
                                       'example_prj']
                main.execute()
                # Checking we successfully completed the whole process
                self.assertTrue(("Get into '%s' directory and type 'python manage.py runserver' to start your project" % self.project_dir) in self.stdout.getvalue())

    def test_cleanup(self):
        with patch('sys.stdout', self.stdout):
            with patch('sys.stderr', self.stderr):
                with self.assertRaises((CalledProcessError, EnvironmentError)):
                    sys.argv = ['main'] + ['--db=sqlite://localhost/test.db',
                                           '-len', '--cms-version=2.4',
                                           '--django=1.7',
                                           '-q', '-u', '-p'+self.project_dir,
                                           'example_prj']
                    main.execute()
        self.assertFalse(os.path.exists(self.project_dir))

    @unittest.skipIf(sys.version_info >= (3, 0),
                     reason="django 1.4 does not support python3")
    def test_django_1_4(self):
        with patch('sys.stdout', self.stdout):
            with patch('sys.stderr', self.stderr):
                sys.argv = ['main'] + ['--db=sqlite://localhost/test.db',
                                       '-len', '--django-version=1.4',
                                       '--cms-version=3.0',
                                       '-q', '-u', '-p'+self.project_dir,
                                       'example_prj']
                main.execute()
                # Checking we successfully completed the whole process
                self.assertTrue(("Get into '%s' directory and type 'python manage.py runserver' to start your project" % self.project_dir) in self.stdout.getvalue())

    @unittest.skipIf(sys.version_info >= (3, 0),
                     reason="django 1.5 does not support python3")
    def test_django_1_5(self):
        with patch('sys.stdout', self.stdout):
            with patch('sys.stderr', self.stderr):
                sys.argv = ['main'] + ['--db=sqlite://localhost/test.db',
                                       '-len', '--django-version=1.5',
                                       '--cms-version=3.0',
                                       '-q', '-u', '-p'+self.project_dir,
                                       'example_prj']
                main.execute()
                # Checking we successfully completed the whole process
                self.assertTrue(("Get into '%s' directory and type 'python manage.py runserver' to start your project" % self.project_dir) in self.stdout.getvalue())
