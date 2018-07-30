file_result = open('DownLoadList.txt','w',encoding="utf-8")

# input 天地数码 (SZ300743)
# output wget http://basic.10jqka.com.cn/300743/xls/mainsimple.xls -O D:/FromWget/300743_天地数码.xls
def formatCode(fullNameCode):
    # 截取名字( 之前的文字)
    name = fullNameCode[0:fullNameCode.find(" ")]
    # 截取代码（倒数7 到 倒数1 之间字符串）
    code = fullNameCode[-7:-1]
    result = 'wget http://basic.10jqka.com.cn/%s/xls/mainsimple.xls -O C:/FromWget/%s_%s.xls'%(code,code,name);
    # print (result)
    return result

fileOpen = open("testList.txt",encoding="utf-8")
for line in fileOpen.readlines():
    # print(line.replace('\n',''))
    print(formatCode(line.replace('\n','')))
    file_result.write(formatCode(line.replace('\n','')) + '\n')
file_result.close()

