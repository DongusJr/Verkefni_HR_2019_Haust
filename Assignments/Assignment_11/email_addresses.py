def get_emails():
    email_lst = []
    email_input = input("Email address: ")
    while(email_input.lower() != "q"):
        email_lst.append(email_input)
        email_input = input("Email address: ")
    return email_lst

def get_names_and_domains(email_list):
    split_list = []
    for email in email_list:
        split_list.append(tuple(email.split("@")))
    return split_list
# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)