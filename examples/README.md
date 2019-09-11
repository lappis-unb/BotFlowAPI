## How to run webhook listener example

1 - ```pip install -r requirements.txt```
2 - ```python listener.py --debug```
3 - ```python api_mock.py```
4 - ```curl -X POST localhost:3000 -d '{"type":"intents", "file":"http://127.0.0.1:5000/file/intents/"}' -H "Content-Type: application/json"```
5 - The intents.md file should be created in `data` directory
