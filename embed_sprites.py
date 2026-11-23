# assets/poses 의 자세 그림(1배 PNG)을 index.html 안에 넣는다 (파일을 직접 열어도 그림이 보이도록).
# 그림을 바꾼 뒤에는:  python3 embed_sprites.py
import base64, re, os
here = os.path.dirname(os.path.abspath(__file__))
names = ['hero', 'knight', 'archer', 'cleric', 'brawler', 'guard', 'slinger', 'shaman']
poses = ['idle', 'attack', 'hit', 'evade', 'alt', 'wound', 'dead']
def uri(n, p): return 'data:image/png;base64,' + base64.b64encode(open(os.path.join(here, 'assets', 'poses', '%s-%s.png' % (n, p)), 'rb').read()).decode()
bgd = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(here, 'assets', 'bg', 'dungeon-1x.png'), 'rb').read()).decode()
block = '<script id="sprite-data">\nwindow.BG_DATA=\'' + bgd + '\';\nwindow.SPRITE_DATA={\n' + ',\n'.join("%s:{%s}" % (n, ','.join("%s:'%s'" % (p, uri(n, p)) for p in poses)) for n in names) + '\n};\n</script>\n'
p = os.path.join(here, 'index.html'); s = open(p, encoding='utf-8').read()
if '<script id="sprite-data">' in s:
    s = re.sub(r'<script id="sprite-data">.*?</script>\n', lambda m: block, s, flags=re.S)
else:
    i = s.index('<script>'); s = s[:i] + block + s[i:]
open(p, 'w', encoding='utf-8').write(s); print('embedded', len(block), 'bytes; index.html', len(s))
