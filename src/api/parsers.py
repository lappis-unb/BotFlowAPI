
from collections import deque, namedtuple

Token = namedtuple('Token', ['type', 'data'])
    

def parse_story(src):
    """
    Parse a story file and return a list of documents with the format:

    [{
        'story': <name>, 
        'intents': [
            {
                'intent': <name>,
                'utters': [<utter-1>, <utter-2>, ...],
            }
        ],
     }, 
        ...
    ]
    """
    parser = StoryParser(src)
    return parser.parse()


#
# Auxiliary classes
#
class StoryParser:
    """
    Recursive desecent parser for stories (not part of public API)
    """
    def __init__(self, src):
        self.tokens = deque(self.lex(src)) 

    def lex(self, src):
        for line in src.splitlines():
            line = line.strip()
            if line.startswith('<!--') or not line:
                continue
            elif line.startswith('##'):
                data = line[2:].strip()
                yield Token('STORY', data)
            elif line.startswith('*'):
                data = line[1:].strip()
                yield Token('INTENT', data)
            elif line.startswith('-'):
                data = line[1:].strip()
                yield Token('UTTER', data)
            else:
                raise ValueError(f'invalid line: {line}')
    
    def parse(self):
        stories = []
        while self.tokens:
            stories.append(self.story())
        return stories

    def story(self):
        tks = self.tokens
        story = tks.popleft()
        assert story.type == 'STORY'
        intents = []
        while tks and tks[0].type == 'INTENT':
            intents.append(self.intent())
        return {'story': story.data, 'intents': intents}

    def intent(self):
        tks = self.tokens
        intent = tks.popleft()
        assert intent.type == 'INTENT'
        utters = []
        while tks and tks[0].type == 'UTTER':
            utter = tks.popleft()
            utters.append(utter.data)
        return {'intent': intent.data, 'utters': utters}

if __name__ == '__main__':
    from pprint import pprint
    src = '''
<!-- Comentario -->
## Money 8.3
* captacao
    - utter_captacao
    - utter_continuar_conversa

## Money 10
* lei_rouanet_valor_maximo_projeto
    - utter_lei_rouanet_valor_maximo_projeto
* lei_rouanet_valor_maximo_geral
    - utter_lei_rouanet_valor_minimo
    - utter_lei_rouanet_valor_maximo_pessoa_fisica
    - utter_lei_rouanet_valor_maximo_pessoa_juridica
    - utter_lei_rouanet_valor_maximo_regiao
    - utter_continuar_conversa
'''
    pprint(parse_story(src))