import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    if template.strip() == "":
        print("Error: Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    
    for idx, attendee in enumerate(attendees, start= 1):
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            placeholder = f"{{{key}}}"
            invitation = invitation.replace(placeholder, value)
    
    output_filename = f"output_{idx}.txt"
    
        
    if os.path.exists(output_filename):
        print(f"Error: File {output_filename} already exists. Skipping.")
        
    
    try:
        with open(output_filename, 'w') as file:
            file.write(invitation)

        print(f"Invitation written to {output_filename}")

    except Exception as e:
        print(f"Error writing to file {output_filename}: {e}")


           
if __name__ == "__main__":
    with open('template.txt', 'r') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees) 