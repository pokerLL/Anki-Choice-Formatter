import re


path1 = "a.txt"
path2 = "1.txt"

def getText(path):
    f=open(path,'r',encoding='utf-8')
    text = f.read()
    f.close()
    return text

def writeText(text,path):
    f=open(path,'w+',encoding='utf-8')
    f.write(text)
    f.close()

def fileFormat(path):
    text = getText(path)
    text = re.sub("\t| | ","",text)
    text = re.sub("、|．",".",text)
    text = re.sub("（","(",text)
    text = re.sub("）",")",text)
    # text = re.sub("Ｂ","B",text)
    text = re.sub("Ｂ","B",text)
    text = re.sub("Ｃ","C",text)
    text = re.sub("Ｄ","D",text)
    text = re.sub("A\.","\nA.",text)
    text = re.sub("B\.","\nB.",text)
    text = re.sub("C\.","\nC.",text)
    text = re.sub("D\.","\nD.",text)
    # text = re.sub("^[\s*]\n","",text)
    text = re.sub("\n\r","",text)
    writeText(text,path)

def rub(matched):
    value = matched.group()
    return "{{c1::"+value[1:-1]+"}}"

def setCloze(path):
    text = getText(path)
    text = re.sub("\([A|B|C|D]{1,4}\)",rub,text)
    writeText(text,path)

def toAnkiFormat(path1,path2):
    f = open(path1,'r',encoding='utf-8')
    lines = f.readlines()
    f.close()

    f = open(path2,'w+',encoding='utf-8')
    cnt = 0
    for i in lines:
        if len(i)<2:
            continue
        cnt += 1
        i = re.sub("\s","",i)
        f.write(i)
        f.write("+ ")
        if cnt==5:
            f.write('\n')
            cnt = 0
    f.close()
    
if __name__=="__main__":
    fileFormat(path1)
    setCloze(path1)
    input("****清手动删除空行并检查是否有意外情况未处理并手动处理\n****若处理完则键回车以继续\n\
1.若出现空行可用扩展匹配'\\n\\r'解决\n\
2.注意只有空格的行,也必须删除\n\
3.注意题目由于格式问题分成两行的问题,必须放在一行里\n\
4.注意一些题目的ABCD选项并未被分成四行,需要进行检查\n\
****若处理完则键回车以继续\n")
    toAnkiFormat(path1,path2)





'''
日志
    完成时间:2020-12-23
    总时长:2小时左右
    未完成:删除空行
'''













