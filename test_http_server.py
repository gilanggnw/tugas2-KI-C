#!/usr/bin/env python3
"""
Simple test script for DES HTTP Server
Tests all endpoints locally
"""

import requests
import json

SERVER_URL = "http://localhost:5000"  # Change to your server URL

def test_server_info():
	"""Test GET / endpoint"""
	print("=" * 60)
	print("Testing GET / (Server Info)")
	print("=" * 60)
	try:
		response = requests.get(f"{SERVER_URL}/")
		print(f"Status Code: {response.status_code}")
		print(f"Response: {json.dumps(response.json(), indent=2)}")
		return response.status_code == 200
	except Exception as e:
		print(f"Error: {e}")
		return False

def test_encrypt():
	"""Test POST /encrypt endpoint"""
	print("\n" + "=" * 60)
	print("Testing POST /encrypt")
	print("=" * 60)
	
	data = {
		"plaintext": "0123456789ABCDEF",
		"key": "133457799BBCDFF1"
	}
	
	print(f"Request: {json.dumps(data, indent=2)}")
	
	try:
		response = requests.post(f"{SERVER_URL}/encrypt", json=data)
		print(f"Status Code: {response.status_code}")
		result = response.json()
		print(f"Response: {json.dumps(result, indent=2)}")
		
		if result['status'] == 'success':
			print(f"\n✓ Encryption successful!")
			print(f"  Ciphertext: {result['ciphertext']}")
			return True, result['ciphertext']
		return False, None
	except Exception as e:
		print(f"Error: {e}")
		return False, None

def test_decrypt(ciphertext):
	"""Test POST /decrypt endpoint"""
	print("\n" + "=" * 60)
	print("Testing POST /decrypt")
	print("=" * 60)
	
	data = {
		"ciphertext": ciphertext,
		"key": "133457799BBCDFF1"
	}
	
	print(f"Request: {json.dumps(data, indent=2)}")
	
	try:
		response = requests.post(f"{SERVER_URL}/decrypt", json=data)
		print(f"Status Code: {response.status_code}")
		result = response.json()
		print(f"Response: {json.dumps(result, indent=2)}")
		
		if result['status'] == 'success':
			print(f"\n✓ Decryption successful!")
			print(f"  Plaintext: {result['plaintext']}")
			return True
		return False
	except Exception as e:
		print(f"Error: {e}")
		return False

def test_process_encrypt():
	"""Test POST /process with ENCRYPT operation"""
	print("\n" + "=" * 60)
	print("Testing POST /process (ENCRYPT)")
	print("=" * 60)
	
	data = {
		"operation": "ENCRYPT",
		"plaintext": "FEDCBA9876543210",
		"key": "0E329232EA6D0D73"
	}
	
	print(f"Request: {json.dumps(data, indent=2)}")
	
	try:
		response = requests.post(f"{SERVER_URL}/process", json=data)
		print(f"Status Code: {response.status_code}")
		result = response.json()
		print(f"Response: {json.dumps(result, indent=2)}")
		
		if result['status'] == 'success':
			print(f"\n✓ Process (Encrypt) successful!")
			return True
		return False
	except Exception as e:
		print(f"Error: {e}")
		return False

def test_process_decrypt():
	"""Test POST /process with DECRYPT operation"""
	print("\n" + "=" * 60)
	print("Testing POST /process (DECRYPT)")
	print("=" * 60)
	
	data = {
		"operation": "DECRYPT",
		"plaintext": "85E813540F0AB405",  # This is actually ciphertext
		"key": "133457799BBCDFF1"
	}
	
	print(f"Request: {json.dumps(data, indent=2)}")
	
	try:
		response = requests.post(f"{SERVER_URL}/process", json=data)
		print(f"Status Code: {response.status_code}")
		result = response.json()
		print(f"Response: {json.dumps(result, indent=2)}")
		
		if result['status'] == 'success':
			print(f"\n✓ Process (Decrypt) successful!")
			return True
		return False
	except Exception as e:
		print(f"Error: {e}")
		return False

def main():
	print("\n" + "=" * 70)
	print(" " * 15 + "DES HTTP SERVER TEST SUITE")
	print("=" * 70)
	print(f"\nTesting server at: {SERVER_URL}")
	print("\nMake sure the server is running before running this test!")
	print("Run: python des_server_5000.py")
	print("=" * 70)
	
	input("\nPress Enter to start testing...")
	
	# Run tests
	tests_passed = 0
	tests_total = 0
	
	# Test 1: Server info
	tests_total += 1
	if test_server_info():
		tests_passed += 1
	
	# Test 2: Encrypt
	tests_total += 1
	success, ciphertext = test_encrypt()
	if success:
		tests_passed += 1
		
		# Test 3: Decrypt (only if encrypt succeeded)
		if ciphertext:
			tests_total += 1
			if test_decrypt(ciphertext):
				tests_passed += 1
	
	# Test 4: Process (Encrypt)
	tests_total += 1
	if test_process_encrypt():
		tests_passed += 1
	
	# Test 5: Process (Decrypt)
	tests_total += 1
	if test_process_decrypt():
		tests_passed += 1
	
	# Summary
	print("\n" + "=" * 70)
	print("TEST SUMMARY")
	print("=" * 70)
	print(f"Tests Passed: {tests_passed}/{tests_total}")
	
	if tests_passed == tests_total:
		print("✓ All tests passed! Server is working correctly.")
	else:
		print(f"✗ {tests_total - tests_passed} test(s) failed.")
	
	print("=" * 70)

if __name__ == "__main__":
	main()
