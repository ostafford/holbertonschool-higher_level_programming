def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): A list of dictionaries containing attendee information
    """
    # Step 1: Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: All items in attendees must be dictionaries.")
        return
    
    # Step 2: Check for empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Step 3: Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        personalized_invitation = template
        
        # Define the placeholders we need to replace
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        
        # Replace each placeholder with the corresponding value
        for placeholder in placeholders:
            # Get the value from the attendee dict, or 'N/A' if missing or None
            value = attendee.get(placeholder, 'N/A')
            if value is None:
                value = 'N/A'
                
            # Replace the placeholder in the template
            personalized_invitation = personalized_invitation.replace(f"{{{placeholder}}}", str(value))
        
        # Step 4: Write to output file
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as file:
            file.write(personalized_invitation)
        
        print(f"Created invitation for {attendee.get('name', 'Unknown')} as {output_filename}")