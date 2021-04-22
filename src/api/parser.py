from .models import Story, Intent, Utter, Project
from unidecode import unidecode


def format_utter(utter_name):
    if not utter_name.startswith('utter_'):
        return 'utter_' + utter_name
    else:
        return utter_name


class StoryParser:
    """
    Generate a markdown string from a given
    story object.
    """
    def parse(self, story: Story):
        name = f'## {unidecode(story.name)}\n'
        body = ''
        
        for content in story.content:
            if content['type'] == "intent":
                body += self._intent_parser(content)
            elif content['type'] == "utter":
                body += '\t' + self._utter_parser(content)

        return name + body + '\n'

    def _intent_parser(self, intent):
        return f'* {unidecode(intent["name"])}\n'
  
    def _utter_parser(self, utter):
        return f'- {unidecode(format_utter(utter["name"]))}\n'


class IntentParser:
    """
    Generate a markdown string from a given
    intent object.
    """
    def parse(self, intent: Intent):
        name = f'## intent:{unidecode(intent.name)}\n'
        content = ''

        for sample in intent.samples:
            content += f'- {sample}\n'

        return name + content + '\n'


class DomainParser:
    """
    Generate a domain yaml string for a given project.
    """
    def parse(self, project: Project):
        content = ''
        
        intents = Intent.objects.filter(project=project)
        utters = Utter.objects.filter(project=project)
        entities = []

        if not intents and not utters:
            return ''

        content += self._generic_list_parser('intents', [unidecode(intent.name) for intent in intents])
        content += self._templates_parser(utters)
        content += self._generic_list_parser('actions', [unidecode(format_utter(utter.name)) for utter in utters])
   
        return content

    def _generic_list_parser(self, name: str, elements: list):
        result = f'{unidecode(name)}:\n'

        for element in elements:
            result += f'  - {element}\n'
   
        return result + '\n'

    def _templates_parser(self, utters: list):
        result = f'templates:\n'

        for utter in utters:    
            ident = 2 * ' '
            utter_name = format_utter(utter.name)
            result += f'{ident}{unidecode(utter_name)}:\n'
            for texts in utter.alternatives:
                ident = 4 * ' '
                result += f'{ident}- text: |\n'
                for text in texts:
                    ident = 10 * ' '
                    result += f'{ident}{text}\n'
                    result += f'\n'
        
        return result + '\n'
