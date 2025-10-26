"""
Test script untuk client-to-client communication
"""
import requests
import time

SERVER_URL = "http://localhost:5000"

def test_client_to_client():
	print("=" * 70)
	print("TESTING CLIENT-TO-CLIENT COMMUNICATION")
	print("=" * 70)
	print()
	
	# Test 1: Client 1 sends message
	print("📤 Test 1: Client 1 (Sender) sends message...")
	message_text = "Hello from Client 1! This is a secret message 🔐"
	
	response1 = requests.post(
		f"{SERVER_URL}/send",
		json={'text': message_text}
	)
	
	if response1.status_code == 200:
		result1 = response1.json()
		print("✓ SUCCESS!")
		print(f"  Message ID: {result1['message_id']}")
		print(f"  Key: {result1['key']}")
		print(f"  Original: {result1['plaintext'][:50]}...")
		print()
		
		message_id = result1['message_id']
		
		# Test 2: Client 2 receives message
		print("📥 Test 2: Client 2 (Receiver) receives message...")
		time.sleep(1)
		
		response2 = requests.post(
			f"{SERVER_URL}/receive",
			json={'message_id': message_id}
		)
		
		if response2.status_code == 200:
			result2 = response2.json()
			print("✓ SUCCESS!")
			print(f"  Decrypted: {result2['plaintext']}")
			print()
			
			# Verify
			if result2['plaintext'] == message_text:
				print("✅ VERIFICATION: Plaintext matches! Communication successful!")
			else:
				print("❌ VERIFICATION FAILED: Plaintext doesn't match!")
		else:
			print(f"❌ Failed to receive: {response2.text}")
	else:
		print(f"❌ Failed to send: {response1.text}")
	
	print()
	
	# Test 3: List all messages
	print("📋 Test 3: List all messages on server...")
	response3 = requests.get(f"{SERVER_URL}/messages")
	
	if response3.status_code == 200:
		result3 = response3.json()
		print(f"✓ Total messages stored: {result3['total_messages']}")
		for msg in result3['messages']:
			print(f"  - ID: {msg['message_id']}, Time: {msg['timestamp']}")
	else:
		print(f"❌ Failed: {response3.text}")
	
	print()
	print("=" * 70)
	print("TEST COMPLETED!")
	print("=" * 70)

if __name__ == "__main__":
	print("\nMake sure server is running: python des_server.py\n")
	input("Press Enter to start testing...")
	print()
	
	try:
		test_client_to_client()
	except requests.exceptions.ConnectionError:
		print("❌ ERROR: Cannot connect to server!")
		print("   Please run: python des_server.py")
	except Exception as e:
		print(f"❌ ERROR: {e}")
