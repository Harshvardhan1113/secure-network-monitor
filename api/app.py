from flask import Flask, render_template
from api.defense_metrics import bp as defense_metrics_bp

# -------------------------------
# Flask App Configuration
# -------------------------------
app = Flask(
    __name__,
    template_folder="../dashboard/templates"
)

# -------------------------------
# Register Blueprints
# -------------------------------
app.register_blueprint(defense_metrics_bp)

# -------------------------------
# Dashboard Route
# -------------------------------
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# -------------------------------
# Application Entry Point
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
