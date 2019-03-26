#!/usr/bin/python
import re,os
from time import strftime,gmtime

def parseTags(tags,st,child,dest_file):
    '''处理每个文件的自定义标签'''
    list=tags.split("|")
    for tag in list:
        
        strs=re.findall(r'((<emp:'+tag+'\s*([a-zA-Z0-9_-]{1,}=[\'\"]{1}[a-zA-Z0-9_-\u4E00-\u9FA5]{1,}[\'\"]{1}\s*)+)/?>)',st,re.S|re.M)

        print(strs)
        ''' list<tuple> 结构'''
        '''print(type(strs))'''

        '''print(strs)'''

        for tpl in strs:
        
               '''print(type(tpl))'''

            

               '''for key, value in enumerate(tpl):'''
               '''字典记录每个JSP文件中的每个标签中的重复属性'''
               repeats={}
               '''print('---from '+tpl[0]+' finding duplicates---')'''
               '''找出每一条自定义标签条目<emp:XXX> </emp>|<emp:XXX /> 中的key=value,统计重复的属性'''
               array=re.findall(r'([a-zA-Z0-9_-]{1,}=[\"\']{1}[a-zA-Z0-9_-\u4E00-\u9FA5]{1,}[\"\']{1})',tpl[0])
               '''print(array)'''
               for kv in array:
                           
                   if kv in repeats:
                      repeats[kv]=repeats[kv]+1
                   else:
                      repeats[kv]=1




               for (k,v) in repeats.items():
                   if (v>1):
                      '''print('get the repeat one')'''
                      '''print (k,v)'''

                      dest_file.write('file:'+child+',<emp:'+tag+' '+k+' 重复次数：'+str(v)+'\t\n')


    print('--'+child+' <emp:'+tag+' is done ---')

def deep_read(path,whitelist):

    dest_file=open(dest,'a')
    parents=os.listdir(path)
    
    for parent in parents:

        child=os.path.join(path,parent)

        if os.path.isdir(child):
           deep_read(child,whitelist)
        else:
           
           file=open(child,'r',encoding='utf-8')    
           extension=os.path.splitext(child)[1]
           '''print('extension='+extension)'''
           if ('.jsp' != extension):
               continue
           
           print('-处理文件：'+child)

           ''' (?:XXX):不参与分组'''
           strs=re.findall(r'(<emp:(?:'+whitelist+')(?:\s*[0-9A-Za-z]{1,20}\s*=\s*[\"\']{1}[0-9A-Za-z\u4E00-\u9FA5\-_]{1,}[\"\']{1}\s*){1,}>)|(<emp:(?:'+whitelist+')(?:\s*[0-9A-Za-z]{1,}\s*=\s*[\"\']{1}[0-9A-Za-z\u4E00-\u9FA5\-_]{1,}[\"\']{1}\s*){1,}/>)|(<emp:(?:'+whitelist+')(?:\s*[0-9A-Za-z]{1,}\s*=\s*[\"\']{1}[0-9A-Za-z\u4E00-\u9FA5\-_]{1,}[\"\']{1}\s*){1,}</emp:(?:'+whitelist+'))',file.read(),re.S)
           print(type(strs))
           print(strs)
          
           for tples in strs:
               
               print(type(tples))

               for tple in tples:

                   if ''==tple :

                        '''print('--blank--')'''
                   else:

                        tear_down_tuple(tple,child,dest_file)
               
               '''parseTags(whitelist,st,child,dest_file)'''
               

               

           file.close()
    dest_file.close()
     
      
'''<emp key="value"  /> 中提取重复的key和id值 , 每次处理一个标签'''
def tear_down_tuple(tple,child,dest_file):
    print('---tear down goes---') 
    array=re.findall(r'\s*([a-zA-Z0-9_-]{1,}\s*=\s*[\"\']{1}[a-zA-Z0-9_-\u4E00-\u9FA5]{1,}[\"\']{1})',tple)
    print(array)
    repeats={}
    id=''
    for entry in array:
        '''print(entry)'''
        key=entry.split('=')[0]
        value=entry.split('=')[1]
        if "id"== key or 'id'== key :
            id=value
            print ('key='+key+'id='+value)
         
        if key in repeats:
           repeats[key]=repeats[key]+1
        else:
           repeats[key]=1
           
    for (k,v) in repeats.items():
        if (v>1):
                      
           dest_file.write('file:'+child+','+tple[0:20]+'--- id='+id+' ,重复的KEY为：'+k+' 重复次数：'+str(v)+'\t\n')
               

def itera_tuple():


    tpl_list=[('<emp:select sample1="a1" sample1="a1" sample2="b2" sample2="b2" x="y">',

               '<emp:select sample1="a1" sample1="a1" sample2="b2" sample2="b2" x="y"' 'x="y"'),

              ('<emp:select changerow1="a1" changerow1="a1" changerow23="23" changerow23="23"\n     fg="126">',

               '<emp:select changerow1="a1" changerow1="a1" changerow23="23" changerow23="23"\n     fg="126"', 'fg="126"'),

              ('<emp:select id="select-123_123" id="select-123_123" dictname="ABC_DGH_KKJ"/>',

               '<emp:select id="select-123_123" id="select-123_123" dictname="ABC_DGH_KKJ"', 'dictname="ABC_DGH_KKJ"')]
   
    for tpl in tpl_list:
     
         print(tpl[0])
   
         for k, v in enumerate(tpl):

             '''print (str(k))'''
             print(type(v))
    
                      
class repeat_file:
   def __init__(self):
       self.path=''
       self.lineno=0
       self.repeats={}
    
if __name__=='__main__':

   
   time=strftime("%Y-%m-%d-%H%M%S", gmtime())

   path="/Users/zhangxiao/Desktop/python/samples"

   dest="/Users/zhangxiao/Desktop/python/samples/result-"+time+".txt"

   print('----爬虫分析开始，源目标'+path)
   whitelist='select|text|number|textarea'
   path="/Users/zhangxiao/Desktop/python/samples"
   
   deep_read(path,whitelist)

   print ('---本次爬虫分析结束,分析结果呈现位置：'+dest)
   
   '''
   itera_tuple()
   '''
