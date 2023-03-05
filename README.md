# The SearchMatic 9001
This will search all files in a directory in parallel for a search phrase you input.  It will infer the file"s source lang and translate your phrase to that language.  At the end it will translate the files to English.  Yeah motherfucker, and it is fast as fuck. Well, relatively fast for what it is doing.


---


![Screenshot 2023-03-04 at 12 30 33 AM](https://user-images.githubusercontent.com/93559326/222885681-1bf497a8-411e-4500-bd60-95a67f2b8919.png)


---

## Usage:

- pip3 install googletrans==4.0.0-rc1
- python3 searchmatic.py


*If you are trynna be a power user you might get API errors on the final translation. Sorry idk fix the scipt or something. Add in a huggingface translator or something. Idk maybe just comment it out if it's giving you trouble.*
 
 
--- 
Per googletrans pypi page:

Note on library usage
DISCLAIMER: this is an unofficial library using the web API of translate.google.com and also is not associated with Google.

The maximum character limit on a single text is 15k.

Due to limitations of the web version of google translate, this API does not guarantee that the library would work properly at all times (so please use this library if you don’t care about stability).


---

