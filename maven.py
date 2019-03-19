#!/usr/bin/python
import re
print('---start to read file-----')

file=open('/Users/zhangxiao/Desktop/python/lib.txt','r')
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
