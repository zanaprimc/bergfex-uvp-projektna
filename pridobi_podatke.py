import re

vzorec = re.compile(
    r'<title>BERGFEX: Ski resort (?P<ime>.+) - Skiing holiday (?P<ime>.+)</title>'
    r'.*?'
    r'<li class="tw-text-s tw-flex tw-gap-1 tw-pr-1 tw-items-center">'
    r'<a href="/(?P<drzava>\w+)/"'
    r'<span class="tw-block tw-text-m">'
    r'\d+ - \d+ m'
    r'.*?'
    
)