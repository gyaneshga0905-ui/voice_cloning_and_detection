"""Entry point. Run with:  python app.py"""
from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from config import Config
from routes.detect_routes import detect_bp
from routes.frontend_routes import frontend_bp
from routes.main_routes import main_bp
from routes.upload_routes import upload_bp
from services.errors import AudioValidationError
from services.model_service import model_service


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Try to load the trained model (fine if the file does not exist)
    model_service.load(app.config["MODEL_PATH"])

    app.register_blueprint(main_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(detect_bp)
    app.register_blueprint(frontend_bp)

    @app.errorhandler(AudioValidationError)
    def handle_validation_error(e):
        return jsonify({"status": "error", "code": e.code, "message": e.message}), e.status_code

    @app.errorhandler(413)
    def too_large(e):
        limit_mb = app.config["MAX_CONTENT_LENGTH"] // (1024 * 1024)
        return jsonify({
            "status": "error", "code": "FILE_TOO_LARGE",
            "message": f"File exceeds the {limit_mb} MB limit.",
        }), 413

    @app.errorhandler(HTTPException)
    def handle_http_error(e):
        return jsonify({"status": "error", "code": e.name.upper().replace(" ", "_"),
                        "message": e.description}), e.code

    @app.errorhandler(Exception)
    def handle_unexpected(e):
        app.logger.exception("Unexpected error")
        return jsonify({"status": "error", "code": "INTERNAL_ERROR",
                        "message": "Something went wrong on the server."}), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)