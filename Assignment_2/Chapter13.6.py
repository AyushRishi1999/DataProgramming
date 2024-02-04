import urllib.request
def count_words_in_address(url):
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        word_count = len(content.split())
        print(f"Number of words in President Abraham Lincoln's Gettysburg Address: {word_count}")
    except urllib.error.URLError:
        print("Error accessing the URL. Make sure the URL is correct and accessible.")
    except Exception as e:
        print(f"An error occurred: {e}")

gettysburg_address_url = "http://cs.armstrong.edu/liang/data/Lincoln.txt"
count_words_in_address(gettysburg_address_url)