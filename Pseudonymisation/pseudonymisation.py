"""
# 개인정보 가명/익명조치 : 결합키/일련번호 생성 및 결과물저장(결합키관리기관 전달용, 결합전문기관 전달용)
# Input params : 사용데이터 파일, salt, 결합키(컬럼리스트)
"""
#-*- coding:utf-8 -*-
#!/usr/bin/python
import pandas as pd
# 결합키 생성 알고리즘
import hashlib
import base64
import argparse as argp

_SALT_ = '0123456789abcdef'

def generateKey2Hexa(name, gender, age):
    # ex) 홍길동01234456789abcdefm56
    result = f"{name}{gender}{age}{_SALT_}"

    # 해시값 생성
    # hash = hashlib.sha224(result.encode())
    hash = hashlib.sha256(result.encode())
    # hash = hashlib.sha512(result.encode())

    # 헥사 인코딩
    value = hash.hexdigest().lower()
    # value = hash.hexdigest().upper()

    return value

def generateerateKey2Base64(name, gender, age):
    # ex) 홍길동01234456789abcdefm56
    result = f"{name}{gender}{age}{_SALT_}"

    # 해시값 생성
    hash = hashlib.sha256(result.encode())

    # BASE64인코딩
    value = base64.b64encode(hash.digest())

    return value

 # Columns 적용 로직 수정 필요
def generateKey2HexaColumns(columns = None):
    # ex) 홍길동01234456789abcdefm56
    result = "".join(f"{col}" for col in columns)
    result += f"{_SALT_}"
    # print(result)

    # 해시값 생성
    # hash = hashlib.sha224(result.encode())
    hash = hashlib.sha256(result.encode())
    # hash = hashlib.sha512(result.encode())

    # 헥사 인코딩
    value = hash.hexdigest().lower()
    # value = hash.hexdigest().upper()

    return value

def main(param=None):
    filename = param.filename
    salt = param.salt
    if (salt is not None): _SALT_ = salt
    with open('salt.salt', 'w', encoding='utf-8') as f: f.write(_SALT_)
    merge_key = param.columns
    merge_key = merge_key.split(',')
    # print(merge_key)

    # generateerateKey2Base64('강원권', '', '48')
    # generateKey2Hexa('강원권', '', '48')

    # 원본 파일 적재, default : utf-8
    df = pd.read_csv(filename)
    # print(df.head(3))

    # 결합키 생성
    # 'A', 'B', 'C' 컬럼(속성)에 대하여 결합키를 생성하여 ‘merge_key key’ 컬럼(속성)에 결합키 추가
    # 컬럼의 마지막에 'merge_key key' 컬럼 추가
    # df['merge_key'] = df.apply(lambda df:generateKey2Hexa(df['A'], df['B'], df['C']), axis=1)
    # 지정한 컬럼의 순번(‘ 에 'merge_key key’ 컬럼 추가
    # df.insert(0, 'merge_key', df.apply(lambda df:generateKey2Hexa(df['이름'], df['성별'], df['나이']), axis=1))
    df.insert(0, 'merge_key', df.apply(lambda df:generateKey2HexaColumns(df[col] for col in merge_key), axis=1))

    # 일련번호 생성
    # df['serial_no'] = df.reset_index().index+1
    df.insert(1, 'serial_no', df.reset_index().index+1)
    print(df.head(3))

    # 결합키와 일련번호를 추출한 dataframe
    df_key = df[['merge_key', 'serial_no']]

    # 결합키관리기관 전달용 '결합키'+'일련번호' 파일저장
    df_key.to_csv('./결합키관리기관_전달용.csv', index=False)

    # 일련번호와 결합대상정보를 추출한 dataframe
    df_target = df.drop(['merge_key'], axis=1)

    # 결합전문기관 전달용 '일련번호'+'결합대상정보' 파일저장
    df_target.to_csv('./결합전문기관_전달용.csv', index=False)

def env_args():
    # command-line options, argumetns : https://brownbears.tistory.com/413, https://docs.python.org/3/library/argparse.html
    parser = argp.ArgumentParser(description='가명처리(Pseudonymisation)')

    parser.add_argument('--filename', required=True, help='Input csv filename(default path=./, ie)sample_small_1000_utf8.csv')
    parser.add_argument('--columns', required=True, default='이름,성별,나이', help='Merge key list : "이름,성별,나이"')
    parser.add_argument('--salt', required=False, default='0123456789abcdef', help='Input salt value')

    args = parser.parse_args()
    print("Target File : {filename}, Merging Columns : {columns}".format(filename=args.filename, columns=args.columns))
    return args

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # python3 pseudonymisation.py --filename sample_small_1000_utf8.csv --columns "이름,성별,나이"
    args = env_args()
    main(param=args)