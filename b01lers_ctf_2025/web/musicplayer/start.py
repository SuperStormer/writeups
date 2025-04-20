# patch start.sh to call this instead of gunicorn to log missing imports which can be overridden
import builtins
import inspect
import re
import sys
import traceback

from gunicorn.app.wsgiapp import run


class LogModuleNotFound(ModuleNotFoundError):
	def __init__(self, *args, **kwargs):
		print(*args)
		traceback.print_stack(limit=5)
		super().__init__(*args, **kwargs)


builtins.ModuleNotFoundError = LogModuleNotFound


sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
sys.exit(run())
