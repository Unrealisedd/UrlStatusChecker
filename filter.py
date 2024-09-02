# Define the function to read the file and filter URLs by status code
def filter_urls_by_status():
    # Ask the user for the filename
    filename = input("Enter the name of the text file containing the URL list (e.g., urls.txt): ")
    
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

        # Ask the user for the status code to filter out
        status_code_to_filter = input("Enter the status code to filter out (e.g., 200, 404, Error): ")

        # Initialize a list to store the filtered URLs
        filtered_urls = []

        # Iterate over each line in the file
        for line in lines:
            # Check if the line contains the status code to filter out
            if f"[{status_code_to_filter}" in line:
                # Extract the URL from the line (everything before the '[' character)
                url = line.split('[')[0].strip()
                # Add the URL to the filtered list
                filtered_urls.append(url)

        # Output the filtered URLs
        print("\nFiltered URLs:")
        for url in filtered_urls:
            print(url)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")

# Run the function
if __name__ == "__main__":
    filter_urls_by_status()
