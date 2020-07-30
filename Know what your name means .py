alpha_lowercase = [*map(chr, range(97,123))]

meaning = [
    'Adventurous',
    'Beautiful',
    'Cunning',
    'Determined',
    'Encouraged',
    'Fantastic',
    'Generous',
    'Happiness',
    'Impeccable',
    'Jarring',
    'Kind',
    'Lively',
    'Merciful',
    'Naughty',
    'Optimistic',
    'Perserver',
    'Queen',
    'Ridiculous',
    'Stubborn',
    'Texter',
    'Uruguay',
    'Valuable',
    'Willful',
    'Xcellent',
    'Yyyoure fantastic',
    'Zealous'
]

name = (input() or 'Lily').lower()

Transdict = dict(zip(
                alpha_lowercase, meaning))

Prettydict = dict(zip(
    alpha_lowercase, [*map(chr,range(127462,127489))]
))

__import__('sys').stdout.reconfigure(encoding='utf-16')

print(f'Your Name : {name}\n\n')

try:
    for char in name:
        print(chr(128514),
           f'{Prettydict[char]}{(Transdict[char])[1:]}' )
except:
    pass

finally:
    print('\n\nThought I would make something fun, am thankful for each and every one of us Class of 2020 AkiraChix....')
