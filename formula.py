#formula.py

print "welcome to headways"

# max { 0, d + g ( H - h1 ){
	
d = 5.8
g = 0.8
H = 7


def whats_time(distance_to_bus_ahead, average_velocity):
	return distance_to_bus_ahead/average_velocity


def whats_the_wait(distance_to_bus_ahead, average_velocity, dee, gee, aych):
	return max(0, dee + gee * (aych - (distance_to_bus_ahead / average_velocity)))


def chi_town_wait(distance_to_bus_ahead, average_velocity):
	h_one = distance_to_bus_ahead/average_velocity
	return max(0, d+g * (H - h_one))
	
	