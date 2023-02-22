import Launch
while True:
	text = input('Launch >>> ')
	if text.strip() == "": continue
	result, error = Launch.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))