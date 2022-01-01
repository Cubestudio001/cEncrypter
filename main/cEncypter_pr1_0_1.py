import ensreader
import getpass
import endreader

print("cEncrypter")
print("---------------")
print("Design by CubeStudio")

test_update = True

while True:
    #获取用户行为（加密或解密）
    action = ''
    action = input("加密或解密?[加密/解密]:")


    if action == '加密':
        #加密类型询问循环
        while True:
            dc_type = input("请输入加密类型:[str/doc]:")
            if dc_type == 'str' or dc_type == 'doc':
                break
            else:
               print("非法输入!")
               continue
        
        #加密文件询问循环
        while True:
            if dc_type == 'doc':
                #注:后_operate(prot)和operate(orig)统一用operate代替
                operate = input("请输入文件名（包含后缀！）:")
                try:
                    open(operate,'r')
                except:
                    print('文件名输入有误或文件不存在,加密字符串请使用str模式！')
                else:
                    break
            if dc_type == 'str':
                break

        while True:        
            #询问加密标准库
            _std = input("请输入加密标准库：")
            try:
                open(_std,"r",encoding = "utf-8")
            except:
                print("文件不存在！")
                continue
            else:
                std = open(_std,"r",encoding='utf-8')
                break
        while True:
            _createf = input('是否创建文件?')
            
            
            if _createf == '是':
                _createf = True
                break
            elif _createf == '否':
                _createf = False
                break
            else:
                print('非法输入!')
                continue
        if dc_type == 'doc': 
            ecode = ensreader.encode(operate,_std,method='l',createfile=_createf)
        elif dc_type == 'str':
            ecode = ensreader.encode_str(operate,_std,method='l',createfile=_createf)
        '''
        if _createf:
            while True:
                __usepassword = input('是否在解密时需要密码？[是/否]:')
                if __usepassword == '是':
                    pass_enl = input('请输入密码:')
                    lic = ensreader.licence(_operate,getpass.getuser(),True,pass_enl)
                    break
                if __usepassword == '否':
                    lic = ensreader.licence(_operate,getpass.getuser(),False,"None")
                    break
                else:
                    print('非法输入！')
        '''
        input('加密已完成，按任意键继续，加密结果是(冒号以后)：{0} '.format(ecode))
    elif action == '解密':
        while True:
            file_or_string = input('请问输入一个文件还是一个字符串?[doc(尚未完成)/str]:')
            if file_or_string == 'str':
                __decript_string = input('请输入要解密的内容:')
                __out = endreader.decode_string(__decript_string)
                print("解密已完成，原内容是:"+__out)
                break
            elif file_or_string == 'doc':
                print("您可以期待我们开发出优秀的文档解密功能!")
                pass
            else:
                print("非法输入")
    elif action == 'q':
        break
    else:
        print('非法输入！退出请输入\'q\'')
input("感谢您使用，期待与您再见\n按任意键退出...")
        