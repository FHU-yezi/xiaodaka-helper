print("小打卡自动化汇报信息生成程序 V1.0")
print("初心不变_叶子编写")

print("初始化......")

sum_str = """@白老师
昨日打卡已于 22:00 成功结束，各成员打卡状态如下："""

not_success_member = []
timeout_but_success_member = []

def add_at_the_end_of_str(main_str,add_str):
    new_str = main_str + add_str
    return new_str

while True:
    add_member = input("请输入未打卡成员，输入 q 结束：")
    if add_member == "q":
        break
    elif add_member == "":
        print("请不要输入空值！")
    else:
        not_success_member.append(add_member)
        print("成功！")
        add_member = ""

while True:
    add_member = input("请输入超时成员，输入 q 结束：")
    if add_member == "q":
        break
    elif add_member == "":
        print("请不要输入空值！")
    else:
        timeout_but_success_member.append(add_member)
        print("成功！")
        add_member = ""

overviews_str = """
应打卡 """

overviews_str = add_at_the_end_of_str(overviews_str,"39")
overviews_str = add_at_the_end_of_str(overviews_str," 人，实打卡 ")
overviews_str = add_at_the_end_of_str(overviews_str,str(39-len(not_success_member)))
overviews_str = add_at_the_end_of_str(overviews_str," 人，打卡率 ")

percentage_of_success_member = str((39 - len(not_success_member)) / 39)
percentage_of_success_member = percentage_of_success_member[2:4] + "." + percentage_of_success_member[4:6] + "%"
overviews_str = add_at_the_end_of_str(overviews_str,percentage_of_success_member)

sum_str = add_at_the_end_of_str(sum_str,overviews_str)

sum_str = add_at_the_end_of_str(sum_str,"\n\n未打卡成员如下：\n")

for member in not_success_member:
    add_str = "@" + member +"\n"

    sum_str = add_at_the_end_of_str(sum_str,add_str)

sum_str = add_at_the_end_of_str(sum_str,"（共 ")
sum_str = add_at_the_end_of_str(sum_str,str(len(not_success_member)))
sum_str = add_at_the_end_of_str(sum_str," 人）\n\n")

sum_str = add_at_the_end_of_str(sum_str,"超时，但已打卡成员如下：\n")

for member in timeout_but_success_member:
    add_str = "@" + member +"\n"

    sum_str = add_at_the_end_of_str(sum_str,add_str)

sum_str = add_at_the_end_of_str(sum_str,"（共 ")
sum_str = add_at_the_end_of_str(sum_str,str(len(timeout_but_success_member)))
sum_str = add_at_the_end_of_str(sum_str," 人）\n\n")

sum_str = add_at_the_end_of_str(sum_str,"欲下载更多数据，请登录网页版小打卡管理平台（web.xiaodaka.com）。\n\n")

sum_str = add_at_the_end_of_str(sum_str,"[该消息由 Python 自动化程序生成]")

with open("output.txt","w") as output:
   output.write(sum_str)

print("输出成功！")