from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# -----------------------------------------
# Main Routes
# -----------------------------------------
@app.route("/")
def main():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template("products.html", active_section="ce-certified")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/products/<category>")
def product_category(category):
    valid_categories = ["ce-certified", "non-ce-certified", "drug-delivery", "oem"]
    
    if category not in valid_categories:
        category = "ce-certified"
    
    return render_template("products.html", active_section=category)



from flask import send_from_directory, abort
import os

@app.route("/download/<path:filename>")
def download_brochure(filename):
    return send_from_directory(
        directory="static/brochure",
        path=filename,
        as_attachment=True
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway provides PORT dynamically
    app.run(host="0.0.0.0", port=port, debug=True)