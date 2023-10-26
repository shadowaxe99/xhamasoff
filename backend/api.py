```python
from flask import Flask, request, jsonify
from models import tweets, model_outputs, audit_logs

app = Flask(__name__)

@app.route('/get_recent_flags', methods=['GET'])
def get_recent_flags():
    flags = model_outputs.query.order_by(model_outputs.timestamp.desc()).limit(10).all()
    return jsonify([flag.serialize for flag in flags])

@app.route('/audit_flag', methods=['POST'])
def audit_flag():
    flag_id = request.json.get('flag_id')
    audit_result = request.json.get('audit_result')

    flag = model_outputs.query.get(flag_id)
    if not flag:
        return jsonify({'error': 'Flag not found'}), 404

    audit_log = audit_logs(flag_id=flag_id, audit_result=audit_result)
    db.session.add(audit_log)
    db.session.commit()

    return jsonify(audit_log.serialize), 201

if __name__ == '__main__':
    app.run(debug=True)
```