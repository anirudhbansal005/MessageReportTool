import requests


REPORT_SUBMIT_URL = "https://discord.com/api/v9/reporting/message"
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
headers = {
    'Authorization': BOT_TOKEN,
    'Content-Type': 'application/json',
}

# breadcrumb presets
PRESETS = {
    "1": [3, 78],
    "2": [3, 79],
    "3": [3, 57],
    "4": [3, 75],
    "5": [3, 60]
}

def submit_report(channel_id, message_id, breadcrumbs):
    data = {
        "version": "1.0",
        "variant": "5",
        "language": "en",
        "breadcrumbs": breadcrumbs,
        "report_type": None,
        "elements": {},
        "channel_id": channel_id,
        "message_id": message_id,
        "name": "message"
    }

    response = requests.post(REPORT_SUBMIT_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        print("Full response:", response_data)
        report_id = response_data.get('report_id') 
        if report_id:
            print(f"Report submitted successfully! Report ID: {report_id}")
        else:
            print("Report submitted, but no Report ID found in the response.")
    else:
        print(f"Failed: {response.status_code} - {response.json().get('message', 'No message provided')}")

if __name__ == "__main__":
    channel_id = input("Enter the channel ID: ")
    message_id = input("Enter the message ID: ")

    print("Select a preset for breadcrumbs:")
    for key, value in PRESETS.items():
        print(f"{key}: {value}")
    
    preset_choice = input("Enter the number of your choice: ")
    breadcrumbs = PRESETS.get(preset_choice, [])

    #report_type = 'sub_spam' 
    
    submit_report(channel_id, message_id, breadcrumbs)
