import requests


def get_data_from_api():
    url = "https://api.2fa.directory/v3/all.json"

    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None


def find_and_print_documentation(data, search_term):
    found = False
    for entry in data:
        service_name, info = entry[0], entry[1]
        if search_term.lower() in service_name.lower():
            found = True
            print(f"Service Name: {service_name}")
            print(f"Domain: {info['domain']}")
            if "additional-domains" in info:
                print(f"Additional Domains: {', '.join(info['additional-domains'])}")
            print(f"TFA Methods: {', '.join(info['tfa'])}")
            if "documentation" in info:
                print(f"Documentation: {info['documentation']}")
            print(f"Keywords: {', '.join(info['keywords'])}")
            print()

    if not found:
        print(f"Could not find information for '{search_term}'.")


if __name__ == "__main__":
    api_data = get_data_from_api()
    if api_data:
        search_term = input("Enter the service name: ")
        find_and_print_documentation(api_data, search_term)
    else:
        print("Failed to fetch data from the API.")
