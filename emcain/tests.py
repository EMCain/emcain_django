from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase, RequestFactory

from emcain.views import index, portfolio, project

from emcain.models import Project, ProjectSkill, Skill

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
