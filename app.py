from flask import Flask, make_response, redirect, render_template, request

app = Flask(__name__)

def is_true(value):
  return value.lower() == 'true'

def get_star_rating(rating, size=24):
    """Get the star rating representation of progress based on a scale.

    This function calculates the ratio of progress to scale and returns an
    SVG representation of the star rating. The star rating is defined as
    follows: - 1 star for progress less than 20% - 2 stars for progress
    between 20% and 40% - 3 stars for progress between 40% and 60% - 4 stars
    for progress between 60% and 80% - 5 stars for progress of 80% or more.

    Args:
        rating (float): The rating value between 0 and 5.
        size (int): The size of each star in pixels.

    Returns:
        str: An SVG representation of the star rating.
    """

    rating = max(0, min(5, rating))
    full_stars = int(rating)
    partial = rating - full_stars
    empty_stars = 5 - full_stars - (1 if partial > 0 else 0)

    star_svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size * 5} {size}" width="{size * 5}" height="{size}">'
    
    # Add full stars
    for i in range(full_stars):
        x = i * size
        star_svg += f'''
        <path transform="translate({x},0)" fill="gold" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
        '''
    
    # Add partial star if needed
    if partial > 0:
        x = full_stars * size
        star_svg += f'''
        <defs>
            <clipPath id="partial">
                <rect x="0" y="0" width="{partial * size}" height="{size}" />
            </clipPath>
        </defs>
        <path transform="translate({x},0)" fill="#ddd" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
        <path transform="translate({x},0)" fill="gold" clip-path="url(#partial)" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
        '''
    
    # Add empty stars
    for i in range(empty_stars):
        x = (full_stars + 1) * size if partial > 0 else full_stars * size
        star_svg += f'''
        <path transform="translate({x},0)" fill="#ddd" d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
        '''
        full_stars += 1

    star_svg += '</svg>'
    return star_svg

@app.route('/<rating>/')
def star_rating(rating):
    if not rating:
        return redirect("https://github.com/GoulartNogueira/Star-Rating/")
    
    try:
        rating = float(rating)
    except ValueError:
        return "Invalid rating value", 400

    size = request.args.get('size', default=24, type=int)
    svg = get_star_rating(rating, size)
    response = make_response(svg)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response

if __name__ == '__main__':
    app.run(debug=True)