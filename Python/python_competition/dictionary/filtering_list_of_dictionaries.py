def filter_by_star_rating(hotels, min_stars):
    filtered_hotels = []

    for hotel in hotels:
        if hotel['stars'] >= min_stars:
            filtered_hotels.append(hotel)

    return filtered_hotels
