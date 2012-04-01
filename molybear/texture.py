#!/usr/bin/python

global texture_files
global object_map

texture_files = [
	"textures/environment.png",
	"textures/char.png"
]

object_map = ({
	".": ((texture_files[0], 5, 2), True),
	"-": ((texture_files[0], 0, 2), False),
	"#": ((texture_files[0], 4, 2), False),
	" ": ((texture_files[0], 14, 0), True),
	"P": ((texture_files[1], 5, 13), False),
	"p": ((texture_files[1], 8, 7), False),
	"H": ((texture_files[1], 10, 2), False),
	"W": ((texture_files[1], 11, 2), False),
	"R": ((texture_files[1], 12, 2), False),
	"S": ((texture_files[1], 0, 6), False),
})

