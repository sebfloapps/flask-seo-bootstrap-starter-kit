from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# ---------------------------------------------------
# Global Defaults (used if a route doesn't pass data)
# ---------------------------------------------------

DEFAULT_SEO = {
    'site_name': 'Your Site Name',
    'site_url': 'https://yoursite.com',
    'page_title': 'Your Site Title',
    'page_description': 'This is the default SEO description for your website.',
    'page_keywords': 'keyword1, keyword2, keyword3',
    'page_author': 'Your Brand',
    'page_robots': 'index,follow',
    'theme_color': '#000000',

    # Open Graph
    'og_type': 'website',
    'og_locale': 'en_US',
    'og_site_name': 'Your Site Name',
    'og_image': 'https://yoursite.com/static/img/og-default.jpg',

    # Twitter
    'twitter_card': 'summary_large_image',
    'twitter_site': '@YourBrandHandle',
    'twitter_creator': '@YourBrandHandle',
}


# ---------------------------------------------------
# Context Processor – Inject SEO defaults everywhere
# ---------------------------------------------------

@app.context_processor
def inject_defaults():
    return {
        **DEFAULT_SEO,
        'current_year': datetime.now().year
    }


# ---------------------------------------------------
# Routes
# ---------------------------------------------------

@app.route("/")
def index():
    return render_template(
        "index.html",

        # Optional SEO overrides per page
        page_title="Home | Your Site Name",
        page_description="Welcome to Your Site — the best place for awesome content.",
        page_keywords="home, website, flask, bootstrap",

        og_title="Your Site — Home",
        og_description="Discover awesome content on Your Site.",

        twitter_title="Your Site — Home"
    )


@app.route("/about")
def about():
    # This page uses ONLY defaults
    return render_template("about.html")


# ---------------------------------------------------
# Run App
# ---------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)