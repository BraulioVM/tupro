class OverloadEnvironment(object):
	def __init__(self):
		self.environment = {}


	def __call__(self, function):
		name = function.__name__
		number_of_paremeters = function.__code__.co_argcount

		self.environment[name] = self.environment.get(name, {})
		self.environment[name][number_of_paremeters] = function

		def result_function(*args):
			number_of_args = len(args)

			return self.environment[name][number_of_args](*args)

		return result_function
