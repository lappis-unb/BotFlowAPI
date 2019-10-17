from .models import Story, Intent, Utter, Project
from unidecode import unidecode


def format_utter(utter_name):
    if not utter_name.startswith('utter_'):
        return 'utter_' + utter_name
    else:
        return utter_name

def format_checkpoint(name):
    return "checkpoint_" + name

class StoryParser:
    """
    Generate a markdown string from a given
    story object.
    """
    def parse(self, story: Story):
        name = f'## {unidecode(story.name)}\n'
        body = ''

        if story.is_checkpoint:
            body += self._checkpoint_parser(story.name)

        for c in story.content:
            if c['type'] == "intent":
                body += self._intent_parser(c)
            elif c['type'] == "utter":
                body += '\t' + self._utter_parser(c)
            elif c['type'] == "checkpoint":
                body += self._checkpoint_parser(c["name"])

        return name + body + '\n'


    def _intent_parser(self, intent):
        return f'* {unidecode(intent["name"])}\n'

    def _utter_parser(self, utter):
        return f'- {unidecode(format_utter(utter["name"]))}\n'

    def _checkpoint_parser(self, name):
        return f'> {unidecode(format_checkpoint(name))}\n'


class IntentParser:
    """
    Generate a markdown string from a given
    intent object.
    """
    def parse(self, intent: Intent):
        intent_name = unidecode(intent.name)
        if intent_name.startswith('synonym:'):
            name = f'## {intent_name}\n'
        else:
            name = f'## intent:{intent_name}\n'
            
        content = ''

        for s in intent.samples:
            content += f'- {s}\n'

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

        content += self._generic_list_parser('intents', [unidecode(i.name) for i in intents])
       # content += self._generic_list_parser('entities', [e.name for e in entities])
        content += self._templates_parser(utters)
        content += self._generic_list_parser('actions', [unidecode(format_utter(u.name)) for u in utters])

        return content

    def _generic_list_parser(self, name: str, elements: list):
        result = f'{unidecode(name)}:\n'

        for e in elements:
            result += f'  - {e}\n'

        return result + '\n'





    def _templates_parser(self, utters: list):
        result = f'templates:\n'

        for u in utters:
            ident = 2 * ' '
            utter_name = format_utter(u.name)
            result += f'{ident}{unidecode(utter_name)}:\n'
            for texts in u.alternatives:
                ident = 4 * ' '
                result += f'{ident}- text: |\n'
                for t in texts:
                    ident = 10 * ' '
                    result += f'{ident}{t}\n'
                    result += f'\n'

        return result + '\n'
