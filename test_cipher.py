# CIPHER.PY -MODUULIN YKSIKKÖTESTIT
# =================================

import pytest # Järjestelmätason virheiden testaus
import cipher # Testattavan moduulin lataus


plainText = b"Selkokieliteksti"
key = b"-SsqnFWfgh2pX_nnnojiCXDH3LN91myhSd9SUt6S2HM="
cipherEngine = cipher.createChipher(key)
cryptoText = cipher.encrypt(cipherEngine, plainText)

def test_decrypt():
    assert cipher.decrypt(cipherEngine, cryptoText, True) == plainText

# TODO: Tee tähän testi decryptString-funktiosta
# Luodaan salateksti käyttämöllä encryptString-funktiosta
cryptoText2 = cipher.encryptString("Selkokieliteksti")

# Tehdään testi, joka käyttää decrypString-funktiosta
def test_decryptString():
    assert cipher.decryptString(cryptoText2)


