第一次修改内容：
创建工程

第二次提交内容：
1.使用open文件代替从命令行输入，根据打印文件别名，理解文件别名f与stdin等效，而非f.read()与stdin等效，如果以f.read()作为输入，则lines方法会按单词进行解析而非行
2.调试yield，理解yield生成器可以实现循环操作，且yield具备return功能，下一次循环时从yield下一条语句开始执行
3.装饰器@的功能是动态给方法增加功能
4.增加打印，可对比output.html与test_output.html理解yield