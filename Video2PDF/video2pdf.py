"""
Refernce sites : (1)video capturing https://deftkang.tistory.com/182
(2)Image comparing https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/?_ga=2.70968851.2043555178.1635338626-1428126889.1634818476
(3)Export pdf file https://anythink.tistory.com/entry/Python-이미지-파일을-PDF-파일로-변환하기, https://datatofish.com/images-to-pdf-python/
(4)Compress pdf file cf)https://stackoverflow.com/questions/12632291/cant-find-initialization-file-gs-init-ps
"""
#-*- coding:utf-8 -*-
#!/usr/bin/python
import sys
import cv2
import os
import shutil
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from img2pdf import convert
# from PIL import Image
import utils.pdf_compressor as pdf_compressor
# argparse
import argparse as argp

def set_file(input='in', filename=None, eachByFrame=5):
    ln = len(filename.split('/'))
    if (ln == 1):
        filename = './{input}/{filename}'.format(input=input, filename=filename)

    try:
        video = cv2.VideoCapture(filename)

        # Print information # 프레임 너비/높이, 초당 프레임 수 확인
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # 또는 cap.get(3)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 또는 cap.get(4)
        fps = video.get(cv2.CAP_PROP_FPS)  # 또는 cap.get(5)
        loop = int(fps // eachByFrame)  # 30프레임을 기준으로 원하는 캡쳐 수를 추출하기 위한 주기
        # video.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 1280x720, 640x480
        print('프레임 너비: {width}, 프레임 높이: {height}, 초당 프레임 수: {fps}, 캡쳐 주기: {eachByFrame}/sec'
              .format(width=width, height=height, fps=fps, eachByFrame=eachByFrame))
    except Exception as error:
        print(error)

    ln = len(filename.split('/'))
    if (ln > 1):
        filename = filename.split('/')[ln - 1]

    return video, loop, filename

def capture(video=None, loop=0, output='out', init=False):
    output = './{output}'.format(output=output)
    before_image = None
    current_image = None
    try:
        if (init): shutil.rmtree(output)

        if not os.path.exists(output):
            os.makedirs(output)
    except Exception as error:
        print(error)

    print("Capturing started...")
    currentframe = 0
    while(True):
        ret, frame = video.read()

        if ret:
            result = False
            if (int(video.get(1) % loop) == 0):
                name = 'frame{sequence}.png'.format(output=output, sequence=str(currentframe).zfill(5))
                # PNG cv2.IMWRITE_PNG_COMPRESSION, 0~9, 압축율 : 숫자가 크면 높은 압축, 시간 오래 걸림
                # JPEG cv2.IMWRITE_JPEG_QUALITY, 0~100 : 품질, 높을 수록 품질 좋은
                cv2.imwrite('{output}/{name}'.format(output=output, name=name), frame
                            , [cv2.IMWRITE_PNG_COMPRESSION, 5])
                            # , [cv2.IMWRITE_JPEG_QUALITY, 10])

                if (currentframe == 0):
                    before_image = name
                    current_image = name
                    # print('{currentframe} :: {before_image} {current_image}'
                    #       .format(currentframe=currentframe, before_image=before_image, current_image=current_image))
                else:
                    current_image = name
                    # print('{currentframe} :: {before_image} {current_image}'
                    #       .format(currentframe=currentframe, before_image=before_image, current_image=current_image))
                    result = image_compare(target_input=output, before_image=before_image, current_image=current_image)

                if (result):
                    # print('[Skiped] {currentframe} :: before : {before_image} -> current : {current_image}'
                    #       .format(currentframe=currentframe, before_image=before_image, current_image=current_image))
                    pass
                else:
                    print('[Captured] {currentframe} :: before : {before_image} -> current : {current_image}'
                          .format(currentframe=currentframe, before_image=before_image, current_image=current_image))
                    before_image = name
                    currentframe += 1
        else:
            os.remove('{output}/{name}'.format(output=output, name=current_image))
            break

    video.release()
    cv2.destroyAllWindows()
    print("Capturing completed...")

def image_compare(target_input='out', before_image=None, current_image=None):
    rtn = False
    input = './{target_input}/'.format(target_input=target_input)

    before_image = cv2.imread('{input}{before_image}'.format(input=input, before_image=before_image))
    current_image = cv2.imread('{input}{current_image}'.format(input=input, current_image=current_image))

    before_image = cv2.cvtColor(before_image, cv2.COLOR_BGR2GRAY)
    current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)

    m = mse(before_image, current_image)
    s = ssim(before_image, current_image)
    c_m = str('%.2f' % m)
    c_s = str('%.2f' % s)

    if (c_s == '1.00'):
        # print("(True) MSE: %.2f, SSIM: %.2f" % (m, s))
        rtn = True
    else:
        # print("(False) MSE: %.2f, SSIM: %.2f" % (m, s))
        pass

    return rtn

def export_pdf(images_dir=None, pdf_filename=None):
    input = './{images_dir}/'.format(images_dir=images_dir)
    list_of_files = sorted(filter(lambda x: os.path.isfile(os.path.join(input, x)), os.listdir(input)))

    pdf = './pdf'
    try:
        if not os.path.exists(pdf):
            os.makedirs(pdf)
    except Exception as error:
        print(error)

    print("Export pdf started...")
    pdf_lists = []

    # tmp_image = None
    # for file in os.listdir(input): # list_of_files:
    #     if (file.endswith('.png')):
    #         image = Image.open('{input}{file}'.format(input=input, file=file))
    #         cv_image = image.convert('RGB')
    #         pdf_lists.append(cv_image)
    #     tmp_image = pdf_lists[0]
    # tmp_image.save(pdf_filename, save_all=True, append_images=pdf_lists)

    for file in list_of_files: # os.listdir(input):
        if (file.endswith('.png')):
            pdf_lists.append('{input}{file}'.format(input=input, file=file))
    export = convert(pdf_lists, dpi=100, x=None, y=None)
    # export = convert(pdf_lists)
    export_file = '{pdf}/{pdf_filename}'.format(pdf=pdf, pdf_filename=pdf_filename)
    with open(export_file, 'wb') as f:
        f.write(export)
        print('PDF Completed : {pdf_filename}'.format(pdf_filename=pdf_filename))
    f.close()
    print("Export pdf completed...")

    compress_pdf(pdf_filename=pdf_filename)

# PDF Compress
def compress_pdf(pdf='./pdf', pdf_filename=None, quality=0):
    ln = len(pdf_filename.split('/'))
    if (ln == 1):
        pdf_filename = '{pdf}/{pdf_filename}'.format(pdf=pdf, pdf_filename=pdf_filename)

    print("Compress pdf started...{pdf_filename}".format(pdf_filename=pdf_filename))
    origin_file = '{pdf_filename}'.format(pdf=pdf, pdf_filename=pdf_filename)
    c_file = '{pdf_filename}_comp.pdf'.format(pdf=pdf, pdf_filename=pdf_filename.split('.')[0])
    # pdf_compressor.compress(origin_file, c_file, 3)
    pdf_compressor.compress(origin_file, c_file, quality)
    # rename
    os.remove(origin_file)
    os.rename(c_file, origin_file)
    print("Compress pdf completed...")

def main(param=None):
    # filename = '세상을 바꿀 거대한 변화 7가지.mov' 통계가 빨라지는 수학력- 빅데이터 분석에 필요한 기본 수학.mov
    filename = param.filename
    processing = param.env
    output = 'out' # 'ToeicLC'

    # compress pdf only
    if (processing == 'cmp' ):
        pdf_filename = '{pdf_filename}.pdf'.format(pdf_filename=filename.split('.')[0])
        # pdf_filename = '/Users/wisemanlim/Downloads/Study/완벽한IT인프라구축을위한Doker(최종).pdf'
        compress_pdf(pdf_filename=pdf_filename, quality=4)

    if ((processing == 'full') or (processing == 'cnv')):
        video, loop, filename = set_file(filename=filename, eachByFrame=10)
        capture(video=video, loop=loop, output=output, init=True)

    if ((processing == 'full') or (processing == 'pdf')):
        pdf_filename = '{pdf_filename}.pdf'.format(pdf_filename=filename.split('.')[0])
        # export & compress pdf
        export_pdf(images_dir=output, pdf_filename=pdf_filename)

def env_args():
    # command-line options, argumetns : https://brownbears.tistory.com/413, https://docs.python.org/3/library/argparse.html
    parser = argp.ArgumentParser(description='Video to pdf file')

    parser.add_argument('--filename', required=True, help='Inpur video filename(default path=./in, ie)Education.mov')
    parser.add_argument('--env', required=False, default='full'
                        , help='[full,cnv,pdf,cmp] full:convert+pdf+compress, cnv:only image convert, pdf:pdf+compress, cmp:only compress')

    args = parser.parse_args()
    print("In : {filename}, Processing : {env}".format(filename=args.filename, env=args.env))
    return args

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = env_args()
    main(param=args)
