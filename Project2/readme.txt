The function "removeRedEyes" is respondible for removing the red eyes of the image.
The imageFileName var is assumed to be already of type "FileImage", however the line 
	# imageFileName = FileImage(imageFileName)
can fix a bug where the image file itself is passed through the function.
The "disp" and "main" functions simply allow the testing of the file to see if it works properly on the given test cases.
When running the program, it first generates all three of the images, then displays them in order on the screen.

The rectangles used in (col, row) are:

	redEyes1 -  (120, 195) - (140, 215)
			(229, 185) - (240, 205)

	redEyes2 -  ( 70, 180) - (115, 195)
			(210, 170) - (250, 180)

	redEyes3 -  (100,  90) - (140, 140)
			(250, 100) - (395, 145)