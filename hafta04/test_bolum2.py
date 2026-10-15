import pytest

from bolum2 import otopark_ucreti, sifre_gucu, yuzde_degisim


@pytest.mark.parametrize(
    ("sifre", "beklenen"),
    [
        ("a", "zayıf"),
        ("1234567", "zayıf"),
        ("12345678", "orta"),
        ("12345678901", "orta"),
        ("123456789012", "güçlü"),
        ("cok_guclu_uzun_sifre", "güçlü"),
    ],
)
def test_sifre_gucu(sifre, beklenen):
    assert sifre_gucu(sifre) == beklenen


def test_sifre_gucu_bos_sifre_icin_hata_verir():
    with pytest.raises(ValueError):
        sifre_gucu("")


@pytest.mark.parametrize(
    ("dakika", "beklenen"),
    [
        (0, 0),
        (15, 0),
        (16, 20),
        (60, 20),
        (61, 40),
        (180, 40),
        (181, 60),
        (300, 60),
    ],
)
def test_otopark_ucreti(dakika, beklenen):
    assert otopark_ucreti(dakika) == beklenen


def test_otopark_ucreti_negatif_dakika_icin_hata_verir():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


@pytest.mark.parametrize(
    ("eski", "yeni", "beklenen"),
    [
        (200, 250, 25.0),
        (200, 150, -25.0),
        (100, 100, 0.0),
    ],
)
def test_yuzde_degisim(eski, yeni, beklenen):
    assert yuzde_degisim(eski, yeni) == beklenen


def test_yuzde_degisim_eski_deger_sifir_icin_hata_verir():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)