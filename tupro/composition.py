class Composable(object):
	def __init__(self, f):
		self.f = f

	def __call__(self, *args, **kwargs):
		return self.f(*args, **kwargs)

	def __mul__(self, g):
		def result(*args, **kwargs):
			return self(g(*args, **kwargs))

		return Composable(result)

	def __rmul__(self, g):
		def result(*args, **kwargs):
			return g(self(*args, **kwargs))

		return Composable(result)