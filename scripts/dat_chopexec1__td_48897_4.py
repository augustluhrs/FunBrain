# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

n = op('null_toNano')
# cs = op('colorStrengths')
cs = op('table_colorStrengths')


def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	#when we get a new color chain event, send to nano
	print("new color event")
	# print(op('null_toNano')['r'])
	chainIndex = n['chainIndex'].eval()
	r = n['r'].eval()
	g = n['g'].eval()
	b = n['b'].eval()
	print('sending to arduino')
	print(f"{chainIndex},{r},{g},{b}")
	op('serial1').send(f"{str(chainIndex)},{str(r)},{str(g)},{str(b)},")
	if n['hueIndex'].eval() == 0:
		op('container1/button0').click();
	if n['hueIndex'].eval() == 1:
		op('container1/button1').click();
	if n['hueIndex'].eval() == 2:
		op('container1/button2').click();
	if n['hueIndex'].eval() == 3:
		op('container1/button3').click();
	if n['hueIndex'].eval() == 4:
		op('container1/button4').click();
	if n['hueIndex'].eval() == 5:
		op('container1/button5').click();
	if n['hueIndex'].eval() == 6:
		op('container1/button6').click();
	if n['hueIndex'].eval() == 7:
		op('container1/button7').click();
	if n['hueIndex'].eval() == 8:
		op('container1/button8').click();
	if n['hueIndex'].eval() == 9:
		op('container1/button9').click();
	if n['hueIndex'].eval() == 10:
		op('container1/button10').click();
	if n['hueIndex'].eval() == 11:
		op('container1/button11').click();
	if n['hueIndex'].eval() == 12:
		op('container1/button12').click();
	# op('serial1').sendBytes(r)
	# print(str(chainIndex) + " " + str(r) + " " + str(g) + " " + str(b))
	# op('serial1').send(str(chainIndex) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")
	return
	#mod(op('mqttclient_local_callbacks')).sendToNano(chainIndex, r, g, b)
	#update the color strength by hueIndex
	#hueIndex = int(n['hueIndex'].eval())



  #   #le sigh
  # print(hueIndex)
  # print(cs[0,0])
  # match hueIndex:
  #   case 0:
  #     cs[0,0] = str(int(cs[0,0]) + 1)
  #   case 1:
  #     cs[1,0] = str(int(cs[1,0]) + 1)
  #   case 2:
  #     cs[2,0] = str(int(cs[2,0]) + 1)
  #   case 3:
  #     cs[3,0] = str(int(cs[3,0]) + 1)
  #   case 4:
  #     cs[4,0] = str(int(cs[4,0]) + 1)
  #   case 5:
  #     cs[5,0] = str(int(cs[5,0]) + 1)
  #   case 6:
  #     cs[6,0] = str(int(cs[6,0]) + 1)
  #   case 7:
  #     cs[7,0] = str(int(cs[7,0]) + 1)
  #   case 8:
  #     cs[8,0] = str(int(cs[8,0]) + 1)
  #   case 9:
  #     cs[9,0] = str(int(cs[9,0]) + 1)
  #   case 10:
  #     cs[10,0] = str(int(cs[10,0]) + 1)
  #   case 11:
  #     cs[11,0] = str(int(cs[11,0]) + 1)
  #   case 12:
  #     cs[12,0] = str(int(cs[12,0]) + 1)
#return
	
def onOffToOn(channel, sampleIndex, val, prev):
	#when we get a new color chain event, send to nano
	print("new color event")
	# print(op('null_toNano')['r'])
	chainIndex = n['chainIndex'].eval()
	r = n['r'].eval()
	g = n['g'].eval()
	b = n['b'].eval()
	#mod(op('mqttclient_local_callbacks')).sendToNano(chainIndex, r, g, b)
	
	#update the color strength by hueIndex
	hueIndex = int(n['hueIndex'].eval())

	#le sigh
	print(hueIndex)
	print(cs[0,0])
	match hueIndex:
		case '0':
			cs[0,0] += 1
		case '1':
			cs[1,0] += 1
		case '2':
			cs[2,0] += 1
		case '3':
			cs[3,0] += 1
		case '4':
			cs[4,0] += 1
		case '5':
			cs[5,0] += 1
		case '6':
			cs[6,0] += 1
		case '7':
			cs[7,0] += 1
		case '8':
			cs[8,0] += 1
		case '9':
			cs[9,0] += 1
		case '10':
			cs[10,0] += 1
		case '11':
			cs[11,0] += 1
		case '12':
			cs[12,0] += 1
		# case '0':
		# 	cs['hue0'] += 1
		# case '1':
		# 	cs['hue1'] += 1
		# case '2':
		# 	cs['hue2'] += 1
		# case '3':
		# 	cs['hue3'] += 1
		# case '4':
		# 	cs['hue4'] += 1
		# case '5':
		# 	cs['hue5'] += 1
		# case '6':
		# 	cs['hue6'] += 1
		# case '7':
		# 	cs['hue7'] += 1
		# case '8':
		# 	cs['hue8'] += 1
		# case '9':
		# 	cs['hue9'] += 1
		# case '10':
		# 	cs['hue10'] += 1
		# case '11':
		# 	cs['hue11'] += 1
		# case '12':
		# 	cs['grey12'] += 1
	



	# hueNum = 'hue'+str(hueIndex)
	# op('colorStrengths')[hueNum] += 1
	#todo check if this works, if not make string before

	# for chan in op('colorStrengths').chans():
		# print(chan.name)
		# index = channel.name[len('hue'):]
		# print(index)
	return
