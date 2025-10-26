# Universal DES Client - Send and Receive Encrypted Messages
import requests
import json

def send_message(server_url, text):
    try:
        response = requests.post(f"{server_url}/send", json={'text': text}, headers={'Content-Type': 'application/json'}, timeout=10)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"Error: {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def receive_message(server_url, message_id):
    try:
        response = requests.post(f"{server_url}/receive", json={'message_id': message_id}, headers={'Content-Type': 'application/json'}, timeout=10)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"Error: {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    while True:
        print("\n" + "="*50)
        print("     DES ENCRYPTED COMMUNICATION CLIENT")
        print("="*50)
        print("\nMENU:")
        print("  1. Send Message")
        print("  2. Receive Message")
        print("  3. Exit")
        print("="*50)
        
        choice = input("\nChoose option (1/2/3): ").strip()
        
        if choice == '1':
            print("\n=== SEND MESSAGE ===")
            server_url = input("Server URL: ").strip()
            text = input("Message: ").strip()
            print("\nSending...")
            success, result = send_message(server_url, text)
            if success:
                print(f"\nSUCCESS!")
                print(f"Message ID: {result['message_id']}")
                print(f"Key: {result['key']}")
                print(f"Ciphertext: {result['ciphertext']}")
            else:
                print(f"\nFAILED: {result}")
        
        elif choice == '2':
            print("\n=== RECEIVE MESSAGE ===")
            server_url = input("Server URL: ").strip()
            message_id = input("Message ID: ").strip()
            print("\nReceiving...")
            success, result = receive_message(server_url, message_id)
            if success:
                print(f"\nSUCCESS!")
                print(f"Plaintext: {result['plaintext']}")
                print(f"Ciphertext: {result['ciphertext']}")
                print(f"Key: {result['key']}")
            else:
                print(f"\nFAILED: {result}")
        
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
