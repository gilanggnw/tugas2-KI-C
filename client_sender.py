# Client 1 (Sender) - Send encrypted messages to other clients
import requests
import json

def send_message(server_url, text):
	"""Send an encrypted message and get message_id to share"""
	try:
		response = requests.post(
			f"{server_url}/send",
			json={'text': text},
			timeout=30
		)
		return response.json()
	except Exception as e:
		return {
			'status': 'error',
			'message': f'Connection error: {str(e)}'
		}

def main():
	print("=" * 70)
	print(" " * 20 + "DES MESSAGE SENDER (Client 1)")
	print("=" * 70)
	print("Send encrypted messages to other clients securely!")
	print("=" * 70)
	print()
	
	# Get server URL
	print("Enter server URL (e.g., http://localhost:5000 or https://your-tunnel.loca.lt)")
	server_url = input("Server URL: ").strip()
	
	if not server_url:
		server_url = "http://localhost:5000"
		print(f"Using default: {server_url}")
	
	# Remove trailing slash
	if server_url.endswith('/'):
		server_url = server_url[:-1]
	
	# Add http:// if no protocol
	if not server_url.startswith('http://') and not server_url.startswith('https://'):
		server_url = 'http://' + server_url
	
	print(f"\nConnected to: {server_url}")
	print()
	
	while True:
		try:
			print("-" * 70)
			print("What would you like to do?")
			print("1. Send a new message")
			print("2. View all messages on server")
			print("3. Exit")
			print("-" * 70)
			
			choice = input("Your choice (1/2/3): ").strip()
			
			if choice == '3':
				print("\nGoodbye! 👋")
				break
			
			elif choice == '1':
				print("\n" + "=" * 70)
				print("SEND MESSAGE")
				print("=" * 70)
				
				# Get message text (any text, no restrictions!)
				print("Enter your message (can be anything - text, numbers, symbols):")
				text = input("Message: ")
				
				if not text:
					print("⚠ Message cannot be empty!")
					continue
				
				# Send to server
				print("\n📤 Encrypting and sending message...")
				response = send_message(server_url, text)
				
				# Display result
				print("\n" + "=" * 70)
				print("RESULT")
				print("=" * 70)
				
				if response['status'] == 'success':
					print("✓ SUCCESS! Message encrypted and stored on server.")
					print()
					print(f"📋 MESSAGE ID: {response['message_id']}")
					print(f"🔑 KEY: {response['key']}")
					print(f"📦 Encrypted blocks: {response['encrypted_blocks']}")
					print()
					print("📌 IMPORTANT:")
					print(f"   Share this MESSAGE ID with the receiver: {response['message_id']}")
					print(f"   They can use it to decrypt your message!")
					print()
					print(f"   Original message: {response['plaintext'][:50]}{'...' if len(response['plaintext']) > 50 else ''}")
				else:
					print(f"✗ ERROR: {response['message']}")
				
				print("=" * 70)
				print()
			
			elif choice == '2':
				print("\n📋 Fetching messages from server...")
				try:
					response = requests.get(f"{server_url}/messages", timeout=10)
					result = response.json()
					
					if result['status'] == 'success':
						print("\n" + "=" * 70)
						print(f"STORED MESSAGES: {result['total_messages']}")
						print("=" * 70)
						
						if result['total_messages'] == 0:
							print("No messages stored on server yet.")
						else:
							for msg in result['messages']:
								print(f"\n  ID: {msg['message_id']}")
								print(f"  Time: {msg['timestamp']}")
								print(f"  Blocks: {msg['blocks_count']}")
								print(f"  Sender: {msg.get('sender_info', 'Unknown')}")
								print("  " + "-" * 60)
						
						print("=" * 70)
					else:
						print(f"Error: {result['message']}")
				except Exception as e:
					print(f"Error: {e}")
				print()
			
			else:
				print("⚠ Invalid choice! Please enter 1, 2, or 3.")
				print()
		
		except KeyboardInterrupt:
			print("\n\nGoodbye! 👋")
			break
		except Exception as e:
			print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
	main()
