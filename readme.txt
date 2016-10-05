Git is a version control system.
Git is free software.

在github上修改后，若要把修改合并到本地，则需：
$ git fetch origin
$ git merge origin/master

创建本地git仓库,在文件中：
$ git init
添加文件到本地仓库：
$ git add file1.doc file2.txt file3.py
提交：
$ git commit -m "this is why to change"
把远程仓库与本地仓库关联：
$ git remote add origin https://github.com/Dganzh/algorithm-problem.git
把本地仓库内容推送到远程仓库：
$ git push -u origin master   #首次推送要加-u

查看远程仓库有哪些：
$ git remote [-v]
删除远程仓库(名为origin)：
$ git remote rm origin



