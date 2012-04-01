#!/usr/bin/python

global texture_files
global object_map

texture_files = [
	"textures/environment.png",
	"textures/char.png"
]

object_map = ({
	"=": ((texture_files[0], 12, 11), False),
	"+": ((texture_files[0], 12, 12), False),
	"x": ((texture_files[0], 3, 1), False),
	"#": ((texture_files[0], 4, 1), False),
	" ": ((texture_files[0], 14, 0), True),
	"P": ((texture_files[1], 5, 13), False),
	"p": ((texture_files[1], 8, 7), False),
	"H": ((texture_files[1], 0, 8), False),
	"S": ((texture_files[1], 0, 6), False),
})

