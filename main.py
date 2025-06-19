import os
import time

from config import comfyui_path,direct_path

old_file_list = set()
new_file_list = set()
file_counter = 1

#打印边界，美化界面
def print_boundaries():
   for i in range(1,21):
      print('=',end='=')
   print()

#预处理文件夹里面的文件
def preprocess_legacy_files():
   old_file_list.update( os.listdir(comfyui_path))

#查看是否有新文件
def check_files():
   global file_counter
   new_file_list.update( os.listdir(comfyui_path))
   new_file = new_file_list - old_file_list
   if new_file:
      print('发现文件，正在处理...')
      for temp_file in new_file:
         move_rename_files(temp_file,file_counter)
         print(f'第{file_counter}个文件已处理')
         file_counter += 1
      old_file_list.update(new_file)

#处理文件
def move_rename_files(file,number):
   extension = os.path.splitext(file)[1]
   new_file_name = f"{number}{extension}"
   file_name = os.path.join(comfyui_path,file)
   dir_name = os.path.join(direct_path,new_file_name)
   os.rename(file_name,dir_name)






print_boundaries()
print("程序启动请按start")
print("完成之后请手动关闭程序")
print_boundaries()

if input("输入以开始") == "start":
   print("好的，程序开始")

   preprocess_legacy_files()

   print("开始处理原有文件")
   preprocess_legacy_files()
   print("处理完毕")

   preprocess_legacy_files()

   while True:
      print("开始检查文件")
      check_files()
      print("检查完成，歇2秒")
      time.sleep(2)


