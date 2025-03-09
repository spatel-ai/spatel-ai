import requests

# Fetch the data from the API
response = requests.get("https://leetcard.jacoblin.cool/spatel-ai?ext=heatmap")

# Make sure to handle the response correctly
if response.status_code == 200:
    # Open a file to write the binary data
    with open('leetcode_activity.svg', 'wb') as file:
        file.write(response.content)
else:
    print(f"Failed to fetch data: {response.status_code}")

# If you need to replace a specific element in the fetched content
def replace_element_in_svg(file_path, old_name, new_name):
    print(old_name,new_name)
    with open(file_path, 'r+', encoding='utf-8') as file:
        svg_content = file.read()
        print(svg_content)
        # Replace the old name with the new name in the SVG content
        updated_svg_content = svg_content.replace(old_name, new_name)
        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Write the updated content back to the file
        file.write(updated_svg_content)
        # Truncate the file to the new length
        file.truncate()

# Example usage
replace_element_in_svg('leetcode_activity.svg', '<rect id="background"></rect>', '<rect id="background" style="opacity: 0;"></rect>')
