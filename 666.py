import os
import shutil
def ALLrename(data_path, out_path, names, ImageGS):
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    list_dir = os.listdir(data_path)
    for index,filename in enumerate(list_dir):
        img_file = data_path + "/" + filename
        filename1 = os.path.splitext(img_file)[1]  # 读取文件后缀名
        filename0 = os.path.splitext(img_file)[0]  # 读取文件名
        shutil.copy(img_file, out_path + "/" + names + str(index) + ImageGS)


if __name__ == "__main__":
    ALLrename("E:/classification-keras-main/img", "output", "4-", ".tiff")
    print('重命名完毕！！')