

import os

from pathlib import Path



tmpl = """xxx株式会社　xxx様



お世話になります。xxxです。



現在をもちまして、本日の作業を終了いたします。



----------------------------------------------------------------------

作業時間：

{time1}～{time2}（休憩{rest1}）



作業内容：

・{work}



作業予定：

{next_date} 9:00～18:00（休憩1:00）

・{next_work}

----------------------------------------------------------------------





ご確認のほど、よろしくお願いいたします。



xxx"""







def embed(current_date, time1, time2, rest1, work, next_date, next_work):

    return tmpl.format(current_date=current_date, time1=time1, time2=time2, rest1=rest1, work=work, next_date=next_date, next_work=next_work)







"1月6日（木）"



def get_input(name, default):

    val = input(str(name + "  [" + default + "]").ljust(30) + " : ")

    if val == "":

        return default

    else:

        return val





def get_week(week: int):

    if week == 0:

        return "月"

    elif week == 1:

        return "火"

    elif week == 2:

        return "水"

    elif week == 3:

        return "木"

    elif week == 4:

        return "金"

    elif week == 5:

        return "土"

    elif week == 6:

        return "日"

    else:

        raise Exception()



def main():

    from datetime import datetime, timedelta



    current_dt = datetime.now()

    current_minute = current_dt.minute

    if current_minute > 30:

        current_minute = 30

    else:

        current_minute = 0



    current_hour = current_dt.hour



    next_dt = datetime.now() + timedelta(days=1)



    current_date = f"{current_dt.month}月{current_dt.day}日"

    current_date = get_input("本日", current_date)

    time1 = get_input("開始時間", "9:00")

    time2 = get_input("終了時間", f"{current_hour}:{str(current_minute).zfill(2)}")

    rest1 = get_input("休憩時間(1 or 1.5 etc)", "1.0")

    work1 = get_input("本日の作業", "xxxxxx作業")

    work2 = get_input("次の作業", "xxxxx作業")

    note = get_input("備考（休暇、遅刻、早退、夜勤理由等）", "")

    next_date = f"{next_dt.month}月{next_dt.day}日（{get_week(next_dt.weekday())}）"



    rest1 = str(float(rest1))



    rest_hour, rest_minite = rest1.split(".")

    if rest_minite == "5":

        rest_minite = "30"

    elif rest_minite == "0":

        rest_minite = "00"

    else:

        raise Exception()



    print(embed(current_date=current_date, time1=time1, time2=time2, rest1=f"{rest_hour}:{rest_minite}", work=work1, next_date=next_date, next_work=work2))



    rest_start = f"13:00"

    rest_end = f"{13 + int(rest_hour)}:{rest_minite}"



    fname = Path(__file__).parent / "history.log"

    print("========================================")

    print(fname)



    with open(fname, "a") as f:

        s = "\t".join([current_date, time1, time2, rest_start, rest_end, work1, note, "\n"])

        f.write(s)





if __name__ == "__main__":

    main()
