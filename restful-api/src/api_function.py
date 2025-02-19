import requests


def fetch_and_save_post():
    # Create the URL
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Make the request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Convert JSON to Python data
        csv_data = response.json()

        # Create empty list to store our filtered data
        posts_data = []

        # Go through each post in our data
        for data in csv_data:
            # Create a dictionary with just the fields we want
            post = {
                'id': data['id'],
                'title': data['title'],
                'body': data['body']
            }
            # Add this dictionary to our list
            posts_data.append(post)

        return posts_data
    else:
        print(f"Status Code Error: {response.status_code}")
