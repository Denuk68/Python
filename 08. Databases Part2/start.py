from lib.db_manager import Db_manager
from lib.settings import HOST, USERNAME, PASSWORD

m = Db_manager(HOST, USERNAME, PASSWORD)
m.menu()