import os
import os.path
import xlrd
# 读取文档路径
rootdir = r"D:\FromWget\test"
# 将符合金融行业的文件名写入以下文档
file_object = open('Result.txt','w',encoding='utf-8')
# 最后更新日期
last_Update_Date = "2018-06-30"
# 结果集列表
finance_List = [] # 金融产品结果
last_Update_List = [] # 符合最后更新日期结果
grow_List = [] # 符合成长条件结果

# 读取文件，根据A16是否有值 判断 是否是金融行业
def checkFinance(file_path_name):
    result = False
    excel = xlrd.open_workbook(file_path_name)
    dataRes = excel.sheets()[0]
    # 判定条件,根据A16是否有值 判断 是否是金融行业
    if (dataRes.row_values(15)[0] == "") : result = True
    return result

# 读取文件，判断最新数据日期是否满足条件
def checkLastUpdateDate(file_path_name):
    result = False
    excel = xlrd.open_workbook(file_path_name)
    dataRes = excel.sheets()[0]
    # 判定条件,数据最新更新日期是否满足条件
    if (dataRes.row_values(0)[1] == last_Update_Date) : result = True
    return result

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
#        print(rootdir+"\\"+filename)
        if(checkFinance(rootdir+"\\"+filename)):
            finance_List.append(filename)
        if(checkLastUpdateDate(rootdir+"\\"+filename)):
            last_Update_List.append(filename)
        if(checkGrow(rootdir+"\\"+filename)):
            grow_List.append(filename)

#根据结果集输出
file_object.write("金融行业产品文件名称：" + '\n')
print("================= 金融行业产品文件名称：======================")
for str_Item in finance_List:
    file_object.write(str_Item + '\n')
    print(str_Item)
file_object.write("================= 数据最终更新日期为 " +last_Update_Date+" 的数据文件名称：================= "+ '\n')
print("数据最终更新日期为 " +last_Update_Date+" 的数据文件名称：")
for str_Item in last_Update_List:
    file_object.write(str_Item + '\n')
    print(str_Item)
file_object.write("================= 符合成长条件的结果：================= "+ '\n')
print("符合成长条件的结果：")
for str_Item in grow_List:
    file_object.write(str_Item + '\n')
    print(str_Item)

file_object.close()