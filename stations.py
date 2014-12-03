from math import floor, ceil
from decimal import *

'''Added test_branch'''
'''test 2'''
class Angle:
	degrees = Decimal(0)
	minutes = Decimal(0)
	seconds = Decimal(0)
	decimal_degrees = None
	
	def __init__(self, deg, min, sec):
		self.degrees =Decimal(deg)
		self.minutes = Decimal(min)
		self.seconds = Decimal(sec)
		self.decimal_degrees = Angle.DMS_to_Dec(self)
	
	@staticmethod
	def DMS_to_Dec(angle):
		dec = angle.degrees + angle.minutes/Decimal(60) + angle.seconds/Decimal(3600)
		return dec
	
	@staticmethod
	def Dec_to_DMS(angle):
		deg = Decimal(floor(angle))
		min = Decimal(floor((angle - deg)*Decimal(60)))
		sec = Decimal(floor(((angle - deg)*Decimal(60) - min)*Decimal(60)))
		return (deg, min, sec)
	
	@staticmethod
	def DMStuple_to_Dec(angle_tuple):
		dec = angle_tuple[0] + angle_tuple[1]/Decimal(60) + angle_tuple[2]/Decimal(3600)
		return dec
def Station1():
	r1 = Angle(0, 0, 0)
	r2 = Angle(180, 0, 15)
	r3 = Angle(85, 1, 39)
	r4 = Angle(265, 1, 24)
	r5 = Angle(0, 0 , 0)
	r6 = Angle(180, 0, 18)
	r7 = Angle(274, 59, 5)
	r8 = Angle(94, 59, 3)
	
	four_angles = []
	four_angles.append(r3.decimal_degrees)
	four_angles.append(r4.decimal_degrees - r2.decimal_degrees)
	four_angles.append(Decimal(360) - r7.decimal_degrees)
	four_angles.append(r6.decimal_degrees - r8.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<4):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))

	return avg_angle

def Station2():
	r1 = Angle(0, 0, 0)
	r2 = Angle(180, 0, 1)
	r3 = Angle(182, 34, 40)
	r4 = Angle(2, 34, 48)
	r5 = Angle(0, 0 , 0)
	r6 = Angle(180, 0, 0)
	r7 = Angle(177, 25, 22)
	r8 = Angle(352, 25, 28)
	
	four_angles = []
	four_angles.append(r3.decimal_degrees)
	four_angles.append(r2.decimal_degrees + r4.decimal_degrees)
	four_angles.append(Decimal(360) - r7.decimal_degrees)
	#four_angles.append(r6.decimal_degrees - r8.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<len(four_angles)):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))

	return avg_angle
	
def Station3():
	r1 = Angle(0, 0, 0)
	r2 = Angle(180, 0, 13)
	r3 = Angle(161, 55, 0)
	r4 = Angle(341, 55, 2)
	r5 = Angle(0, 0 , 0)
	r6 = Angle(180, 0, 1)
	r7 = Angle(18, 5, 14)
	r8 = Angle(198, 5, 13)
	
	four_angles = []
	four_angles.append(r3.decimal_degrees)
	four_angles.append(r4.decimal_degrees - r2.decimal_degrees)
	four_angles.append(Decimal(360) - r8.decimal_degrees)
	four_angles.append(r6.decimal_degrees - r7.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<len(four_angles)):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))

	return avg_angle
	
def Station4():
	r1 = Angle(0, 0, 0)
	r2 = Angle(179,59, 52)
	r3 = Angle(98, 43, 7)
	r4 = Angle(278, 43, 16)
	r5 = Angle(0, 0 , 0)
	r6 = Angle(179, 59, 59)
	r7 = Angle(81, 17, 1)
	r8 = Angle(261, 16, 50)
	
	four_angles = []
	four_angles.append(r3.decimal_degrees)
	four_angles.append(r4.decimal_degrees - r2.decimal_degrees)
	four_angles.append(Decimal(360) - r8.decimal_degrees)
	four_angles.append(r6.decimal_degrees - r7.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<len(four_angles)):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))

	return avg_angle
	
def Station5():
	r1 = Angle(0, 0, 0)
	r2 = Angle(180, 0, 5)
	r3 = Angle(112, 45, 38)
	r4 = Angle(292, 45, 25)
	r5 = Angle(0, 0 , 0)
	r6 = Angle(180, 0, 2)
	r7 = Angle(247, 14, 43)
	r8 = Angle(67, 14, 57)
	
	four_angles = []
	four_angles.append(r3.decimal_degrees)
	four_angles.append(r4.decimal_degrees - r2.decimal_degrees)
	four_angles.append(Decimal(360) - r7.decimal_degrees)
	four_angles.append(r6.decimal_degrees - r8.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<len(four_angles)):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))

	return avg_angle
	
def Station6():
	r1 = Angle(0, 0, 0)
	r2 = Angle(180, 0, 18)
	r3 = Angle(147, 41, 21)
	r4 = Angle(327, 41, 28)
	r5 = Angle(0, 0 , 0)
	r6 = Angle(180, 0, 7)
	r7 = Angle(212, 19, 19)
	r8 = Angle(32, 18, 24)
	
	four_angles = []
	four_angles.append(r3.decimal_degrees)
	four_angles.append(r4.decimal_degrees - r2.decimal_degrees)
	four_angles.append(Decimal(360) - r7.decimal_degrees)
	four_angles.append(r6.decimal_degrees - r8.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<len(four_angles)):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))

	return avg_angle
	
def Station7():
	r1 = Angle(0, 0, 0)
	r2 = Angle(179, 59, 41)
	r3 = Angle(172, 41, 39)
	r4 = Angle(352, 41, 50)
	r5 = Angle(0, 0 , 0)
	r6 = Angle(180, 0, 3)
	r7 = Angle(187, 18, 2)
	r8 = Angle(7, 18, 3)
	
	four_angles = []
	four_angles.append(r3.decimal_degrees)
	four_angles.append(r4.decimal_degrees - r2.decimal_degrees)
	four_angles.append(Decimal(360) - r7.decimal_degrees)
	four_angles.append(r6.decimal_degrees - r8.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<len(four_angles)):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))
	
	return avg_angle
	
def Station8():
	r1 = Angle(0, 0, 0)
	r2 = Angle(180, 0, 3)
	r3 = Angle(241, 23, 16)
	r4 = Angle(61, 23, 26)
	
	four_angles = []
	four_angles.append(Decimal(360)-r3.decimal_degrees)
	four_angles.append(r2.decimal_degrees - r4.decimal_degrees)
	
	i=0
	sum = Decimal(0)
	while (i<len(four_angles)):
		sum += four_angles[i]
		i += 1
	
	avg_angle = sum / Decimal(len(four_angles))
	
	return avg_angle
	
	
s1 = Station1()
s1_dms = Angle.Dec_to_DMS(s1)

s2 = Station2()
s2_dms = Angle.Dec_to_DMS(s2)

s3 = Station3()
s3_dms = Angle.Dec_to_DMS(s3)

s4 = Station4()
s4_dms = Angle.Dec_to_DMS(s4)

s5 = Station5()
s5_dms = Angle.Dec_to_DMS(s5)

s6 = Station6()
s6_dms = Angle.Dec_to_DMS(s6)

s7 = Station7()
s7_dms = Angle.Dec_to_DMS(s7)

s8 = Station8()
s8_dms = Angle.Dec_to_DMS(s8)

print "Station 1 Avg. Angle = " + str(s1_dms[0]) + " degrees " + str(s1_dms[1]) + " minutes " + str(s1_dms[2]) + " seconds" 
print "Station 2 Avg. Angle = " + str(s2_dms[0]) + " degrees " + str(s2_dms[1]) + " minutes " + str(s2_dms[2]) + " seconds" 
print "Station 3 Avg. Angle = " + str(s3_dms[0]) + " degrees " + str(s3_dms[1]) + " minutes " + str(s3_dms[2]) + " seconds" 
print "Station 4 Avg. Angle = " + str(s4_dms[0]) + " degrees " + str(s4_dms[1]) + " minutes " + str(s4_dms[2]) + " seconds" 
print "Station 5 Avg. Angle = " + str(s5_dms[0]) + " degrees " + str(s5_dms[1]) + " minutes " + str(s5_dms[2]) + " seconds" 
print "Station 6 Avg. Angle = " + str(s6_dms[0]) + " degrees " + str(s6_dms[1]) + " minutes " + str(s6_dms[2]) + " seconds" 
print "Station 7 Avg. Angle = " + str(s7_dms[0]) + " degrees " + str(s7_dms[1]) + " minutes " + str(s7_dms[2]) + " seconds" 
print "Station 8 Avg. Angle = " + str(s8_dms[0]) + " degrees " + str(s8_dms[1]) + " minutes " + str(s8_dms[2]) + " seconds" 

# Calculate actual sum and theoretical sum
sum = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
sum_dms = Angle.Dec_to_DMS(sum)
sum_t = 6*180
sum_t = Angle.Dec_to_DMS(sum_t)
print "Theoretical Sum = " + str(sum_t[0]) + " degrees " + str(sum_t[1]) + " minutes " + str(sum_t[2]) + " seconds" 
print "Actual Sum = " + str(sum_dms[0]) + " degrees " + str(sum_dms[1]) + " minutes " + str(sum_dms[2]) + " seconds" 

# Calculate misclosure and correction amount
misclosure = Decimal(1080) - sum
misclosure_dms = Angle.Dec_to_DMS(misclosure)
horizontal_correction = misclosure_dms[2] / Decimal(8)
print "Total Misclosure = " + str(misclosure_dms[2]) + " seconds"
print "Horizontal Correction = " + str(ceil(horizontal_correction))

# Calculate corrected angles
s1_dms = (s1_dms[0], s1_dms[1], s1_dms[2] + Decimal(ceil(horizontal_correction)))
s2_dms = (s2_dms[0], s2_dms[1], s2_dms[2] + Decimal(ceil(horizontal_correction)))
s3_dms = (s3_dms[0], s3_dms[1], s3_dms[2] + Decimal(ceil(horizontal_correction)))
s4_dms = (s4_dms[0], s4_dms[1], s4_dms[2] + Decimal(ceil(horizontal_correction)))
s5_dms = (s5_dms[0], s5_dms[1], s5_dms[2] + Decimal(ceil(horizontal_correction)))
s6_dms = (s6_dms[0], s6_dms[1], s6_dms[2] + Decimal(ceil(horizontal_correction)))
s7_dms = (s7_dms[0], s7_dms[1], s7_dms[2] + Decimal(ceil(horizontal_correction)))
s8_dms = (s8_dms[0], s8_dms[1], s8_dms[2] + Decimal(ceil(horizontal_correction)))

print "Station 1 Corrected Angle = " + str(s1_dms[0]) + " degrees " + str(s1_dms[1]) + " minutes " + str(s1_dms[2]) + " seconds" 
print "Station 2 Corrected Angle = " + str(s2_dms[0]) + " degrees " + str(s2_dms[1]) + " minutes " + str(s2_dms[2]) + " seconds" 
print "Station 3 Corrected Angle = " + str(s3_dms[0]) + " degrees " + str(s3_dms[1]) + " minutes " + str(s3_dms[2]) + " seconds" 
print "Station 4 Corrected Angle = " + str(s4_dms[0]) + " degrees " + str(s4_dms[1]) + " minutes " + str(s4_dms[2]) + " seconds" 
print "Station 5 Corrected Angle = " + str(s5_dms[0]) + " degrees " + str(s5_dms[1]) + " minutes " + str(s5_dms[2]) + " seconds" 
print "Station 6 Corrected Angle = " + str(s6_dms[0]) + " degrees " + str(s6_dms[1]) + " minutes " + str(s6_dms[2]) + " seconds" 
print "Station 7 Corrected Angle = " + str(s7_dms[0]) + " degrees " + str(s7_dms[1]) + " minutes " + str(s7_dms[2]) + " seconds" 
print "Station 8 Corrected Angle = " + str(s8_dms[0]) + " degrees " + str(s8_dms[1]) + " minutes " + str(s8_dms[2]) + " seconds" 

new_sum = Angle.DMStuple_to_Dec(s1_dms) + Angle.DMStuple_to_Dec(s2_dms) + Angle.DMStuple_to_Dec(s3_dms) + Angle.DMStuple_to_Dec(s4_dms) + Angle.DMStuple_to_Dec(s5_dms) + Angle.DMStuple_to_Dec(s6_dms) + Angle.DMStuple_to_Dec(s7_dms) + Angle.DMStuple_to_Dec(s8_dms)

print(new_sum)
new_sum_dms = Angle.Dec_to_DMS(new_sum)

print "Corrected Angle Sum = " + str(new_sum_dms[0]) + " degrees " + str(new_sum_dms[1]) + " minutes " + str(new_sum_dms[2]) + " seconds" 

