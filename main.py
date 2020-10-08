import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),
]

txt1 = urwid.Text(('banner',
    u"    / /  ___  ___  / /__ /  |/  /__ ____  \n   / /__/ _ \/ _ \/  '_// /|_/ / _ `/ _ \ \n  /____/\___/\___/_/\_\/_/  /_/\_,_/_//_/ \n v 0.0.3 \n A terminal-based GPL3 phonebook manager \n based on Urwid and Python 3 "), align='center')
map1 = urwid.AttrMap(txt1, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.run()