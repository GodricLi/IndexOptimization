# _*_ coding=utf-8 _*_


import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123', database='db1')
cursor = conn.cursor()
"""
#1. 一定是为搜索条件的字段创建索引，比如select * from s1 where id = 333;就需要为id加上索引

#2. 在表中已经有大量数据的情况下，建索引会很慢，且占用硬盘空间，建完后查询速度加快
比如create index idx on s1(id);会扫描表中所有的数据，然后以id为数据项，创建索引结构，存放于硬盘的表中。
建完以后，再查询就会很快了。
"""
# 测试索引
# 1.创建表
create_table = """
                create table s1(
                id int,
                name char(20),
                gender char(6),
                email varchar(50)
                );
            """
# 2.创建存储过程，实现批量插入记录
"""
delimiter $$                            #声明存储过程的结束符号为$$
create procedure auto_insert1()
BEGIN
    declare i int default 1;
    while(i<1000000)do
        insert into s1 values(i,'egon','male',concat('egon',i,'@oldboy'));
        set i=i+1;
    end while;
END$$                                    #$$结束
delimiter ;                              #重新声明分号为结束符号
"""
# 3.查看存储过程
show_procedure = "show create procedure auto_insert1\G"

# 4.调用存储过程
call_procedure = "call auto_insert1()"

