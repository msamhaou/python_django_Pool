import requests, json ,dewiki, sys

url = 'https://en.wikipedia.org/w/api.php'
if (len(sys.argv) < 2):
    exit(1);

subject = sys.argv[1]
print(subject)
param = {
        'action': 'query',
        'format': 'json',
        'titles': subject,
        'prop': 'extracts',
        'explaintext': False
    }

res = requests.get(url, params=param)
data = res.json()
key = list(data['query']['pages'].keys())
raw_html = data['query']['pages'][key[0]]['extract']
plain_text = dewiki.from_string(raw_html)

filename = sys.argv[1] + '.wiki'
file = open(filename, 'w').write(plain_text)
print(plain_text)