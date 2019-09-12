from .models import Story, Intent, Utter


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
        return f'- {utter["name"]}\n'


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
