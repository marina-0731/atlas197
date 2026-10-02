"""src/app.html と data/countries.json から index.html（PWA版）を組み立てる。

  python3 tools/build.py
"""
import datetime, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
app = (root / "src/app.html").read_text()
data = (root / "data/countries.json").read_text()

title = re.search(r"<title>.*?</title>\n?", app).group(0)
body = app.replace(title, "").replace("__DATA__", data)

head = f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{title.strip()}
<meta name="description" content="国旗・国名・場所をセットで覚える地球儀つきクイズとテスト">
<meta name="theme-color" content="#17262E">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="国旗暗記帳">
<style>
:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
body{{margin:0}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>
</head>
<body>
"""
tail = """<script>
if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
</script>
</body>
</html>
"""
(root / "index.html").write_text(head + body + tail)

version = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
sw = root / "sw.js"
sw.write_text(re.sub(r'const VERSION = ".*?";', f'const VERSION = "{version}";', sw.read_text()))
print("built index.html, sw version", version)
