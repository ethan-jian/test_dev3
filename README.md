# test_dev3
测试开发项目目录

笔记
cmder
git add hello.py
git commit -m 
git push origin master
git pull origin dev

查看分支
git branch -l 


创建一个分支
git branch dev

切换分支
git checkout dev

把代码push到dev分支
git add dev.py
git commit -m 
git push origin dev

把dev合并到master分支
git merge dev
git push origin master


解决代码冲突:
	git pull origin dev发现有冲突
	提交冲突的文件
	git add hello.py
	git commit -m "A dev change"
	解决冲突
	vim hello.py
	git add hello.py
	git commit -m "A and B 解决冲突"

django 处理过程：
    1.url指定路径/hello/
    2.setting.py 找到url的配置文件
    3.urls.py匹配路径/hello/,把请求指到views文件
    4.在views.py 写Response的处理,把template目录下html文件返回给前端
