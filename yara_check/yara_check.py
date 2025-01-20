import yara,sys,os,shutil
from glob import glob

#############################################################################################
#                                                                                           #
#   use: python yara_check.py [yara rule file] [dir path]                                   #
#                                                                                           #
#       python yara_check.py marewale.yara 'c:\marwale_analys\'                             #
#                                                                                           #
#                                                                                           #
#############################################################################################

class yara_check():
    def __init__(self):
        try:

            self.yara_rule = ".\\yara_rules\\"+sys.argv[1]
            self.yara_check_path = sys.argv[2]
            self.type_path = []
            self.main()

        except Exception as e:
            print(e)
        
    def get_dir_path(self):
        try:
            for root,_,files in os.walk(self.yara_check_path):
                for file in files:
                    file_path = os.path.join(root,file)
                    self.check(file_path)
        except Exception as e:
            print(e)


    def check(self,check_file_path):
        try:
            rules  = yara.compile(filepath=self.yara_rule)
            with open(check_file_path,"rb") as f:
                matches =  rules.match(data = f.read())
            if matches:
                self.type_path.append((matches[0].rule,check_file_path))
        except Exception as e:
            print(e)
            exit()
    
    def movfile(self,src_file_path,dst_file_path):
        if not os.path.isfile(src_file_path):
            print("%s not exist",(src_file_path))
        else:
            fpath,fname = os.path.split(src_file_path)
            if not os.path.exists(dst_file_path):
                os.makedirs(dst_file_path)                       # 创建路径
            shutil.move(src_file_path, dst_file_path +'\\'+ fname)          # 移动文件
            print ("move %s -> %s"%(src_file_path, dst_file_path + fname))
 




    def main(self):    
        self.get_dir_path()
        for file in self.type_path:
            print(file)
            self.movfile(file[1],file[0])
            # self.movfile(file)
            # print(self.type_path)
if __name__=="__main__":
    get_yara = yara_check()

