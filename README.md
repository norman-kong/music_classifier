# Music Classifier for Romantic Era Composers 

This project aims to classify romantic pieces of music based on their composer.

Todo:

- [x] Find data(sets)
- [ ] Figure out the midi data format, play with music21 library.
- [ ] Apply statistical analyses to find correlations and predict.
- [ ] Apply ML to predict.
- [ ] Clean up code, documentation and make this presentable. 

We tried to think of ways to format timeseries data (the pieces) for machine learning but couldn't think of a way. We thought RNNs may be the solution but we couldn't figure out how to use RNNs (maybe a future todo?). We then turned our attention to statisical analysis given the information of the pieces (pitch, rhythm, etc.) Todo: find a way to move on from basic stats analysis and apply ML (see todo list).

Notes:

- Fixed unicode error by implementing this fix in the source code of the music21 library: https://github.com/cuthbertLab/music21/pull/607/files 

Solution from: https://stackoverflow.com/questions/64132939/unicodedecodeerror-utf-8-codec-cant-decode-byte-0xa9-in-position-10-invalid

midi data: http://www.piano-midi.de/chopin.htm
