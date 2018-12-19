# manual

# 1. user_behaviour_statistics.xlsx

Send this file to student, and collecte after they finish their job.

把这个文件发个学生们，等他们都填写完了再收回来

## how to use this xlsx

+ first sheet(第一个表格)

The first sheet input **your** basic infomation, most of cell work well for selection, just few cells need input number. And the last row will check **your** input, green means word done, else need check your input/selection.

第一个sheet是要输入一些你的个人信息，大部分只用选择就可以了，只有很少几个需要输入数字。最后一行有个检车的功能。如果一切ok，那么会是绿色的，否则需要检查一下你的输入了。

---

+ second sheet(第二个表格)

The second sheet, input more **your** detail infomation about app on your mobile phone. And yes, most cells will work well just by selection, few cells need input some number or text. Opps, the first column **DON NOT INPUT OR SELECTION**, it will show the second column text which you colud **SELECT OR INPUT** any apps you want. 

第二个表格，你需要输入一些你常用的手机app信息。大部分都是选择，只需要填写很少的数字或者文字。**注意**第一例不要动，它会显示第二列的内容，第二列的内容是你常用的APP名称，你可以**选择也可以输入**

And, the consequence column you colud input "是"(menas yes) or nothing, but you **must** select one "是" at least in same color cloumns each row, else,the last colunm will show a error. 

后面的表格，你只需要输入“是”就行了（也就是说，可以不用选否），但是**注意**，每行中，同一个颜色的列中，**至少**要一个选了“是”。否则最后一列会检查出错误。

You will get a error signal if you choose duplicate apps.

如果你选了重复的APP，会得到错误提示的

---

+ third sheet(第三个表格)

It will collecting data automatically.

这个表格会自动收集信息，别动！

---

# 2. marketAnalyseEngine.py

## who should read this

Professor,Assistant professor,Teacher, Faculty

## what it done

It will collection all xlsx files which are in same path, collected from student and merge into a asm.xlsx

## how

``` shell
python marketAnalyseEngine
```

And you will get a new file "asm.xlsx"


