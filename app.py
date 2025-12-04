from flask import Flask, render_template, request, flash, redirect, url_for
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

#home page
@app.route("/")
def index():
    return render_template(
        "index.html",

        # Optional SEO overrides per page
        page_title="Home - Flask SEO Bootstrap Starter Kit",
        meta_description="A lightweight Flask starter kit with built-in SEO support and a clean Bootstrap 5 layout.",
        page_keywords="home, website, flask, bootstrap",

        og_title="Your Site — Home",
        og_description="Discover awesome content on Your Site.",

        twitter_title="Your Site — Home"
    )

#about page
@app.route("/about")
def about():
    # This page uses ONLY defaults
    return render_template("about.html")

#contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill out all fields.", "danger")
            return redirect(url_for("contact"))

        # Wire into email or database later
        flash("Thanks for reaching out. Your message has been received.", "success")
        return redirect(url_for("contact"))

    return render_template(
        "contact.html",
        page_title="Contact – Flask SEO Bootstrap Starter Kit",
        meta_description="Contact page template example for the Flask starter kit."
    )

#dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        page_title="Dashboard – Flask SEO Bootstrap Starter Kit",
        meta_description="Basic dashboard layout template you can extend with your own data and components."
    )

#custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#registration and login pages
@app.route("/register")
def register():
    return render_template(
        "register.html",
        page_title="Register – Flask SEO Bootstrap Starter Kit",
        meta_description="Basic registration UI template for Flask starter projects."
    )

@app.route("/login")
def login():
    return render_template(
        "login.html",
        page_title="Login – Flask SEO Bootstrap Starter Kit",
        meta_description="Basic login UI template for Flask starter apps."
    )

# ---------------------------------------------------
# Run App
# ---------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)