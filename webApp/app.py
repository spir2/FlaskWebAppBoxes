from flask import Flask, render_template, jsonify
from pypugjs.ext.jinja import PyPugJSExtension

app = Flask(__name__)
app.jinja_env.add_extension(PyPugJSExtension)

# Deux boîtes, 10 téléphones par boîte
noiseboxes = {
    1: [{'tel_id': i, 'nbr_notif': 0} for i in range(1, 3)],
    2: [{'tel_id': i, 'nbr_notif': 0} for i in range(1, 3)]
}

@app.route('/')
def index():
    """
    Page principale qui affiche la grille des téléphones.
    """
    print("DEBUG noiseboxes =", noiseboxes, type(noiseboxes))
    return render_template('index.pug', noiseboxes=noiseboxes)

@app.route('/data')
def data():
    """
    Retourne la structure des notifications au format JSON,
    utile pour la mise à jour AJAX (JS).
    """
    return jsonify(noiseboxes)

@app.route('/<int:box_id>/<int:tel_id>')
def increment_notification(box_id, tel_id):
    """
    Incrémente le nombre de notifications du téléphone `tel_id`
    dans la boîte `box_id`.
    """
    if box_id in noiseboxes:
        for tel in noiseboxes[box_id]:
            if tel['tel_id'] == tel_id:
                tel['nbr_notif'] += 1
                break
        return f"Incrémentation OK (box={box_id}, tel={tel_id})", 200
    else:
        return "Box not found", 404

if __name__ == '__main__':
    app.run(debug=True)
