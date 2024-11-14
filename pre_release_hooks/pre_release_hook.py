import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: python pre_release_hook.py <path_to_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        environment_name = data.get("environmentName")
        release_stream = data.get("releaseStream")
        resources = data.get("resources", [])

        print(f"Environment Name: {environment_name}")
        print(f"Release Stream: {release_stream}")
        print("Resources:")
        for resource in resources:
            print(f"  - Resource Type: {resource.get('resourceType')}")
            print(f"    Resource Name: {resource.get('resourceName')}")
            print(f"    Resource Path: {resource.get('resourcePath')}")
            print(f"    Change Type: {resource.get('changeType')}")

    except FileNotFoundError:
        print(f"Error: File not found - {json_file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file - {json_file_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
