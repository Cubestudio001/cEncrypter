import getpass
def decode_string(index,ens="stdens",createfile=False):
    '''
    This function still requst you to verfiry the legitimacy of input value
    But an illegal input won\'t lead a fatal error
    index -> input
    ens —> standard using
    createfile -> Whether create file on PATH
    '''
    std = open(ens,'r',encoding="utf-8")
    #分割加密字符串，去除乱码
    index = index.split("$")
    for i in range(len(index)):
        if index[i] == '':
            index.pop(i)
            
    index.pop(0)
    index.pop(len(index)-1)

    __return = ""

    #读取标准库
    std1 = std.read()
    std.close()
    std = std1.split("$")
    #分割

    #删除无效数据
    for s in range(len(std)):
        if std[s-1] == '':
            std.pop(s)

    __ens = {}

    for i in std:
        b = i.split(':')
        if b[0] != 'infile':
            try:
                __ens[b[1]] = b[0]
            except:
                continue

    for s in index:       
        
        try:
            __return = __return + __ens[s]
        except:
            __return = __return + str(chr(int(s)))

    return __return

def decode_file(filename,ens="stdens",createfile=False):
    '''
    This function still requst you to verfiry the legitimacy of input value
    An illegal input will lead a fatal error
    filename -> input file name
    ens —> standard using
    createfile -> Whether create file on PATH
    '''
    std = open(ens,'r',encoding="utf-8")
    #分割加密字符串，去除乱码
    index = open(filename,'r',encoding='utf-8')
    index = index.split("$")
    for i in range(len(index)):
        if index[i] == '':
            index.pop(i)
            
    index.pop(0)
    index.pop(len(index)-1)

    __return = ""

    #读取标准库
    std1 = std.read()
    std.close()
    std = std1.split("$")
    #分割

    #删除无效数据
    for s in range(len(std)):
        if std[s-1] == '':
            std.pop(s)

    __ens = {}

    for i in std:
        b = i.split(':')
        if b[0] != 'infile':
            try:
                __ens[b[1]] = b[0]
            except:
                continue

    for s in index:       
        
        try:
            __return = __return + __ens[s]
        except:
            __return = __return + str(chr(int(s)))

    return __return
