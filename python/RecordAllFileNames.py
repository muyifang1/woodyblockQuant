import os
import os.path
import xlrd
rootdir = "C:\FromWget\Sheet1"
#rootdir = "C:\FromWget\Sheet2"
#rootdir = "C:\FromWget\Sheet3"
# 将C:\test路径下所有文件名 写入 train_list.txt
file_object = open('good_Part_one.txt','w')
#file_object = open('good_Part_two.txt','w')
#file_object = open('good_Part_three.txt','w')

# 读取文件，判定是否符合成长性
def checkGrow(file_path_name):
    result = False
    excel = xlrd.open_workbook(file_path_name)
    dataRes = excel.sheets()[0]
    # 判定条件
    # 扣非净利润大于0
    # 季度EPS同比增长大于20 %
    # 净利润同比增长率大于20 %
    # 营业收入增长率大于25 %
    # 净资产收益率 - 摊薄大于5
    # 销售毛利率大于20
    if (dataRes.row_values(17)[1] == "OK"
    and dataRes.row_values(18)[1] >20
    and dataRes.row_values(19)[1]>20
    and dataRes.row_values(20)[1]>25
    and dataRes.row_values(21)[1]>5
    and dataRes.row_values(22)[1]>20) : result = True
    return result

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        print  (rootdir+"\\"+filename)
        if(checkGrow(rootdir+"\\"+filename)):
            file_object.write(filename + '\n')
file_object.close()