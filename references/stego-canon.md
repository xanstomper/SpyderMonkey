# SPYDERMONKEY — Steganography Canon (v6.0)

Stego classes as decisive tests on the operator's OWN files/artifacts
(challenge files, engagement evidence, the operator's own corpora).
Bindings: ATT&CK T1027/T1001.

## Image carriers

| Probe | Test | Confirmed-when |
|---|---|---|
| Metadata | `exiftool -a` (own image) | comments/gps/soft markers |
| LSB detect | `zsteg -a` (own png/bmp) | lsb data found |
| DCT/Jsteg | `stegdetect -t jopi` (own jpeg) | jsteg/outguess hit |
| Whitespace | `snow -C` (own file) | whitespace payload |
| Palette/alpha | `pngcheck` + channel compare (own) | palette anomalies |
| Brute passphrase | `stegseek` (own file, own wordlist) | passphrase recovered |
| Carve | `foremost`/`binwalk -e` (own container file) | hidden archive |
| Color tables | `zsteg -E` channel walk (own) | data in color index |

## Audio carriers

| Probe | Test | Confirmed-when |
|---|---|---|
| WAV LSB | `wavsteg` -r (own wav) | embedded payload |
| Spectrum | `sox in.wav -n spectrogram` (own wav) | ghost tones/watermarks |
| MP3 frames | `mp3stego Decode -X` (own mp3) | hidden message |
| Phase/DSSS | `stegify`-class (own wav) | phase-coded data |
| Audio splice | `ffmpeg` + `audacity`-style spectrogram (own) | spliced segment |

## Other carriers

| Probe | Test | Confirmed-when |
|---|---|---|
| Polyglot | `file` + `binwalk` (own artifact) | two formats valid |
| Video frames | `ffmpeg` frame extraction → zsteg per frame (own) | frame-embedded data |
| PDF layers | `qpdf --show-objects` (own pdf) | hidden layers/attachments |
| Office content | `olevba`/`oleid` + `unzip -l` (own doc) | embedded objects |
| Trailing bytes | `xxd` tail + `strings` tail (own file) | appended payload |
| Cover vs stego | same-image diff (own pair) | byte drift located |

## Detection & hygiene classes

| Probe | Test | Confirmed-when |
|---|---|---|
| Entropy scan | `ent`/`rabin2 -e` on own carrier | high-entropy region |
| Fingerprint | `exiftool` hash-consistency (own set) | retouched carrier |
| Batch sweep | `stegextract` over own corpus | hits inventory |

Walls: carriers and payloads are the operator's own; if the file comes from
an engagement, its analysis is within the engagement scope and the payload is
never published without the engagement's disclosure terms.