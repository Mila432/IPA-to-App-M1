# How to convert IPA to Mac App (M1 SIP disabled)

requirements:
- decrypted app
- convert.py
- https://github.com/DanTheMan827/ios-app-signer

before you start make sure the bin of the decrypted app has a signature blob

for this example i will use `Spotify (v8.6.12 v861201032 Univ PI DY ELEVEN os120)-Mila432.ipa`
![iOS App Signer](https://raw.github.com/Mila432/IPA-to-App-M1/master/1.png)

save as `tmp.ipa` and run `python convert.py tmp.ipa`

or double click on the `tmp.ipa`

![Spotify on Mac](https://raw.github.com/Mila432/IPA-to-App-M1/master/2.png)
