import cgi, os

form=cgi.FieldStorage()

fileitem = form['file']

if fileitem.filename:
   # 设置文件路径 
   fn = os.path.basename(fileitem.filename)
   if not os.path.exists('tmp'):
       os.makedirs('tmp')
   open('tmp/' + fn, 'wb').write(fileitem.file.read())