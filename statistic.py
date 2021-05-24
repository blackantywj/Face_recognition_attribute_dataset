# -*- coding: utf-8 -*-
# !/usr/bin/env python3

'''
Divide face accordance CelebA Attr type.
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import matplotlib.pyplot as plt
import shutil
import os

output_path = "./CelebA_makeup/"
image_path = "./img_celeba"
CelebA_Attr_file = "./list_attr_celeba.txt"
CelebA_ident_file = './identity_CelebA.txt'
Attr_type = range(1, 41)  # Eyeglasses

def main():
    '''Divide face accordance CelebA Attr eyeglasses label.'''
    # trainA_dir = os.path.join(output_path, "trainA")
    # trainB_dir = os.path.join(output_path, "trainB")
    # if not os.path.isdir(trainA_dir):
    #     os.makedirs(trainA_dir)
    # if not os.path.isdir(trainB_dir):
    #     os.makedirs(trainB_dir)
    #
    # not_found_txt = open(os.path.join(output_path, "not_found_img.txt"), "w"
    pl = []
    nl = []

    for attr in Attr_type:
        fn_to_id = {}
        fn_to_attr = {}
        n = 0
        p = 0
        with open(CelebA_Attr_file, "r") as Attr_file:
            Attr_info = Attr_file.readlines()

            Attr_info = Attr_info[2:]
            index = 0
            for line in Attr_info:
                index += 1
                info = line.split()
                # fn_to_attr[info[0]] = info[attr]
                if info[attr] == '-1':
                    n += 1
                else:
                    p += 1
        nl.append(n)
        pl.append(p)
        Attr_file.close()
    with open(CelebA_Attr_file, "r") as Attr_file:
        Attr_info = Attr_file.readlines()
        Attr_info = Attr_info[1]
        Attr_info = Attr_info.split(' ')
        print(len(Attr_info))
    Attr_file.close()
    plt.scatter(Attr_info[0:40], pl)
    plt.scatter(Attr_info[0:40], nl)
    plt.show()
        # print(fn_to_attr)
        # with open(CelebA_ident_file, 'r') as id_file:
        #     id_info = id_file.readlines()
        #     id_info = id_info[:]
        #     # listbbb = id_info.split(' ')
        #     for line in id_info:
        #         info = line.split()
        #         filename = info[0]
        #         fn_to_id.setdefault(info[1], []).append(filename)
        # id_file.close()
        # print(fn_to_id)
        # for ele in fn_to_id:
        #     print(type(ele))
        #     os.makedirs(os.path.join(output_path, 'id' + str(int(ele) - 1)))
        #     index = 0
        #     for fileele in fn_to_id[ele]:
        #         if index < 10:
        #             index_copy = '00' + str(index)
        #         elif 10 <= index and index < 100:
        #             index_copy = '0' + str(index)
        #         filepath_old = os.path.join(image_path, fileele)
        #         filepath_new = os.path.join(output_path + 'id' + str(int(ele) - 1), index_copy + '_' +fn_to_attr[fileele] +'.jpg')
        #         shutil.copy(filepath_old, filepath_new)
        #         index += 1
    # with open(CelebA_Attr_file, "r") as Attr_file:
    #     Attr_info = Attr_file.readlines()
    #     Attr_info = Attr_info[2:]
    #     index = 0
    #     for line in Attr_info:
    #         index += 1
    #         info = line.split()
    #         filename = info[0]
    #         filepath_old = os.path.join(image_path, filename)
    #         if os.path.isfile(filepath_old):
    #             if int(info[Attr_type]) == 1:
    #                 filepath_new = os.path.join(trainA_dir, filename)
    #                 shutil.copyfile(filepath_old, filepath_new)
    #                 count_A += 1
    #             else:
    #                 filepath_new = os.path.join(trainB_dir, filename)
    #                 shutil.copyfile(filepath_old, filepath_new)
    #                 count_B += 1
    #             print("%d: success for copy %s -> %s" % (index, info[Attr_type], filepath_new))
    #         else:
    #             print("%d: not found %s\n" % (index, filepath_old))
    #             not_found_txt.write(line)
    #             count_N += 1
    #
    # not_found_txt.close()
    print('succeed!')
    # print("TrainA have %d images!" % count_A)
    # print("TrainB have %d images!" % count_B)
    # print("Not found %d images!" % count_N)


if __name__ == "__main__":
    main()