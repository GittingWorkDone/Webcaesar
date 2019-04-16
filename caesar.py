from string import ascii_lowercase as lowers


def alphabet_position(letter):
    assert len(letter) == 1, 'Only give me one letter please'
    return lowers.index(letter.lower())


def rotate_character(char, rot=1):
    if char.isalpha():
        origin_pos = alphabet_position(char)
        new_pos = (origin_pos + rot) % 26
        new_char = lowers[new_pos]
        return new_char if char.islower() else new_char.upper()
    else:
        return char



def encrypt(text, rot):
    return ''.join(rotate_character(char, rot) for char in text)


def main(shift, verbose, text):
    msg = input('Type a message:\n') if text is None else text
    while True:
        try:
            rot = int(input('Rotate by:\n')) if shift is None else shift
            break
        except ValueError:
            print('error: the shift must be an integer, please try again')
            continue
    if verbose:
        print('Encrypted message:')
    print(encrypt(msg, rot))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='encrypt plaintext with Caesar cypher')
    parser.add_argument('shift', type=int, nargs='?',
                        help='distance to shift character down alphabet')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help="increase output verbosity")
    parser.add_argument('-t', '--text', help='plaintext to encrypt', dest='text')
    args = parser.parse_args()
    main(args.shift, args.verbose, args.text)
