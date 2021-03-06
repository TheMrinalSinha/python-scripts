from itertools import permutations

def validate_name(ORIGINAL_NAME, PROVIDED_NAME=None):
    ORIGINAL_NAME       = ORIGINAL_NAME.lower()
    PROVIDED_NAME       = PROVIDED_NAME.lower() if PROVIDED_NAME else None

    # Check if both the names are equal
    if ORIGINAL_NAME == PROVIDED_NAME:
        return True

    ORIGINAL_NAME       = ORIGINAL_NAME.split(' ')
    FAMILY_NAME         = ORIGINAL_NAME[-1]
    OTHER_NAME          = ORIGINAL_NAME[:-1]
    NAME_COMBINATIONS   = []

    # Validating name based of permutations
    for i in range(1, len(ORIGINAL_NAME) + 1):
        combi = list(permutations(ORIGINAL_NAME, i))
        for _ in combi:
            if not PROVIDED_NAME:
                NAME_COMBINATIONS.append(' '.join(_))
            else:
                if PROVIDED_NAME == ' '.join(_):
                    return True

    # Validating based on initials
    for i in range(1, len(OTHER_NAME) + 1):
        combi = list(permutations(OTHER_NAME, i))
        for _ in combi:
            initials = [x[0] for x in _]
            _w = ''.join(initials) +' '+ FAMILY_NAME
            _x = ' '.join(initials) +' '+ FAMILY_NAME
            _y = '. '.join(initials) +' '+ FAMILY_NAME
            _z = '. '.join(initials) +'. '+ FAMILY_NAME
            _p = FAMILY_NAME +' '+ ''.join(initials)
            _q = FAMILY_NAME +' '+ ' '.join(initials)
            _r = FAMILY_NAME +' '+ '. '.join(initials)
            _s = FAMILY_NAME +'. '+ '. '.join(initials)

            if not PROVIDED_NAME:
                for _ in (_w, _x, _y, _z, _p, _q, _r, _s):
                    NAME_COMBINATIONS.append(_)
            else:
                if PROVIDED_NAME in (_w, _x, _y, _z, _p, _q, _r, _s):
                    return True

        for texts in combi:
            if len(texts) > 1:
                first_pos  = texts[0][0]
                remainings = list(texts[1:])
                remainings.append(first_pos)
                _w = ' '.join(remainings) +' '+ FAMILY_NAME
                _x = FAMILY_NAME +' '+ ' '.join(remainings)

                if not PROVIDED_NAME:
                    for _ in (_w, _x):
                        NAME_COMBINATIONS.append(_)
                else:
                    if PROVIDED_NAME in (_w, _x):
                        return True

    return list(set(NAME_COMBINATIONS)) if not PROVIDED_NAME else False


# original_name = input('ORIGINAL NAME: ').strip()
# while True:
#     provided_name = input('PROVIDED NAME: ').strip()
#     print('Match: ', validate_name(original_name, provided_name), end='\n--------------\n')

print(validate_name('Mrinal Vinay Sinha'))
