#not accepted, seems correct to me

done={}

def GetHand(letter):
	if(letter == 'd' or letter == 'f'):
		return 0
	else:
		return 1
	
def GetTime(word):
	time = 0
	if(word in done):
		time = (done[word])/2
		return time
	prevHand = None
	for letter in word:
		hand = GetHand(letter)
		if(hand==prevHand):
			time+=4
		else:
			time+=2
		prevHand = hand
	print(time)
	done[word] = time
	return time

if __name__=='__main__':
	t = int(raw_input())
	for i in xrange(t):
		n = int(raw_input())
		ans = 0
		for j in xrange(n):
			string = raw_input()
			ans += GetTime(string)
		print(ans)
		print(done)

''' solution by user "benja55"
tests = int(input())
while tests != 0:
	time = 0
	word_count = int(input())
	words = []
	last = None
	while word_count != 0:
		words.append(input())
		word_count -= 1
		k = words[-1]
		last = None
		if k in words[:len(words) - 1]:
			for p in k:
				if p == 'd' or p == 'f':
					if last == 'left':
						time += 2
					else:
						time += 1
					last = "left"

				if p == 'j' or p == 'k':
					if last == 'right':
						time += 2
					else:
						time += 1
					last = "right"
		else:
			for p in k:
				if p == 'd' or p == 'f':
					if last == 'left':
						time += 4
					else:
						time += 2
					last = "left"

				if p == 'j' or p == 'k':
					if last == 'right':
						time += 4
					else:
						time += 2
					last = "right"
	print(time)
	tests -= 1
'''