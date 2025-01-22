import yara,sys,os,shutil
from tqdm import tqdm
from glob import glob

#############################################################################################
#                                                                                           #
#   use: python yara_check.py  [dir path]                                                   #
#                                                                                           #
#       python yara_check.py  'c:\marwale_analys\'                                          #
#                                                                                           #
#                                                                                           #
#############################################################################################

class yara_check():
    def __init__(self):
        try:

            self.yara_rule = ".\\yara_rules\\"
            self.yara_check_path = sys.argv[1]
            self.type_path = []
            self.rules_path = []
            # self.get_yara_path()
            self.main()

        except Exception as e:
            print(e)
        
    def get_dir_path(self,yara_rule_file_path):
        try:
            for root,_,files in os.walk(self.yara_check_path):
                for file in files:
                    file_path = os.path.join(root,file)
                    self.check(file_path,yara_rule_file_path)
        except Exception as e:
            print(e)

    def get_yara_path(self):
        for root,_,rules in os.walk(self.yara_rule):
            for rule in rules:
                file_path = os.path.join(root,rule)
                self.rules_path.append(file_path)
                # print(file_path)

    def check(self,check_file_path,yara_rule_file_path):
        try:
            rules  = yara.compile(filepath=yara_rule_file_path)
            with open(check_file_path,"rb") as f:
                matches =  rules.match(data = f.read())
            if matches:
                self.type_path.append((matches[0].rule,check_file_path))
        except Exception as e:
            print(e)
            exit()
    
    def movfile(self,src_file_path,dst_file_path):
        if not os.path.isfile(src_file_path):
            print("文件不存在",(src_file_path))
        else:
            fpath,fname = os.path.split(src_file_path)
            if not os.path.exists(dst_file_path):
                os.makedirs(dst_file_path)                       # 创建路径
            shutil.move(src_file_path, dst_file_path +'\\'+ fname)          # 移动文件
            print ("move %s -> %s"%(src_file_path, dst_file_path + fname))
 




    def main(self):    
        self.get_yara_path()
        test = tqdm(self.rules_path,ncols=100)
        for rule in test:
            self.get_dir_path(rule)
            for file in self.type_path:
                self.movfile(file[1],file[0])
                # self.movfile(file)
                # print(self.type_path)
if __name__=="__main__":
    get_yara = yara_check()

