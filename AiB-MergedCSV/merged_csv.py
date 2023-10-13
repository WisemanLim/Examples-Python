# -*- coding:utf-8 -*-
# !/usr/bin/python
import pandas as pd

# 파일 경로와 구분자 정보
def set_files(level='Class'):
    filename = '{level}_Level_Aggregate_Counts.csv'.format(level=level)
    file_paths = [
        {'path': './raw/1_211015/{filename}'.format(filename=filename), 'delimiter': ','},
        {'path': './raw/2_merge230919/{filename}'.format(filename=filename), 'delimiter': ','}
    ]
    return file_paths

# 함수를 통해 데이터를 읽고 처리
def process_csv(file_path, delimiter, sample_ids_set):
    df = pd.read_csv(file_path, sep=delimiter)

    # 첫 번째 컬럼을 Class로, 나머지 컬럼을 샘플 아이디로 설정
    df = df.set_index(df.columns[0]).T
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    print(file_path, rows, cols)

    # 구분자가 없는 경우, 샘플 아이디 컬럼의 값이 숫자인지 확인하여 0으로 채움
    if not delimiter:
        for col in df.columns:
            if df[col].dtype == 'int64':
                df[col] = 0

    # 구분자가 두번째 파일에 있는데 첫번째 파일에는 없는 경우,
    # 해당 구분자에 대한 컬럼을 추가하고 첫번째 파일의 샘플 아이디에 대한 값을 0으로 업데이트
    for sample_id in sample_ids_set:
        if sample_id not in df.columns:
            # df[sample_id] = 0
            pass

    return df

if __name__ == "__main__":
    # Domain, Kingdom, Phylum, Class, Order, Family, Tribe, Genus, Species
    levels = ['Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
    for level in levels:
        file_paths = set_files(level)

        # 샘플 아이디를 저장할 집합
        sample_ids_set = set()

        # 각 파일별로 샘플 아이디 추출
        for file_info in file_paths:
            file_path = file_info['path']
            delimiter = file_info['delimiter']

            # 데이터를 읽어와 샘플 아이디 추출
            df = pd.read_csv(file_path, sep=delimiter)
            sample_ids_set.update(df.columns[1:])

        # 결과를 저장할 데이터프레임
        result_df = pd.DataFrame()

        # 각 파일별로 데이터 읽기
        for file_info in file_paths:
            file_path = file_info['path']
            delimiter = file_info['delimiter']

            # 데이터 처리 함수 호출
            df = process_csv(file_path, delimiter, sample_ids_set)

            # 결과 데이터프레임에 추가
            result_df = pd.concat([result_df, df])

        final_output_file = '{level}_merged.csv'.format(level=level)

        # 결과를 CSV 파일로 저장
        result_df.reset_index(inplace=True)
        result_df.rename(columns={'index': level}, inplace=True)
        result_df.to_csv('_output.csv', index=False)

        print('Output saved to output.csv')

        # 읽어들일 파일의 경로
        input_file = '_output.csv'

        # 결과를 저장할 파일의 경로
        output_file = '_transposed_output.csv'

        # CSV 파일을 읽어서 DataFrame으로 변환
        df = pd.read_csv(input_file)

        # Transpose 수행
        df_transposed = df.transpose()

        # Transpose된 DataFrame을 CSV 파일로 저장
        df_transposed.to_csv(output_file, header=False)
        print('Transposed output saved to', output_file)

        # 읽어들일 파일의 경로
        input_file = '_transposed_output.csv'

        # 결과를 저장할 파일의 경로
        output_file = '_final_output.csv'

        # CSV 파일을 읽어서 DataFrame으로 변환
        df = pd.read_csv(input_file, header=None)

        # 첫 번째 행을 샘플 아이디로 설정
        df.columns = df.iloc[0]
        df = df.drop(0)

        # 구분자를 기준으로 샘플 아이디의 값이 없으면 0으로 업데이트
        df = df.fillna(0)

        # Transpose 수행
        df_transposed = df.transpose()
        # Transpose된 DataFrame을 CSV 파일로 저장
        df_transposed.to_csv(output_file, header=False)

        print('Final output saved to', output_file)

        # CSV 파일을 읽어서 DataFrame으로 변환
        df = pd.read_csv(output_file)

        # Transpose 수행
        df_transposed = df.transpose()

        # Transpose된 DataFrame을 CSV 파일로 저장
        df_transposed.to_csv(final_output_file, header=False)
        rows = len(df_transposed.axes[1]) # transpose하여 로그 찍음
        cols = len(df_transposed.axes[0])
        print(final_output_file, rows, cols)

        print('Transposed output saved to', final_output_file)