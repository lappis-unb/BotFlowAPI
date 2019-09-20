import pytest

from api.parser import DomainParser
from api.models import Project, Story
from api.utils import story_content_formatter

class TestDomainParser:

    @pytest.fixture
    def project_1(self, db):
        """
        Project with one story and without entities.
        """
        project = Project.objects.create(name='name', description='description')
        Intent.objects.create(name='cumprimentar', project=project, samples=['oi', 'ola', 'bom dia'])
        Story.objects.create(name='Despedir Story', project=project, content=story_content_formatter([
            {'name': 'cumprimentar', 'type': 'intent'},
            {'name': 'utter_cumprimentar', 'type': 'utter'}

        ]))

        return project

    def test_domain_without_entities(self, project_1):
        parser = DomainParser()
        print(parser.parse(project_1))
        assert False
