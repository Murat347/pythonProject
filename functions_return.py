# 03/25/2021

def get_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name


def print_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title ()} {lastname.title ()}"
    print(name)


full_name = get_formatted_name('john', 'doe')
print(full_name)
print(get_formatted_name('jane', 'doe'))


print_formatted_name('ali','tehrani')
student = print_formatted_name('baur', 'eskara')
print(f"value of student is: {student}")
print(f"value of student is: {print_formatted_name('baur', 'eskara')}")


# getter, setter functions
def get_desc_of_what_you_want_to_get():
    # logic
    return





# 03/27/2021

def print_usernames(users: list):
    for user in users:
        print(f"current user is: {user}")

print_usernames(['karim', 'ronaldo', 'roger'])


