from datetime import datetime, timedelta

TIMESTAMP_FORMAT = "%Y-%m-%dT%H; %M: %S.00Z"
ent_time = datetime.now().strftime(TIMESTAMP_FORMAT)
start_time = (datetime.now() + timedelta(-1)).date()
