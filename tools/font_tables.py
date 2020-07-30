from collections import Counter
import pprint
import urllib.request

from freetypybind import Face
from matplotlib import afm, cbook, _mathtext_data

# TODO: handle dupes.

url = "https://raw.githubusercontent.com/adobe-type-tools/agl-aglfn/master/glyphlist.txt"
agl = {
    line.split(";", 1)[0]: int(line.split(";", 1)[1], 16)
    for line in urllib.request.urlopen(url).read().decode("ascii").split("\n")
    # Glyphs mapping to multi-codepoints sequences don't occur in the fonts we ship.
    if line and not line.startswith("#") and " " not in line}

counts = Counter(agl.values())
agl_dupes = {k: [n for n in agl if agl[n] == k]
         for k, c in Counter(agl.values()).items() if c > 1}
# pprint.pprint(agl_dupes)

used = set()

# ttf_all_names = {}
# for path in cbook._get_data_path("fonts/ttf").glob("cm*.ttf"):
#     f = Face(path)
#     for i in range(f.num_glyphs):
#         name = f.get_glyph_name(i)
#         ttf_all_names.setdefault(path.stem, []).append(name)
#         if name in agl:
#             used.add(name)
#         else:
#             print(path.stem, name)
#
# print("=========")

afm_all_names = {}
for path in cbook._get_data_path("fonts/afm").glob("*.afm"):
    if path.name.startswith("cm"):
        continue
    for name in afm.AFM(open(path, "rb"))._metrics_by_name:
        afm_all_names.setdefault(path.stem, []).append(name)
        if name in agl:
            used.add(name)
        else:
            print(path.stem, name)

print("=========")

# # Generate the non-8bit part of the uni2type1 table.
# for n in sorted(used, key=agl.__getitem__):
#     if agl[n] > 0xff:
#         suffix = f"  # also {agl_dupes[agl[n]]}" if agl[n] in agl_dupes else ""
#         print(f"{agl[n]:#06x}: {n!r},{suffix}")
# used_dupes = {k: [n for n in used if agl[n] == k]
#               for k, c in Counter(agl[n] for n in used).items() if c > 1}
# pprint.pprint(used_dupes)
#
# # Find characters that only occur once in cm*.ttf.
# ttf_counts = Counter([n for ttf_names in ttf_all_names.values() for n in ttf_names])
# pairs = []
# for n, c in ttf_counts.items():
#     fonts = [k for k in ttf_all_names if n in ttf_all_names[k]]
#     if c == 1:
#         font, = fonts
#     elif c == 2 and "cmtt10" in fonts:
#         font, = (font for font in fonts if font != "cmtt10")
#     else:
#         continue
#     face = Face(cbook._get_data_path(f"fonts/ttf/{font}.ttf"))
#     _chars = face._get_chars()
#     cp, = [cp for cp, gi, name in _chars if name == n]
#     pairs.append((font, cp))
# pprint.pprint({*_mathtext_data.latex_to_bakoma.values()} - {*pairs})
# pprint.pprint({*pairs} - {*_mathtext_data.latex_to_bakoma.values()})
# print({*_mathtext_data.latex_to_bakoma.values()} & {*pairs})

# Find characters that only occur once in afm/*.afm.
afm_counts = Counter([n for afm_names in afm_all_names.values() for n in afm_names])
pairs = []
for n, c in afm_counts.items():
    fonts = [k for k in afm_all_names if n in afm_all_names[k]]
    if c == 1:
        font, = fonts
    else:
        continue
    face = afm.AFM(open(cbook._get_data_path(f"fonts/afm/{font}.afm"), "rb"))
    idxs = [i for i, m in face._metrics.items() if m.name == n]
    if not idxs:
        continue
    idx, = idxs
    pairs.append((font, idx))
for font, cp in sorted({*_mathtext_data.latex_to_standard.values()} - {*pairs}):
    texs = [n for n, k1 in _mathtext_data.latex_to_standard.items() if k1 == (font, cp)]
    for tex in sorted(texs):
        print(f"{tex!r:29}: ({font!r}, {cp}),")
# pprint.pprint({*pairs} - {*_mathtext_data.latex_to_standard.values()})
pprint.pprint({*_mathtext_data.latex_to_standard.values()} & {*pairs})
