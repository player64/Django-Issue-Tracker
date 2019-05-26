from django.test import TestCase
from .templatetags.archive_extras import readable_status, bootstrap_status, active_helper


class TestsArchiveExtras(TestCase):

    def test_readable_status(self):
        self.assertEqual(readable_status('todo'), 'To do')
        self.assertEqual(readable_status('doing'), 'Doing')
        self.assertEqual(readable_status('done'), 'Done')
        self.assertEqual(readable_status('something'), '')

    def test_bootstrap_status(self):
        self.assertEqual(bootstrap_status('success'), 'success')
        self.assertEqual(bootstrap_status('error'), 'danger')
        self.assertEqual(bootstrap_status('warning'), 'warning')
        self.assertEqual(bootstrap_status('something'), '')

    def test_active_helper(self):
        self.assertTrue(active_helper('/accounts/profile/', '/accounts'))
        self.assertFalse(active_helper('/accounts/profile/', '/features'))
