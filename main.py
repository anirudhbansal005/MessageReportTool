import requests

def load_tokens(file_path):
    with open(file_path, 'r') as file:
        tokens = [line.strip() for line in file]
    return tokens

def report_message(token, channel_id, message_id, breadcrumbs):
    url = "https://discord.com/api/v9/reporting/message"
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }
    data = {
        "version": "1.0",
        "variant": "5",
        "language": "en",
        "breadcrumbs": breadcrumbs,
        "elements": {},
        "report_type": None,
        "channel_id": channel_id,
        "message_id": message_id,
        "name": "message"
    }
    response = requests.post(url, headers=headers, json=data)
    return response

def main():
    token_file = "python/project_snip/token.txt"
    tokens = load_tokens(token_file)
    
    channel_id = input("Enter the channel ID: ")
    message_id = input("Enter the message ID: ")
    breadcrumbs_presets = [
        [], 
        [3, 78],
        [3, 79],
        [3, 57],
        [3, 75]
    ]
    
    print("Available breadcrumb presets:")
    for i, preset in enumerate(breadcrumbs_presets):
        print(f"{i}: {preset}")
    preset_choice = int(input("Choose a breadcrumb preset by number: "))
    breadcrumbs = breadcrumbs_presets[preset_choice]

    for token in tokens:
        response = report_message(token, channel_id, message_id, breadcrumbs)
        if response.status_code == 200:
            report_id = response.json().get('report_id')
            print(f"Token {token} - Reported successfully! Report ID: {report_id}")
        else:
            print(f"Token {token} - Failed to report. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
