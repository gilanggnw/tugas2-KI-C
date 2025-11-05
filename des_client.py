# Universal DES Client - Send and Receive Encrypted Messages
import requests
import json

def send_message(server_url, text):
    """
    Sends a plaintext message to the DES server for encryption.
    
    Workflow:
    1. Prepares HTTP headers to bypass tunnel reminders
    2. Sends POST request to server's /send endpoint with plaintext
    3. Server encrypts the message using DES algorithm
    4. Returns message_id, encryption key, and ciphertext
    """
    try:
        headers = {
            'Content-Type': 'application/json',
            'Bypass-Tunnel-Reminder': 'true'  # Prevents tunnel service warnings
        }
        # Send plaintext to server for encryption
        response = requests.post(f"{server_url}/send", json={'text': text}, headers=headers, timeout=30)
        if response.status_code == 200:
            return True, response.json()  # Returns message_id, key, and ciphertext
        else:
            return False, f"Error: {response.status_code} - {response.text[:100]}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def receive_message(server_url, message_id):
    """
    Retrieves and decrypts a message from the DES server using message_id.
    
    Workflow:
    1. Prepares HTTP headers
    2. Sends POST request to server's /receive endpoint with message_id
    3. Server looks up the encrypted message and decryption key
    4. Server decrypts the message using DES algorithm
    5. Returns plaintext, ciphertext, and key used
    """
    try:
        headers = {
            'Content-Type': 'application/json',
            'Bypass-Tunnel-Reminder': 'true'
        }
        # Request message decryption from server using message_id
        response = requests.post(f"{server_url}/receive", json={'message_id': message_id}, headers=headers, timeout=30)
        if response.status_code == 200:
            return True, response.json()  # Returns plaintext, ciphertext, and key
        else:
            return False, f"Error: {response.status_code} - {response.text[:100]}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """
    Main program loop for DES encrypted communication client.
    
    Overall Workflow:
    1. Display menu with three options: Send, Receive, or Exit
    2. Send Message Flow:
       - User provides server URL and plaintext message
       - Client sends to server for encryption
       - Server responds with message_id, key, and ciphertext
       - User shares message_id with intended receiver
    3. Receive Message Flow:
       - User provides server URL and message_id (received from sender)
       - Client requests decryption from server
       - Server decrypts and returns plaintext
    4. Repeat until user chooses to exit
    """
    while True:
        # Display menu interface
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
            # SEND MESSAGE WORKFLOW
            print("\n=== SEND MESSAGE ===")
            server_url = input("Server URL: ").strip()  # Get DES server address
            text = input("Message: ").strip()  # Get plaintext to encrypt
            print("\nSending...")
            success, result = send_message(server_url, text)
            if success:
                # Display encryption results
                print(f"\nSUCCESS!")
                print(f"Message ID: {result['message_id']}")  # Unique identifier for this message
                print(f"Key: {result['key']}")  # DES encryption key used
                print(f"Ciphertext: {result.get('ciphertext', 'N/A')}")  # Encrypted message
                print("\nShare the Message ID with the receiver!")
            else:
                print(f"\nFAILED: {result}")
        
        elif choice == '2':
            # RECEIVE MESSAGE WORKFLOW
            print("\n=== RECEIVE MESSAGE ===")
            server_url = input("Server URL: ").strip()  # Get DES server address
            message_id = input("Message ID: ").strip()  # Get message_id from sender
            print("\nReceiving...")
            success, result = receive_message(server_url, message_id)
            if success:
                # Display decryption results
                print(f"\nSUCCESS!")
                print(f"Plaintext: {result['plaintext']}")  # Decrypted message
                print(f"Ciphertext: {result.get('ciphertext', 'N/A')}")  # Original encrypted message
                print(f"Key: {result.get('key', 'N/A')}")  # DES key used for encryption/decryption
            else:
                print(f"\nFAILED: {result}")
        
        elif choice == '3':
            # EXIT WORKFLOW
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice!")

if __name__ == "__main__":
    try:
        main()  # Start the client program
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")  # Handle Ctrl+C gracefully