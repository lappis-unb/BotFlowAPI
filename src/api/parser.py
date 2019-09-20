from .models import Story, Intent, Utter, Project


class StoryParser:
    """
    Generate a markdown string from a given
    story object.
    """
    def parse(self, story: Story):
        name = f'## {story.name}\n'
        body = ''
        
        for c in story.content:
            if c['type'] == "intent":
                body += self._intent_parser(c)
            elif c['type'] == "utter":
                body += self._utter_parser(c)

        return name + body


    def _intent_parser(self, intent):
        return f'* {intent["name"]}\n'

    
    def _utter_parser(self, utter):
        return f'{4 * " "}- {utter["name"]}\n'


class IntentParser:
    """
    Generate a markdown string from a given
    intent object.
    """
    def parse(self, intent: Intent):
        name = f'## intent:{intent.name}\n'
        content = ''

        for s in intent.samples:
            content += f'- {s}\n'

        return name + content


class DomainParser:
    """
    Generate a domain yaml string for a given project.
    """
    def parse(self, project: Project):
        content = ''
       
        stories = Story.objects.filter(project=project)
        intents = Intent.objects.filter(project=project)
        utters = Utter.objects.filter(project=project)
        entities = []

        if not intents and not utters:
            return ''

        
        stories_intents = []
        stories_utters = []
        
        for s in stories:
            for c in s.content:
                c = dict(c)
                if c['type'] == 'intent':
                    stories_intents.append(c['name'])
                else:
                    stories_utters.append(c['name'])

        used_intents = list(filter(lambda intent: intent.name in stories_intents, intents))
        used_utters = list(filter(lambda utter: utter.name in stories_utters, utters))

        content += self._generic_list_parser('intents', [i.name for i in used_intents])
       # content += self._generic_list_parser('entities', [e.name for e in entities])
        content += self._generic_list_parser('actions', [u.name for u in used_utters])
        content += self._templates_parser(used_utters)

        return content

    def _generic_list_parser(self, name: str, elements: list):
        result = f'\n{name}:\n'

        for e in elements:
            result += f'  - {e}\n'

        return result

    def _templates_parser(self, utters: list):
        result = f'\ntemplates:\n'

        for u in utters:
            ident = 2 * ' '
            result += f'{ident}{u.name}:\n'
            for texts in u.alternatives:
                ident = 4 * ' '
                result += f'{ident}- text: |\n'
                for t in texts:
                    ident = 10 * ' '
                    result += f'{ident}{t}\n'
                    result += f'\n'

        return result
