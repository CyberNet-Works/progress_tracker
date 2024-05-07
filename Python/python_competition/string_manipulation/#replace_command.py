#replace_spaces
def replace_spaces():
    user_input = input("\n\n\nPlease enter name:\n>>")
    result = '\n\n\n\n#' + user_input.replace(" ", "_") + '.py\n\n\n'
    result = result.replace(":", "_")
    result = result.replace("(", "_")
    result = result.replace(")", "_")
    print(result)
    
replace_spaces()
