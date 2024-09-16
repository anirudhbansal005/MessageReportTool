import requests
import time
import random

# Load tokens from token.txt
def load_tokens(file_path):
    with open(file_path, 'r') as file:
        tokens = [line.strip() for line in file]
    return tokens

# Report message function
def report_message(token, channel_id, message_id, breadcrumbs, breadcrumbs_presets):
    url = "https://discord.com/api/v9/reporting/message"
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }
    # if breadcrumbs_presets == 13:
    data = {
            "version": "1.0",
            "variant": "5",
            "language": "en",
            "breadcrumbs": breadcrumbs,
            #"elements": {"pii_select": ["phone_info"]}, 
                   # elements for different report types is not implemented  
            "elements": {},
            "report_type": None,
            "channel_id": channel_id,
            "message_id": message_id,
            "name": "message"
        }

    response = requests.post(url, headers=headers, json=data)
    return response

# Main function
def main():
    token_file = "TOKEN_FILE_RELATIVE_PATH_"
    tokens = load_tokens(token_file)
    
    channel_id = input("Enter the channel ID: ")
    message_id = input("Enter the message ID: ")
    
    # Define breadcrumb presets (can be modified)
    breadcrumbs_presets = [
        [3, 61, 103],  # drug and other sell          0
        [3, 57, 86], # hate speech                    1
        [3, 57, 68, 92], # cp talks                   2
        [3, 57, 68, 91], # cp images                  3
        [3, 57, 66, 87], # gore and sensitive content 4
        [3, 75, 76, 112], # fake information          5
        [3, 57, 82], # harassment                     6
        [3, 57, 83], # vulgar language                7  
        [3, 57, 66, 89], # pprn report                8
        [3, 57, 66, 90], # prn share threat           9
        [3, 57, 66, 88], # unwanted prn img           10
        [3, 57, 70, 97], # celebrating violence       11
        [3, 57, 82], # verbal harassment              12
        [3, 60, 7] # number leak                      13
    ]
    
    # Choose a breadcrumb preset
    print("Available breadcrumb presets:")
    for i, preset in enumerate(breadcrumbs_presets):
        print(f"{i}: {preset}")
    preset_choice = int(input("Choose a breadcrumb preset by number: "))
    breadcrumbs = breadcrumbs_presets[preset_choice]

    for token in tokens:
        rnd = random.randint(2,5)
        response = report_message(token, channel_id, message_id, breadcrumbs, breadcrumbs_presets)
        if response.status_code == 200:
            report_id = response.json().get('report_id')
            print(f"Token {token} - Reported successfully! Report ID: {report_id} - Time Slept: {rnd}s")
        else:
            print(f"Token {token} - Failed to report. Status code: {response.status_code}")
        time.sleep(rnd)
if __name__ == "__main__":
    main()
