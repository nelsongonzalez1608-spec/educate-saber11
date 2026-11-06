#!/usr/bin/env python3
"""SVG (W=2000, carta) → PDF carta + JPG de revisión."""
import re, sys, subprocess, os, glob
os.chdir("/home/claude/libro")

def conv(src, out):
    h = open(src).read(400)
    Wd = float(re.search(r'width="(\d+)"', h).group(1)); Hd = float(re.search(r'height="(\d+)"', h).group(1))
    pw, ph, m = 612, 792, 10          # carta
    s = min((ph - 2 * m) / Hd, (pw - 2 * m) / Wd); w, hh = Wd * s, Hd * s
    subprocess.run(["rsvg-convert", "-f", "pdf", "--page-width", f"{pw}pt", "--page-height", f"{ph}pt",
                    "--width", f"{w:.1f}pt", "--height", f"{hh:.1f}pt", "--left", f"{(pw-w)/2:.1f}pt",
                    "--top", f"{(ph-hh)/2:.1f}pt", src, "-o", out], check=True)

names = sys.argv[1:] or sorted(glob.glob("ap*.svg"))
outs = []
for n in names:
    base = n[:-4]
    conv(n, f"pdf_{base}.pdf"); outs.append(f"pdf_{base}.pdf")
    subprocess.run(["pdftoppm", "-jpeg", "-r", "70", "-singlefile", f"pdf_{base}.pdf", f"chk_{base}"], check=True)
if len(outs) > 1:
    subprocess.run(["pdfunite", *outs, "Cuaderno_APERTURA.pdf"], check=True)
print("ok", len(outs))
