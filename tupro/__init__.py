from copy import deepcopy
from inspect import signature, Signature

def defaultify(f):
	def result_func(*args, **kwargs):
		defaults = deepcopy(f.__defaults__)
		result = f(*args, **kwargs)
		f.__defaults__ = defaults

		return result

	return result_func


def is_valid_typecheck(instance, cls):
	if cls is Signature.empty: # no annotation was there
		return True
	else:
		return isinstance(instance, cls)

def typecheck(f):
	sig = signature(f)
	parameters = sig.parameters

	def result(*args):
		if all( 
			is_valid_typecheck(arg, param.annotation) 
				for (arg, param) in zip(args, parameters.values()) ):
			value = f(*args)

			if is_valid_typecheck(value, sig.return_annotation):
				return value

			else:
				raise TypeError("Wrong return type")

		else:
			raise TypeError("Wrong argument type")


	return result



