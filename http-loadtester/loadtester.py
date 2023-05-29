import requests
import threading

# Set the target URL
target_url = "http://35.240.42.203:80"

# Set the number of concurrent users
num_users = 100

# Set the number of iterations per user
num_iterations = 30

# Function to send HTTP requests
def send_request():
    # Make a GET request to the target URL
    response = requests.get(target_url)

    # Process the response as needed
    # For example, you can check the response status code, content, etc.
    print(f"Response Code: {response.status_code}")
    print(f"Response Content: {response.text}")

# Function to simulate load by creating concurrent users
def simulate_load():
    # Create a list to store the threads
    threads = []

    # Create the desired number of threads
    for _ in range(num_users):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Perform the load test
if __name__ == "__main__":
    # Loop through the desired number of iterations
    for _ in range(num_iterations):
        simulate_load()

    # Print the result summary
    print(f"Load test completed. Total users: {num_users}, Total iterations per user: {num_iterations}")
