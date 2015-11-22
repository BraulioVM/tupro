from copy import deepcopy
from inspect import signature, Signature

def defaultify(f):
	def result_func(*args, **kwargs):
		defaults = deepcopy(f.__defaults__)
		result = f(*args, **kwargs)
		f.__defaults__ = defaults

		return result

	return result_func


def valid_typecheck(instance, annotation_cls):
	if annotation_cls is Signature.empty: # no annotation was there
		return True
	else:
		return isinstance(instance, annotation_cls)

def typecheck(f):
	sig = signature(f)

	annotations = ( param.annotation for param in sig.parameters.values() )

	def result(*args):
		args_and_annotations = zip(args, annotations)
		
		if all(valid_typecheck(arg, cls) for (arg, cls) in args_and_annotations): 
			value = f(*args)

			if valid_typecheck(value, sig.return_annotation):
				return value

			else:
				raise TypeError("Wrong return type")

		else:
			raise TypeError("Wrong argument type")


	return result



