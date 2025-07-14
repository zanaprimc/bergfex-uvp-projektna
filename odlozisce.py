import re

vzorec = re.compile(
    r'<title>BERGFEX: Ski resort (?P<ime>.+) - Skiing holiday .+'
    r'.*?'
    r'<li class="tw-text-s tw-flex tw-gap-1 tw-pr-1 tw-items-center">'
    r'<a href="/(?P<drzava>\w+)/"'
    r'<span class="tw-block tw-text-m">'
    r'(?P<nadmorska>.+) m'
    r'.*?'
    r'Pistes'
    r'.*?'
    r'</div><span class="tw-pl-2 tw-text-m tw-font-semibold">(?P<proge>.+) km</span>'
    r'Prices'
    r'.*?'
    r'€ (?P<cena>.+)'
)

vzorec = re.compile(
    r'<title>.*?Skiing holiday (?P<ime>.+)</title'
    r'<a href="\/(?P<drzava>\w+)\/"'
    r'<span class="tw-block tw-text-m">.*?'
    r'(?P<nadmorska>.+).*?'
    r'Pistes.*?'
    r'<\/div><span class="tw-pl-2 tw-text-m tw-font-semibold">(?P<proge>.+) km.*?'
    r'Prices.*?'
    r'€ (?P<cena>.+)\s?',
    re.DOTALL | re.IGNORECASE
)

vzorec = re.compile(
    r'<title>.*?Skiing holiday (?P<resort>.+?)<\/title>.*?'
    r'<a\s+href="/(?P<drzava>[^/"]+)/".*?'
    r'<span[^>]*>\s*(?P<visina>\d+\s*-\s*\d+)\s*m\s*</span>.*?'
    r'<span[^>]*>\s*(?P<dolzina>\d+[\.]\d+|\d+)\s*km\s*</span>.*?'
    r'Prices</h2>.*?'
    r'€\s*(?P<cena>\d+[\,]\d+|\d+)',
    re.IGNORECASE | re.DOTALL
)