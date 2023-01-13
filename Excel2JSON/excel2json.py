# Ref : https://github.com/yagneshlp/excel2json
# -*- coding:utf-8 -*-
# !/usr/bin/python

def parse_args():
    import argparse
    import os

    parser = argparse.ArgumentParser(description='Convert Excel to JSON')
    parser.add_argument(
        '-f', '--force',
        help='Overwrite destination file if it already exists')
    parser.add_argument(
        '-o', '--outfile',
        help='Destination file (.json)')
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        default=False,
        help='Be quiet')
    parser.add_argument(
        'src',
        nargs='+',
        type=str,
        help='source file (.xlsx)')
    parser.add_argument(
        '-s', '--sheet',
        help='Selection sheet')

    return parser.parse_args()


def records_for_json(df):
    columns = [str(k) for k in df.columns]
    return [dict(zip(columns, row)) for row in df.values]


def main():
    import os
    import simplejson as json
    import pandas as pd

    class PandasJsonEncoder(json.JSONEncoder):
        def default(self, obj):
            import datetime
            if any(isinstance(obj, cls) for cls in (datetime.time, datetime.datetime, pd.Timestamp)):
                return obj.isoformat()
            elif pd.isnull(obj):
                return None
            else:
                return super(PandasJsonEncoder, self).default(obj)

    args = parse_args()

    for src in args.src:
        if args.outfile:
            dst = args.outfile
        else:
            path, _ = os.path.split(src)
            filename, _ = os.path.splitext(os.path.basename(src))
            dst = f'{path}/{filename}.json'

        if args.sheet:
            sheet = pd.read_excel(src, args.sheet)
        else:
            sheet = pd.read_excel(src, "Sheet1")
        records = records_for_json(sheet)

        mode = 'w' if args.force else 'x'
        # 한글 깨짐 : https://datamod.tistory.com/104
        with open(dst, mode, encoding='UTF-8-sig') as f:
            json.dump(records, f, ignore_nan=True, cls=PandasJsonEncoder, indent=4, ensure_ascii=False)

        if not args.quiet:
            arrow = '\u2192'
            print(f'{src} {arrow} {dst}\nJSON generated successfully!')


if __name__ == '__main__':
    # python3 excel2json.py. / xls / NutrientsByFood.xlsx - -sheet 20221208
    main()
