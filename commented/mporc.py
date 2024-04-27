import logging  # Importing the logging library for logging purposes
import xml.etree.ElementTree as ET  # Importing ElementTree from xml.etree module for XML parsing

# Function to find the answer to a question based on keywords
def accresp(maintext):
    answerid = -1  # Initializing answer ID to -1, indicating that the ID is not found
    with open('answer_data.xml', 'r', encoding='utf-8') as file:  # Opening the XML file with answers for reading
        data = file.read()

    root = ET.fromstring(data)  # Parsing the XML data

    # List of keyword groups
    keywords = [
        ['enter ebs', 'log in to ebs'],
        ['access to databases'],
        ['when to return book', 'when to return textbook', 'where to return textbook', 'where to return book', 'return book', 'return textbook'],
        ['which books to return', 'outstanding', 'took out'],
        ['sign bypass sheet'],
        ['lost book', 'lost books', 'lost books', 'lost book', 'when lost'],
        ['renew book', 'renew books'],
        ['what is unibec', 'what is nb'],
        ['library working hours', 'how library works', 'library hours'],
        ['enroll in unibec', 'enroll in library', 'enroll in nb'],
        ['submit dissertation'],
        ['can take out at main library'],
        ['remote access to'],
        ['what is ebs'],
        ['electronic version'],
        ['did not manage to return book'],
        ['reading room for muslims', 'place for muslims', 'corner for muslims'],
        ['register in tuys']
    ]

    # Loop through keyword groups
    for k in range(len(keywords) - 1):
        flag = 0  # Flag to stop the loop in case of finding the correct answer
        # Loop through individual keywords
        for text in keywords[k]:
            txt = text[0:len(text) - 1].split(' ')  # Splitting the text into individual keywords
            # Loop through keywords
            for el in txt:
                if el in maintext.lower():  # Checking if the keyword is present in the question
                    flag = 1  # Setting flag to 1 if keyword is found
                else:
                    flag = 0  # Setting flag to 0 if keyword is not found
                    break
            if flag != 0:  # Breaking the loop if flag is not 0
                break
        if flag != 0:  # Breaking the loop and getting the answer ID
            answerid = k
            break
    if answerid >= 0:  # If the ID is found, retrieve the corresponding answer from the XML
        for answer in root.findall('answer'):
            if int(answer.attrib['id']) == answerid + 1:
                return answer.text.strip()
    else:
        return "Sorry, I don't know the answer to your question"  # If the corresponding answer is not found, inform the user

import logging  # Importing the logging library for logging purposes
import xml.etree.ElementTree as ET  # Importing ElementTree from xml.etree module for XML parsing

# Function to find the answer to a question based on keywords
def accresp(maintext):
    answerid = -1  # Initializing answer ID to -1, indicating that the ID is not found
    with open('answer_data.xml', 'r', encoding='utf-8') as file:  # Opening the XML file with answers for reading
        data = file.read()

    root = ET.fromstring(data)  # Parsing the XML data

    # List of keyword groups
    keywords = [
        ['enter ebs', 'log in to ebs'],
        ['access to databases'],
        ['when to return book', 'when to return textbook', 'where to return textbook', 'where to return book', 'return book', 'return textbook'],
        ['which books to return', 'outstanding', 'took out'],
        ['sign bypass sheet'],
        ['lost book', 'lost books', 'lost books', 'lost book', 'when lost'],
        ['renew book', 'renew books'],
        ['what is unibec', 'what is nb'],
        ['library working hours', 'how library works', 'library hours'],
        ['enroll in unibec', 'enroll in library', 'enroll in nb'],
        ['submit dissertation'],
        ['can take out at main library'],
        ['remote access to'],
        ['what is ebs'],
        ['electronic version'],
        ['did not manage to return book'],
        ['reading room for muslims', 'place for muslims', 'corner for muslims'],
        ['register in tuys']
    ]

    # Loop through keyword groups
    for k in range(len(keywords) - 1):
        flag = 0  # Flag to stop the loop in case of finding the correct answer
        # Loop through individual keywords
        for text in keywords[k]:
            txt = text[0:len(text) - 1].split(' ')  # Splitting the text into individual keywords
            # Loop through keywords
            for el in txt:
                if el in maintext.lower():  # Checking if the keyword is present in the question
                    flag = 1  # Setting flag to 1 if keyword is found
                else:
                    flag = 0  # Setting flag to 0 if keyword is not found
                    break
            if flag != 0:  # Breaking the loop if flag is not 0
                break
        if flag != 0:  # Breaking the loop and getting the answer ID
            answerid = k
            break
    if answerid >= 0:  # If the ID is found, retrieve the corresponding answer from the XML
        for answer in root.findall('answer'):
            if int(answer.attrib['id']) == answerid + 1:
                return answer.text.strip()
    else:
        return "Sorry, I don't know the answer to your question"  # If the corresponding answer is not found, inform the user

def addfeedback(maintext, userid):
    """
    Function to add user feedback to an XML file.

    Args:
        maintext (str): The text of the user's feedback.
        userid (int): The user ID associated with the feedback.

    Returns:
        None
    """
    # Create an XML parser with specified encoding
    parser = ET.XMLParser(encoding="utf-8")

    # Parse the XML file containing feedback data
    tree = ET.parse('feedback_data.xml', parser=parser)

    # Get the root element of the XML tree
    root = tree.getroot()

    # Find the first "feedback" element in the XML structure
    first = root.find("feedback")

    # Create attributes dictionary with user ID
    attributes = {"from_user": str(userid)}

    # Create a new XML element under the root node with the user's feedback text and attributes
    child = ET.SubElement(root, "text", attributes)
    child.text = maintext  # Set the text content of the new XML element to the user's feedback

    ET.dump(tree)  # Print the XML tree to the console (optional)

    # Write the modified XML tree back to the XML file with specified encoding and XML declaration
    tree.write('feedback_data.xml', encoding="utf-8", xml_declaration=True)
