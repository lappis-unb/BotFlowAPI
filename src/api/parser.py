from .models import Story, Intent, Utter


class StoryParser:
    """
    Generate a markdown string from a given
    story object.
    """
    def parse(self, story: Story):
        name = f'## {story.name}\n'
        content = ''

        for i in story.intents:
            content += self._intent_parser(i)

        return name + content


    def _intent_parser(self, intent: Intent):
        name = f'* {intent.name}\n'
        content = ''

        for s in intent.samples:
            content += f'\t {self._utter_parser(s)}'

        return name + content

    
    def _utter_parser(self, utter : Utter):
        return f'- {utter}\n'


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
