# constants

e = 2.71


# functions

def summation(X):
	# X is a list of numbers

	# initializes the variable to contain the sum of the values in list X
	X_sum = 0

	# loops through list X, and adds each value to x_sum
	for value in X:
		X_sum = (X_sum + value)

	return X_sum


def square_root(x):
	# x is a positive number
	if (x < 0):
		return "Cannot compute the square root of a negative number"

	# raises x to the power of 0.5, which produces the square root of x
	square_root = (x ** 0.5)

	return square_root


def factorial(x):
	# x is a positive number
	if (x < 0):
		return "Cannot compute the factorial of a negative number"

	# initializes a list to contain descending integers starting with x
	X_descending = []

	# initializes a variable to store the product of integers in x_descending
	factorial = 1

	# pushes a list of descending integers into x_descending
	while x > 0:
		X_descending.append(x)
		x = (x - 1)

	for value in X_descending:
		factorial = (factorial * value)

	return factorial


def mean(X):
	# X is a list of numbers

	# computes the sum of all numbers in X
	X_sum = summation(X)

	# computes the length of list X
	length = len(X)

	# computes the mean of X
	X_mean = (X_sum / length)

	return X_mean


def mean_minus_1(X):
	# X is a list of numbers

	# computes the sum of all numbers in X
	X_sum = summation(X)

	# computes the length of list X
	length = len(X)

	# computes the mean of X
	X_mean = (X_sum / (length - 1))

	return X_mean


def median(X):
	# X is a list of numbers

	# sorts X in ascending order
	X.sort()

	# if the length of X is even: computes the mean of the middle two values; if the length of X is odd: gets the middle value
	if ((len(X) % 2) == 0):
		X_median = mean([X[int((len(X) / 2) - 1)], X[int((len(X) / 2))]])
		return X_median
	else:
		X_median = X[int((len(X) - 1) / 2)]
		return X_median


def mode(X):
	# X is a list of numbers

	# initializes an object to count occurrences of unique values in X
	counter = {}

	# loops through X and counts the number of times each unique value occurs
	for value in X:
		keys = counter.keys()

		if value in keys:	
			counter[value] = counter[value] + 1
		else:
			counter[value] = 1

	# initializes a variable to hold the most common value in X
	X_mode = 0

	# initializes a variable to hold the hightest value count in X
	X_count = 0

	# loops through the counter object to find the most common value in X
	for key in counter:
		value = counter[key]

		if (value > X_count):
			X_mode = key
			X_count = value 

	# initializes a variable to count how many modes occur
	mode_count = 0

	# loops through the counter object to check to see if there is more than one mode in X
	counter_keys = counter.keys()

	for key in counter_keys:
		value = counter[key]

		if (value == X_count):
			mode_count = mode_count + 1

	if (mode_count > 1):
		return "This set has no unique mode"
	else:	
		return X_mode


def variance(X):
	# X is a list of numbers

	# initializes an empty list to contain the squared differences between each value of X and the mean of X
	differences_squared = []

	# computes the mean of X
	X_mean = mean(X)

	# loops through list X, finds the difference between each value of X and the mean of X, squares that difference, and pushes it to the end of differences_squared
	for value in X:
		difference = (value - X_mean)
		squared_difference = (difference ** 2)
		differences_squared.append(squared_difference)

	# computes the mean of differences_squared
	X_variance = mean_minus_1(differences_squared)

	return X_variance


def standard_deviation(X):
	# X is a list of numbers

	# computes variance of X
	X_variance = variance(X)

	# computes the standard deviation of X
	X_standard_deviation = square_root(X_variance)

	return X_standard_deviation
	

def z_score(X, x):
	# X is a list of numbers
	# x is a number

	# computes the mean of X
	X_mean = mean(X)

	# computes the standard deviation of X
	X_standard_deviation = standard_deviation(X)

	# computes the z-score of x
	x_z_score = ((x - X_mean) / (X_standard_deviation))

	return x_z_score


def positive_z_score(X, x):
	# X is a list of numbers
	# x is a number

	# computes the mean of X
	X_mean = mean(X)

	# computes the standard deviation of X
	X_standard_deviation = standard_deviation(X)

	# computes the positive z-score of x
	positive_x_z_score = (((x - X_mean) ** 2) / (X_standard_deviation ** 2))

	return positive_x_z_score


def z_scores(X):
	# X is a list of numbers

	# initializes an empty list to contain the computes z-scores
	X_z_scores = []

	# loops through X, computs the z-score of each value, and pushes each value into z_scores
	for value in X:
		value_z_score = z_score(X, value)
		X_z_scores.append(value_z_score)

	return X_z_scores


def unintegrated_beta_pdf(x, a, b):
	# x is some probability that some proposition is true
	# a is the number of true propositions in (a + b) experiments
	# b is the number of false propositions in (a + b) experiments

	# computes the probability distribution height for the given value on the x-axis
	pdf = ((x ** (a - 1)) * ((1 - x) ** (b - 1)))

	return pdf


def beta_cdf(a, b, start, end):
	# x is some probability that some proposition is true
	# a is the number of true propositions in (a + b) experiments
	# b is the number of false propositions in (a + b) experiments
	# start is the lower bound of the cumulative distribution
	# end is the upper bound of the cumulative distribution

	# checks to ensure start is not greater than or equal to end
	if (start >= end):
		return "end must be greater than start"

	# this object represents the starting and ending points of the full range of the distribution
	full_range = {'start': 0, 'end': 1}

	# computes the length of the full range
	full_range_length = (full_range['end'] - full_range['start'])

	# computes the interval size with which to sum the full range
	full_range_delta = (full_range_length / 1000000)

	# initializes a list to store the starting positions of each interval of the full range
	full_range_interval_start_positions = []
	full_range_interval_start_positions.append(full_range['start'])

	# intializes a variable to track the current position of the below loop
	full_range_current_position = full_range['start']

	# loops through all interval start positions of the full range and adds them to the full_range_interval_start_positions list
	while (full_range_current_position < (full_range['end'] - full_range_delta)):
		next_position = (full_range_current_position + full_range_delta)
		full_range_interval_start_positions.append(next_position)
		full_range_current_position = next_position

	# this object represents the starting and ending points of the cdf range of the distribution
	cdf_range = {'start': start, 'end': end}

	# computes the length of the cdf range
	cdf_range_length = (cdf_range['end'] - cdf_range['start'])

	# computes the interval size with which to sum the cdf range
	cdf_range_delta = (cdf_range_length / 1000000)

	# initializes a list to store the starting positions of each interval of the cdf range
	cdf_range_interval_start_positions = []
	cdf_range_interval_start_positions.append(cdf_range['start'])

	# initializes a variable to track the current position of the below loop
	cdf_range_current_position = cdf_range['start']

	# loops through all interval start positions of the cdf range and adds them to the cdf_range_interval_start_positions list
	while (cdf_range_current_position < (cdf_range['end'] - cdf_range_delta)):
		next_position = (cdf_range_current_position + cdf_range_delta)
		cdf_range_interval_start_positions.append(next_position)
		cdf_range_current_position = next_position

	# initializes a list to store the interval areas beneath the distribution curve of the full range
	full_range_interval_areas = []

	# initializes a list to store the interval areas beneath the distribution curve of the cdf range
	cdf_range_interval_areas = []

	# loops through full_range_interval_start_positions, and for each position, calculates its pdf height, multiplies the height by the full range delta, and pushes the result to the full_range_interval_areas list	
	for position in full_range_interval_start_positions:
		height = unintegrated_beta_pdf(position, a, b)
		area = (height * full_range_delta)
		full_range_interval_areas.append(area)

	#print("full range interval areas")
	#print(full_range_interval_areas)

	# loops through cdf_range_interval_start_positions, and for each position, calculates its pdf height, multiplies the height by the cdf range delta, and pushes the result to the cdf_range_interval_areas list
	for position in cdf_range_interval_start_positions:
		height = unintegrated_beta_pdf(position, a, b)
		area = (height * cdf_range_delta)
		cdf_range_interval_areas.append(area)

	# computes the sum of the intervals of the full range area beneath the distribution curve
	full_range_interval_sum = summation(full_range_interval_areas)

	# computes the sum of the intervals of the cdf range area beneath the distribution curve
	cdf_range_interval_sum = summation(cdf_range_interval_areas)

	# computes the cumululative probability of the cdf range
	cdf = (cdf_range_interval_sum / full_range_interval_sum)

	return cdf 


def bernoulli(p, k):
	# p is some probability that some proposition is true
	# k is equal to 1 if the proposition is true, and 0 if it is false

	# computes the probability of k
	probability = ((p ** k) * ((1 - p) ** (1 - k)))

	# the mean
	mean = p

	# computes the variance
	variance = (p * (1 - p))

	# computes the standard deviation
	standard_deviation = square_root(variance)

	bernoulli = {'probability': probability, 'mean': mean, 'variance': variance, 'standard_deviation': standard_deviation}

	return bernoulli


def binomial_pmf(p, n, k):
	# p is some probability that some proposition is true
	# n is a number of experiments
	# k is a number of true propositions out of n experiments

	# computes the factorials needed to compute the pmf
	n_factorial = factorial(n)
	k_factorial = factorial(k)
	n_minus_k_factorial = factorial(n - k)

	# computes n_choose_k and probability
	n_choose_k = (n_factorial / (k_factorial * n_minus_k_factorial))
	probability = ((p ** k) * ((1 - p) ** (n - k))) 

	# computes pmf
	pmf = (n_choose_k * probability)

	return pmf


def binomial_cdf(p, n, start, end):
	# p is some probability that some proposition is true
	# n is a number of experiments
	# start is the lower bound of the cumulative distribution
	# end is the upper bound of the cumulative distribution

	# checks to ensure start is not greater than or equal to end
	if (start >= end):
		return "end must be greater than start"

	# initializes a variable to store the cumulative probability distribution of values 0 through k
	cdf = 0

	# loops through range 0 to k + 1, computes the probability of i, and adds it to the cdf
	for i in range(start, (end + 1)):
		i_pmf = binomial_pmf(p, n, i)
		cdf = (cdf + i_pmf)

	return cdf 


def binomial(p, n, k, start, end):
	# p is some probability that some proposition is true
	# n is a number of experiments
	# k is a number of true propositions out of n experiments
	# start is the lower bound of the cumulative distribution
	# end is the upper bound of the cumulative distribution

	# computes the mean
	mean = (p * n) 

	# computes the variance
	variance = ((p * n) * (1 - p))

	# computes the standard deviation
	standard_deviation = square_root(variance)

	# computes the pmf
	pmf = binomial_pmf(p, n, k)

	# computes the cdf
	cdf = binomial_cdf(p, n, start, end)

	binomial = {'mean': mean, 'variance': variance, 'standard_deviation': standard_deviation, 'pmf': pmf, 'cdf': cdf}

	return binomial


def unintegrated_normal_pdf(X, x):
	# X is a list of numbers
	# x is a number in X

	# computes the standard devation of X
	X_standard_deviation = standard_deviation(X)

	# computes the positive z-score of x
	x_positive_z_score = positive_z_score(X, x)

	# computes the probability distribution height for the given value on the x-axis
	pdf = ((e ** (x_positive_z_score * -0.5)) / X_standard_deviation)

	return pdf


def normal_cdf(X, start, end):
	# X is a list of numbers
	# start is the lower bound of the cumulative distribution
	# end is the upper bound of the cumulative distribution

	# checks to ensure start is not greater than or equal to end
	if (start >= end):
		return "end must be greater than start"

	# computes the mean of X
	X_mean = mean(X)

	# computes the standard deviation of X
	X_standard_deviation = standard_deviation(X)

	# this object represents the starting and ending points of the full range of the distribution
	full_range = {'start': (X_mean - (27 * X_standard_deviation)), 'end': (X_mean + (27 * X_standard_deviation))}


	# computes the length of the full range
	full_range_length = (full_range['end'] - full_range['start'])


	# computes the interval size with which to sum the full range
	full_range_delta = (full_range_length / 100000)

	# initializes a list to store the starting positions of each interval of the full range
	full_range_interval_start_positions = []
	full_range_interval_start_positions.append(full_range['start'])

	# intializes a variable to track the current position of the below loop
	full_range_current_position = full_range['start']

	# loops through all interval start positions of the full range and adds them to the full_range_interval_start_positions list
	while (full_range_current_position < full_range['end']):
		next_position = (full_range_current_position + full_range_delta)
		full_range_interval_start_positions.append(next_position)
		full_range_current_position = next_position

	# this object represents the starting and ending points of the cdf range of the distribution
	cdf_range = {'start': start, 'end': end}

	# computes the length of the cdf range
	cdf_range_length = (cdf_range['end'] - cdf_range['start'])

	# computes the interval size with which to sum the cdf range
	cdf_range_delta = (cdf_range_length / 100000)

	# initializes a list to store the starting positions of each interval of the cdf range
	cdf_range_interval_start_positions = []
	cdf_range_interval_start_positions.append(cdf_range['start'])

	# initializes a variable to track the current position of the below loop
	cdf_range_current_position = cdf_range['start']

	# loops through all interval start positions of the cdf range and adds them to the cdf_range_interval_start_positions list
	while (cdf_range_current_position < cdf_range['end']):
		next_position = (cdf_range_current_position + cdf_range_delta)
		cdf_range_interval_start_positions.append(next_position)
		cdf_range_current_position = next_position

	# initializes a list to store the interval areas beneath the distribution curve of the full range
	full_range_interval_areas = []

	# initializes a list to store the interval areas beneath the distribution curve of the cdf range
	cdf_range_interval_areas = []

	# loops through full_range_interval_start_positions, and for each position, calculates its pdf height, multiplies the height by the full range delta, and pushes the result to the full_range_interval_areas list	
	for position in full_range_interval_start_positions:
		height = unintegrated_normal_pdf(X, position)
		area = (height * full_range_delta)
		full_range_interval_areas.append(area)

	# loops through cdf_range_interval_start_positions, and for each position, calculates its pdf height, multiplies the height by the cdf range delta, and pushes the result to the cdf_range_interval_areas list
	for position in cdf_range_interval_start_positions:
		height = unintegrated_normal_pdf(X, position)
		area = (height * cdf_range_delta)
		cdf_range_interval_areas.append(area)

	# computes the sum of the intervals of the full range area beneath the distribution curve
	full_range_interval_sum = summation(full_range_interval_areas)

	# computes the sum of the intervals of the cdf range area beneath the distribution curve
	cdf_range_interval_sum = summation(cdf_range_interval_areas)

	# computes the cumululative probability of the cdf range
	cdf = (cdf_range_interval_sum / full_range_interval_sum)

	if (cdf > 1):
		return 1
	else:
		return cdf 