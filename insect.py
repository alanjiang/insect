#!/usr/bin/python
import re,os


print('---start to extract jsp files-----')

'''file=open('/Users/zhangxiao/Desktop/python/samples','r')
dest_file=open('/Users/zhangxiao/Desktop/python/lib_pom.xml','w')
for line in file:
  if (line.strip() !='' ):
      m = re.match( r'(.*).jar', line, re.M|re.I)
      print(m.group(1))
      artifactId=m.group(1)
      dest_file.write('<dependency>\t\n')
      dest_file.write('<groupId>my</groupId>\t\n')
      dest_file.write('<artifactId>'+artifactId+'</artifactId>\t\n')
      dest_file.write('<version>0.0.0</version>\t\n')
      dest_file.write('<scope>system</scope>\t\n')
      dest_file.write('<systemPath>${base.dir}/src/main/webapp/WEB-INF/lib/'+line.strip()+'</systemPath>\t\n')
      dest_file.write('</dependency>\t\n')

file.close()
'''


path="/Users/zhangxiao/Desktop/python/samples"

dest="/Users/zhangxiao/Desktop/python/samples/result.txt"

def deep_read(path):

    dest_file=open(dest,'w')
    parents=os.listdir(path)

    for parent in parents:

        child=os.path.join(path,parent)

        if os.path.isdir(child):
           deep_read(child)
        else:
           print('-file='+child)
           file=open(child,'r',encoding='utf-8')

           row=0
           
           for line in file:
               
               
               if ('' != line.strip()):
                  row+=1
                  print(row)
                  repeats={}
                  strs=re.findall(r'<emp:[a-zA-Z0-9]{1,}(.*)/>',line)
                  

                  for st in strs:

                       '''print(st)'''
                       array=re.findall(r'([a-zA-Z0-9]{1,}=[\"\']{1}[a-zA-Z0-9]{1,}[\"\']{1})',st)
                       print(array)
                       for kv in array:

                           '''print(kv)'''
                           
                           if kv in repeats:
                              repeats[kv]=repeats[kv]+1
                           else:
                              repeats[kv]=1


                  for (k,v) in repeats.items():
                        if (v>1):
                           print('get the repeat one')
                           print (k,v)

                           dest_file.write('file:'+child+',rows='+str(row)+',repeat key='+k+',times='+str(v)+'\t\n')

      
                 
                      
class repeat_file:
   def __init__(self):
       self.path=''
       self.lineno=0
       self.repeats={}
    
if __name__=='__main__':

   path="/Users/zhangxiao/Desktop/python/samples"
   
   deep_read(path)
