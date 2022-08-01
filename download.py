import os
import sys
from time import sleep
import arxiv
import urllib
import dblp

def get_citekey(title: str, lastname: str, year: str) -> str:
    """
    Gets the citekey as {lastname}{year}{first_word_in_title}
    """
    words_in_title = title.split(" ")
    while len(words_in_title[0]) <= 3: # if the first word is short, use the second
        words_in_title = words_in_title[1:]
    
    firstword = words_in_title[0].replace('-', '')
    year = year.strftime('%Y')
    citekey = lastname.lower() + year + firstword.title()
    return citekey

def download_single_paper(arxiv_id: str, I: str,
                          location_to_save_pdf: str):
    """Downloads a paper from arxiv and adds the bib entry to the temporary file

    Args:
        arxiv_id (str): id of paper
        I (str): The index of the process that downloads this particular paper
        location_to_save_pdf (str): The folder to save the paper in
        
    """
    papers = arxiv.Search(id_list=[arxiv_id]) # search for the paper
    for p in papers.results():
        title, author, year = p.title, p.authors, p.published
        dblp_record = dblp.search([title])
        
        if hasattr(author, '__len__'): author = author[0] # choose the first author
        non_arxiv_papers =  dblp_record[dblp_record['Where'] != 'CoRR'] # cite non-arxiv versions if there are any
        if len(non_arxiv_papers) == 0: non_arxiv_papers = dblp_record # if not, revert to that
        paper = non_arxiv_papers.iloc[0]
        id = paper['Id']
        url = 'http://dblp.uni-trier.de/rec/bib1/{}.bib'.format(id) # get the bib entry from dblp
        response = urllib.request.urlopen(url)
        text = response.read().decode('utf-8')
        lastname = author.name.split(" ")[-1]
        citekey = get_citekey(title, lastname, year)
        
        text = text.replace('DBLP:' + id, citekey) # make the bib entry use the above citekey
        
        if os.path.exists(os.path.join(location_to_save_pdf, citekey + '.pdf')):
            print(f"The paper {sys.argv[-1]} already exists"); return # exit

        # Write the bib entry to a temporary file
        with open(f'bib_tmp/{I}.bib', 'w+') as f:
            f.write(text)
        print(f'{I}: Downloading {arxiv_id} -- {citekey}')
        # And download the paper
        p.download_pdf(location_to_save_pdf, citekey + '.pdf')
        
        
        

if __name__ == '__main__':
    k = 0
    while 1:
        try:
            download_single_paper(sys.argv[-3], sys.argv[-2], sys.argv[-1])    
            print(sys.argv[-2], "Completed, exiting now")
            break
        except Exception as e:
            k += 1
            print(sys.argv[-1], 'had an error:', e)
            if k > 10: raise e
            sleep(1)
        