from flask import Blueprint, jsonify, request # type: ignore
import PyPDF2 as pdf # type: ignore

api_blueprint = Blueprint('api', __name__);

@api_blueprint.route('/')
def index():
    data = {
        "message": "api end point"
    }

    return jsonify(data);


@api_blueprint.route('/post', methods=['POST'])
def post_trial():
    data = request.json
    return jsonify(data);

@api_blueprint.route('/upload', methods=['POST'])
def handle_upload():
    file = request.files["file"]
    pdf_reader = pdf.PdfReader(file)
    length = len(pdf_reader.pages)
    file_string = ''
    for i in range(0, length):
        page1 = pdf_reader.pages[i]
        file_string += page1.extract_text()

    data = {"fileContent": file_string}
    return jsonify(data);


