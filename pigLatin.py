
def pigLatin(word):
	vow = ['a','e','i','o','u']
	if word[0] in vow:
		answer = word + "ay"
	else:
		removed = ""
		while word[0] not in vow:
			removed += word[0]
			word = word[1:]
		answer = word + removed + "ay"
	return answer

print(pigLatin("banana"))
print(pigLatin("latin"))
print(pigLatin("shesh"))
print(pigLatin("omelet"))
