from typing import Tuple
from datetime import datetime, timedelta, date

def get_begin_of_month() -> str:
    return date.today().replace(day=1).isoformat()

def get_prev_day(prev: int) -> str:
    return (date.today() - timedelta(days=prev)).isoformat()

def get_today() -> str:
    return date.today().isoformat()

def get_total_cost_date_range() -> Tuple[str, str]:
    start_date = get_begin_of_month()
    end_date = get_today()

    # get_cost_and_usage()のstartとendに同じ日付は指定不可のため、
    # 「今日が1日」なら、「先月1日から今月1日（今日）」までの範囲にする
    if start_date == end_date:
        end_of_month = datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=-1)
        begin_of_month = end_of_month.replace(day=1)
        return begin_of_month.date().isoformat(), end_date
    return start_date, end_date

