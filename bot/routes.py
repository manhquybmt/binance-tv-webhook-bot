from flask import Blueprint
from flask import jsonify
from flask import render_template

main_bp = Blueprint(
    "main",
    __name__,
    template_folder="../dashboard/templates",
    static_folder="../dashboard/static",
)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "version": "0.1.0",
            "service": "Binance TV Webhook Bot",
        }
    )