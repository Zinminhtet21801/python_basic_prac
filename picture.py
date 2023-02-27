picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

index = len(picture[0])

for image in picture:
    for i, pixel in enumerate(image):
        if pixel == 1:
            is_last_index = i == index - 1
            end_line = "\n" if is_last_index else ""
            print('*', end=f'{end_line}')
        else:
            print(' ', end='')

# for x in picture:
#   image = ''
#   for y in x:
#     if y == 0:
#       image += ' '
#     else:
#       image += '*'
#   print(image)