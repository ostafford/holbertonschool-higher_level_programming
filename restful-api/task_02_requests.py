import requests
import csv


def fetch_and_print_posts():
    # Create the URL
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Make the request
    response = requests.get(url)

    # Print status code 
    print(f"Status Code: {response.status_code}")

    # Check if request was successful
    if response.status_code == 200:
        # Convert JSON to Python data
        posts = response.json()

        # Print titles
        for post in posts:
            print(f"- {post['title']}")
    else:
        print(f"Error: {response.status_code}")


def fetch_and_save_posts():
    # Create the URL
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Make the request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Convert JSON to Python data
        posts = response.json()

        # Create empty list for our filtered data
        posts_data = []

        # Process each post
        for post in posts:
            # Create dictionary with required fields
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            # Add to our list
            posts_data.append(post_dict)
            # append to csv file
        with open('posts.csv', 'w') as file:
            # Define which fields we want in our CSV
            fields = ['id',
                      'title', 
                      'body']
            # Create CSV writer
            writer = csv.DictWriter(file, fieldnames=fields)
            # Write the headers
            writer.writeheader()
            # Write all the posts
            writer.writerows(posts_data)
        return posts_data
    else:
        print(f"Error: {response.status_code}")
