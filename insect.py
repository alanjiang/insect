#!/usr/bin/python
import re,os
from time import strftime,gmtime



time=strftime("%Y-%m-%d-%H%M%S", gmtime())

path="/Users/zhangxiao/Desktop/python/samples"

dest="/Users/zhangxiao/Desktop/python/samples/result-"+time+".txt"

print('----爬虫分析开始，源目标'+path+',分析结果呈现位置：'+dest)

def deep_read(path):

    dest_file=open(dest,'a')
    parents=os.listdir(path)
    
    for parent in parents:

        child=os.path.join(path,parent)

        if os.path.isdir(child):
           deep_read(child)
        else:
           print('-处理文件：'+child)
           file=open(child,'r',encoding='utf-8')    
           extension=os.path.splitext(child)[1]
           '''print('extension='+extension)'''
           if ('.jsp' != extension):

               continue
        
           strs=re.findall(r'<emp:[a-zA-Z0-9]{1,}(.*)/?>',file.read().replace('\n','').replace('\t',''))          
           for st in strs:

               repeats={}
               '''找出每一条自定义标签条目<emp:XXX> </emp>|<emp:XXX /> 中的key=value,统计重复的属性'''
               array=re.findall(r'([a-zA-Z0-9]{1,}=[\"\']{1}[a-zA-Z0-9]{1,}[\"\']{1})',st)
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

                      dest_file.write('file:'+child+',repeat key:'+k+',times='+str(v)+'\t\n')

           file.close()
    dest_file.close()
     
      
                 
                      
class repeat_file:
   def __init__(self):
       self.path=''
       self.lineno=0
       self.repeats={}
    
if __name__=='__main__':

   path="/Users/zhangxiao/Desktop/python/samples"
   
   deep_read(path)

   print ('---本次爬虫分析结束----')
