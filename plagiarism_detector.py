from difflib import SequenceMatcher
with open(r"C:\Users\vamsh\OneDrive\Desktop\sampletxt1.txt") as file1,open(r"C:\Users\vamsh\OneDrive\Desktop\sampletxt2.txt") as file2 :
    file1_=file1.read()
    file2_=file2.read()

    similarity_ratio=SequenceMatcher(None,file1_,file2_).ratio()
    print(similarity_ratio*100)
 
 