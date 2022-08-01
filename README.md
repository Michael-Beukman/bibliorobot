# BiblioRobot

This repo provides a script to download, rename and save the bibtex information for papers. This is a convenient way to keep track of papers. For instance, the paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762) will be saved as `vaswani2017Attention.pdf`, and the following citation will be put into your bibtex file (from dblp):

```
@inproceedings{vaswani2017Attention,
  author    = {Lina Achaji and
               Julien Moreau and
               Thibault Fouqueray and
               Fran{\c{c}}ois Aioun and
               Fran{\c{c}}ois Charpillet},
  title     = {Is attention to bounding boxes all you need for pedestrian action
               prediction?},
  booktitle = {2022 {IEEE} Intelligent Vehicles Symposium, {IV} 2022, Aachen, Germany,
               June 4-9, 2022},
  pages     = {895--902},
  publisher = {{IEEE}},
  year      = {2022},
  url       = {https://doi.org/10.1109/IV51971.2022.9827084},
  doi       = {10.1109/IV51971.2022.9827084},
  timestamp = {Tue, 26 Jul 2022 10:29:47 +0200},
  biburl    = {https://dblp.org/rec/conf/ivs/AchajiMFAC22.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## How to Install
To install, simply run

```
pip install -r requirements.txt
```

## How to Use
Inside `to_download`, add lines of the arxiv identifier
For instance, would download the papers https://arxiv.org/abs/2103.14030 and https://arxiv.org/abs/1706.03762.
```
2103.14030
1706.03762
```

Then, in `env.sh` (do this only once), specify values for `PATH_TO_BIB` and `RESOURCES_FOLDER`
For instance, the following config will save the bibliography info inside a file called `bib.bib` and save the paper pdfs in `resources/`
```
export PATH_TO_BIB='bib.bib'
export RESOURCES_FOLDER=resources
```


Finally, run
```
./dl_all.sh
```

This will save the papers and put their citation information into the bib file. You can delete the contents of `to_download` at this point.

## Note
The code inside `dblp` is from here: https://github.com/sebastianGehrmann/dblp-pub
