from pathlib import Path

root = Path('.')
files = list(root.glob('*.html')) + list(root.glob('*.css')) + list(root.glob('*.js'))


def strip_comments(text):
    result = []
    i = 0
    n = len(text)
    state = 'normal'
    quote = ''
    escape = False
    while i < n:
        ch = text[i]
        nxt = text[i + 1] if i + 1 < n else ''
        if state == 'normal':
            if ch == '<' and text.startswith('<!--', i):
                j = text.find('-->', i + 4)
                if j == -1:
                    break
                i = j + 3
                continue
            if ch == '/' and nxt == '*':
                j = text.find('*/', i + 2)
                if j == -1:
                    break
                i = j + 2
                continue
            if ch == '/' and nxt == '/':
                i += 2
                while i < n and text[i] not in '\r\n':
                    i += 1
                continue
            if ch in ('"', "'", '`'):
                state = 'string'
                quote = ch
                result.append(ch)
                i += 1
                continue
            result.append(ch)
            i += 1
        else:
            result.append(ch)
            if escape:
                escape = False
            elif ch == '\\':
                escape = True
            elif ch == quote:
                state = 'normal'
            i += 1
    return ''.join(result)

for path in files:
    text = path.read_text(encoding='utf-8')
    new_text = strip_comments(text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(f'updated: {path.name}')
