# Client 2 (Receiver) - Receive and decrypt messages from other clients
import requests
import json

def receive_message(server_url, message_id):
	"""Receive and decrypt a message using message_id"""
	try:
		response = requests.post(
			f"{server_url}/receive",
			json={'message_id': message_id},
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
	print(" " * 18 + "DES MESSAGE RECEIVER (Client 2)")
	print("=" * 70)
	print("Receive and decrypt messages from other clients!")
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
			print("1. Receive a message (using Message ID)")
			print("2. View all messages on server")
			print("3. Exit")
			print("-" * 70)
			
			choice = input("Your choice (1/2/3): ").strip()
			
			if choice == '3':
				print("\nGoodbye! 👋")
				break
			
			elif choice == '1':
				print("\n" + "=" * 70)
				print("RECEIVE MESSAGE")
				print("=" * 70)
				
				# Get message ID from sender
				message_id = input("Enter Message ID (from sender): ").strip()
				
				if not message_id:
					print("⚠ Message ID cannot be empty!")
					continue
				
				# Receive from server
				print("\n📥 Retrieving and decrypting message...")
				response = receive_message(server_url, message_id)
				
				# Display result
				print("\n" + "=" * 70)
				print("DECRYPTED MESSAGE")
				print("=" * 70)
				
				if response['status'] == 'success':
					print("✓ SUCCESS! Message decrypted.")
					print()
					print(f"📋 Message ID: {response['message_id']}")
					print(f"🔑 Key used: {response['key']}")
					print(f"🕐 Sent at: {response['timestamp']}")
					print(f"📦 Encrypted blocks: {response['encrypted_blocks']}")
					print()
					print("=" * 70)
					print("📄 ORIGINAL MESSAGE:")
					print("-" * 70)
					print(response['plaintext'])
					print("=" * 70)
				else:
					print(f"✗ ERROR: {response['message']}")
				
				print()
			
			elif choice == '2':
				print("\n📋 Fetching messages from server...")
				try:
					response = requests.get(f"{server_url}/messages", timeout=10)
					result = response.json()
					
					if result['status'] == 'success':
						print("\n" + "=" * 70)
						print(f"AVAILABLE MESSAGES: {result['total_messages']}")
						print("=" * 70)
						
						if result['total_messages'] == 0:
							print("No messages available to receive.")
						else:
							for msg in result['messages']:
								print(f"\n  📋 ID: {msg['message_id']}")
								print(f"  🕐 Time: {msg['timestamp']}")
								print(f"  📦 Blocks: {msg['blocks_count']}")
								print(f"  👤 Sender: {msg.get('sender_info', 'Unknown')}")
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
