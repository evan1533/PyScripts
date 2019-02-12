def rgb2hex( list ):
   rgb = ((list[0]&0x0ff)<<16)|((list[1]&0x0ff)<<8)|(list[2]&0x0ff);
   return rgb

def tohex(r,g,b):
	hexchars = "0123456789ABCDEF"
	return "#" + hexchars[r / 16] + hexchars[r % 16] + hexchars[g / 16] + hexchars[g % 16] + hexchars[b / 16] + hexchars[b % 16]


myCol = (0, 255, 255)
hexCol = rgb2hex((0, 255, 255))
print(hexCol)
print(0x00FFFF)
