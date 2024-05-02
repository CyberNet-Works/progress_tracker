def copy_elements(original_tuple, indices):
    new_tuple = ()

    for index in indices:
        new_tuple += (original_tuple[index],)

    return new_tuple

#return tuple(original_tuple[index] for index in indices)
