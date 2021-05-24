import os
import shutil
path='./img_align_celeba_Eyeglasses'
new_path='./img_align_celeba_Eyeglasses_test'
dirs = os.listdir(path)
for dir in dirs:
    print('oldname is:' + dir)  # 输出老的名字
    # temp = "%03d" % int(num)  # 主要目的是在数字统一为3位，不够的前面补0
    # temp = 'id' + str(num)
    oldpathname = os.path.join(path, dir)# 老文件夹的名字
    index = 0
    for file in os.listdir(oldpathname):
        if index < 10:
            index_copy = '00' + str(index)
        elif 10 <= index and index < 100:
            index_copy = '0' + str(index)
        filesnum = int(file.split('_')[0])
        newpathname = os.path.join(new_path, dir)  # 新文件夹的名字
        flag = int(len([file for file in os.listdir(oldpathname)]) * 0.8)
        if int(filesnum) > flag:
            shutil.move(oldpathname + '/' + file, newpathname + '/' + index_copy +'_'+ file.split('_')[1][:-4] + '.jpg')
            index += 1
    # oldname = os.path.join(rootDir, dir)  # 老文件夹的名字
    # newname = os.path.join(rootDir, temp)  # 新文件夹的名字
# for root, dirs, files in os.walk(path):
#     for i in dirs:
#         os.makedirs(os.path.join(new_path, i))
    # for i in range(len(files)):
    #     filesname = files[i].split('.')
    #     filenum = filesname[0].split('_')[0]
    #     # print(int(filenum))
    #     flag = int(len(files) * 0.2)
    #     if (files[i][-3:] == 'jpg') or (files[i][-3:] == 'png')or (files[i][-3:] == 'PNG') or (files[i][-3:] == 'JPG') and int(filesnum) > flag:
    #         file_path = root + '/' + files[i]
    #         new_file_path = new_path+'/' + files[i]
    #         shutil.copy(file_path, new_file_path)


