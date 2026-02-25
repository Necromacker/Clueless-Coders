import requests
import json

# Configuration
API_BASE_URL = "https://api.foodoscope.com/recipe2-api/instructions/"
API_TOKEN = "Bearer X-rU-MJr4BiA64g2PnbvlJp3Ek4HvW1QKniooxvk9sX-l6u0"
RECIPE_ID = 2623  # Quick and Easy Egyptian Chicken Broth

def verify_cook_with_us_api():
    print("=== COOK WITH US API VERIFICATION ===")
    print(f"Recipe ID: {RECIPE_ID}")
    print(f"API Token: {API_TOKEN}")
    
    url = f"{API_BASE_URL}{RECIPE_ID}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": API_TOKEN,
    }
    
    print(f"\n1. CALLING API...")
    print(f"URL: {url}")
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n2. RAW API RESPONSE:")
            print(json.dumps(data, indent=2))
            
            # Simulated Frontend Conversion Logic
            print("\n3. CONVERSION (FRONTEND PARSING LOGIC):")
            instructions = []
            
            # Logic from CookWithUs.jsx
            if isinstance(data, list):
                instructions = data
            elif isinstance(data, dict):
                if "instructions" in data and isinstance(data["instructions"], list):
                    instructions = data["instructions"]
                elif "steps" in data and isinstance(data["steps"], list):
                    instructions = data["steps"]
                else:
                    instructions = [json.dumps(data)]
            
            parsed_steps = []
            for item in instructions:
                if isinstance(item, str):
                    parsed_steps.append(item)
                elif isinstance(item, dict) and "step" in item:
                    parsed_steps.append(item["step"])
                else:
                    parsed_steps.append(json.dumps(item))
            
            print("Final Parsed Steps for Voice/UI:")
            for i, step in enumerate(parsed_steps, 1):
                print(f"  Step {i}: {step}")
                
            print("\n--- VERIFICATION COMPLETE ---")
        else:
            print(f"Error: Received status code {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Exception occurred: {str(e)}")

if __name__ == "__main__":
    verify_cook_with_us_api()
