import argparse
import pandas as pd
from collections import Counter


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def main():
    args = arguments()

    with open(args.file) as file:
        codes = file.read().strip()
        codes = codes.splitlines()

    def top_five(x):
        d = dict(Counter(''.join(sorted(x))))
        s = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        return (''.join([i[0] for i in s[:5]]))

    def decrypt(encrypted_text):
        'http://programeveryday.com/post/implementing-a-basic-caesar-cipher-in-python/'
        """Encrypt the string and return the ciphertext"""
        key = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        e_room = encrypted_text[:-11]
        d_room = []
        c_shift = int(encrypted_text[-10:-7])

        for word in e_room.split('-'):
            for line in word:
                i = (key.index(line) + c_shift) % 26
                result += key[i]
            d_room.append(result)
            result = ''
        return(" ".join(d_room))

    # Part 1:
    df = pd.read_csv(args.file, names=["raw_strings"])
    df["checksum"] = df["raw_strings"].str.extract('\[(\w+)\]')
    df["sectID"] = df["raw_strings"].str.extract('-(\d+)\[')
    df["string"] = df.raw_strings.str[:-11]
    df["string"] = df["string"].str.replace('-', '')
    df.sectID = pd.to_numeric(df.sectID)
    df["top_five"] = df["string"].apply(top_five)
    print(df.loc[df.checksum == df.top_five]['sectID'].sum())

    # Part 2:
    df["room"] = df["raw_strings"].apply(decrypt)
    print(df.loc[df['room'].str.contains('north')]['sectID'])


if __name__ == '__main__':
    main()
