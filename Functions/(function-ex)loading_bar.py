def loading_bar(list_bar, n_bars_to_check):
    for i in range(n_bars_to_check):
        list_bar[i] = "%"
    return list_bar


bar = []

for num in range(10):
    bar.append('.')

percent = int(input())
bars_to_fill = percent//10

filled = loading_bar(bar, bars_to_fill)

if percent < 100:
    print(f'{percent}% [{"".join(filled)}]')
    print('Still loading...')
else:
    print('100% Complete!')
    print(f'[{"".join(filled)}]')