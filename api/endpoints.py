# /home/xty/Documents/Projects/PetProject/BomberBot_GUI/BomberBot_GUI/api/endpoints.py
from storage.credentials import DOMAIN

SERVICE_STATUS_URL = f"{DOMAIN}/calls/api/endpoints/service/status"
BALANCE_URL = f"{DOMAIN}/calls/api/endpoints/account/get_balance"
CREATE_ORDER_TIME_URL = f"{DOMAIN}/calls/api/endpoints/create/time"
CREATE_ORDER_SMART_URL = f"{DOMAIN}/calls/api/endpoints/create/smart"

TEST_SERVICE_STATUS_URL = "http://localhost:8000/calls/api/endpoints/service/status"
TEST_BALANCE_URL = "http://localhost:8000/calls/api/endpoints/account/get_balance"
TEST_CREATE_ORDER_TIME_URL = "http://localhost:8000/calls/api/endpoints/create/time"
TEST_CREATE_ORDER_SMART_URL = "http://localhost:8000/calls/api/endpoints/create/smart"
