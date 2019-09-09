from .models import Story, Intent, Utter


class StoryParser:
    
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
