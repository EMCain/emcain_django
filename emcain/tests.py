from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from emcain.views import index, portfolio, contact
from emcain.forms import ContactForm

# tests for emcain.views:

title_base = b' | Emily Cain, Software Developer'

class IndexTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)

        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>Home' + title_base + b'</title>', response.content)
        self.assertIn(b'<h2>Software Developer based in Portland, OR</h2>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


class PortfolioTest(TestCase):

    def test_projects_url_resolves_to_portfolio_view(self):
        found = resolve('/projects/')
        self.assertEqual(found.func, portfolio)

    def test_portfolio_page_returns_correct_html(self):
        request = HttpRequest()
        response = portfolio(request)

        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>Portfolio' + title_base + b'</title>', response.content)
        self.assertIn(b'<ul>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


# tests for forms:
class ContactFormTest(TestCase):

    def test_contact_url_resolves_to_contact_view(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, contact)

    def test_form_is_valid_with_good_data(self):
        form_data = {'contact_name': 'Jean-Luc Picard', 'contact_email': 'picard@starfleet.org', 'content':'Tea. Earl Grey. Hot'}
        form = ContactForm(data=form_data, captcha_valid=True)
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid_with_captcha_failing(self):
        form_data = {'contact_name': 'Locutus', 'contact_email': 'picard@starfleet.org', 'content':'I am Locutus - of Borg. Resistance - is futile.'}
        form = ContactForm(data=form_data, captcha_valid=False)
        self.assertFalse(form.is_valid())

    def test_form_is_not_valid_with_invalid_email(self):
        form_data = {'contact_name': 'Benjamin Sisko', 'contact_email': 'sisko at starfleet dot org', 'content':' You know, Jake, we really need to get away more often.'}
        form = ContactForm(data=form_data, captcha_valid=True)
        self.assertFalse(form.is_valid())


    def test_form_is_not_valid_with_no_name(self):
        form_data = {'contact_name': '', 'contact_email': 'info@starfleet.org',
                     'content': ' Space: The Final Frontier.'}
        form = ContactForm(data=form_data, captcha_valid=True)
        self.assertFalse(form.is_valid())


    def test_form_is_not_valid_with_no_message(self):
        form_data = {'contact_name': 'Morn', 'contact_email': 'morn@galacticshipping.com',
                     'content': ''}
        form = ContactForm(data=form_data, captcha_valid=True)
        self.assertFalse(form.is_valid())

