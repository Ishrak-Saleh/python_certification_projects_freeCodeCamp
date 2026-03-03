"""
This is the first certification project of the freeCodeCamp Python course 
and this is my approach on how I build a User Configuration Manager
"""
#Formatting the input string (key or value) for consistency
def string_formatter(input_string):
    return input_string.lower()


def add_setting(settings_dict, tuple_param):
    #Getting the key and value from tuple
    key, value = tuple_param
    #Lowercasing key,value pairs for formatting
    formatted_key = string_formatter(key)
    formatted_value = string_formatter(value)

    #Checking if the lowercase key setting already exists in settings_dict
    if formatted_key in settings_dict:
        return f"Setting '{formatted_key}' already exists! Cannot add a new setting with this name."
    else:
        #Adding to dictionary
        settings_dict[formatted_key] = formatted_value
        return f"Setting '{formatted_key}' added with value '{formatted_value}' successfully!"


def update_setting(settings_dict, tuple_param):
    key, value = tuple_param

    formatted_key = string_formatter(key)
    formatted_value = string_formatter(value)
    #Checking if the formatted_key exists in the settings_dict to update
    if formatted_key in settings_dict:
        settings_dict[formatted_key] = formatted_value
        return f"Setting '{formatted_key}' updated to '{formatted_value}' successfully!"
    else: 
        return f"Setting '{formatted_key}' does not exist! Cannot update a non-existing setting."



def delete_setting(settings_dict, key):
    #This is the key to remove
    formatted_key = string_formatter(key)
    if formatted_key in settings_dict:
        #Removing the key
        del settings_dict[formatted_key]
        return f"Setting '{formatted_key}' deleted successfully!"
    else: 
        return f"Setting not found!"


def view_settings(settings_dict):
    #If the settings_dict is empty
    if not settings_dict: 
        return f"No settings available."
    #Making a string to properly format the settings_dict as per requirement
    else:
        output_return_text = "Current User Settings:\n"
        for key, value in settings_dict.items():
            uppercase_formatted_key = key.capitalize()
            output_return_text += f"{uppercase_formatted_key}: {value}\n"
        
        return output_return_text
        


test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

"""#Testing the functions with the provided test_settings dictionary
print(add_setting(test_settings, ('Language', 'English')))
print(add_setting(test_settings, ('theme', 'light')))
print(update_setting(test_settings, ('volume', 'medium')))
print(update_setting(test_settings, ('brightness', 'high')))
print(delete_setting(test_settings, 'notifications'))
print(delete_setting(test_settings, 'non_existing_setting'))

print(view_settings(test_settings))"""
