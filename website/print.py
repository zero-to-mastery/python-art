#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()


#Magic Line
print("Content-type: text/html\r\n\r\n")
basic='''
<!DOCTYPE html><html>
<head><title>Ascii Print</title>
</head>
<body   bgcolor="#000000"><center>
<font color="white">
'''

print(basic)
form = cgi.FieldStorage()
if form:
	#get the input from form
	image=form['image']
	clarity=form.getvalue('clarity')

	# validating if there is any file uploaded or not

	if not image.filename or not clarity:
		print('<script>window.location="/cgi-bin/pythonascii/print";</script>')
	f=open('./'+image.filename,'wb') # this is testcontent
	f.write(image.file.read())
	f.close()
	#validating clarity input
	clarity=float(clarity)
	if not clarity or clarity <0:
		clarity=1
	from PIL import Image
	ASCII_CHARS = [ '#', '?', ' ', '.', '=', '+', '.', '*', '3', '&', '@']

	def scale_image(image, clearity):
		"""Resizes an image preserving the aspect ratio.
		"""
		new_width=int(100*clearity)
		(original_width, original_height) = image.size
		aspect_ratio = original_height/float(original_width)
		new_height = int(aspect_ratio * new_width)

		new_image = image.resize((new_width, new_height))
		return new_image

	def convert_to_grayscale(image):
		return image.convert('L')

	def map_pixels_to_ascii_chars(image, range_width=25):
		"""Maps each pixel to an ascii char based on the range
		in which it lies.

		0-255 is divided into 11 ranges of 25 pixels each.
		"""

		pixels_in_image = list(image.getdata())
		pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
				pixels_in_image]

		return "".join(pixels_to_chars)

	def convert_image_to_ascii(image,clearity):
		new_width=int(100*clearity)
		image = scale_image(image,clearity)
		image = convert_to_grayscale(image)

		pixels_to_chars = map_pixels_to_ascii_chars(image)
		len_pixels_to_chars = len(pixels_to_chars)

		image_ascii = [pixels_to_chars[index: index + new_width] for index in
				range(0, len_pixels_to_chars, new_width)]
		return "</br>".join(image_ascii)

	def handle_image_conversion(image_filepath,clearity):
		image = None
		try:
			image = Image.open(image_filepath)
		except Exception as e:
			print(f"Unable to open image file {image_filepath}.")
			print(e)
			return

		image_ascii = convert_image_to_ascii(image,clearity)
		print(image_ascii)
	print("<pre>")
	handle_image_conversion(image.filename,clarity)
	print("</pre>")

	print('</font></center></body></html>')
else:
	form='''
	<form  action="/cgi-bin/pythonascii/print" enctype = "multipart/form-data" method="post">
            </br>
			Clarity
              <input type="number" name="clarity" step="0.01" ></br>
			Select Image File
              <input type="file"  name="image" >
			  </br><input type="submit">
            <br>
            <br>
          </form>
	 '''
	print(form)
	print('</font></center></body></html>')
