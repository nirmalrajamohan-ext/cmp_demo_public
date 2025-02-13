
import sys
import json

def process_data(json_arg):
    try:
        data = json.loads(json_arg)  # Parse JSON string to dict
        print("Parsed JSON:", data)
        return data
    except json.JSONDecodeError:
        print("Invalid JSON format")

def check_key_from_args(args:dict, key):
        if key not in args:
            raise ValueError(f"Missing required key: '{key}' in provided JSON")

        return args[key]  # Return value if key exists

    
def validate_args(args:dict):  
   instance_id=check_key_from_args(args, "instance_id")
   cmp_url=check_key_from_args(args, "cmp_url")


def main(vargs:str):
    args = process_data(vargs)
    
    

    print("instance_id is ", args["instance_id"])
    with open("hello.txt", "w") as file:
        file.write("Hello, World!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py '<json_string>'")
    else:
       main(sys.argv[1])


