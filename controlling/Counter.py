class Counter():

	def __init__(self, initial_value, max_value, min_value, delta):
		self.initial_value = initial_value
		self.min_value = min_value
		self.max_value = max_value
		self.delta = delta		

	def increase(self):
		if self.initial_value + self.delta < self.max_value:	
			self.initial_value += self.delta

        def reset(self):
            self.initial_value = self.min_value;

	def decrease(self):
		if (self.initial_value - self.delta) > self.min_value:
                        self.initial_value -= self.delta
