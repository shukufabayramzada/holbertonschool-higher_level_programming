import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in data:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()