import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_URL(URL):
    try:
        response = requests.get(URL)
        response.raise_for_status()


        soup = BeautifulSoup(response.text, "html.parser")

        links = []

        for a_tag in soup.find_all("a",href =True):
            full_url = urljoin(URL,a_tag["href"])
            links.append(full_url)
            with open("myLinks.txt", 'a') as saved:
                print(links[:10], file=saved)

        

        return links

    except requests.exceptions.RequestException as e:
        print(f"Error in fetching {URL} : {e}")
        return[]


def fetch_img(URL, save_folder="downloaded_images"):
    try:
        response = requests.get(URL)
        response.raise_for_status()


        soup = BeautifulSoup(response.text, "html.parser")

        images = []

        for idx, img_tag in enumerate(soup.find_all("img",src =True), start =1):
            full_img = urljoin(URL,img_tag["src"])
            images.append(full_img)

            try:
                    img_data = requests.get(full_img, ).content
                    img_name = os.path.join(save_folder, f"image_{idx}.jpg")
                    with open(img_name, "wb") as f:
                        f.write(img_data)
                    print(f"Saved: {img_name}")
            except Exception as err:
                print(f"Failed to download {full_img} -> {err}")

    
        return images

    except requests.exceptions.RequestException as e:
        print(f"Error in fetching {URL} : {e}")
        return[]


if __name__ == "__main__":
    website = input("Enter the URL : ")
    j=1
    i=1

    while True:
        choice = int(input("choose the following option:\n1.Fetch URL\n2.Fetch Images\n3.Exit\nEnter..: "))

        if(choice==1):
            urls = fetch_URL(website)
            for link in urls:
                print(j,":",link)
                j+=1

        elif(choice == 2):
            all_images = fetch_img(website)
            for  img in all_images:
                print(i,":",img)
                i+=1

        elif(choice == 3):
            break
        else:
            print("Invalid choice!!!!!!!")
            


    
    
    
    

    
        

    
        

        
