# DES Client - Sends encryption/decryption requests to server via HTTP
import requests
import json

def validate_hex_input(data, length):
	if len(data) != length:
		return False, f"Must be exactly {length} hexadecimal characters"
	
	valid_hex_chars = set('0123456789ABCDEF')
	if not all(c in valid_hex_chars for c in data.upper()):
		return False, "Contains invalid hexadecimal characters"
	
	return True, "Valid"

def send_request_http(url, operation, data, key):
	"""Send HTTP request to the DES server"""
	try:
		# Prepare request payload
		request_data = {
			'operation': operation,
			'plaintext': data,
			'key': key
		}
		
		# Send POST request to /process endpoint
		response = requests.post(f"{url}/process", json=request_data, timeout=30)
		
		# Return JSON response
		return response.json()
	
	except requests.exceptions.ConnectionError:
		return {
			'status': 'error',
			'message': f'Cannot connect to server at {url}. Make sure the server is running.'
		}
	except requests.exceptions.Timeout:
		return {
			'status': 'error',
			'message': 'Request timed out. Server took too long to respond.'
		}
	except Exception as e:
		return {
			'status': 'error',
			'message': f'Connection error: {str(e)}'
		}

def main():
	print("=" * 60)
	print("DES ENCRYPTION/DECRYPTION HTTP CLIENT")
	print("=" * 60)
	print("This client connects to a DES HTTP server for encryption/decryption.")
	print("Please enter your data in hexadecimal format (0-9, A-F).")
	print("Both data and key must be exactly 16 hex characters (64 bits).")
	print("=" * 60)
	print()
	
	# Server connection details
	print("Enter server URL (e.g., http://localhost or https://your-tunnel.loca.lt)")
	server_url = input("Server URL: ").strip()
	
	# Remove trailing slash if present
	if server_url.endswith('/'):
		server_url = server_url[:-1]
	
	# Add http:// if no protocol specified
	if not server_url.startswith('http://') and not server_url.startswith('https://'):
		server_url = 'http://' + server_url
	
	print(f"\nConnecting to server at {server_url}")
	
	# Test connection
	try:
		test_response = requests.get(f"{server_url}/", timeout=5)
		if test_response.status_code == 200:
			print("✓ Server connection successful!")
			server_info = test_response.json()
			if 'message' in server_info:
				print(f"  {server_info['message']}")
		else:
			print(f"⚠ Server responded with status code: {test_response.status_code}")
	except Exception as e:
		print(f"⚠ Could not verify server connection: {e}")
		print("  Proceeding anyway...")
	
	print()
	
	while True:
		try:
			# Get operation
			print("Choose operation:")
			print("1. ENCRYPT")
			print("2. DECRYPT")
			print("3. EXIT")
			
			choice = input("Enter your choice (1/2/3): ").strip()
			
			if choice == '3':
				print("Goodbye!")
				break
			
			if choice not in ['1', '2']:
				print("Invalid choice. Please enter 1, 2, or 3.")
				continue
			
			operation = 'ENCRYPT' if choice == '1' else 'DECRYPT'
			
			# Get input data
			if operation == 'ENCRYPT':
				data = input("Enter plaintext (16 hex characters): ").strip().upper()
			else:
				data = input("Enter ciphertext (16 hex characters): ").strip().upper()
			
			# Get key
			key = input("Enter key (16 hex characters): ").strip().upper()
			
			# Validate inputs
			valid_data, data_msg = validate_hex_input(data, 16)
			valid_key, key_msg = validate_hex_input(key, 16)
			
			if not valid_data:
				print(f"Error - Data: {data_msg}")
				continue
			
			if not valid_key:
				print(f"Error - Key: {key_msg}")
				continue
			
			# Send request to server
			print(f"\nSending {operation} request to server...")
			response = send_request_http(server_url, operation, data, key)
			
			# Display response
			print("\n" + "=" * 50)
			print("SERVER RESPONSE")
			print("=" * 50)
			
			if response['status'] == 'success':
				print(f"✓ Operation: {response['operation'].upper()}")
				if operation == 'ENCRYPT':
					print(f"  Plaintext:  {response['plaintext']}")
					print(f"  Key:        {response['key']}")
					print(f"  Ciphertext: {response['ciphertext']}")
				else:
					print(f"  Ciphertext: {response['ciphertext']}")
					print(f"  Key:        {response['key']}")
					print(f"  Plaintext:  {response['plaintext']}")
				print("✓ SUCCESS: Operation completed successfully!")
			else:
				print(f"✗ ERROR: {response['message']}")
			
			print("=" * 50)
			print()
			
		except KeyboardInterrupt:
			print("\nGoodbye!")
			break
		except Exception as e:
			print(f"Unexpected error: {e}")

if __name__ == "__main__":
	main()