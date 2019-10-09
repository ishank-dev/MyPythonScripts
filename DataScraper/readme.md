# Dataset Scraper:relieved: <br>

### How to use
Use `git clone https://github.com/ishank-dev/MyPythonScripts.git ` to download the scripts <br>
###### Go to the directory using<br>
```cd MyPythonScripts/DataScraper```<br>
###### Install the library
```pip install google_images_download```
###### Run the script using
`Python3 download.py`
This will download the images given in the code as keywords which you can modify by yourself.
### Directly running the app from commandline
- **Simple example of using keywords and limit arguments**<br>
```googleimagesdownload --keywords "Cats, Dogs, Beaches" --limit 20``` <br>
- **Using Suffix Keywords allows you to specify words after the main keywords.** <br> For example if the ```keyword = cat``` and suffix ```keyword = 'black,white'``` then it will first search for ```cat black``` and then ```cat white```<br>
- **To use the short hand command**<br>
```googleimagesdownload -k "Cats, Dogs, Koala,Panda" -l 20```<br>
- **To download images with specific image extension/format**<br>
```googleimagesdownload --keywords "banner" --format svg```<br>
- **To use color filters for the images**<br>
```googleimagesdownload -k "playground" -l 20 -co red ```
- **To download images with size and type constrains**<br>
```googleimagesdownload --keywords "baloons" --size medium --type animated```
- **To download images with specific color type**
```googleimagesdownload --keywords "flowers" --color_type black-and-white```
- **To download images with size and type constrains**
```googleimagesdownload --keywords "baloons" --size medium --type animated ```






