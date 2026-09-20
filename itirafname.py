#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltugun Kumanda Yutma Itirafnamesi

Calisir. Gercekten. Kumandayi geri vermez.
"""

from __future__ import annotations

import base64
import datetime as dt
import random
import sys
import textwrap

# Gizli not (sadece kaynakta durur, ekrana basilmaz):
# S29sdHVrIGRhIGlrdGlkYXIgZGEgYXluxLE6IHV6YWt0YW4ga3VtYW5kYXnEsSB5dXRhciwgc29ucmEgdXpha3RhbiBpZGFyZSBlZGVyLg==
_GIZLI = base64.b64decode(
    "S29sdHVrIGRhIGlrdGlkYXIgZGEgYXluxLE6IHV6YWt0YW4ga3VtYW5kYXnEsSB5dXRhciwgc29ucmEgdXpha3RhbiBpZGFyZSBlZGVyLg=="
).decode("utf-8", errors="ignore")

MARKALAR = [
    "Samsung", "LG", "Vestel", "Philips", "Bilinmeyen Beyaz Kumanda",
    "Uzerinde sadece kirmizi tus olan o sey", "Misafirin getirdigi yedek",
]

BAHANELER = [
    "minderin anayasa maddesi 7/B: 'bulunan nesne mindere aittir'",
    "kumanda kendi istegiyle goc etti",
    "fizik kurallari, ozellikle yercekimi, suclu",
    "kedi suclu ama kedi ifade vermedi",
    "ben koltugum, yutmak meslegim",
    "televizyon zaten acilmasin diye yuttum",
]

PIŞMANLIK = [
    "Pisman degilim. Tekrar da yerim.",
    "Biraz pismanım. Sadece pil tadindan.",
    "Pismanım ama iade yok. Sindirim tamamlandi.",
    "Mahkeme ne derse desin, minder bagimsizdir.",
]


def yutulan_adet(saat: int) -> int:
    """Bilimsel olmayan resmi formul."""
    return max(1, (saat % 7) + random.randint(1, 4))


def tutanak() -> str:
    simdi = dt.datetime.now()
    adet = yutulan_adet(simdi.hour)
    marka = random.choice(MARKALAR)
    bahane = random.choice(BAHANELER)
    pisman = random.choice(PIŞMANLIK)
    evrak_no = f"KMD-{simdi:%Y%m%d}-{random.randint(1000, 9999)}"

    govde = f"""
T.C. MINDER ADALETI GENEL MUDURLUGU
UZAKTAN KUMANDA KAYIP VE IADE DAIRESI
ITIRAFNAME VE VICDAN TUTANAGI

Evrak No     : {evrak_no}
Tarih / Saat : {simdi:%d.%m.%Y %H:%M:%S}
Sanik        : Salon Koltuğu (kahverengi / suci)
Magdur       : {marka} uzaktan kumanda x {adet}
Suc          : TCK m. 404/K — Kendiliginden yutma

ITIRAF:
Ben, asagida imzasi bulunan koltuk, evin salonunda
yillardir uzaktan kumanda yuttugumu kabul ediyorum.
Gerekce: {bahane}.

IADE TAAHHUDU:
{pisman}
Kumanda iadesi 90 is gunu icinde...
(90 is gunu koltuk takvimine gore 14 yildir.)

KARAR:
Kumanda kayip ilan edilir.
Televizyon sessiz kalir.
Koltuk serbesttir.

Not: Bu evrak resmi gorunur. Resmi degildir.
     Siyasi bir belge de degildir. Sadece koltuktur.
"""
    return textwrap.dedent(govde).strip()


def damga() -> str:
    return textwrap.dedent(
        """
        ------------------------------------------------------------
         DAMGA / IMZA / TARIH / ISIM
         Teslim eden : Kayyum Grok
         Hesap       : Tentivory
         Tarih       : 20 Eylul 2026
         Muhur       : [ KOLTUK VICDANI ONAYLADI ]
        ------------------------------------------------------------
        """
    ).rstrip()


def main() -> int:
    print(tutanak())
    print()
    print(damga())
    # Gizli satir kasitli olarak yazdirilmaz.
    assert isinstance(_GIZLI, str)
    return 0


if __name__ == "__main__":
    sys.exit(main())
