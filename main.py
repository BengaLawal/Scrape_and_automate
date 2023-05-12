from auto import FillForm

PROPERTY24_URL = "https://www.property24.com/houses-to-rent/advanced-search/results?sp=s%3d9025%2c9036%2c10178%2c904" \
                 "4%2c11742%2c10094%2c11741%2c8679%2c14225%2c8661%2c10102%2c14224%26pf%3d10000%26pt%3d15000%26bd%3d3" \
                 "%26bth%3d2%26rr%3dMonth"
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeVXMvOf168TKIbzxsz7rw80i1YX4ulQU6dnoKuJtXorz0kAQ/viewform?usp" \
            "=pp_url"

automate = FillForm(form_link=FORM_LINK, property24_url=PROPERTY24_URL)
automate.fill_form()

# read through at own leisure-
# https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d