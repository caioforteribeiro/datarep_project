from flask import Flask, jsonify, request, abort
from catDAO import catDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#Get all
@app.route('/cats')
def getAll():
    
    results = catDAO.getAll()
    return jsonify(results)

#Find by ID
@app.route('/cats/<int:id>')
def findById(id):
    foundcat = catDAO.findByID(id)

    return jsonify(foundcat)

#Create new
@app.route('/cats', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
     
    cat = {
        "name": request.json['name'],
        "sex": request.json['sex'],
        "age": request.json['age'],
        "breed": request.json['breed'],
    }
    values =(cat['name'],cat['sex'],cat['age'],cat['breed'])
    newId = catDAO.create(values)
    cat['id'] = newId
    return jsonify(cat)

#Update
@app.route('/cats/<int:id>', methods=['PUT'])
def update(id):
    foundcat = catDAO.findByID(id)
    if not foundcat:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'age' in reqJson and type(reqJson['age']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundcat['name'] = reqJson['name']
    if 'sex' in reqJson:
        foundcat['sex'] = reqJson['sex']
    if 'age' in reqJson:
        foundcat['age'] = reqJson['age']
    if 'breed' in reqJson:
        foundcat['breed'] = reqJson['breed']
    values = (foundcat['name'],foundcat['sex'],foundcat['age'],foundcat['breed'],foundcat['id'])
    catDAO.update(values)
    return jsonify(foundcat)
        

    
#Delete
@app.route('/cats/<int:id>' , methods=['DELETE'])
def delete(id):
    catDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)