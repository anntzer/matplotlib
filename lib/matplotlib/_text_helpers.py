"""
Low-level text helper utilities.
"""

from . import cbook
from .ft2font import KERNING_DEFAULT, LOAD_NO_HINTING


def warn_on_missing_glyph(codepoint):
    cbook._warn_external(
        "Glyph {} ({}) missing from current font.".format(
            codepoint,
            chr(codepoint).encode("ascii", "namereplace").decode("ascii")))
    block = ("Hebrew" if 0x0590 <= codepoint <= 0x05ff else
             "Arabic" if 0x0600 <= codepoint <= 0x06ff else
             "Devanagari" if 0x0900 <= codepoint <= 0x097f else
             "Bengali" if 0x0980 <= codepoint <= 0x09ff else
             "Gurmukhi" if 0x0a00 <= codepoint <= 0x0a7f else
             "Gujarati" if 0x0a80 <= codepoint <= 0x0aff else
             "Oriya" if 0x0b00 <= codepoint <= 0x0b7f else
             "Tamil" if 0x0b80 <= codepoint <= 0x0bff else
             "Telugu" if 0x0c00 <= codepoint <= 0x0c7f else
             "Kannada" if 0x0c80 <= codepoint <= 0x0cff else
             "Malayalam" if 0x0d00 <= codepoint <= 0x0d7f else
             "Sinhala" if 0x0d80 <= codepoint <= 0x0dff else
             None)
    if block:
        cbook._warn_external(
            f"Matplotlib currently does not support {block} natively.")


def layout(string, font, *, kern_mode=KERNING_DEFAULT):
    """
    Render *string* with *font*.  For each character in *string*, yield a
    (glyph-index, x-position) pair.  When such a pair is yielded, the font's
    glyph is set to the corresponding character.

    Parameters
    ----------
    string : str
        The string to be rendered.
    font : FT2Font
        The font.
    kern_mode : int
        A FreeType kerning mode.

    Yields
    ------
    glyph_index : int
    x_position : float
    """
    x = 0
    last_glyph_idx = None
    for char in string:
        glyph_idx = font.get_char_index(ord(char))
        kern = (font.get_kerning(last_glyph_idx, glyph_idx, kern_mode)
                if last_glyph_idx is not None else 0) / 64
        x += kern
        glyph = font.load_glyph(glyph_idx, flags=LOAD_NO_HINTING)
        yield glyph_idx, x
        x += glyph.linearHoriAdvance / 65536
        last_glyph_idx = glyph_idx
