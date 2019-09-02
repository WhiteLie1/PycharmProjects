#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/8 11:04
# @Author : chenxin
# @Site : 
# @File : test4.py
# @Software: PyCharm
Create or Replace
Procedure
Pro_DepEmpInfo
(DepId in varchar - -输入参数，部门编号)
as
begin
Declare cursor cur_emp IS select * from Employee where department=DepID; --  定义游标
v_empRow Employee % Rowtype;             --定义记录变量
Begin
open cur_emp;             --打开游标
loop
fetch cur_emp into v_empRow;--提取游标当前行数据
exit when cur_emp % notfound;--如果没有任何数据，则退出循环
dbms_output.put_line(cur_emp % rowcount || --输出雇员信息表
',雇员编号：' || v_empRow.EmpNumber ||
',雇员姓名：' || v_empRow.EmpName ||
',性别：' || v_empRow.Sex ||
',电话：' || v_empRow.Phone ||
',薪水：' || v_empRow.Salary);
end
loop;
close
cur_emp;
--关闭游标
end;
End
Pro_DepEmpInfo;

