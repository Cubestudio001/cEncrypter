import random
import getpass
def encode(file,ens,method="l",createfile=False,filename="a.end"):
    '''
    Encrpty file to an *.end encrypted file
    file -> file name; ens -> standard library
    P.S. Please verfiry if the file and ens is avaliable!
    method -> "s" or "c"
    S:Return a string  C:Return a dictionary
    createfile:Whether create a encoded file
    filename:the name of the created file(if "createfile" is true)
    '''
    #请自行验证文件合法性，此程序没有验证过程
    inp = open(file,'r',encoding="utf-8")
    #导入文件
    #从此版本起，ens直接接收传入的str

    
    std = ens.split("$")
    #分割

    #删除无效数据
    for s in range(len(std)):
        if std[s-1] == '':
            std.pop(s)

    #数值保存在一个字典里
    __return = {}
    #优先级保存在一个列表里
    priv = []

    for i in std:
        b = i.split(':')
        if b[0] != 'infile':
            try:
                __return[b[0]] = b[1]
            except:
                continue



    #返回一个编译的字典标准
    if method == 'c':
        return __return
    #返回已编译的字符串
    if method == 'l':
        pre_exec = inp.read()
        output = list(pre_exec)
        __out = ''
        for s in range(random.randint(50,320)):
            __out += random.choice('abcdefghijklmnopqrstuvwxyz!@#%^&*()')
        for i in output:
            __out = __out + "$"
            try:
                __out = __out+__return[i]
            
            except:
                __out = __out + str(ord(str(i)))
        __out += '$'
        for s in range(random.randint(50,320)):
            __out += random.choice('abcdefghijklmnopqrstuvwxyz!@#%^&*()')
        #如果选择输出为一个文件
        if createfile:
            s = open(filename,'w',encoding='utf-8')
            s.write(__out)
        inp.close()
        return __out
    
    
def licence(file,user=getpass.getuser(),regist=True,needlogin=False,password=""):
    '''
    An *.end file must work with a licence
    file -> file name
    user -> Decoding program will check the system user's name
    regist -> If the program will check username
    needlogin -> Whether need another password
    password -> The password if "needlogin" is true
    '''
    l = open(file+".enl",'w',encoding="utf-8")
    l.close()
    l = open(file+".enl",'a',encoding = "utf-8")
    
    mass = ''
    #向许可证文件中添加乱码和信息
    for i in range(random.randint(100,5000)):
        mass = mass + random.choice('abcdefghijklmnopqrstuvwxyz!@#%^&*()')
    l.write(mass)
    l.write("${0}${1}${2}${3}${4}$".format(file,user,str(regist),str(needlogin),password))
    mass=''
    for i in range(random.randint(1000,6000)):
        mass = mass + random.choice('abcdefghijklmnopqrstuvwxyz!@#%^&*()')
    l.write(mass)
    l.close()

def encode_str(inp:str,ens,method="l",createfile=False,filename='a.end'):
    #从此版本起，ens直接接收传入的str

    
    std = ens.split("$")
    #分割

    #删除无效数据
    for s in range(len(std)):
        if std[s-1] == '':
            std.pop(s)

    #数值保存在一个字典里
    __return = {}
    #优先级保存在一个列表里
    priv = []

    for i in std:
        b = i.split(':')
        if b[0] != 'infile':
            try:
                __return[b[0]] = b[1]
            except:
                continue



    #返回一个编译的字典标准
    if method == 'c':
        return __return
    #返回已编译的字符串
    if method == 'l':
        pre_exec = inp
        output = list(pre_exec)
        __out = ''
        for s in range(random.randint(50,320)):
            __out += random.choice('abcdefghijklmnopqrstuvwxyz!@#%^&*()')
        for i in output:
            __out = __out + "$"
            try:
                __out = __out+__return[i]
            
            except:
                __out = __out + str(ord(str(i)))
        __out += '$'
        for s in range(random.randint(50,320)):
            __out += random.choice('abcdefghijklmnopqrstuvwxyz!@#%^&*()')
        #如果选择输出为一个文件
        if createfile:
            s = open(filename,'w',encoding='utf-8')
            s.write(__out)
        
        return __out