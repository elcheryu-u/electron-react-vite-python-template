from flask import Flask, jsonify, request , render_template

app = Flask(__name__)

items1 = []
 
@app.route('/api/items1', methods=['POST'])
def add_item1():
    new_item2 = request.get_json() 
    try:
        if not new_item2 or 'product' not in new_item2 or 'name' not in new_item2['product'] or 'provider' not in new_item2 or 'timestamp'not in new_item2 or 'price' not in new_item2['provider'] or 'currency' not in new_item2['provider']['price'] or 'value' not in new_item2['provider']['price'] or 'weight' not in new_item2['product'] or 'key' not in new_item2['product']['weight'][0] or 'value' not in new_item2['product']['weight'][0] or 'key' not in new_item2['product']['weight'][1] or 'value' not in new_item2['product']['weight'][1] or len(new_item2['product']['weight']) < 2:
            return jsonify({'error': 'Datos inválidos'}), 400
    except (KeyError, TypeError, IndexError):
        return jsonify({'error': 'Datos inválidos'}), 400
    
    product_name = new_item2['product']['name']
    if not isinstance(product_name, str) or product_name.strip() == '' or product_name.isnumeric():
        return jsonify({'error': 'El nombre del producto no es válido'}), 400
    
    if not 'id' in new_item2:
        return jsonify({'error':'id no encontrado'}), 400
    if not isinstance(new_item2['id'], str) or new_item2['id'].strip() == ' ':
        return jsonify({'error':'El id no es válido'}), 400
    
    product_id = new_item2['product']['id']
    if not isinstance(product_id, int) or product_id <= 0:
        return jsonify({'error':' El id del producto no es válido'}), 400
    
    provider_id = new_item2['provider']['id']
    if not isinstance(provider_id, str) or provider_id.strip() == ' ':
        return jsonify({'error':'El id del proveedor no es válido'}), 400
    
    provider_name = new_item2['provider']['name']
    if not isinstance(provider_name, str) or provider_name.strip() == ' ' or provider_name.isnumeric():
        return jsonify({'error':'El nombre del proveedor no es válido'}), 400
    
    product_weight = new_item2['product']['weight'][0]['key']
    if not isinstance(product_weight, str) or not product_weight == 'kg':
        return jsonify({'error':'el tipo no es valido'}), 400
    if not isinstance(new_item2['product']['weight'][0]['value'], (int, float)) or new_item2['product']['weight'][0]['value'] <= 0:
        return jsonify({'error':'El peso en kg no es válido'}), 400
    if not isinstance(new_item2['product']['weight'][1]['key'], str) or not new_item2['product']['weight'][1]['key'] == 'lb':
        return jsonify({'error':'el tipo no es valido'}), 400
    if not isinstance(new_item2['product']['weight'][1]['value'], (int, float)) or new_item2['product']['weight'][1]['value'] <= 0:
        return jsonify({'error':'El peso en lb no es válido'}), 400
    
    provider_price_value = new_item2['provider']['price']['value']
    provider_price_currency = new_item2['provider']['price']['currency']
    if not isinstance(provider_price_currency, str) or provider_price_currency.strip() == '' or provider_price_currency.isnumeric():
        return jsonify({'error':'la moneda no es valida'}), 400
    if not isinstance(provider_price_value, (int)) or provider_price_value <= 0:
        return jsonify({'error':'El precio no es válido'}), 400
    
    if not isinstance(new_item2['timestamp'], int) or new_item2['timestamp'] <= 0:
        return jsonify({'error':'El timestamp no es válido'}), 400

    
    items1.append(new_item2)
    return jsonify(new_item2), 201


@app.route('/items1', methods=['GET'])
def mostrar_items1():
    return items1

@app.route('/')
def index():
    return '¡Bienvenido! Puedes ir a /items para ver la lista en la web o a /api/items para obtenerla en JSON (GET) o agregar nuevos items (POST).'

if __name__ == '__main__':
    app.run(debug=True)